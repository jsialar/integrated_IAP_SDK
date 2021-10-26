# CreateLibraryPrepKitRequest

Request to create a library prep kit
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the library prep kit | 
**display_name** | **str** | User-friendly name of the library prep kit | [optional] 
**organization** | **str** | Organization from where the library prep kit originated (e.g. Illumina) | [optional] 
**description** | **str** | Description of the library prep kit | [optional] 
**allowed_read_types** | **list[str]** | Reads types allowed for the library prep kit | 
**default_read1_length** | **int** | Default read 1 length | [optional] 
**default_read2_length** | **int** | Default read 2 length | [optional] 
**is_application_specific** | **bool** | Whether the library prep kit is application specific | [optional] 
**settings** | [**LibraryPrepKitSettings**](LibraryPrepKitSettings.md) |  | [optional] 
**checksum** | **str** | Checksum of LibraryPrepKit | [optional] 
**index_adapter_kit_ids** | **list[str]** | Array of index adapter kit IDs that are compatible with the library prep kit | [optional] 
**acl** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


