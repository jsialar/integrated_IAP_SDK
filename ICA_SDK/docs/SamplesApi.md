# ICA_SDK.SamplesApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sample**](SamplesApi.md#create_sample) | **POST** /v1/sequencing/samples | Create a sample.
[**deliver_samples**](SamplesApi.md#deliver_samples) | **POST** /v1/sequencing/samples:delivery | Deliver samples.
[**get_sample**](SamplesApi.md#get_sample) | **GET** /v1/sequencing/samples/{sampleId} | Get sample details.
[**list_sample_analysis_datasets**](SamplesApi.md#list_sample_analysis_datasets) | **GET** /v1/sequencing/samples/{sampleId}/analysisDatasets | List analysis datasets associated with the specified sample.
[**list_samples**](SamplesApi.md#list_samples) | **GET** /v1/sequencing/samples | Get a list of samples.
[**merge_sample_acl**](SamplesApi.md#merge_sample_acl) | **PATCH** /v1/sequencing/samples/{sampleId}/acl | Merge the access control list of a sample with the input access control list.
[**register_sample_data**](SamplesApi.md#register_sample_data) | **POST** /v1/sequencing/samples:registerData | Register data for a sample.
[**remove_sample_acl**](SamplesApi.md#remove_sample_acl) | **DELETE** /v1/sequencing/samples/{sampleId}/acl | Remove the access control list of a sample.
[**replace_sample_acl**](SamplesApi.md#replace_sample_acl) | **PUT** /v1/sequencing/samples/{sampleId}/acl | Replace the access control list of a sample with the input access control list.
[**update_sample**](SamplesApi.md#update_sample) | **PATCH** /v1/sequencing/samples/{sampleId} | Update sample information.


# **create_sample**
> Sample create_sample()

Create a sample.

Create a sample, and return information about that sample.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import samples_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.sample import Sample
from ICA_SDK.model.create_sample_request import CreateSampleRequest
from pprint import pprint
# Defining the host is optional and defaults to https://use1.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ICA_SDK.Configuration(
    host = "https://use1.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = ICA_SDK.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samples_api.SamplesApi(api_client)
    body = CreateSampleRequest(
        name="name_example",
        description="description_example",
        status="New",
        lab_status="lab_status_example",
        project_name="project_name_example",
        acl=[
            "acl_example",
        ],
    ) # CreateSampleRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a sample.
        api_response = api_instance.create_sample(body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SamplesApi->create_sample: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSampleRequest**](CreateSampleRequest.md)|  | [optional]

### Return type

[**Sample**](Sample.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Sample created successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deliver_samples**
> SamplesDeliveryResponse deliver_samples()

Deliver samples.

Deliver samples to allow subscription in ENS.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import samples_api
from ICA_SDK.model.samples_delivery_request import SamplesDeliveryRequest
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.samples_delivery_response import SamplesDeliveryResponse
from pprint import pprint
# Defining the host is optional and defaults to https://use1.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ICA_SDK.Configuration(
    host = "https://use1.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = ICA_SDK.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samples_api.SamplesApi(api_client)
    body = SamplesDeliveryRequest(
        sample_delivery={},
    ) # SamplesDeliveryRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deliver samples.
        api_response = api_instance.deliver_samples(body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SamplesApi->deliver_samples: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SamplesDeliveryRequest**](SamplesDeliveryRequest.md)|  | [optional]

### Return type

[**SamplesDeliveryResponse**](SamplesDeliveryResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sample delivered successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sample**
> Sample get_sample(sample_id)

Get sample details.

For a given sample ID, return information about that sample.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import samples_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.sample import Sample
from pprint import pprint
# Defining the host is optional and defaults to https://use1.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ICA_SDK.Configuration(
    host = "https://use1.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = ICA_SDK.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samples_api.SamplesApi(api_client)
    sample_id = "sampleId_example" # str | The ID of the requested sample.

    # example passing only required values which don't have defaults set
    try:
        # Get sample details.
        api_response = api_instance.get_sample(sample_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SamplesApi->get_sample: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **str**| The ID of the requested sample. |

### Return type

[**Sample**](Sample.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sample details returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sample found for given sample ID. |  -  |
**410** | The sample with the given sample ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sample_analysis_datasets**
> AnalysisDatasetCompactAnalysisDatasetSortFieldsPagedItems list_sample_analysis_datasets(sample_id)

List analysis datasets associated with the specified sample.

For a given sample ID, return a list of associated analysis datasets.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import samples_api
from ICA_SDK.model.analysis_dataset_compact_analysis_dataset_sort_fields_paged_items import AnalysisDatasetCompactAnalysisDatasetSortFieldsPagedItems
from ICA_SDK.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://use1.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ICA_SDK.Configuration(
    host = "https://use1.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = ICA_SDK.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samples_api.SamplesApi(api_client)
    sample_id = "sampleId_example" # str | 
    type = [
        "type_example",
    ] # [str] | The analysis dataset types requested. (optional)
    include = [
        "TotalItemCount",
    ] # [str] | Available include flags for list of analysisDatasets associated with a sample (optional)
    page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) if omitted the server will use the default value of 10
    page_token = "pageToken_example" # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
    sort = "timeCreated asc" # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) if omitted the server will use the default value of "timeCreated asc"

    # example passing only required values which don't have defaults set
    try:
        # List analysis datasets associated with the specified sample.
        api_response = api_instance.list_sample_analysis_datasets(sample_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SamplesApi->list_sample_analysis_datasets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List analysis datasets associated with the specified sample.
        api_response = api_instance.list_sample_analysis_datasets(sample_id, type=type, include=include, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SamplesApi->list_sample_analysis_datasets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **str**|  |
 **type** | **[str]**| The analysis dataset types requested. | [optional]
 **include** | **[str]**| Available include flags for list of analysisDatasets associated with a sample | [optional]
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] if omitted the server will use the default value of 10
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional]
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] if omitted the server will use the default value of "timeCreated asc"

### Return type

[**AnalysisDatasetCompactAnalysisDatasetSortFieldsPagedItems**](AnalysisDatasetCompactAnalysisDatasetSortFieldsPagedItems.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analysis datasets returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sample found for given sample ID. |  -  |
**410** | The sample with the given sample ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_samples**
> SampleCompactSampleSortFieldsPagedItems list_samples()

Get a list of samples.

Get a list of samples accessible by the request token.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import samples_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.sample_compact_sample_sort_fields_paged_items import SampleCompactSampleSortFieldsPagedItems
from pprint import pprint
# Defining the host is optional and defaults to https://use1.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ICA_SDK.Configuration(
    host = "https://use1.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = ICA_SDK.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samples_api.SamplesApi(api_client)
    include = [
        "TotalItemCount",
    ] # [str] | Include flags to specify what is included in the response (optional)
    name = "name_example" # str | Optional parameter. Set to filter the sample list and only include samples with the specified name. (optional)
    data_aggregation_group = "dataAggregationGroup_example" # str | Optional parameter. Set to filter the sample list and only include samples with the specified dataAggregationGroup. (optional)
    project_name = "projectName_example" # str | Optional parameter. Set to filter the sample list and only include samples with the specified ProjectName.  Note: This field is an alias of DataAggregationGroup field until DataAggregationGroups is deprecated. (optional)
    tenant_ids = [
        "tenantIds_example",
    ] # [str] | Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids (optional)
    page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) if omitted the server will use the default value of 10
    page_token = "pageToken_example" # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
    sort = "timeCreated asc" # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) if omitted the server will use the default value of "timeCreated asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of samples.
        api_response = api_instance.list_samples(include=include, name=name, data_aggregation_group=data_aggregation_group, project_name=project_name, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SamplesApi->list_samples: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **[str]**| Include flags to specify what is included in the response | [optional]
 **name** | **str**| Optional parameter. Set to filter the sample list and only include samples with the specified name. | [optional]
 **data_aggregation_group** | **str**| Optional parameter. Set to filter the sample list and only include samples with the specified dataAggregationGroup. | [optional]
 **project_name** | **str**| Optional parameter. Set to filter the sample list and only include samples with the specified ProjectName.  Note: This field is an alias of DataAggregationGroup field until DataAggregationGroups is deprecated. | [optional]
 **tenant_ids** | **[str]**| Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids | [optional]
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] if omitted the server will use the default value of 10
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional]
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] if omitted the server will use the default value of "timeCreated asc"

### Return type

[**SampleCompactSampleSortFieldsPagedItems**](SampleCompactSampleSortFieldsPagedItems.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sample list returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_sample_acl**
> Sample merge_sample_acl(sample_id)

Merge the access control list of a sample with the input access control list.

Merge the access control list of a given sample with the input access control list, and return information about that sample.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import samples_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_acl_request import UpdateAclRequest
from ICA_SDK.model.sample import Sample
from pprint import pprint
# Defining the host is optional and defaults to https://use1.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ICA_SDK.Configuration(
    host = "https://use1.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = ICA_SDK.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samples_api.SamplesApi(api_client)
    sample_id = "sampleId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Merge the access control list of a sample with the input access control list.
        api_response = api_instance.merge_sample_acl(sample_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SamplesApi->merge_sample_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Merge the access control list of a sample with the input access control list.
        api_response = api_instance.merge_sample_acl(sample_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SamplesApi->merge_sample_acl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **str**|  |
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional]

### Return type

[**Sample**](Sample.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Access control list updated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sample found for given sample ID. |  -  |
**410** | The sample with the given sample ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_sample_data**
> Sample register_sample_data()

Register data for a sample.

Register data for a sample that may or may not exist yet.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import samples_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.sample import Sample
from ICA_SDK.model.register_sample_data_request import RegisterSampleDataRequest
from pprint import pprint
# Defining the host is optional and defaults to https://use1.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ICA_SDK.Configuration(
    host = "https://use1.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = ICA_SDK.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samples_api.SamplesApi(api_client)
    body = RegisterSampleDataRequest(
        skip_copy_files_to_project_volume=True,
        total_sample_count=1,
        total_dataset_count=1,
        sample_id="sample_id_example",
        sample_name="sample_name_example",
        project_name="project_name_example",
        external_sample_id="external_sample_id_example",
        external_project_id="external_project_id_example",
        external_analysis_run_id="external_analysis_run_id_example",
        analysis_datasets=[
            CreateAnalysisDatasetParameters(
                name="name_example",
                display_name="display_name_example",
                external_id="external_id_example",
                task_run_id="task_run_id_example",
                workflow_run_id="workflow_run_id_example",
                lane_number=1,
                data_folder_urn="data_folder_urn_example",
                data_folder_volume_path="data_folder_volume_path_example",
                attributes={},
                type="type_example",
                qc_status="qc_status_example",
                qc_status_summary="qc_status_summary_example",
                file_urns=[
                    "file_urns_example",
                ],
            ),
        ],
    ) # RegisterSampleDataRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Register data for a sample.
        api_response = api_instance.register_sample_data(body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SamplesApi->register_sample_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterSampleDataRequest**](RegisterSampleDataRequest.md)|  | [optional]

### Return type

[**Sample**](Sample.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sample data added successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sample found for given sample ID/Urn. |  -  |
**409** | Conflict |  -  |
**410** | The sample with the given sample ID/Urn has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_sample_acl**
> Sample remove_sample_acl(sample_id)

Remove the access control list of a sample.

Remove the access control list of a given sample, and return information about that sample.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import samples_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_acl_request import UpdateAclRequest
from ICA_SDK.model.sample import Sample
from pprint import pprint
# Defining the host is optional and defaults to https://use1.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ICA_SDK.Configuration(
    host = "https://use1.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = ICA_SDK.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samples_api.SamplesApi(api_client)
    sample_id = "sampleId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove the access control list of a sample.
        api_response = api_instance.remove_sample_acl(sample_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SamplesApi->remove_sample_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove the access control list of a sample.
        api_response = api_instance.remove_sample_acl(sample_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SamplesApi->remove_sample_acl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **str**|  |
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional]

### Return type

[**Sample**](Sample.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Input access control list removed successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sample found for given sample ID. |  -  |
**410** | The sample with the given sample ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_sample_acl**
> Sample replace_sample_acl(sample_id)

Replace the access control list of a sample with the input access control list.

Replace the access control list of a sample with the input access control list, and return information about that sample.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import samples_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_acl_request import UpdateAclRequest
from ICA_SDK.model.sample import Sample
from pprint import pprint
# Defining the host is optional and defaults to https://use1.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ICA_SDK.Configuration(
    host = "https://use1.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = ICA_SDK.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samples_api.SamplesApi(api_client)
    sample_id = "sampleId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Replace the access control list of a sample with the input access control list.
        api_response = api_instance.replace_sample_acl(sample_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SamplesApi->replace_sample_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Replace the access control list of a sample with the input access control list.
        api_response = api_instance.replace_sample_acl(sample_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SamplesApi->replace_sample_acl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **str**|  |
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional]

### Return type

[**Sample**](Sample.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Access control list of sample updated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sample found for given sample ID. |  -  |
**410** | The sample with the given sample ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sample**
> Sample update_sample(sample_id)

Update sample information.

For a given sample ID, update sample information.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import samples_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.sample import Sample
from ICA_SDK.model.update_sample_request import UpdateSampleRequest
from pprint import pprint
# Defining the host is optional and defaults to https://use1.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ICA_SDK.Configuration(
    host = "https://use1.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = ICA_SDK.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samples_api.SamplesApi(api_client)
    sample_id = "sampleId_example" # str | 
    body = UpdateSampleRequest(
        name="name_example",
        description="description_example",
        status="New",
        lab_status="lab_status_example",
        project_name="project_name_example",
        acl=[
            "acl_example",
        ],
    ) # UpdateSampleRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update sample information.
        api_response = api_instance.update_sample(sample_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SamplesApi->update_sample: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update sample information.
        api_response = api_instance.update_sample(sample_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SamplesApi->update_sample: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **str**|  |
 **body** | [**UpdateSampleRequest**](UpdateSampleRequest.md)|  | [optional]

### Return type

[**Sample**](Sample.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sample updated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sample found for given sample ID. |  -  |
**410** | The sample with the given sample ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

