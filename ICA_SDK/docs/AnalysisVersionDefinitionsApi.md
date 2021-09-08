# ICA_SDK.AnalysisVersionDefinitionsApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_analysis_version_definition**](AnalysisVersionDefinitionsApi.md#archive_analysis_version_definition) | **POST** /v1/sequencing/analysisdefinitions/versions/{analysisVersionDefinitionId}:archive | Archives the given Analysis Version Definition.
[**create_analysis_version_definition**](AnalysisVersionDefinitionsApi.md#create_analysis_version_definition) | **POST** /v1/sequencing/analysisdefinitions/{analysisDefinitionId}/versions | Create an analysis version definition.
[**get_analysis_version_definition**](AnalysisVersionDefinitionsApi.md#get_analysis_version_definition) | **GET** /v1/sequencing/analysisdefinitions/{analysisDefinitionId}/versions/{versionName} | Get a specific analysis definition version by version name.
[**get_analysis_version_definition_by_id_or_urn**](AnalysisVersionDefinitionsApi.md#get_analysis_version_definition_by_id_or_urn) | **GET** /v1/sequencing/analysisdefinitions/versions/{analysisVersionDefinitionId} | Get details of an analysis definition version by ID or URN.
[**list_analysis_version_definitions**](AnalysisVersionDefinitionsApi.md#list_analysis_version_definitions) | **GET** /v1/sequencing/analysisdefinitions/{analysisDefinitionId}/versions | Get a list of analysis definition versions.
[**merge_analysis_version_definition_acl**](AnalysisVersionDefinitionsApi.md#merge_analysis_version_definition_acl) | **PATCH** /v1/sequencing/analysisdefinitions/versions/{analysisVersionDefinitionId}/acl | Merge the access control list of an analysis version definition with the input access control list.
[**remove_analysis_version_definition_acl**](AnalysisVersionDefinitionsApi.md#remove_analysis_version_definition_acl) | **DELETE** /v1/sequencing/analysisdefinitions/versions/{analysisVersionDefinitionId}/acl | Remove the access control list of an analysis version definition.
[**render_analysis_version_definition_by_id_or_urn**](AnalysisVersionDefinitionsApi.md#render_analysis_version_definition_by_id_or_urn) | **POST** /v1/sequencing/analysisdefinitions/versions/{analysisVersionDefinitionId}:render | Dynamically render an analysis definition version by ID or URN.
[**replace_analysis_version_definition_acl**](AnalysisVersionDefinitionsApi.md#replace_analysis_version_definition_acl) | **PUT** /v1/sequencing/analysisdefinitions/versions/{analysisVersionDefinitionId}/acl | Replace the access control list of an analysis version definition with the input access control list.
[**unarchive_analysis_version_definition**](AnalysisVersionDefinitionsApi.md#unarchive_analysis_version_definition) | **POST** /v1/sequencing/analysisdefinitions/versions/{analysisVersionDefinitionId}:unarchive | Unarchive the given Analysis Version Definition.
[**update_analysis_version_definition**](AnalysisVersionDefinitionsApi.md#update_analysis_version_definition) | **PATCH** /v1/sequencing/analysisdefinitions/{analysisDefinitionId}/versions/{versionName} | Update an analysis version definition.


# **archive_analysis_version_definition**
> AnalysisVersionDefinition archive_analysis_version_definition(analysis_version_definition_id)

Archives the given Analysis Version Definition.

For the given Id, Status of Analysis Version Definition is set to archived.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import analysis_version_definitions_api
from ICA_SDK.model.analysis_version_definition import AnalysisVersionDefinition
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
    api_instance = analysis_version_definitions_api.AnalysisVersionDefinitionsApi(api_client)
    analysis_version_definition_id = "analysisVersionDefinitionId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Archives the given Analysis Version Definition.
        api_response = api_instance.archive_analysis_version_definition(analysis_version_definition_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->archive_analysis_version_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_version_definition_id** | **str**|  |

### Return type

[**AnalysisVersionDefinition**](AnalysisVersionDefinition.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analysis version definition is archived successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No analysis version definition found for given Id. |  -  |
**409** | Analysis version definition cannot be archived due to conflict. |  -  |
**410** | Analysis version definition already deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_analysis_version_definition**
> AnalysisVersionDefinition create_analysis_version_definition(analysis_definition_id)

Create an analysis version definition.

Create an analysis version definition, and return information about that analysis definition.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import analysis_version_definitions_api
from ICA_SDK.model.analysis_version_definition import AnalysisVersionDefinition
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.create_analysis_version_definition_request import CreateAnalysisVersionDefinitionRequest
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
    api_instance = analysis_version_definitions_api.AnalysisVersionDefinitionsApi(api_client)
    analysis_definition_id = "analysisDefinitionId_example" # str | 
    body = CreateAnalysisVersionDefinitionRequest(
        version="version_example",
        supported_instrument_platform_and_types=[
            SupportedInstrumentPlatformAndTypes(
                instrument_platform="instrument_platform_example",
                instrument_types=[
                    "instrument_types_example",
                ],
            ),
        ],
        description="description_example",
        status="Active",
        analysis_type="Local",
        skip_analysis_section=True,
        is_dragen=True,
        library_prep_kit_ids=[
            "library_prep_kit_ids_example",
        ],
        supported_genome_ids=[
            "supported_genome_ids_example",
        ],
        excluded_genome_ids=[
            "excluded_genome_ids_example",
        ],
        analysis_settings={},
        analysis_sample_settings={},
        on_submit_function="on_submit_function_example",
        on_render_function="on_render_function_example",
        on_render_require_run_contents=True,
        settings=AnalysisVersionDefinitionSettings(
            sample_sheet=AnalysisVersionDefinitionSettingsSampleSheetConfiguration(
                bcl_convert_section_settings={
                    "key": "key_example",
                },
                analysis_section_settings={
                    "key": "key_example",
                },
                cloud_section_settings={
                    "key": "key_example",
                },
            ),
            run_analysis_settings={},
            run_setup_validation=RunSetupValidation(
                require_unique_sample_ids_per_lane=True,
                enable_custom_prep_kits=True,
                read1_length_min=1,
                read1_length_max=1,
                read2_length_min=1,
                read2_length_max=1,
                allowed_index_strategies=[
                    "NoIndex",
                ],
                allowed_read_types=[
                    "Single",
                ],
                allow_deviations=True,
                deviation_warning_message="deviation_warning_message_example",
                custom_prep_kit_warning_message="custom_prep_kit_warning_message_example",
                skip_validate_index_cycles_with_index_sequence_lengths=True,
            ),
            workflow_metadata=WorkflowMetadataDto(
                workflow_type="workflow_type_example",
                workflow_url="workflow_url_example",
                volume_size_in_gigabytes=1,
                tags={},
                workflow_params={},
                workflow_resources_folder="workflow_resources_folder_example",
            ),
        ),
        checksum="checksum_example",
        acl=[
            "acl_example",
        ],
    ) # CreateAnalysisVersionDefinitionRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an analysis version definition.
        api_response = api_instance.create_analysis_version_definition(analysis_definition_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->create_analysis_version_definition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an analysis version definition.
        api_response = api_instance.create_analysis_version_definition(analysis_definition_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->create_analysis_version_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_definition_id** | **str**|  |
 **body** | [**CreateAnalysisVersionDefinitionRequest**](CreateAnalysisVersionDefinitionRequest.md)|  | [optional]

### Return type

[**AnalysisVersionDefinition**](AnalysisVersionDefinition.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Analysis version definition created successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**409** | Analysis version definition not created due to conflict with input parameters. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_version_definition**
> AnalysisVersionDefinition get_analysis_version_definition(analysis_definition_id, version_name)

Get a specific analysis definition version by version name.

Get a specific analysis definition version accessible by the current request token.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import analysis_version_definitions_api
from ICA_SDK.model.analysis_version_definition import AnalysisVersionDefinition
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
    api_instance = analysis_version_definitions_api.AnalysisVersionDefinitionsApi(api_client)
    analysis_definition_id = "analysisDefinitionId_example" # str | 
    version_name = "versionName_example" # str | 
    include = [
        "CompatibleLibraryPrepKits",
    ] # [str] | Include flags to specify what is included in the response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a specific analysis definition version by version name.
        api_response = api_instance.get_analysis_version_definition(analysis_definition_id, version_name)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->get_analysis_version_definition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a specific analysis definition version by version name.
        api_response = api_instance.get_analysis_version_definition(analysis_definition_id, version_name, include=include)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->get_analysis_version_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_definition_id** | **str**|  |
 **version_name** | **str**|  |
 **include** | **[str]**| Include flags to specify what is included in the response | [optional]

### Return type

[**AnalysisVersionDefinition**](AnalysisVersionDefinition.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analysis version definition returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No analysis version definition found for given version name. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_version_definition_by_id_or_urn**
> AnalysisVersionDefinition get_analysis_version_definition_by_id_or_urn(analysis_version_definition_id)

Get details of an analysis definition version by ID or URN.

For a given ID or URN, get details of an analysis definition version accessible by the current request token.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import analysis_version_definitions_api
from ICA_SDK.model.analysis_version_definition import AnalysisVersionDefinition
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
    api_instance = analysis_version_definitions_api.AnalysisVersionDefinitionsApi(api_client)
    analysis_version_definition_id = "analysisVersionDefinitionId_example" # str | 
    include = [
        "CompatibleLibraryPrepKits",
    ] # [str] | Include flags to specify what is included in the response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of an analysis definition version by ID or URN.
        api_response = api_instance.get_analysis_version_definition_by_id_or_urn(analysis_version_definition_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->get_analysis_version_definition_by_id_or_urn: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of an analysis definition version by ID or URN.
        api_response = api_instance.get_analysis_version_definition_by_id_or_urn(analysis_version_definition_id, include=include)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->get_analysis_version_definition_by_id_or_urn: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_version_definition_id** | **str**|  |
 **include** | **[str]**| Include flags to specify what is included in the response | [optional]

### Return type

[**AnalysisVersionDefinition**](AnalysisVersionDefinition.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analysis version definitions returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No analysis definition version found for given ID/URN. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_analysis_version_definitions**
> AnalysisVersionDefinitionCompactAnalysisVersionDefinitionSortFieldsPagedItems list_analysis_version_definitions(analysis_definition_id)

Get a list of analysis definition versions.

Get a list of analysis definition versions accessible by the current request token.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import analysis_version_definitions_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.analysis_version_definition_compact_analysis_version_definition_sort_fields_paged_items import AnalysisVersionDefinitionCompactAnalysisVersionDefinitionSortFieldsPagedItems
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
    api_instance = analysis_version_definitions_api.AnalysisVersionDefinitionsApi(api_client)
    analysis_definition_id = "analysisDefinitionId_example" # str | ID of the analysis definition
    instrument_platform = "instrumentPlatform_example" # str | Instrument platform (optional)
    instrument_type = "instrumentType_example" # str | Instrument type (optional)
    include = [
        "TotalItemCount",
    ] # [str] | Include flags to specify what is included in the response (optional)
    tenant_ids = [
        "tenantIds_example",
    ] # [str] | Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids (optional)
    page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) if omitted the server will use the default value of 10
    page_token = "pageToken_example" # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
    sort = "timeCreated asc" # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) if omitted the server will use the default value of "timeCreated asc"

    # example passing only required values which don't have defaults set
    try:
        # Get a list of analysis definition versions.
        api_response = api_instance.list_analysis_version_definitions(analysis_definition_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->list_analysis_version_definitions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of analysis definition versions.
        api_response = api_instance.list_analysis_version_definitions(analysis_definition_id, instrument_platform=instrument_platform, instrument_type=instrument_type, include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->list_analysis_version_definitions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_definition_id** | **str**| ID of the analysis definition |
 **instrument_platform** | **str**| Instrument platform | [optional]
 **instrument_type** | **str**| Instrument type | [optional]
 **include** | **[str]**| Include flags to specify what is included in the response | [optional]
 **tenant_ids** | **[str]**| Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids | [optional]
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] if omitted the server will use the default value of 10
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional]
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] if omitted the server will use the default value of "timeCreated asc"

### Return type

[**AnalysisVersionDefinitionCompactAnalysisVersionDefinitionSortFieldsPagedItems**](AnalysisVersionDefinitionCompactAnalysisVersionDefinitionSortFieldsPagedItems.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analysis version definitions returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No analysis definition found for given ID. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_analysis_version_definition_acl**
> AnalysisVersionDefinition merge_analysis_version_definition_acl(analysis_version_definition_id)

Merge the access control list of an analysis version definition with the input access control list.

Merge the access control list of an analysis version definition with the input access control list, and return information about that analysis definition.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import analysis_version_definitions_api
from ICA_SDK.model.analysis_version_definition import AnalysisVersionDefinition
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_acl_request import UpdateAclRequest
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
    api_instance = analysis_version_definitions_api.AnalysisVersionDefinitionsApi(api_client)
    analysis_version_definition_id = "analysisVersionDefinitionId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Merge the access control list of an analysis version definition with the input access control list.
        api_response = api_instance.merge_analysis_version_definition_acl(analysis_version_definition_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->merge_analysis_version_definition_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Merge the access control list of an analysis version definition with the input access control list.
        api_response = api_instance.merge_analysis_version_definition_acl(analysis_version_definition_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->merge_analysis_version_definition_acl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_version_definition_id** | **str**|  |
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional]

### Return type

[**AnalysisVersionDefinition**](AnalysisVersionDefinition.md)

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
**404** | No analysis definition found for given ID. |  -  |
**410** | The analysis definition with the given ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_analysis_version_definition_acl**
> AnalysisVersionDefinition remove_analysis_version_definition_acl(analysis_version_definition_id)

Remove the access control list of an analysis version definition.

Remove the access control list of an analysis version definition, and return information about that analysis definition.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import analysis_version_definitions_api
from ICA_SDK.model.analysis_version_definition import AnalysisVersionDefinition
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_acl_request import UpdateAclRequest
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
    api_instance = analysis_version_definitions_api.AnalysisVersionDefinitionsApi(api_client)
    analysis_version_definition_id = "analysisVersionDefinitionId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove the access control list of an analysis version definition.
        api_response = api_instance.remove_analysis_version_definition_acl(analysis_version_definition_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->remove_analysis_version_definition_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove the access control list of an analysis version definition.
        api_response = api_instance.remove_analysis_version_definition_acl(analysis_version_definition_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->remove_analysis_version_definition_acl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_version_definition_id** | **str**|  |
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional]

### Return type

[**AnalysisVersionDefinition**](AnalysisVersionDefinition.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Input access control list of the analysis definition removed successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No analysis definition found for given ID. |  -  |
**410** | The analysis definition with the given ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_analysis_version_definition_by_id_or_urn**
> RenderAnalysisVersionDefinitionResponse render_analysis_version_definition_by_id_or_urn(analysis_version_definition_id)

Dynamically render an analysis definition version by ID or URN.

For a given ID or URN, get details of an analysis definition version accessible by the current request token.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import analysis_version_definitions_api
from ICA_SDK.model.render_analysis_version_definition_response import RenderAnalysisVersionDefinitionResponse
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.render_analysis_version_definition_request import RenderAnalysisVersionDefinitionRequest
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
    api_instance = analysis_version_definitions_api.AnalysisVersionDefinitionsApi(api_client)
    analysis_version_definition_id = "analysisVersionDefinitionId_example" # str | 
    body = RenderAnalysisVersionDefinitionRequest(
        context="Initial",
        field_id="field_id_example",
        run_configuration=CreateSequencingRunConfigurationRequest(
            instrument_type="instrument_type_example",
            instrument_platform="instrument_platform_example",
            run_name="run_name_example",
            description="description_example",
            regulatory_mode="RUO",
            num_cycles_read1=0,
            num_cycles_read2=0,
            read_type="Single",
            num_cycles_index1=0,
            num_cycles_index2=0,
            use_custom_primer_for_read1=True,
            use_custom_primer_for_read2=True,
            use_custom_primer_for_index1=True,
            use_custom_primer_for_index2=True,
            input_container_identifier="input_container_identifier_example",
        ),
        run_contents=UpdateSequencingRunContentsRequest(
            allow_index_updates=True,
            lane_contents=[
                LaneContent(
                    lane_number=1,
                    same_as_lane_number=1,
                    adapter_sequence_read1="adapter_sequence_read1_example",
                    adapter_sequence_read2="adapter_sequence_read2_example",
                    lane_libraries=[
                        LaneLibrary(
                            sample_name="sample_name_example",
                            sample_urn="sample_urn_example",
                            project_name="project_name_example",
                            library_name="library_name_example",
                            library_urn="library_urn_example",
                            adapter_sequence_read1="adapter_sequence_read1_example",
                            adapter_sequence_read2="adapter_sequence_read2_example",
                            index1_sequence="index1_sequence_example",
                            index2_sequence="index2_sequence_example",
                            index_container_position="index_container_position_example",
                            index1_name="index1_name_example",
                            index2_name="index2_name_example",
                            library_prep_kit_urn="library_prep_kit_urn_example",
                            index_adapter_kit_urn="index_adapter_kit_urn_example",
                        ),
                    ],
                ),
            ],
        ),
        run_analysis_configuration=CreateSequencingRunAnalysisConfigurationRequest(
            name="name_example",
            description="description_example",
            analysis_version_definition_id="analysis_version_definition_id_example",
            settings={},
            sample_settings=[
                SampleSettingEntry(
                    sample_id="sample_id_example",
                    settings={},
                ),
            ],
        ),
        current_analysis_settings={},
        current_analysis_sample_settings={},
    ) # RenderAnalysisVersionDefinitionRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Dynamically render an analysis definition version by ID or URN.
        api_response = api_instance.render_analysis_version_definition_by_id_or_urn(analysis_version_definition_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->render_analysis_version_definition_by_id_or_urn: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Dynamically render an analysis definition version by ID or URN.
        api_response = api_instance.render_analysis_version_definition_by_id_or_urn(analysis_version_definition_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->render_analysis_version_definition_by_id_or_urn: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_version_definition_id** | **str**|  |
 **body** | [**RenderAnalysisVersionDefinitionRequest**](RenderAnalysisVersionDefinitionRequest.md)|  | [optional]

### Return type

[**RenderAnalysisVersionDefinitionResponse**](RenderAnalysisVersionDefinitionResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analysis version definitions is rendered successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No analysis definition version found for given ID/URN. |  -  |
**409** | Analysis definition version cannot be rendered due to conflict with input parameters. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_analysis_version_definition_acl**
> AnalysisVersionDefinition replace_analysis_version_definition_acl(analysis_version_definition_id)

Replace the access control list of an analysis version definition with the input access control list.

Replace the access control list of an analysis version definition with the input access control list, and return information about that analysis definition.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import analysis_version_definitions_api
from ICA_SDK.model.analysis_version_definition import AnalysisVersionDefinition
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_acl_request import UpdateAclRequest
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
    api_instance = analysis_version_definitions_api.AnalysisVersionDefinitionsApi(api_client)
    analysis_version_definition_id = "analysisVersionDefinitionId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Replace the access control list of an analysis version definition with the input access control list.
        api_response = api_instance.replace_analysis_version_definition_acl(analysis_version_definition_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->replace_analysis_version_definition_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Replace the access control list of an analysis version definition with the input access control list.
        api_response = api_instance.replace_analysis_version_definition_acl(analysis_version_definition_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->replace_analysis_version_definition_acl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_version_definition_id** | **str**|  |
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional]

### Return type

[**AnalysisVersionDefinition**](AnalysisVersionDefinition.md)

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
**404** | No analysis definition found for given ID. |  -  |
**410** | The analysis definition with the given ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unarchive_analysis_version_definition**
> AnalysisVersionDefinition unarchive_analysis_version_definition(analysis_version_definition_id)

Unarchive the given Analysis Version Definition.

For the given Id, Status of Analysis Version Definition is set to active.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import analysis_version_definitions_api
from ICA_SDK.model.analysis_version_definition import AnalysisVersionDefinition
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
    api_instance = analysis_version_definitions_api.AnalysisVersionDefinitionsApi(api_client)
    analysis_version_definition_id = "analysisVersionDefinitionId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Unarchive the given Analysis Version Definition.
        api_response = api_instance.unarchive_analysis_version_definition(analysis_version_definition_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->unarchive_analysis_version_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_version_definition_id** | **str**|  |

### Return type

[**AnalysisVersionDefinition**](AnalysisVersionDefinition.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analysis version definition is unarchived successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No analysis version definition found for given Id. |  -  |
**409** | Analysis version definition cannot be unarchived due to conflict. |  -  |
**410** | Analysis version definition already deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_analysis_version_definition**
> AnalysisVersionDefinition update_analysis_version_definition(analysis_definition_id, version_name)

Update an analysis version definition.

Update an analysis version definition, and return information about that analysis definition.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import analysis_version_definitions_api
from ICA_SDK.model.analysis_version_definition import AnalysisVersionDefinition
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_analysis_version_definition_request import UpdateAnalysisVersionDefinitionRequest
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
    api_instance = analysis_version_definitions_api.AnalysisVersionDefinitionsApi(api_client)
    analysis_definition_id = "analysisDefinitionId_example" # str | 
    version_name = "versionName_example" # str | 
    body = UpdateAnalysisVersionDefinitionRequest(
        version="version_example",
        supported_instrument_platform_and_types=[
            SupportedInstrumentPlatformAndTypes(
                instrument_platform="instrument_platform_example",
                instrument_types=[
                    "instrument_types_example",
                ],
            ),
        ],
        description="description_example",
        status="Active",
        analysis_type="Local",
        skip_analysis_section=True,
        is_dragen=True,
        supported_genome_ids=[
            "supported_genome_ids_example",
        ],
        excluded_genome_ids=[
            "excluded_genome_ids_example",
        ],
        library_prep_kit_ids=[
            "library_prep_kit_ids_example",
        ],
        analysis_settings={},
        analysis_sample_settings={},
        on_submit_function="on_submit_function_example",
        on_render_function="on_render_function_example",
        on_render_require_run_contents=True,
        settings=AnalysisVersionDefinitionSettings(
            sample_sheet=AnalysisVersionDefinitionSettingsSampleSheetConfiguration(
                bcl_convert_section_settings={
                    "key": "key_example",
                },
                analysis_section_settings={
                    "key": "key_example",
                },
                cloud_section_settings={
                    "key": "key_example",
                },
            ),
            run_analysis_settings={},
            run_setup_validation=RunSetupValidation(
                require_unique_sample_ids_per_lane=True,
                enable_custom_prep_kits=True,
                read1_length_min=1,
                read1_length_max=1,
                read2_length_min=1,
                read2_length_max=1,
                allowed_index_strategies=[
                    "NoIndex",
                ],
                allowed_read_types=[
                    "Single",
                ],
                allow_deviations=True,
                deviation_warning_message="deviation_warning_message_example",
                custom_prep_kit_warning_message="custom_prep_kit_warning_message_example",
                skip_validate_index_cycles_with_index_sequence_lengths=True,
            ),
            workflow_metadata=WorkflowMetadataDto(
                workflow_type="workflow_type_example",
                workflow_url="workflow_url_example",
                volume_size_in_gigabytes=1,
                tags={},
                workflow_params={},
                workflow_resources_folder="workflow_resources_folder_example",
            ),
        ),
        checksum="checksum_example",
        acl=[
            "acl_example",
        ],
    ) # UpdateAnalysisVersionDefinitionRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an analysis version definition.
        api_response = api_instance.update_analysis_version_definition(analysis_definition_id, version_name)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->update_analysis_version_definition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an analysis version definition.
        api_response = api_instance.update_analysis_version_definition(analysis_definition_id, version_name, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->update_analysis_version_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_definition_id** | **str**|  |
 **version_name** | **str**|  |
 **body** | [**UpdateAnalysisVersionDefinitionRequest**](UpdateAnalysisVersionDefinitionRequest.md)|  | [optional]

### Return type

[**AnalysisVersionDefinition**](AnalysisVersionDefinition.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analysis version definition updated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No analysis version definition found for given ID. |  -  |
**409** | Analysis version definition not updated due to conflict with input parameters. |  -  |
**410** | The analysis version definition with the given ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

