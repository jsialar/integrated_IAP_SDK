# RequeueSequencingRunAnalysisRequest

Request for requeue sequencing run analysis
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_name** | **str** | Name of the run provided by the user | 
**run_contents** | [**UpdateSequencingRunContentsRequest**](UpdateSequencingRunContentsRequest.md) |  | [optional] 
**run_analysis_configurations** | [**list[CreateSequencingRunAnalysisConfigurationRequest]**](CreateSequencingRunAnalysisConfigurationRequest.md) | Requeue run analysis configurations | [optional] 
**requeue_reason** | **str** | Reason for requeue of a sequencing run | [optional] 
**replace_existing_run_requeue** | **bool** | Indicates replacement of existing run requeue | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


