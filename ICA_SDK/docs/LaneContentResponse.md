# LaneContentResponse

Defines the API response model that represents the libraries and library pools contained in one lane of the sequencing run
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lane_number** | **int** | Number of the lane | [optional] 
**library_pool** | [**LibraryPoolCompact**](LibraryPoolCompact.md) |  | [optional] 
**library_pool_name** | **str** | Name of library pool the lane contains | [optional] 
**library_pool_urn** | **str** | URN of library pool the lane contains | [optional] 
**lane_libraries** | [**list[LaneLibraryResponse]**](LaneLibraryResponse.md) | Libraries and related information the lane contains | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


