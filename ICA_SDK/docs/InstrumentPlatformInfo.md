# InstrumentPlatformInfo

Information about InstrumentPlatform
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_platform** | **str** | Instrument Platform | [optional] 
**display_name** | **str** | Display name of instrument platform | [optional] 
**run_planning_supported** | **bool** | Indicate if run planning is supported | [optional] 
**cloud_orchestration_supported** | **bool** | Indicate if cloud orchestration is supported | [optional] 
**require_instrument_type** | **bool** | Indicate if require instrument type for planned run | [optional] 
**max_number_of_lanes** | **int** | Maximum Number of lanes supported by instrument type/platform | [optional] 
**supported_analysis_locations** | **list[str]** | Analysis Location Supported by instrument type/platform | [optional] 
**configure_flowcell_type** | **bool** | Indicate if instrument allow configuring flow cell type | [optional] 
**flow_cell_types** | [**list[FlowCellType]**](FlowCellType.md) | Indicate flow cell configuration for instrument (Optional) | [optional] 
**read1_length_min** | **int** | Minimum Read 1 Length | [optional] 
**read1_length_max** | **int** | Maximum Read 1 Length | [optional] 
**read2_length_min** | **int** | Minimum Read 2 Length | [optional] 
**read2_length_max** | **int** | Maximum Read 2 Length | [optional] 
**multi_analysis_configuration** | [**MultiAnalysisConfiguration**](MultiAnalysisConfiguration.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


