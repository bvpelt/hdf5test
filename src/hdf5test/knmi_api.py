from openapi_client import ApiClient, Configuration
from openapi_client.api.default_api import DefaultApi
import re
import os

def get_config():
    """
    Build the OpenAPI client configuration including the KNMI API key.
    The API key is expected in environment variable KNMI_API_KEY.
    """
    api_key = os.getenv("KNMI_API_KEY")

    if not api_key:
        raise RuntimeError("Missing KNMI_API_KEY environment variable")

    config = Configuration()

    # If KNMI requires: Authorization: ApiKey <token>
    # then split or prefix accordingly.
    config.api_key["APIKeyHeader"] = api_key

    # If "Bearer <token>" is required, enable this:
    # config.api_key_prefix["Authorization"] = "Bearer"

    return config


def list_files(dataset_name: str, version_id: str, **kwargs):
    """
    Wrapper around the KNMI list-files endpoint.
    """
    config = get_config()
    kwargs = fix_kwargs(kwargs)

    with ApiClient(config) as client:
        api = DefaultApi(client)
        return api.list_files(
            dataset_name=dataset_name,
            version_id=version_id,
            **kwargs
        )


def download_files(dataset_name: str, version_id: str, filename: str):
    """
    Wrapper around the KNMI download-url endpoint.
    """
    config = get_config()

    with ApiClient(config) as client:
        api = DefaultApi(client)
        return api.download_files(
            dataset_name=dataset_name,
            version_id=version_id,
            filename=filename
        )


def camel_to_snake(name):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def fix_kwargs(kwargs):
    return {camel_to_snake(k): v for k, v in kwargs.items()}
