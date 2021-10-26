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
**supported_instrument_platform_and_types** | [**list[InstrumentPlatformAndTypesResponse]**](InstrumentPlatformAndTypesResponse.md) | Supported Instrument Platforms and Types of the analysis | [optional] 
**status** | **str** | Status of this version of analysis definition | [optional] 
**analysis_type** | **str** | Analysis type of this version of analysis definition | [optional] 
**is_dragen** | **bool** | Indicate whether an analysis is a DRAGEN analysis or not | [optional] 
**analysis_settings** | [**object**](.md) | Settings for the analysis (at the global analysis level) | [optional] 
**settings** | [**AnalysisVersionDefinitionSettings**](AnalysisVersionDefinitionSettings.md) |  | [optional] 
**skip_analysis_section** | **bool** | Skip analysis section in generated sample sheets | [optional] 
**analysis_sample_settings** | [**object**](.md) | Per-sample settings for the analysis (at the per-sample level) | [optional] 
**on_render_require_run_contents** | **bool** | Whether the OnRenderFunction depends on RunContents or not | [optional] 
**analysis_definition** | [**AnalysisDefinitionCompact**](AnalysisDefinitionCompact.md) |  | [optional] 
**checksum** | **str** | Stores the checksum of AnalysisVersionDefinition | [optional] 
**sub_tenant_id** | **str** | Organizational or Workgroup ID. If neither are present, User ID. | [optional] 
**acl** | **list[str]** | Access control list of the object | [optional] 
**compatible_library_prep_kits** | [**list[LibraryPrepKitCompact]**](LibraryPrepKitCompact.md) | The library preparation kits that are compatible with this version of analysis definition  (possibly inherited from parent analysis definition if there is no compatible kits defined in analysis definition version level) | [optional] 
**compatible_library_prep_kits_defined_for_version** | [**list[LibraryPrepKitCompact]**](LibraryPrepKitCompact.md) | The library preparation kits that are compatible with this version of analysis definition that is defined in analysis definition version level | [optional] 
**supported_genomes** | [**list[GenomeCompact]**](GenomeCompact.md) | The optional list of genomes that are supported by this analysis definition version | [optional] 
**excluded_genomes** | [**list[GenomeCompact]**](GenomeCompact.md) | The optional list of genomes that are excluded by this analysis definition version | [optional] 
**on_submit_function** | **str** | Logic for validating and transforming AnalysisSettings and AnalysisSampleSettings | [optional] 
**on_render_function** | **str** | Logic for dynamically rendering AVD settings and AVD setting configurations | [optional] 
**tenant_id** | **str** | Unique identifier for the resource tenant | [optional] 
**tenant_name** | **str** | Unique tenant name for the resource tenant | [optional] 
**created_by_client_id** | **str** | ClientId that created the resource (bssh, stratus...) | [optional] 
**created_by** | **str** | User that created the resource | [optional] 
**modified_by** | **str** | User that last modified the resource | [optional] 
**time_created** | **datetime** | Time (in UTC) the resource was created | [optional] 
**time_modified** | **datetime** | Time (in UTC) the resource was modified | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


