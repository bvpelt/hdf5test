import os
from knmi_client import ApiClient, Configuration
from knmi_client.api.default_api import DefaultApi

API_KEY = os.getenv("KNMI_API_KEY", "")

def _get_client():
    config = Configuration()
    config.api_key["Authorization"] = API_KEY
    config.api_key_prefix["Authorization"] = "Apikey"
    return DefaultApi(ApiClient(config))

def list_files(
    dataset="10-minute-in-situ-meteorological-observations",
    version="1.0",
):
    api = _get_client()
    return api.get_v1_datasets_dataset_name_versions_version_id_files(
        dataset_name=dataset,
        version_id=version,
        max_keys=10,
    )

def download_url(dataset, version, filename):
    api = _get_client()
    return api.get_v1_datasets_dataset_name_versions_version_id_files_filename_url(
        dataset_name=dataset,
        version_id=version,
        filename=filename
    )
