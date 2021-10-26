# UpdateLibraryRequest

Request to update a library
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the library. This field is case-insensitive. | [optional] 
**description** | **str** | Description of the library | [optional] 
**status** | **str** | Status of the library | [optional] 
**library_prep_kit_id** | **str** | ID of the library prep kit used to prepare the library | [optional] 
**index_adapter_kit_id** | **str** | ID of the index kit used to prepare the library | [optional] 
**index_container_position** | **str** | The container position (well or plate+well position) for the library that is using an index adapter kit with fixed index position | [optional] 
**index1_name** | **str** | Index 1 name | [optional] 
**index2_name** | **str** | Index 2 name | [optional] 
**index1_sequence** | **str** | Index 1 sequence | [optional] 
**index2_sequence** | **str** | Index 2 sequence | [optional] 
**adapter_sequence_read1** | **str** | Adapter sequence read 1 | [optional] 
**adapter_sequence_read2** | **str** | Adapter sequence read 2 | [optional] 
**acl** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


