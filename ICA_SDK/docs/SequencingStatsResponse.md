# SequencingStatsResponse

Defines the API response model that represents the sequencing stats
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cycle_number** | **int** |  | [optional] 
**run_sequencing_stats** | [**RunSequencingStatsResponse**](RunSequencingStatsResponse.md) |  | [optional] 
**lane_sequencing_stats** | [**list[LaneSequencingStatsResponse]**](LaneSequencingStatsResponse.md) | List of LaneSequencingStats of the run | [optional] 
**read_sequencing_stats** | [**list[ReadSequencingStatsResponse]**](ReadSequencingStatsResponse.md) | List of ReadSequencingStats of the run | [optional] 
**lane_by_read_sequencing_stats** | [**list[LaneByReadSequencingStatsResponse]**](LaneByReadSequencingStatsResponse.md) | List of LaneByReadSequencingStats of the run | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


