# CreateSequencingRunConfigurationRequest

Request to create a sequencing run configuration
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_type** | **str** | Type of instrument for which the run is planned  Recognized values include:  iSeq100, MiniSeq,  MiSeq, MiSeqDx,  NextSeq, NextSeqDx,  HiSeq1000, HiSeq1500, HiSeq2000, HiSeq2500, HiSeq3000, HiSeq4000, HiSeqX  NovaSeq5000, NovaSeq6000. | [optional] 
**instrument_platform** | **str** | Platform of instrument for which the run is planned  Recognized values include:  NextSeq, HiSeq, MiSeq, Eco, iScan, HiSeqX, NeoPrep, MiniSeq, NovaSeq, iSeq, TruSightNIPT, NextSeq1k2k  No value entered is treated as the instrument platform of input InstrumentType | [optional] 
**run_name** | **str** | Name of the run  Must not be null, empty, or consist only of white-space characters | 
**description** | **str** | Description of the run | [optional] 
**regulatory_mode** | **str** | Regulatory mode of the run, default is RUO | [optional] 
**num_cycles_read1** | **int** | Number of cycles in read 1   Must not be a negative value | 
**num_cycles_read2** | **int** | Number of cycles in read 2  Must not be a negative value | 
**read_type** | **str** | Read type of the run | 
**num_cycles_index1** | **int** | Number of cycles in index 1  Must not be a negative value | 
**num_cycles_index2** | **int** | Number of cycles in index 2  Must not be a negative value | 
**use_custom_primer_for_read1** | **bool** | Value indicating whether read 1 uses custom primer | [optional] 
**use_custom_primer_for_read2** | **bool** | Value indicating whether read 2 uses custom primer | [optional] 
**use_custom_primer_for_index1** | **bool** | Value indicating whether index 1 uses custom primer. | [optional] 
**use_custom_primer_for_index2** | **bool** | A value indicating whether index 2 uses custom primer | [optional] 
**input_container_identifier** | **str** | Input container identifier for planned run | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


