# CreatePlannedRunRequest

Request to create a sequencing run plan
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_configuration** | [**CreateSequencingRunConfigurationRequest**](CreateSequencingRunConfigurationRequest.md) |  | 
**run_contents** | [**UpdateSequencingRunContentsRequest**](UpdateSequencingRunContentsRequest.md) |  | [optional] 
**run_analysis_configurations** | [**list[CreateSequencingRunAnalysisConfigurationRequest]**](CreateSequencingRunAnalysisConfigurationRequest.md) | Run analysis configurations | [optional] 
**is_favorite** | **bool** | Set the run as favorite runs | [optional] 
**acl** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


