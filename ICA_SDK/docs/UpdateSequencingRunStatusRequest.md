# UpdateSequencingRunStatusRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_status** | **str** | Verification status updated while the stage is completing | [optional] 
**verification_status_summary** | **str** | Detailed summary of verification status | [optional] 
**instrument_run_status** | **str** | Instrument run status updated by the instrument control software while the stage is completing | [optional] 
**instrument_run_status_summary** | **str** | Detailed summary of instrument run status provided by instrument | [optional] 
**instrument_analysis_status** | **str** | Instrument analysis status updated by the instrument control software while the stage is completing | [optional] 
**instrument_analysis_status_summary** | **str** | Detailed summary of instrument analysis status provided by instrument | [optional] 
**upload_status_summary** | **str** | Detailed summary of upload progress provided by instrument | [optional] 
**verification_progress** | **str** | Progress of the verification stage | [optional] 
**instrument_progress** | **str** | Progress of the instrument stage | [optional] 
**sequencing_progress** | **str** | Progress of the sequencing stage | [optional] 
**instrument_analysis_progress** | **str** | Progress of the instrument analysis stage | [optional] 
**upload_progress** | **str** | Progress of the upload stage | [optional] 
**failure_reason** | **str** | Reason for reported failure | [optional] 
**needs_attention** | **bool** | True if the run should be marked as needing attention for user, false otherwise | [optional] 
**needs_attention_reason** | **str** | Reason why the run needs attention | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


