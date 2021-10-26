# DirectUploadCredentials

Defines the credentials for uploading to GDS directly
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** | Optional path prefix for all file uploads using these credentials. Should be prepended to relative path | [optional] 
**volume_name** | **str** | Name of the volume for the file uploads | [optional] 
**expiration_date** | **datetime** | Optional expiration date for the credentials or null if they don&#39;t expire | [optional] 
**file_creation_api_path** | **str** | API path for the file creation endpoint (relative to base URL) | [optional] 
**file_upload_api_path** | **str** | API path for the file upload endpoint (relative to base URL) | [optional] 
**upload_id** | **str** | File upload id, used to upload file | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


