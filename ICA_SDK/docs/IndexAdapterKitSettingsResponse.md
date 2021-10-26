# IndexAdapterKitSettingsResponse

Custom settings for an index adapter kit
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_index_strategy** | **str** | Default index strategy for index adapter kit | [optional] 
**override_cycles** | **str** | Override cycles settings for index adapter kit | [optional] 
**fixed_layout** | **bool** | Indicates if the index adapter kit is a fixed layout kit | [optional] 
**multiplate** | **bool** | Indicates if the index adapter kit is a multi-plate fixed layout kit | [optional] 
**multiple_indexes_per_well** | **bool** | Indicates if the index adapter kit supports multiple indices in one well | [optional] 
**fixed_index_positions** | **list[str]** | Fixed layout index positions for this index adapter kit  Format: \&quot;{[Plate-]Well[-IndexesCount]}/{Index1Name}[-{Index2Name}]\&quot; | [optional] 
**enable_custom_index_cycles** | **bool** | Indicates if the UI will display a checkbox to enable users to enter custom index cycles for the kit | [optional] 
**num_cycles_index1_override** | **int** | Indicates if the UI should use this value as the default Index1Cycles entry | [optional] 
**num_cycles_index2_override** | **int** | Indicates if the UI should use this value as the default Index2Cycles entry | [optional] 
**fixed_layout_position_key_by_index_id** | **bool** | Indicates the container position for FixedLayout is based on IndexId | [optional] 
**custom_bcl_convert_settings** | **dict(str, str)** | Custom BCL Convert settings of the IndexAdapterKit | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


