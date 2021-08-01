# ParseSampleSheetRequest

Request to parse a sample sheet to sequencing run

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **[str]** | Include flags to specify what is included in the response | [optional] 
**sample_sheet_content** | **str** | The csv string of the sample sheet | [optional] 
**resolve_prep_kits** | **bool** | If true, resolve prep kit information from sample sheet if possible | [optional] 
**resolve_prep_kits_by_name** | **bool** | If true, attempt to resolve prep kits by name if they cannot be resolved using URN column | [optional] 
**resolve_index_sequence_info** | **bool** | If true, attempt to resolve index sequence info like Index Name and Position based on the index sequences | [optional] 
**enable_warnings_for_missing_cloud_sections** | **bool** | Enable warnings if cloud sections are not provided | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


