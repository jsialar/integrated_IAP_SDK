# RunSetupValidation

Data transfer object (DTO) for the Settings.RunSetupValidation field of a validated analysis version definition
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**require_unique_sample_ids_per_lane** | **bool** | If true, the workflow requires unique sampleId values in each lane and does not support repeated sampleIds  in a given lane with different index sequences | [optional] 
**enable_custom_prep_kits** | **bool** | If true the workflow allows custom prep kits. If false, the workflow requires that all prep kits used are in  the list of compatible prep kits defined by the analysis. | [optional] 
**read1_length_min** | **int** | Minimum value for read1 length | [optional] 
**read1_length_max** | **int** | Maximum value for read1 length | [optional] 
**read2_length_min** | **int** | Minimum value for read2 length | [optional] 
**read2_length_max** | **int** | Maximum value for read2 length | [optional] 
**allowed_index_strategies** | **list[str]** | Selected index strategy must match one of these values. Provided run contents must match. | [optional] 
**allowed_read_types** | **list[str]** | Read type selection must match one of these values. | [optional] 
**allow_deviations** | **bool** | If true, the UI should allow deviations from default read length specified in prep kit,  index strategies and read types (does not apply to unique sample IDs per lane or custom kits) | [optional] 
**deviation_warning_message** | **str** | Desired warning message when deviations are detected | [optional] 
**custom_prep_kit_warning_message** | **str** | Desired warning message when using a custom kit (not part of the compatible kits) | [optional] 
**skip_validate_index_cycles_with_index_sequence_lengths** | **bool** | If true, skip index sequence length validation against run configured index cycles | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


