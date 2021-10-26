# Library

Data contract for the full library
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique object ID | [optional] 
**urn** | **str** | URN of the object | [optional] 
**href** | **str** | HREF to the object | [optional] 
**name** | **str** | Name of the library | [optional] 
**description** | **str** | Description of the library | [optional] 
**status** | **str** | Status of the library | [optional] 
**index_container_position** | **str** | The container position (well or plate+well position) for the library that is using index adapter kit with fixed index position | [optional] 
**index1_name** | **str** | Index 1 name | [optional] 
**index2_name** | **str** | Index 2 name | [optional] 
**index1_sequence** | **str** | Index 1 sequence used for this library | [optional] 
**index2_sequence** | **str** | Index 2 sequence used for this library | [optional] 
**adapter_sequence_read1** | **str** | Adapter sequence read 1 | [optional] 
**adapter_sequence_read2** | **str** | Adapter sequence read 2 | [optional] 
**sample** | [**SampleCompact**](SampleCompact.md) |  | [optional] 
**library_prep_kit** | [**LibraryPrepKitCompact**](LibraryPrepKitCompact.md) |  | [optional] 
**index_adapter_kit** | [**IndexAdapterKitCompact**](IndexAdapterKitCompact.md) |  | [optional] 
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


