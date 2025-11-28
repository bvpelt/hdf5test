import requests
from hdf5test.knmi_api import list_files, download_files

DATASET = "Tx1"
VERSION = "2"

next_token = None

while True:
    resp = list_files(DATASET, VERSION, maxKeys=5, nextPageToken=next_token)

    for f in resp.files:
        print("Retrieving:", f.filename)

        # Step 1: Get temporary download URL
        dl = download_files(DATASET, VERSION, f.filename)

        # Step 2: Stream file to disk
        r = requests.get(dl.temporary_download_url)
        r.raise_for_status()

        with open(f.filename, "wb") as outfile:
            outfile.write(r.content)

        print("Saved", f.filename)

    if not resp.next_page_token:
        break

    next_token = resp.next_page_token
