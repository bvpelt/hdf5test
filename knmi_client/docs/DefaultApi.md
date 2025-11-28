# openapi_client.DefaultApi

All URIs are relative to *https://api.dataplatform.knmi.nl/open-data*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_files**](DefaultApi.md#download_files) | **GET** /v1/datasets/{datasetName}/versions/{versionId}/files/{filename}/url | Get a temporary download URL for a dataset file
[**list_files**](DefaultApi.md#list_files) | **GET** /v1/datasets/{datasetName}/versions/{versionId}/files | Get paginated list of files for dataset


# **download_files**
> FileDownload download_files(dataset_name, version_id, filename)

Get a temporary download URL for a dataset file

Get a temporary download URL for a dataset file

### Example

* Api Key Authentication (APIKeyHeader):

```python
import openapi_client
from openapi_client.models.file_download import FileDownload
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dataplatform.knmi.nl/open-data
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dataplatform.knmi.nl/open-data"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    dataset_name = '10-minute-in-situ-meteorological-observations' # str | Name of the dataset
    version_id = '1.0' # str | Version of the dataset
    filename = 'KMDS__OPER_P___10M_OBS_L2_202212102330.nc' # str | Name of the file

    try:
        # Get a temporary download URL for a dataset file
        api_response = api_instance.download_files(dataset_name, version_id, filename)
        print("The response of DefaultApi->download_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->download_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**| Name of the dataset | 
 **version_id** | **str**| Version of the dataset | 
 **filename** | **str**| Name of the file | 

### Return type

[**FileDownload**](FileDownload.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Access-Control-Allow-Origin - The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given origin. <br>  * X-KNMI-Deprecation - Specifies if the dataset is deprecated. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_files**
> ListFilesResponse list_files(dataset_name, version_id, max_keys=max_keys, sorting=sorting, order_by=order_by, begin=begin, end=end, next_page_token=next_page_token, start_after_filename=start_after_filename)

Get paginated list of files for dataset

Get paginated list of files for dataset

### Example

* Api Key Authentication (APIKeyHeader):

```python
import openapi_client
from openapi_client.models.list_files_response import ListFilesResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dataplatform.knmi.nl/open-data
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dataplatform.knmi.nl/open-data"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    dataset_name = '10-minute-in-situ-meteorological-observations' # str | Name of the dataset
    version_id = '1.0' # str | Version of the dataset
    max_keys = 10 # int | Maximum number of files to return (optional) (default to 10)
    sorting = asc # str | Sort the files in ascending or descending order (optional) (default to asc)
    order_by = filename # str | Order the files by filename, timestamp of creation or timestamp of last modification (optional) (default to filename)
    begin = 'begin_example' # str | This parameter controls filtering (together with end). It defines the lower limit of the requested data. If ordering by filename, provide a string. If ordering by lastModified or created, provide a timestamp in ISO8601 format with a timezone (e.g. 2022-01-01T00:00:00Z). (optional)
    end = 'end_example' # str | This parameter controls filtering (together with begin). It defines the upper limit of the requested data. If ordering by filename, provide a string. If ordering by lastModified or created, provide a timestamp in ISO8601 format with a timezone (e.g. 2022-01-01T00:00:00Z). (optional)
    next_page_token = 'next_page_token_example' # str | Token to retrieve the next page of results. This token is returned by the API if the result set is larger than the maximum number of files to return. (optional)
    start_after_filename = 'start_after_filename_example' # str | Provide a filename to start listing after. Note: This deprecated parameter cannot be combined with orderBy, begin, end or sorting. Instead, use `nextPageToken`. (optional)

    try:
        # Get paginated list of files for dataset
        api_response = api_instance.list_files(dataset_name, version_id, max_keys=max_keys, sorting=sorting, order_by=order_by, begin=begin, end=end, next_page_token=next_page_token, start_after_filename=start_after_filename)
        print("The response of DefaultApi->list_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**| Name of the dataset | 
 **version_id** | **str**| Version of the dataset | 
 **max_keys** | **int**| Maximum number of files to return | [optional] [default to 10]
 **sorting** | **str**| Sort the files in ascending or descending order | [optional] [default to asc]
 **order_by** | **str**| Order the files by filename, timestamp of creation or timestamp of last modification | [optional] [default to filename]
 **begin** | **str**| This parameter controls filtering (together with end). It defines the lower limit of the requested data. If ordering by filename, provide a string. If ordering by lastModified or created, provide a timestamp in ISO8601 format with a timezone (e.g. 2022-01-01T00:00:00Z). | [optional] 
 **end** | **str**| This parameter controls filtering (together with begin). It defines the upper limit of the requested data. If ordering by filename, provide a string. If ordering by lastModified or created, provide a timestamp in ISO8601 format with a timezone (e.g. 2022-01-01T00:00:00Z). | [optional] 
 **next_page_token** | **str**| Token to retrieve the next page of results. This token is returned by the API if the result set is larger than the maximum number of files to return. | [optional] 
 **start_after_filename** | **str**| Provide a filename to start listing after. Note: This deprecated parameter cannot be combined with orderBy, begin, end or sorting. Instead, use &#x60;nextPageToken&#x60;. | [optional] 

### Return type

[**ListFilesResponse**](ListFilesResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Access-Control-Allow-Origin - The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given origin. <br>  * X-KNMI-Deprecation - Specifies if the dataset is deprecated. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

