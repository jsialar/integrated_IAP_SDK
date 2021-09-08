# AwsS3PostPolicy

POST Policy as a credential for uploading using POST

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | **str** | A base64 policy to restrict uploads with expiry time and for a given key prefix | [optional] 
**signature** | **str** | Signature for the upload operation | [optional] 
**credential** | **str** | Credential for the upload | [optional] 
**algorithm** | **str** | This is AWS4-HMAC-SHA256 | [optional] 
**date** | **str** | The current upload date | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


