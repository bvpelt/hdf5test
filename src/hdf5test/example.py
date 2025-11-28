import requests
from hdf5test.knmi_api import list_files, download_files

# KNMI example dataset
DATASET = "10-minute-in-situ-meteorological-observations"
VERSION = "1.0"

print("Listing files...")
resp = list_files(DATASET, VERSION, maxKeys=5)

print(resp)


for f in resp.files:
    filename = f.filename
    print("Retrieving file:", filename)

    # Step 1: Request temporary download URL
    dl = download_files(DATASET, VERSION, filename)

    # Step 2: Download file bytes
    url = dl.temporary_download_url
    r = requests.get(url)
    r.raise_for_status()

    # Step 3: Write file to disk
    with open(filename, "wb") as fout:
        fout.write(r.content)

    print("Saved", filename, "(", len(r.content), "bytes )")