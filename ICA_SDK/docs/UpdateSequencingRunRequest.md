# UpdateSequencingRunRequest

Request to update an existing sequencing run resource. Metadata update must follow these rules:  (1) If the run originates from instrument, metadata update is not permitted after instrument run starts.  (2) If the run originates from upload, metadata update is not permitted after upload starts.  (3) If the run is locked, metadata update is only permitted by the user who locked the run.  Note that Description update is not constrained by these rules.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_name** | **str** | User-provided name of the experiment/run  Not guaranteed to be unique for either request token or system  If null or undefined, existing value is left as is  Any other non-null values are used to update the RunName field of the run  This property is considered metadata, and is restricted by metadata update rules | [optional] 
**description** | **str** | User-provided description of the experiment/run  If null or undefined, existing value is left as is  Any other non-null values are used to update the RunName field of the run  This property is NOT considered metadata, and is not restricted by metadata update rules  If the run is locked, description may only be updated by the user who locked the run | [optional] 
**prep_kit_info** | [**SequencingRunPrepKitInfo**](SequencingRunPrepKitInfo.md) |  | [optional] 
**flow_cell_barcode** | **str** | The barcode of the FlowCell used in the sequencing run.  If null or undefined, existing value is left as is  Any other non-null values are used to update the RunName field of the run  This property is considered metadata, and is restricted by metadata update rules | [optional] 
**input_container_identifier** | **str** | Input container identifier used in the sequencing run | [optional] 
**consumables** | [**object**](.md) | Information (such as barcodes) of the consumables (such as reagents, buffers, ...) used in the sequencing run.  If null or undefined, existing value is left as is  Any other non-null values are used to update the RunName field of the run  This property is considered metadata, and is restricted by metadata update rules | [optional] 
**sample_sheet_name** | **str** | Name of the sample sheet file  If null or undefined, existing value is left as is  Any other non-null values are used to update the RunName field of the run  This property is considered metadata, and is restricted by metadata update rules | [optional] 
**is_favorite** | **bool** | Set the run as favorite runs | [optional] 
**acl** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


