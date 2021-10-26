# LaneLibrary

Defines the API model that represents the sample content in the lane
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_name** | **str** | Sample name. This field is case-insensitive. | [optional] 
**sample_urn** | **str** | Sample URN | [optional] 
**project_name** | **str** | Name of the project the sample belongs to.  Note: This field is an alias of DataAggregationGroup field until DataAggregationGroups is deprecated. | [optional] 
**library_name** | **str** | Library name. This field is case-insensitive. | [optional] 
**library_urn** | **str** | Library URN | [optional] 
**adapter_sequence_read1** | **str** | Adapter sequence read 1 | [optional] 
**adapter_sequence_read2** | **str** | Adapter sequence read 2 | [optional] 
**index1_sequence** | **str** | Index 1 sequence of the library | [optional] 
**index2_sequence** | **str** | Index 2 sequence of the library | [optional] 
**index_container_position** | **str** | The container position (well or plate+well position) for the library that is using an index adapter kit with fixed index position | [optional] 
**index1_name** | **str** | Name of index 1 sequence | [optional] 
**index2_name** | **str** | Name of index 2 sequence | [optional] 
**library_prep_kit_urn** | **str** | URN of library prep kit | [optional] 
**index_adapter_kit_urn** | **str** | URN of index adapter kit | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


