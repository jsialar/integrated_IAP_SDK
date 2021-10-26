# RenderAnalysisVersionDefinitionResponse

Response of rendering an analysis version definition
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validation_errors** | [**list[RenderMessage]**](RenderMessage.md) | List of rendered message with errors | [optional] 
**validation_warnings** | [**list[RenderMessage]**](RenderMessage.md) | List of rendered message with warnings | [optional] 
**analysis_version_definition** | [**AnalysisVersionDefinitionCompact**](AnalysisVersionDefinitionCompact.md) |  | [optional] 
**run_analysis_configuration** | [**CreateSequencingRunAnalysisConfigurationRequest**](CreateSequencingRunAnalysisConfigurationRequest.md) |  | [optional] 
**changed_setting_ids** | **list[str]** | List of changed ids of analysis version definition settings | [optional] 
**changed_setting_value_ids** | **list[str]** | List of changed ids of run analysis configuration setting values | [optional] 
**changed_sample_setting_ids** | **list[str]** | List of changed ids of analysis version definition sample settings | [optional] 
**changed_sample_setting_value_ids** | [**object**](.md) | Array of samples with list of changed sample setting value ids | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


