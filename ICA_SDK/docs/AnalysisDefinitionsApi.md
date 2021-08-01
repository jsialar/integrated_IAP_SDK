# ICA_SDK.AnalysisDefinitionsApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_analysis_definition**](AnalysisDefinitionsApi.md#create_analysis_definition) | **POST** /v1/sequencing/analysisdefinitions | Create an analysis definition.
[**get_analysis_definition**](AnalysisDefinitionsApi.md#get_analysis_definition) | **GET** /v1/sequencing/analysisdefinitions/{analysisDefinitionId} | Get analysis definition details.
[**list_analysis_definitions**](AnalysisDefinitionsApi.md#list_analysis_definitions) | **GET** /v1/sequencing/analysisdefinitions | Get a list of analysis definitions.
[**merge_analysis_definition_acl**](AnalysisDefinitionsApi.md#merge_analysis_definition_acl) | **PATCH** /v1/sequencing/analysisdefinitions/{analysisDefinitionId}/acl | Merge the access control list of an analysis definition with the input access control list.
[**remove_analysis_definition_acl**](AnalysisDefinitionsApi.md#remove_analysis_definition_acl) | **DELETE** /v1/sequencing/analysisdefinitions/{analysisDefinitionId}/acl | Remove the access control list of an analysis definition.
[**replace_analysis_definition_acl**](AnalysisDefinitionsApi.md#replace_analysis_definition_acl) | **PUT** /v1/sequencing/analysisdefinitions/{analysisDefinitionId}/acl | Replace the access control list of an analysis definition.
[**update_analysis_definition**](AnalysisDefinitionsApi.md#update_analysis_definition) | **PATCH** /v1/sequencing/analysisdefinitions/{analysisDefinitionId} | Update analysis definition details.


# **create_analysis_definition**
> AnalysisDefinition create_analysis_definition()

Create an analysis definition.

Create an analysis definition, and return information about that analysis definition.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import analysis_definitions_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.create_analysis_definition_request import CreateAnalysisDefinitionRequest
from ICA_SDK.model.analysis_definition import AnalysisDefinition
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
    api_instance = analysis_definitions_api.AnalysisDefinitionsApi(api_client)
    body = CreateAnalysisDefinitionRequest(
        name="name_example",
        organization="organization_example",
        display_name="display_name_example",
        description="description_example",
        status="Active",
        library_prep_kit_ids=[
            "library_prep_kit_ids_example",
        ],
        illumina_kit_support_mode="All",
        regulatory_mode="RUO",
        acl=[
            "acl_example",
        ],
    ) # CreateAnalysisDefinitionRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an analysis definition.
        api_response = api_instance.create_analysis_definition(body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisDefinitionsApi->create_analysis_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAnalysisDefinitionRequest**](CreateAnalysisDefinitionRequest.md)|  | [optional]

### Return type

[**AnalysisDefinition**](AnalysisDefinition.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Analysis definition created successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**409** | Analysis definition not created due to conflict with input parameters. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_definition**
> AnalysisDefinition get_analysis_definition(analysis_definition_id)

Get analysis definition details.

For a given analysis definition ID, get the analysis definition details.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import analysis_definitions_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.analysis_definition import AnalysisDefinition
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
    api_instance = analysis_definitions_api.AnalysisDefinitionsApi(api_client)
    analysis_definition_id = "analysisDefinitionId_example" # str | ID of the analysis definition
    include = [
        "CompatibleLibraryPrepKits",
    ] # [str] | Include flags to specify what is included in the response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get analysis definition details.
        api_response = api_instance.get_analysis_definition(analysis_definition_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisDefinitionsApi->get_analysis_definition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get analysis definition details.
        api_response = api_instance.get_analysis_definition(analysis_definition_id, include=include)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisDefinitionsApi->get_analysis_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_definition_id** | **str**| ID of the analysis definition |
 **include** | **[str]**| Include flags to specify what is included in the response | [optional]

### Return type

[**AnalysisDefinition**](AnalysisDefinition.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analysis definition details returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No analysis definition found for given analysis definition ID. |  -  |
**410** | The analysis definition for the given ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_analysis_definitions**
> AnalysisDefinitionCompactAnalysisDefinitionSortFieldsPagedItems list_analysis_definitions()

Get a list of analysis definitions.

Get a list of analysis definitions accessible by the request token.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import analysis_definitions_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.analysis_definition_compact_analysis_definition_sort_fields_paged_items import AnalysisDefinitionCompactAnalysisDefinitionSortFieldsPagedItems
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
    api_instance = analysis_definitions_api.AnalysisDefinitionsApi(api_client)
    analysis_location = "Local" # str | Filter parameter to only show Local/Cloud analysis version definitions (optional)
    regulatory_mode = [
        "RUO",
    ] # [str] | Filter by regulatory modes using comma separated values, e.g <example>RUO,IVD,IUO</example> (optional)
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
    # and optional values
    try:
        # Get a list of analysis definitions.
        api_response = api_instance.list_analysis_definitions(analysis_location=analysis_location, regulatory_mode=regulatory_mode, instrument_platform=instrument_platform, instrument_type=instrument_type, include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisDefinitionsApi->list_analysis_definitions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_location** | **str**| Filter parameter to only show Local/Cloud analysis version definitions | [optional]
 **regulatory_mode** | **[str]**| Filter by regulatory modes using comma separated values, e.g &lt;example&gt;RUO,IVD,IUO&lt;/example&gt; | [optional]
 **instrument_platform** | **str**| Instrument platform | [optional]
 **instrument_type** | **str**| Instrument type | [optional]
 **include** | **[str]**| Include flags to specify what is included in the response | [optional]
 **tenant_ids** | **[str]**| Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids | [optional]
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] if omitted the server will use the default value of 10
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional]
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] if omitted the server will use the default value of "timeCreated asc"

### Return type

[**AnalysisDefinitionCompactAnalysisDefinitionSortFieldsPagedItems**](AnalysisDefinitionCompactAnalysisDefinitionSortFieldsPagedItems.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of analysis definitions returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_analysis_definition_acl**
> AnalysisDefinition merge_analysis_definition_acl(analysis_definition_id)

Merge the access control list of an analysis definition with the input access control list.

Merge the access control list of an analysis definition with the input access control list, and return information about that analysis definition.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import analysis_definitions_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_acl_request import UpdateAclRequest
from ICA_SDK.model.analysis_definition import AnalysisDefinition
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
    api_instance = analysis_definitions_api.AnalysisDefinitionsApi(api_client)
    analysis_definition_id = "analysisDefinitionId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Merge the access control list of an analysis definition with the input access control list.
        api_response = api_instance.merge_analysis_definition_acl(analysis_definition_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisDefinitionsApi->merge_analysis_definition_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Merge the access control list of an analysis definition with the input access control list.
        api_response = api_instance.merge_analysis_definition_acl(analysis_definition_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisDefinitionsApi->merge_analysis_definition_acl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_definition_id** | **str**|  |
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional]

### Return type

[**AnalysisDefinition**](AnalysisDefinition.md)

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

# **remove_analysis_definition_acl**
> AnalysisDefinition remove_analysis_definition_acl(analysis_definition_id)

Remove the access control list of an analysis definition.

Remove the access control list of an analysis definition, and return information about that analysis definition.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import analysis_definitions_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_acl_request import UpdateAclRequest
from ICA_SDK.model.analysis_definition import AnalysisDefinition
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
    api_instance = analysis_definitions_api.AnalysisDefinitionsApi(api_client)
    analysis_definition_id = "analysisDefinitionId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove the access control list of an analysis definition.
        api_response = api_instance.remove_analysis_definition_acl(analysis_definition_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisDefinitionsApi->remove_analysis_definition_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove the access control list of an analysis definition.
        api_response = api_instance.remove_analysis_definition_acl(analysis_definition_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisDefinitionsApi->remove_analysis_definition_acl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_definition_id** | **str**|  |
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional]

### Return type

[**AnalysisDefinition**](AnalysisDefinition.md)

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

# **replace_analysis_definition_acl**
> AnalysisDefinition replace_analysis_definition_acl(analysis_definition_id)

Replace the access control list of an analysis definition.

Replace the access control list of an analysis definition, and return information about that analysis definition.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import analysis_definitions_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_acl_request import UpdateAclRequest
from ICA_SDK.model.analysis_definition import AnalysisDefinition
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
    api_instance = analysis_definitions_api.AnalysisDefinitionsApi(api_client)
    analysis_definition_id = "analysisDefinitionId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Replace the access control list of an analysis definition.
        api_response = api_instance.replace_analysis_definition_acl(analysis_definition_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisDefinitionsApi->replace_analysis_definition_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Replace the access control list of an analysis definition.
        api_response = api_instance.replace_analysis_definition_acl(analysis_definition_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisDefinitionsApi->replace_analysis_definition_acl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_definition_id** | **str**|  |
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional]

### Return type

[**AnalysisDefinition**](AnalysisDefinition.md)

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

# **update_analysis_definition**
> AnalysisDefinition update_analysis_definition(analysis_definition_id)

Update analysis definition details.

For a given analysis definition ID, update the analysis definition details.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import analysis_definitions_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_analysis_definition_request import UpdateAnalysisDefinitionRequest
from ICA_SDK.model.analysis_definition import AnalysisDefinition
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
    api_instance = analysis_definitions_api.AnalysisDefinitionsApi(api_client)
    analysis_definition_id = "analysisDefinitionId_example" # str | 
    body = UpdateAnalysisDefinitionRequest(
        name="name_example",
        organization="organization_example",
        display_name="display_name_example",
        description="description_example",
        status="Active",
        library_prep_kit_ids=[
            "library_prep_kit_ids_example",
        ],
        illumina_kit_support_mode="All",
        regulatory_mode="RUO",
        acl=[
            "acl_example",
        ],
    ) # UpdateAnalysisDefinitionRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update analysis definition details.
        api_response = api_instance.update_analysis_definition(analysis_definition_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisDefinitionsApi->update_analysis_definition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update analysis definition details.
        api_response = api_instance.update_analysis_definition(analysis_definition_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisDefinitionsApi->update_analysis_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_definition_id** | **str**|  |
 **body** | [**UpdateAnalysisDefinitionRequest**](UpdateAnalysisDefinitionRequest.md)|  | [optional]

### Return type

[**AnalysisDefinition**](AnalysisDefinition.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analysis definition details updated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No analysis definition found for given analysis definition ID. |  -  |
**409** | Analysis definition not updated due to conflict with input parameters. |  -  |
**410** | The analysis definition for the given ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

