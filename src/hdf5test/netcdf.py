import os
import xarray as xr
import pandas as pd

def inspect_netcdf_directory(directory: str, output_md="summary.md", output_csv="summary.csv"):
    """
    Scan all NetCDF (.nc) files in a directory and generate a Markdown and CSV summary.
    """
    rows = []
    md_lines = []

    md_lines.append("# NetCDF Dataset Summary\n")

    for filename in sorted(os.listdir(directory)):
        if not filename.endswith(".nc"):
            continue

        path = os.path.join(directory, filename)
        md_lines.append(f"\n## File: {filename}\n")

        try:
            ds = xr.open_dataset(path)
        except Exception as e:
            md_lines.append(f"❌ Could not open file: {e}\n")
            continue

        # --- Global attributes ---
        md_lines.append("### Global Attributes")
        if ds.attrs:
            for key, val in ds.attrs.items():
                md_lines.append(f"- **{key}**: {val}")
        else:
            md_lines.append("(none)")

        # --- Dimensions ---
        md_lines.append("\n### Dimensions")
        for dim, size in ds.dims.items():
            md_lines.append(f"- **{dim}**: {size}")

        # --- Variables ---
        md_lines.append("\n### Variables")
        for var_name, var in ds.data_vars.items():
            shape = tuple(var.shape)
            units = var.attrs.get("units", "-")
            long_name = var.attrs.get("long_name", "-")

            md_lines.append(f"- **{var_name}** (shape={shape}, units='{units}', desc='{long_name}')")

            rows.append({
                "file": filename,
                "variable": var_name,
                "shape": str(shape),
                "units": units,
                "description": long_name
            })

        ds.close()

    # Write markdown file
    with open(output_md, "w") as f:
        f.write("\n".join(md_lines))

    # Write CSV file
    df = pd.DataFrame(rows)
    df.to_csv(output_csv, index=False)

    print(f"✅ Summary written to {output_md} and {output_csv}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Scan and summarize NetCDF files.")
    parser.add_argument("directory", help="Directory containing .nc files")
    parser.add_argument("--md", default="summary.md", help="Output Markdown file")
    parser.add_argument("--csv", default="summary.csv", help="Output CSV file")

    args = parser.parse_args()

    inspect_netcdf_directory(args.directory, args.md, args.csv)
