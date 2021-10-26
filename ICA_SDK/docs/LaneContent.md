# LaneContent

Defines the API model that represents the library or library pool that one lane in the sequencing run contains
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lane_number** | **int** | Optional number of the lane. If not provided, it implies that the contents are the same across all lanes | [optional] 
**same_as_lane_number** | **int** | Indicates that the content of this lane is the same as that of the previously-defined lane | [optional] 
**adapter_sequence_read1** | **str** | Default Adapter sequence read 1 for this lane | [optional] 
**adapter_sequence_read2** | **str** | Default Adapter sequence read 2 for this lane | [optional] 
**lane_libraries** | [**list[LaneLibrary]**](LaneLibrary.md) | Information about the samples and libraries the lane contains | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


