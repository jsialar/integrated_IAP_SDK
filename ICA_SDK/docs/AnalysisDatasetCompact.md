# AnalysisDatasetCompact

Data contract for analysis dataset (compact)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique object ID | [optional] 
**urn** | **str** | URN of the object | [optional] 
**href** | **str** | HREF to the object | [optional] 
**name** | **str** | Name of the analysis dataset | [optional] 
**display_name** | **str** | Display name of the analysis dataset | [optional] 
**analysis_run** | [**SequencingAnalysisRunCompact**](SequencingAnalysisRunCompact.md) |  | [optional] 
**task_run_id** | **str** | Task run id of the analysis dataset | [optional] 
**workflow_run_id** | **str** | Workflow run id of the analysis dataset | [optional] 
**lane_number** | **int** | Lane number associated with the analysis dataset | [optional] 
**data_folder_urn** | **str** | Data folder urn of the analysis dataset | [optional] 
**data_folder_volume_path** | **str** | Data folder volume path of the analysis dataset | [optional] 
**attributes** | [**object**](.md) | Attributes of the analysis dataset | [optional] 
**analysis_dataset_type** | [**AnalysisDatasetTypeCompact**](AnalysisDatasetTypeCompact.md) |  | [optional] 
**type** | **str** | Type of the analysis dataset | [optional] 
**qc_status** | **str** | QC status of the analysis dataset | [optional] 
**qc_status_summary** | **str** | QC summary of the analysis dataset | [optional] 
**file_urns** | **list[str]** | FileUrns of the AnalysisDataset resource | [optional] 
**external_id** | **str** | External ID of the dataset | [optional] 
**input_samples** | [**list[SampleCompact]**](SampleCompact.md) | Input samples of the analysis dataset | [optional] 
**sub_tenant_id** | **str** | Organizational or Workgroup ID. If neither are present, User ID. | [optional] 
**acl** | **list[str]** | Access control list of the object | [optional] 
**tenant_id** | **str** | Unique identifier for the resource tenant | [optional] 
**tenant_name** | **str** | Unique tenant name for the resource tenant | [optional] 
**created_by_client_id** | **str** | ClientId that created the resource (bssh, stratus...) | [optional] 
**created_by** | **str** | User that created the resource | [optional] 
**modified_by** | **str** | User that last modified the resource | [optional] 
**time_created** | **datetime** | Time (in UTC) the resource was created | [optional] 
**time_modified** | **datetime** | Time (in UTC) the resource was modified | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


