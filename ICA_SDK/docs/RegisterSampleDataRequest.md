# RegisterSampleDataRequest

Request to register data associated with the given sample
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip_copy_files_to_project_volume** | **bool** | Optional. If true, skip copying files to the project volume if the ProjectName matches a known project context | [optional] 
**total_sample_count** | **int** | Total number of samples that are being registered as part of the same ExternalAnalysisRunId | [optional] 
**total_dataset_count** | **int** | Total number of datasets that are being registered as part of the same ExternalAnalysisRunId | [optional] 
**sample_id** | **str** | Optional Sample Id of the sample (if name based matching is not being used) | [optional] 
**sample_name** | **str** | Optional name of the sample (when identifying sample by Name+ProjectName) | [optional] 
**project_name** | **str** | ProjectName of the sample (when identifying sample by Name+ProjectName) | [optional] 
**external_sample_id** | **str** | Optional external ID to associate with the sample (only when a new sample is being created) | [optional] 
**external_project_id** | **str** | Optional external ID for the project associated with the sample (only when a new sample is being created) | [optional] 
**external_analysis_run_id** | **str** | Optional external Id for the analysis run | [optional] 
**analysis_datasets** | [**list[CreateAnalysisDatasetParameters]**](CreateAnalysisDatasetParameters.md) | One or more analysis datasets that should be associated with the analysis | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


