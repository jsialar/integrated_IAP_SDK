# ReplaceSequencingStatsRequest

Request to update sequencing stats of a sequencing run

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cycle_number** | **int** |  | 
**run_sequencing_stats** | [**RunSequencingStats**](RunSequencingStats.md) |  | [optional] 
**lane_sequencing_stats** | [**[LaneSequencingStats]**](LaneSequencingStats.md) | List of LaneSequencingStats of the run | [optional] 
**read_sequencing_stats** | [**[ReadSequencingStats]**](ReadSequencingStats.md) | List of ReadSequencingStats of the run | [optional] 
**lane_by_read_sequencing_stats** | [**[LaneByReadSequencingStats]**](LaneByReadSequencingStats.md) | List of LaneByReadSequencingStats of the run | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


