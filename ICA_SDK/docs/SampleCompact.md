# SampleCompact

Data contract for sample (compact)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique object ID | [optional] 
**urn** | **str** | URN of the object | [optional] 
**href** | **str** | HREF to the object | [optional] 
**name** | **str** | Name of the sample | [optional] 
**description** | **str** | Description of the sample | [optional] 
**status** | **str** | Status of the sample | [optional] 
**lab_status** | **str** | User-customizable value indicating the status of the sample | [optional] 
**data_aggregation_group** | **str** | Data aggregation group | [optional] 
**project_name** | **str** | Project Name  Note: This field is an alias of DataAggregationGroup field until DataAggregationGroups is deprecated. | [optional] 
**external_id** | **str** | Optional external ID associated with the sample | [optional] 
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


