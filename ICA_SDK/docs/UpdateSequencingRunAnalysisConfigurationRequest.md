# UpdateSequencingRunAnalysisConfigurationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the analysis configuration | [optional] 
**description** | **str** | Description of the analysis configuration | [optional] 
**analysis_version_definition_id** | **str** | The ID of the analysis version definition on which this analysis configuration is based | [optional] 
**settings** | [**object**](.md) | User-provided analysis-level settings for this analysis configuration (validated against the analysis version definition) | [optional] 
**sample_settings** | [**list[SampleSettingEntry]**](SampleSettingEntry.md) | User provided per-sample settings for this analysis configuration  These must follow the schema described in the analysis version definition | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


