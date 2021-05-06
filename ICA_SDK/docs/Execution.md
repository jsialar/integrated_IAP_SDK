# Execution


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**Image**](Image.md) |  | [optional] 
**command** | **str** |  | [optional] 
**args** | **[str]** | Argument to run specified task | [optional] 
**inputs** | [**[InputMountMappingWithCreds]**](InputMountMappingWithCreds.md) | Path (Inputs) - Path to mount file at valid Url  URL (Inputs) - Url of file mounted at specified path | [optional] 
**outputs** | [**[MountMappingWithCreds]**](MountMappingWithCreds.md) | Path (Outputs) - Path where files will be output to valid Url  URL (Outputs) - Url of folder with files from the path will be uploaded | [optional] 
**system_files** | [**SystemFiles**](SystemFiles.md) |  | [optional] 
**environment** | [**Environment**](Environment.md) |  | [optional] 
**working_directory** | **str** |  | [optional] 
**retry_limit** | **int** |  | [optional]  if omitted the server will use the default value of 3
**retry_count** | **int** |  | [optional]  if omitted the server will use the default value of 0

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


