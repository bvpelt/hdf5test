from knmi_client.openapi_client import ApiClient, Configuration
from knmi_client.openapi_client.api.default_api import DefaultApi

API_KEY = "eyJvcmciOiI1ZTU1NGUxOTI3NGE5NjAwMDEyYTNlYjEiLCJpZCI6IjA1YmFmNTQ0NTllZjRiYmNhNDMxNTA1MThmMzUyZDMzIiwiaCI6Im11cm11cjEyOCJ9"

config = Configuration()
config.api_key["Authorization"] = API_KEY
config.api_key_prefix["Authorization"] = "Apikey"

api = DefaultApi(ApiClient(config))

resp = api.get_v1_datasets_dataset_name_versions_version_id_files(
    dataset_name="Tx1",
    version_id="2",
    max_keys=10,
)

print(resp)
