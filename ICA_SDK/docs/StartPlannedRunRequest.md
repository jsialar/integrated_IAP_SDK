# StartPlannedRunRequest

Request to start a planned run

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_run_id** | **str** | Run ID typically generated by instrument (not guaranteed to be unique for either request token or system) | 
**instrument_run_status** | **str** | Instrument run status, provided by the instrument control software | 
**flow_cell_barcode** | **str** | Barcode of the flow cell used in the sequencing run | 
**consumables** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Information (e.g. barcodes) about consumables (e.g. reagents or buffers) used in the sequencing run | 
**run_mode** | **str** | Method by which analysis data is uploaded and process in the cloud | 
**run_parameters_xml** | **str** | Content of the instrument RunParameters.xml file, generated in XML format when sequencing run starts | 
**instrument_run_number** | **int** | Number that records the number of runs that have been performed on a specific instrument | 
**instrument_software_version** | **str** | Version of instrument control software provided by the instrument when the run starts | 
**sample_sheet_name** | **str** | Name of the sample sheet file. Sample sheets are not always required for all instrument types | [optional] 
**run_name** | **str** | Name of the run | [optional] 
**run_info_xml** | **str** | Content of the instrument RunInfo.xml file, generated in XML format when sequencing run starts | [optional] 
**description** | **str** | Description of the run | [optional] 
**external_location** | **str** | Stores the external location of the sequencing run | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

