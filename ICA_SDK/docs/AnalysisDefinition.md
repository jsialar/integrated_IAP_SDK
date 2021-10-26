# AnalysisDefinition

Data contract for an analysis definition
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique object ID | [optional] 
**urn** | **str** | URN of the object | [optional] 
**href** | **str** | HREF to the object | [optional] 
**compatible_library_prep_kits** | [**list[LibraryPrepKitCompact]**](LibraryPrepKitCompact.md) | The library preparation kits that are compatible with this analysis definition | [optional] 
**name** | **str** | Name of the analysis definition | [optional] 
**organization** | **str** | Organization owning the analysis definition | [optional] 
**is_illumina** | **bool** | Indicates whether or not the current analysis definition is from Illumina | [optional] 
**description** | **str** | Description of the analysis definition | [optional] 
**status** | **str** | Status of the analysis definition | [optional] 
**illumina_kit_support_mode** | **str** | Illumina Kit Support Mode | [optional] 
**regulatory_mode** | **str** | Regulatory mode of the analysis definition | [optional] 
**display_name** | **str** | User-friendly name of the analysis definition | [optional] 
**analysis_versions** | [**AnalysisVersionDefinitionCompactItemList**](AnalysisVersionDefinitionCompactItemList.md) |  | [optional] 
**checksum** | **str** | Stores the checksum of AnalysisDefinition | [optional] 
**sub_tenant_id** | **str** | Organizational or Workgroup ID. If neither are present, User ID. | [optional] 
**acl** | **list[str]** | Access control list of the object | [optional] 
**tenant_id** | **str** | Unique identifier for the resource tenant | [optional] 
**tenant_name** | **str** | Unique tenant name for the resource tenant | [optional] 
**created_by_client_id** | **str** | ClientId that created the resource (bssh, stratus...) | [optional] 
**created_by** | **str** | User that created the resource | [optional] 
**modified_by** | **str** | User that last modified the resource | [optional] 
**time_created** | **datetime** | Time (in UTC) the resource was created | [optional] 
**time_modified** | **datetime** | Time (in UTC) the resource was modified | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


