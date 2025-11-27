# ListFilesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_truncated** | **bool** |  | 
**files** | [**List[FileSummary]**](FileSummary.md) |  | 
**result_count** | **int** |  | 
**max_results** | **int** |  | 
**start_after_filename** | **str** |  | 
**next_page_token** | **str** |  | 

## Example

```python
from openapi_client.models.list_files_response import ListFilesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListFilesResponse from a JSON string
list_files_response_instance = ListFilesResponse.from_json(json)
# print the JSON string representation of the object
print(ListFilesResponse.to_json())

# convert the object into a dict
list_files_response_dict = list_files_response_instance.to_dict()
# create an instance of ListFilesResponse from a dict
list_files_response_from_dict = ListFilesResponse.from_dict(list_files_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


