import xarray as xr
import pandas as pd
import numpy as np
import psycopg
import os
import io

def load_file_fast(filename: str):
    print(f"Loading {filename}")
    ds = xr.open_dataset(filename)

    time_val = pd.to_datetime(ds.time.values[0])

    # Extract arrays
    stations = ds["stations"].values[0]            # int grid, may contain NaN
    stationvalues = ds["stationvalues"].values[0]  # float
    prediction = ds["prediction"].values[0]        # float

    # Floats: NaN is fine for COPY → NULL
    stationvalues = stationvalues.astype(float)
    prediction = prediction.astype(float)

    # Stations may contain NaN → convert to strings with empty string for NULL
    stations_series = pd.Series(stations.flatten(), dtype="Float64")
    stations_str = stations_series.astype("Int64").astype("string").fillna("")
    stations_str = np.asarray(stations_str).reshape(stations.shape)

    # Build coordinates
    y, x = np.indices(stations.shape)

    # Build DataFrame
    df = pd.DataFrame({
        "time": time_val,
        "y": y.flatten(),
        "x": x.flatten(),
        "station": stations_str.flatten(),
        "station_value": stationvalues.flatten(),
        "prediction": prediction.flatten(),
    })

    # Prepare CSV in memory
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False, header=False, na_rep="")  # empty string for NULL
    csv_buffer.seek(0)

    try:
        # psycopg v3: use cursor.copy
        with psycopg.connect("dbname=netcf user=testuser password=12345 host=localhost") as conn:
            with conn.cursor() as cur:
                with cur.copy("COPY grid_cells (time, y, x, station, station_value, prediction) FROM STDIN WITH CSV") as copy:
                    copy.write(csv_buffer.read())
        print("Done:", filename)
    except Exception as e:
        print("Error during COPY:", e)

def load_directory(directory: str):
    for name in sorted(os.listdir(directory)):
        if name.endswith(".nc"):
            load_file_fast(os.path.join(directory, name))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Load NetCDF files in postgres database.")
    parser.add_argument("directory", help="Directory containing .nc files")

    args = parser.parse_args()

    load_directory(args.directory)