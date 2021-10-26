# LibraryPrepKitCompact

Data contract for library prep kit (compact)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique object ID | [optional] 
**urn** | **str** | URN of the object | [optional] 
**href** | **str** | HREF to the object | [optional] 
**display_name** | **str** | User-friendly name of the library prep kit | [optional] 
**name** | **str** | Name of the LibraryPrepKit | [optional] 
**organization** | **str** | Organization from which the kit originated, e.g. illumina | [optional] 
**is_illumina** | **bool** | Indicate whether the current library prep kit is from illumina or not. | [optional] 
**description** | **str** | Description of the library prep kit | [optional] 
**allowed_read_types** | **list[str]** | Indicates the types of reads that are allowed for this library prep kit | [optional] 
**default_read1_length** | **int** | Default read 1 length | [optional] 
**default_read2_length** | **int** | Default read 2 length | [optional] 
**is_application_specific** | **bool** | Whether the library prep kit is application specific | [optional] 
**settings** | [**LibraryPrepKitSettingsResponse**](LibraryPrepKitSettingsResponse.md) |  | [optional] 
**checksum** | **str** | Stores the checksum of LibraryPrepKit | [optional] 
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


