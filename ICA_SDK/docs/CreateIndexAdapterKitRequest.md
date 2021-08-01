# CreateIndexAdapterKitRequest

Request to create an index adapter kit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the kit | 
**allowed_index_strategies** | **[str]** | Allowed index strategies | 
**display_name** | **str** | User-friendly name of the kit | [optional] 
**organization** | **str** | Organization owning the kit | [optional] 
**description** | **str** | Description of the kit | [optional] 
**adapter_sequence_read1** | **str** | Optional read 1 adapter sequence | [optional] 
**adapter_sequence_read2** | **str** | Optional read 2 adapter sequence | [optional] 
**settings** | [**IndexAdapterKitSettings**](IndexAdapterKitSettings.md) |  | [optional] 
**index_sequences** | [**[IndexSequence]**](IndexSequence.md) | Index sequence mappings | [optional] 
**skip_index_diversity_validation** | **bool** | Flag to skip index diversity validation | [optional] 
**acl** | **[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


