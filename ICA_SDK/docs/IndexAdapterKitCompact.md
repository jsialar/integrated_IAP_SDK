# IndexAdapterKitCompact

Defines the data contract for index adapter kit compact
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique object ID | [optional] 
**urn** | **str** | URN of the object | [optional] 
**href** | **str** | HREF to the object | [optional] 
**name** | **str** | Name of the kit | [optional] 
**display_name** | **str** | User-friendly name of the kit | [optional] 
**organization** | **str** | Name of organization owning the kit | [optional] 
**is_illumina** | **bool** | Indicates whether or not the current index adapter kit is from Illumina | [optional] 
**description** | **str** | Description of the kit | [optional] 
**allowed_index_strategies** | **list[str]** | List of allowed index strategies | [optional] 
**adapter_sequence_read1** | **str** | Read 1 adapter sequence | [optional] 
**adapter_sequence_read2** | **str** | Read 2 adapter sequence | [optional] 
**settings** | [**IndexAdapterKitSettingsResponse**](IndexAdapterKitSettingsResponse.md) |  | [optional] 
**checksum** | **str** | Stores the checksum of IndexAdapterKit | [optional] 
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


