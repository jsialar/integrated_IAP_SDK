# SequencingAnalysisRunResults

Data contract for analysis run results

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**demuxing_results** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Demuxing results of the analysis run | [optional] 
**analysis_results** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Analysis results of the analysis run | [optional] 
**launch_parameters_snapshot** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Snapshot of the analysis launch parameters | [optional] 
**sample_mapping** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Sample mapping of the analysis run | [optional] 
**sample_sheet_snapshot** | **str** | Snapshot of the sample sheet used in the analysis | [optional] 
**created_by** | **str** | User that created the resource | [optional] 
**modified_by** | **str** | User that last modified the resource | [optional] 
**time_created** | **datetime** | Time (in UTC) the resource was created | [optional] 
**time_modified** | **datetime** | Time (in UTC) the resource was modified | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


