# GenomeCompact

Data contract for genome (compact)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique object ID | [optional] 
**urn** | **str** | URN of the object | [optional] 
**href** | **str** | HREF to the object | [optional] 
**name** | **str** | Name of the genome | [optional] 
**display_name** | **str** | DisplayName of the genome | [optional] 
**order** | **int** | Order of the genome | [optional] 
**organization** | **str** | Organization of the genome, Require gss.genomes.admin scope to set Organization to a value containing  Illumina (case-insensitive) | [optional] 
**description** | **str** | Description of the genome | [optional] 
**status** | **str** | Status of the genome | [optional] 
**species** | **str** | Species of the genome | [optional] 
**source** | **str** | Source of the genome | [optional] 
**build** | **str** | Build of the genome | [optional] 
**dragen_version** | **str** | Dragen version for the genome, it is required when Illumina.GenomicSequencingService.Models.V1.GenomeCompact.GenomeFormat is Dragen | [optional] 
**data_location_urn** | **str** | Urn of the file in GDS containing the genome data file | [optional] 
**genome_format** | **str** | Format for the genome file, Illumina.GenomicSequencingService.Models.V1.GenomeCompact.DragenVersion is required when it is Dragen | [optional] 
**settings** | [**object**](.md) | Custom settings for the genome | [optional] 
**source_file_metadata** | [**object**](.md) | Key-value pairs that indicate the source files for the specific genome | [optional] 
**fasta_file_urn** | **str** | The Fasta file Urn being used by the genome | [optional] 
**is_application_specific** | **bool** | Whether the genome is application specific | [optional] 
**is_illumina** | **bool** | Whether the genome is belonging to Illumina | [optional] 
**checksum** | **str** | Stores the checksum of Genome | [optional] 
**sub_tenant_id** | **str** | Organizational or Workgroup ID. If neither are present, User ID. | [optional] 
**acl** | **list[str]** | Access control list of the object | [optional] 
**tenant_id** | **str** | Unique identifier for the resource tenant | [optional] 
**tenant_name** | **str** | Unique tenant name for the resource tenant | [optional] 
**created_by_client_id** | **str** | ClientId that created the resource (bssh, stratus...) | [optional] 
**created_by** | **str** | User that created the resource | [optional] 
**modified_by** | **str** | User that last modified the resource | [optional] 
**time_created** | **datetime** | Time (in UTC) the resource was created | [optional] 
**time_modified** | **datetime** | Time (in UTC) the resource was modified | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


