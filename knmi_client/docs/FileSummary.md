# FileSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | 
**last_modified** | **str** |  | 
**size** | **int** |  | 
**created** | **str** |  | 

## Example

```python
from openapi_client.models.file_summary import FileSummary

# TODO update the JSON string below
json = "{}"
# create an instance of FileSummary from a JSON string
file_summary_instance = FileSummary.from_json(json)
# print the JSON string representation of the object
print(FileSummary.to_json())

# convert the object into a dict
file_summary_dict = file_summary_instance.to_dict()
# create an instance of FileSummary from a dict
file_summary_from_dict = FileSummary.from_dict(file_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


