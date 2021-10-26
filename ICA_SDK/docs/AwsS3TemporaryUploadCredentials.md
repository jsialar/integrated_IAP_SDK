# AwsS3TemporaryUploadCredentials

Defines the credentials for uploading to Amazon Simple Storage Service (Amazon S3). This definition matches the Upload Credentials API model of the Genomic Data Store (GDS) service.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | Access key for use with AWS S3 | [optional] 
**secret_access_key** | **str** | Secret key for use with AWS S3 | [optional] 
**session_token** | **str** | Token for use with AWS S3 | [optional] 
**region** | **str** | AWS region the folder will/does reside in | [optional] 
**bucket_name** | **str** | AWS bucket the folder will/does reside in | [optional] 
**key_prefix** | **str** | AWS upload location for this folder | [optional] 
**expiration_date** | **datetime** | expiration for temporary credentials | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


