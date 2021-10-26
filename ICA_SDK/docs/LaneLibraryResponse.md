# LaneLibraryResponse

Defines the compact response model for library content in the lane
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_name** | **str** | Sample name | [optional] 
**sample_urn** | **str** | Sample URN | [optional] 
**data_aggregation_group** | **str** | Data aggregation group of the sample | [optional] 
**project_name** | **str** | Project Name of the sample  Note: This field is an alias of DataAggregationGroup field until DataAggregationGroups is deprecated. | [optional] 
**library_name** | **str** | Library name | [optional] 
**library_urn** | **str** | Library URN | [optional] 
**adapter_sequence_read1** | **str** | Read 1 adapter sequence | [optional] 
**adapter_sequence_read2** | **str** | Read 2 adapter sequence | [optional] 
**index_container_position** | **str** | The container position (well or plate+well position) for the library that is using index adapter kit with fixed index position | [optional] 
**index1_sequence** | **str** | Index 1 sequence  of the library | [optional] 
**index2_sequence** | **str** | Index 2 sequence of the library | [optional] 
**index1_name** | **str** | Name of index 1 sequence | [optional] 
**index2_name** | **str** | Name of index 2 sequence | [optional] 
**library_prep_kit_name** | **str** | Name of library prep kit | [optional] 
**library_prep_kit_urn** | **str** | URN of library prep kit | [optional] 
**index_adapter_kit_name** | **str** | Name of index adapter kit | [optional] 
**index_adapter_kit_urn** | **str** | URN of index adapter kit | [optional] 
**adapter_behavior** | **str** | Adapter behavior for this entry | [optional] 
**override_cycles** | **str** | Override cycles for this entry | [optional] 
**library** | [**LibraryCompact**](LibraryCompact.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


