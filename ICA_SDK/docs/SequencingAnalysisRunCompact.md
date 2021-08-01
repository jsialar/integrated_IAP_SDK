# SequencingAnalysisRunCompact

Data contract for sequencing analysis run (compact)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique object ID | [optional] 
**urn** | **str** | URN of the object | [optional] 
**href** | **str** | HREF to the object | [optional] 
**name** | **str** | Name of the sequencing analysis run | [optional] 
**status** | **str** | Status of the sequencing analysis run | [optional] 
**workflow_run_id** | **str** | Id of the associated WorkflowRun of the sequencing analysis run on WES | [optional] 
**workflow_version_name** | **str** | The name of the associated WorkflowVersion of the sequencing analysis run on WES | [optional] 
**workflow_version_id** | **str** | The id of the associated WorkflowVersion of the sequencing analysis run on WES | [optional] 
**analysis_data_folder_urn** | **str** | Urn of AnalysisDataFolder of the sequencing analysis run on GDS | [optional] 
**analysis_data_volume_urn** | **str** | Urn of AnalysisDataVolume of the sequencing analysis run on GDS | [optional] 
**analysis_data_folder_volume_path** | **str** | Combination of GDS volume and path of AnalysisDataFolder of the sequencing analysis run | [optional] 
**external_id** | **str** | External ID of the sequencing analysis run | [optional] 
**sequencing_run** | [**SequencingRunCompact**](SequencingRunCompact.md) |  | [optional] 
**needs_attention** | **bool** | Indicates with value &#39;true&#39; if the analysis run needs attention | [optional] 
**needs_attention_reason** | **str** | Detail reason why the analysis run needs attention | [optional] 
**tenant_id** | **str** | Unique identifier for the resource tenant | [optional] 
**sub_tenant_id** | **str** | Organizational or Workgroup ID. If neither are present, User ID. | [optional] 
**acl** | **[str]** | Access control list of the object | [optional] 
**created_by_client_id** | **str** | ClientId that created the resource (bssh, stratus...) | [optional] 
**created_by** | **str** | User that created the resource | [optional] 
**modified_by** | **str** | User that last modified the resource | [optional] 
**time_created** | **datetime** | Time (in UTC) the resource was created | [optional] 
**time_modified** | **datetime** | Time (in UTC) the resource was modified | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

