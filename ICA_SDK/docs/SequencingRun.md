# SequencingRun

Data contract for the full sequencing run

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique object ID | [optional] 
**urn** | **str** | URN of the object | [optional] 
**href** | **str** | HREF to the object | [optional] 
**run_origin** | **str** | Origin of the run data (Instrument, InstrumentPostRunUpload, Simulated, etc.) | [optional] 
**regulatory_mode** | **str** | Regulatory mode of the run | [optional] 
**instrument_run_id** | **str** | Run ID typically generated by instrument (not guaranteed to be unique for either tenant or system) | [optional] 
**external_run_id** | **str** | ID of the sequencing run in another system | [optional] 
**run_name** | **str** | User-supplied name of the experiment/run (not guaranteed to be unique for either tenant or system) | [optional] 
**description** | **str** | User-supplied description of the run | [optional] 
**is_planned** | **bool** | Indicates with value &#39;true&#39; when the run is in the planning stage (including while locked and assigned to an instrument) | [optional] 
**aggregate_run_status** | **str** | Overall status of the run across all stages, including the status of post-upload cloud processing | [optional] 
**verification_status** | **str** | Status of the verification stage | [optional] 
**verification_status_summary** | **str** | Summary of the current status of the run | [optional] 
**verification_completed** | **bool** | Indicates with value &#39;true&#39; when the verification stage completes | [optional] 
**verification_time_started** | **datetime** | Time when the verification stage started | [optional] 
**verification_time_completed** | **datetime** | Time when the run fully completed on the instrument (if set, this marks the end of the verification stage) | [optional] 
**instrument_run_status** | **str** | Status of the instrument run stage | [optional] 
**instrument_run_status_summary** | **str** | Summary of the current status of the run | [optional] 
**instrument_run_completed** | **bool** | Indicates with value &#39;true&#39; when the instrument run stage completes | [optional] 
**instrument_run_time_started** | **datetime** | Time when the instrument run stage started | [optional] 
**instrument_run_time_completed** | **datetime** | Time when the run fully completed on the instrument (if set, this marks the end of the instrument run stage) | [optional] 
**instrument_completed** | **bool** | Indicates with value &#39;true&#39; when the instrument sub-stage completes | [optional] 
**instrument_time_started** | **datetime** | Time when the instrument starts active work on the run (marks the start of the instrument sub-stage) | [optional] 
**instrument_time_completed** | **datetime** | Time when the instrument completes active work on the run (excluding background file upload) | [optional] 
**sequencing_completed** | **bool** | Indicates with value &#39;true&#39; when the sequencing sub-stage completes | [optional] 
**sequencing_time_started** | **datetime** | Time when the sequencing sub-stage started | [optional] 
**sequencing_time_completed** | **datetime** | Time when the sequencing sub-stage completed | [optional] 
**instrument_analysis_status** | **str** | Status of the on-instrument analysis software | [optional] 
**instrument_analysis_status_summary** | **str** | Summary of the instrument analysis status | [optional] 
**instrument_analysis_performed** | **bool** | Indicates with value &#39;true&#39; if instrument analysis is being performed for the run | [optional] 
**instrument_analysis_completed** | **bool** | Indicates with value &#39;true&#39; when the instrument analysis sub-stage completes | [optional] 
**instrument_analysis_time_started** | **datetime** | Time when the analysis starts on the instrument (marks the start of instrument analysis sub-stage) | [optional] 
**instrument_analysis_time_completed** | **datetime** | Time when the analysis completed on the instrument | [optional] 
**run_upload_status** | **str** | Status of data upload from instrument | [optional] 
**run_upload_status_summary** | **str** | Detailed summary of run upload status/progress | [optional] 
**run_upload_completed** | **bool** | Indicates with value &#39;true&#39; when the run upload sub-stage completes | [optional] 
**run_upload_time_started** | **datetime** | Time when the data upload starts (marks the start of upload sub-stage) | [optional] 
**run_upload_time_completed** | **datetime** | Time when the run upload sub-stage completed | [optional] 
**is_failed** | **bool** | Indicates whether the run failed | [optional] 
**run_failure_type** | **str** | Indicates with value &#39;true&#39; if the run failed during active processing by the instrument | [optional] 
**run_failure_reason** | **str** | Specifies the reason why the run failure occurred | [optional] 
**needs_attention** | **bool** | Indicates with value &#39;true&#39; if the run needs attention | [optional] 
**needs_attention_reason** | **str** | Reason why the run needs attention | [optional] 
**is_aborted** | **bool** | Indicates with value &#39;true&#39; that the run was stopped, canceled, or aborted | [optional] 
**is_timed_out** | **bool** | Indicates with value &#39;true&#39; if the run timed out | [optional] 
**prep_kit_info** | [**SequencingRunPrepKitInfo**](SequencingRunPrepKitInfo.md) |  | [optional] 
**genome_info** | [**SequencingRunGenomeInfo**](SequencingRunGenomeInfo.md) |  | [optional] 
**flow_cell_barcode** | **str** | Barcode of the flow cell used in the sequencing run | [optional] 
**input_container_identifier** | **str** | Input container identifier used in the sequencing run | [optional] 
**consumables** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Information (such as barcodes) about consumables (such as reagents, buffers, etc.) used in the sequencing run | [optional] 
**run_mode** | **str** | Describes the analysis and proactive data that is uploaded and processed in the cloud | [optional] 
**instrument_run_number** | **int** | Records the number of runs performed on a specific instrument | [optional] 
**sample_sheet_name** | **str** | Name of the sample sheet file | [optional] 
**data_volume_urn** | **str** | URN of the data volume where run data is stored | [optional] 
**data_folder_urn** | **str** | URN of the data folder where run data is stored | [optional] 
**data_folder_volume_path** | **str** | Path with volume of the data folder where run data is stored | [optional] 
**total_size** | **int** | Total size of the run data files in bytes when the run data was first uploaded | [optional] 
**locked_by** | **str** | User that locked the sequencing run | [optional] 
**started_by** | **str** | User that started the sequencing run | [optional] 
**time_locked** | **datetime** | Time (in UTC) the sequencing run was locked | [optional] 
**is_locked** | **bool** | Specifies whether or not the sequencing run has been locked | [optional] 
**config** | [**SequencingRunConfiguration**](SequencingRunConfiguration.md) |  | [optional] 
**instrument** | [**Instrument**](Instrument.md) |  | [optional] 
**instrument_type_snapshot** | **str** | Instrument type snapshot when the run is locked or started | [optional] 
**instrument_software_version** | **str** | Version of instrument control software provided by the instrument when the run starts | [optional] 
**analysis_location** | **str** | Indicate the sequencing run will be performing local analysis or cloud analysis | [optional] 
**analysis_summaries** | [**[SequencingRunAnalysisSummary]**](SequencingRunAnalysisSummary.md) | Configured analysis summary information | [optional] 
**run_analysis_settings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Run analysis settings | [optional] 
**is_favorite** | **bool** | Indicate whether the sequencing run is set as favorite run for the user | [optional] 
**external_location** | **str** | Stores the external location of the sequencing run | [optional] 
**checksum_of_manifest** | **str** | Stores the checksum of manifest  Used to verify run contents copied from external location | [optional] 
**requeued_from_run** | [**SequencingRunCompact**](SequencingRunCompact.md) |  | [optional] 
**requeue_reason** | **str** | Reason for Requeue Analysis of a sequencing run | [optional] 
**tenant_id** | **str** | Unique identifier for the resource tenant | [optional] 
**sub_tenant_id** | **str** | Organizational or Workgroup ID. If neither are present, User ID. | [optional] 
**acl** | **[str]** | Access control list of the object | [optional] 
**run_parameters_xml** | **str** | The content of the instrument RunParameters.xml file generated when sequencing run starts | [optional] 
**run_info_xml** | **str** | Content of the instrument RunInfo.xml file, generated in XML format when sequencing run starts | [optional] 
**created_by_client_id** | **str** | ClientId that created the resource (bssh, stratus...) | [optional] 
**created_by** | **str** | User that created the resource | [optional] 
**modified_by** | **str** | User that last modified the resource | [optional] 
**time_created** | **datetime** | Time (in UTC) the resource was created | [optional] 
**time_modified** | **datetime** | Time (in UTC) the resource was modified | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

