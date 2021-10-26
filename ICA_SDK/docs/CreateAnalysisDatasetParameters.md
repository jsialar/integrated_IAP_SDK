# CreateAnalysisDatasetParameters

Data transfer object (DTO) for creating an analysis dataset
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Optional name of the analysis dataset. Must be unique in tenant if provided | [optional] 
**display_name** | **str** | Optional display name of the analysis dataset | [optional] 
**external_id** | **str** | External ID to associate with the analysis dataset | [optional] 
**task_run_id** | **str** | Optional Task run id of the analysis dataset | [optional] 
**workflow_run_id** | **str** | Optional Workflow run id of the analysis dataset | [optional] 
**lane_number** | **int** | Optional Lane number associated with the analysis dataset | [optional] 
**data_folder_urn** | **str** | Data folder urn of the analysis dataset | [optional] 
**data_folder_volume_path** | **str** | VolumeName + path of the DataFolder | [optional] 
**attributes** | [**object**](.md) | Attributes of the analysis dataset | [optional] 
**type** | **str** | Type of the analysis dataset | [optional] 
**qc_status** | **str** | QC status of the analysis dataset | [optional] 
**qc_status_summary** | **str** | QC summary of the analysis dataset | [optional] 
**file_urns** | **list[str]** | FileUrns (or FileIds) of the AnalysisDataset | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


