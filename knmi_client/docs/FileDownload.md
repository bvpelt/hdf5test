# FileDownload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  | 
**size** | **str** |  | 
**last_modified** | **str** |  | 
**temporary_download_url** | **str** |  | 

## Example

```python
from openapi_client.models.file_download import FileDownload

# TODO update the JSON string below
json = "{}"
# create an instance of FileDownload from a JSON string
file_download_instance = FileDownload.from_json(json)
# print the JSON string representation of the object
print(FileDownload.to_json())

# convert the object into a dict
file_download_dict = file_download_instance.to_dict()
# create an instance of FileDownload from a dict
file_download_from_dict = FileDownload.from_dict(file_download_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


