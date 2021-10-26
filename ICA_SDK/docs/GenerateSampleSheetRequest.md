# GenerateSampleSheetRequest

Request to generate a sample sheet
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_configuration** | [**CreateSequencingRunConfigurationRequest**](CreateSequencingRunConfigurationRequest.md) |  | 
**run_contents** | [**UpdateSequencingRunContentsRequest**](UpdateSequencingRunContentsRequest.md) |  | [optional] 
**run_analysis_configurations** | [**list[CreateSequencingRunAnalysisConfigurationRequest]**](CreateSequencingRunAnalysisConfigurationRequest.md) | Run analysis configurations | [optional] 
**include** | **list[str]** | Include flags to specify what is included in the response | [optional] 
**exclude_kit_urns** | **bool** | Exclude prep kits URNs for generated sample sheet | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


