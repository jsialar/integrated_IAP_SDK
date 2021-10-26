# WorkflowMetadataDto

Workflow meta data
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_type** | **str** | Workflow type  We always force it to be nextflow for now | [optional] 
**workflow_url** | **str** | Points to the workflow definition | [optional] 
**volume_size_in_gigabytes** | **int** | The volume size limitation for the analysis output | [optional] 
**tags** | [**object**](.md) | A JSON object that can be used to pass metadata to the workflow | [optional] 
**workflow_params** | [**object**](.md) | Workflow parameters with key/value pairs  A JSON object that allows the definition to provide hard coded parameters to the workflow  These get merged with the parameters provided to the workflow via user settings | [optional] 
**workflow_resources_folder** | **str** | Optional resources folder configured for the workflow | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


