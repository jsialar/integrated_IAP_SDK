# SequencingRunAnalysisConfiguration

Data contract for the full sequencing run analysis configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique object ID | [optional] 
**urn** | **str** | URN of the object | [optional] 
**href** | **str** | HREF to the object | [optional] 
**sequencing_run** | [**SequencingRunCompact**](SequencingRunCompact.md) |  | [optional] 
**sample_settings** | [**[SequencingRunAnalysisSampleConfigurationCompact]**](SequencingRunAnalysisSampleConfigurationCompact.md) | User provided per-sample settings for this analysis configuration. | [optional] 
**name** | **str** | Name of the analysis configuration | [optional] 
**description** | **str** | Description of the analysis configuration | [optional] 
**settings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | User-provided analysis-level settings for this analysis configuration | [optional] 
**sample_settings_snapshot** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Snapshot of user provided per-sample settings for this analysis configuration. | [optional] 
**original_settings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Original User-provided analysis-level settings for this analysis configuration | [optional] 
**original_sample_settings_snapshot** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Original Snapshot of user provided per-sample settings for this analysis configuration. | [optional] 
**analysis_version** | [**AnalysisVersionDefinitionCompact**](AnalysisVersionDefinitionCompact.md) |  | [optional] 
**tenant_id** | **str** | Unique identifier for the resource tenant | [optional] 
**sub_tenant_id** | **str** | Organizational or Workgroup ID. If neither are present, User ID. | [optional] 
**acl** | **[str]** | Access control list of the object | [optional] 
**created_by_client_id** | **str** | ClientId that created the resource (bssh, stratus...) | [optional] 
**created_by** | **str** | User that created the resource | [optional] 
**modified_by** | **str** | User that last modified the resource | [optional] 
**time_created** | **datetime** | Time (in UTC) the resource was created | [optional] 
**time_modified** | **datetime** | Time (in UTC) the resource was modified | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

