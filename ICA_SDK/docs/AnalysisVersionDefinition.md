# AnalysisVersionDefinition

Data contract for analysis version definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique object ID | [optional] 
**urn** | **str** | URN of the object | [optional] 
**href** | **str** | HREF to the object | [optional] 
**version** | **str** | Version of analysis definition | [optional] 
**description** | **str** | Description of this version of analysis definition | [optional] 
**supported_instrument_platform_and_types** | [**[InstrumentPlatformAndTypesResponse]**](InstrumentPlatformAndTypesResponse.md) | Supported Instrument Platforms and Types of the analysis | [optional] 
**status** | **str** | Status of this version of analysis definition | [optional] 
**analysis_type** | **str** | Analysis type of this version of analysis definition | [optional] 
**is_dragen** | **bool** | Indicate whether an analysis is a DRAGEN analysis or not | [optional] 
**analysis_settings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Settings for the analysis (at the global analysis level) | [optional] 
**settings** | [**AnalysisVersionDefinitionSettings**](AnalysisVersionDefinitionSettings.md) |  | [optional] 
**skip_analysis_section** | **bool** | Skip analysis section in generated sample sheets | [optional] 
**analysis_sample_settings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Per-sample settings for the analysis (at the per-sample level) | [optional] 
**on_render_require_run_contents** | **bool** | Whether the OnRenderFunction depends on RunContents or not | [optional] 
**analysis_definition** | [**AnalysisDefinitionCompact**](AnalysisDefinitionCompact.md) |  | [optional] 
**tenant_id** | **str** | Unique identifier for the resource tenant | [optional] 
**sub_tenant_id** | **str** | Organizational or Workgroup ID. If neither are present, User ID. | [optional] 
**acl** | **[str]** | Access control list of the object | [optional] 
**compatible_library_prep_kits** | [**[LibraryPrepKitCompact]**](LibraryPrepKitCompact.md) | The library preparation kits that are compatible with this version of analysis definition  (possibly inherited from parent analysis definition if there is no compatible kits defined in analysis definition version level) | [optional] 
**compatible_library_prep_kits_defined_for_version** | [**[LibraryPrepKitCompact]**](LibraryPrepKitCompact.md) | The library preparation kits that are compatible with this version of analysis definition that is defined in analysis definition version level | [optional] 
**supported_genomes** | [**[GenomeCompact]**](GenomeCompact.md) | The optional list of genomes that are supported by this analysis definition version | [optional] 
**excluded_genomes** | [**[GenomeCompact]**](GenomeCompact.md) | The optional list of genomes that are excluded by this analysis definition version | [optional] 
**on_submit_function** | **str** | Logic for validating and transforming AnalysisSettings and AnalysisSampleSettings | [optional] 
**on_render_function** | **str** | Logic for dynamically rendering AVD settings and AVD setting configurations | [optional] 
**created_by_client_id** | **str** | ClientId that created the resource (bssh, stratus...) | [optional] 
**created_by** | **str** | User that created the resource | [optional] 
**modified_by** | **str** | User that last modified the resource | [optional] 
**time_created** | **datetime** | Time (in UTC) the resource was created | [optional] 
**time_modified** | **datetime** | Time (in UTC) the resource was modified | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


