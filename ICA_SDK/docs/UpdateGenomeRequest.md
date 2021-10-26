# UpdateGenomeRequest

Request to update a genome
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the genome | [optional] 
**display_name** | **str** | DisplayName of the genome | [optional] 
**order** | **int** | Order of the genome | [optional] 
**is_application_specific** | **bool** | Whether the genome is application specific | [optional] 
**build** | **str** | Build of the genome | [optional] 
**organization** | **str** | Organization of the genome | [optional] 
**description** | **str** | Description of the genome | [optional] 
**status** | **str** | Status of the genome | [optional] 
**species** | **str** | Species of the genome | [optional] 
**source** | **str** | Source of the genome | [optional] 
**dragen_version** | **str** | Dragen version for the genome, it is required when Illumina.GenomicSequencingService.Models.Domain.UpdateGenomeParameters.GenomeFormat is Dragen | [optional] 
**data_location_urn** | **str** | Urn of the file in GDS containing the genome data file | [optional] 
**genome_format** | **str** | Format for the genome file, Illumina.GenomicSequencingService.Models.Domain.UpdateGenomeParameters.DragenVersion is required when it is Dragen | [optional] 
**settings** | [**object**](.md) | Custom settings for the genome | [optional] 
**source_file_metadata** | [**object**](.md) | Key-value pairs that indicate the source files for the specific genome | [optional] 
**acl** | **list[str]** |  | [optional] 
**fasta_file_urn** | **str** | Urn of the Fasta file being used by the genome | [optional] 
**checksum** | **str** | Checksum of Genome | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


