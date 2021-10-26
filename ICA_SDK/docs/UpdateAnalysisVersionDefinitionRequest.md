# UpdateAnalysisVersionDefinitionRequest

Request to create an analysis version definition
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Version of the analysis version definition | [optional] 
**supported_instrument_platform_and_types** | [**list[SupportedInstrumentPlatformAndTypes]**](SupportedInstrumentPlatformAndTypes.md) | The instrument platform and instrument type supported by the analysis  If not specified, support all platforms and types | [optional] 
**description** | **str** | Description of this version of analysis definition | [optional] 
**status** | **str** | Status of the analysis version definition | [optional] 
**analysis_type** | **str** | Analysis type of this version | [optional] 
**skip_analysis_section** | **bool** | Controls whether the sample sheet has an analysis-specific section for this analysis. If true, do not  include the analysis-specific section. | [optional] 
**is_dragen** | **bool** | Analysis type of this version of the analysis definition | [optional] 
**supported_genome_ids** | **list[str]** | Array of genome IDs that are supported by this version of analysis definition | [optional] 
**excluded_genome_ids** | **list[str]** | Array of genome IDs that are not supported by this version of analysis definition | [optional] 
**library_prep_kit_ids** | **list[str]** | Array of library prep kit IDs that are compatible with this version of analysis definition | [optional] 
**analysis_settings** | [**object**](.md) | Settings for the analysis (at the global analysis level) | [optional] 
**analysis_sample_settings** | [**object**](.md) | Per-sample settings for the analysis (at the per-sample level) | [optional] 
**on_submit_function** | **str** | Logic for validating and transforming AnalysisSettings and AnalysisSampleSettings | [optional] 
**on_render_function** | **str** | Logic for dynamically rendering AVD settings and AVD setting configurations | [optional] 
**on_render_require_run_contents** | **bool** | Defines whether the analysis fields should be changed based on input of run contents  This is to avoid unnecessary huge input from UI that is not really needed during rendering | [optional] 
**settings** | [**AnalysisVersionDefinitionSettings**](AnalysisVersionDefinitionSettings.md) |  | [optional] 
**checksum** | **str** | Checksum of AnalysisVersionDefinition | [optional] 
**acl** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


