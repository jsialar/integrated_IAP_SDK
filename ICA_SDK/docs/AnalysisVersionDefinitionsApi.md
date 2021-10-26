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
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.AnalysisVersionDefinitionsApi(api_client)
    analysis_version_definition_id = 'analysis_version_definition_id_example' # str | 

    try:
        # Archives the given Analysis Version Definition.
        api_response = api_instance.archive_analysis_version_definition(analysis_version_definition_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->archive_analysis_version_definition: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.AnalysisVersionDefinitionsApi(api_client)
    analysis_version_definition_id = 'analysis_version_definition_id_example' # str | 

    try:
        # Archives the given Analysis Version Definition.
        api_response = api_instance.archive_analysis_version_definition(analysis_version_definition_id)
        pprint(api_response)
    except ApiException as e:
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
> AnalysisVersionDefinition create_analysis_version_definition(analysis_definition_id, body=body)

Create an analysis version definition.

Create an analysis version definition, and return information about that analysis definition.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.AnalysisVersionDefinitionsApi(api_client)
    analysis_definition_id = 'analysis_definition_id_example' # str | 
body = ICA_SDK.CreateAnalysisVersionDefinitionRequest() # CreateAnalysisVersionDefinitionRequest |  (optional)

    try:
        # Create an analysis version definition.
        api_response = api_instance.create_analysis_version_definition(analysis_definition_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->create_analysis_version_definition: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.AnalysisVersionDefinitionsApi(api_client)
    analysis_definition_id = 'analysis_definition_id_example' # str | 
body = ICA_SDK.CreateAnalysisVersionDefinitionRequest() # CreateAnalysisVersionDefinitionRequest |  (optional)

    try:
        # Create an analysis version definition.
        api_response = api_instance.create_analysis_version_definition(analysis_definition_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
> AnalysisVersionDefinition get_analysis_version_definition(analysis_definition_id, version_name, include=include)

Get a specific analysis definition version by version name.

Get a specific analysis definition version accessible by the current request token.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.AnalysisVersionDefinitionsApi(api_client)
    analysis_definition_id = 'analysis_definition_id_example' # str | 
version_name = 'version_name_example' # str | 
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)

    try:
        # Get a specific analysis definition version by version name.
        api_response = api_instance.get_analysis_version_definition(analysis_definition_id, version_name, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->get_analysis_version_definition: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.AnalysisVersionDefinitionsApi(api_client)
    analysis_definition_id = 'analysis_definition_id_example' # str | 
version_name = 'version_name_example' # str | 
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)

    try:
        # Get a specific analysis definition version by version name.
        api_response = api_instance.get_analysis_version_definition(analysis_definition_id, version_name, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->get_analysis_version_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_definition_id** | **str**|  | 
 **version_name** | **str**|  | 
 **include** | [**list[str]**](str.md)| Include flags to specify what is included in the response | [optional] 

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
> AnalysisVersionDefinition get_analysis_version_definition_by_id_or_urn(analysis_version_definition_id, include=include)

Get details of an analysis definition version by ID or URN.

For a given ID or URN, get details of an analysis definition version accessible by the current request token.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.AnalysisVersionDefinitionsApi(api_client)
    analysis_version_definition_id = 'analysis_version_definition_id_example' # str | 
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)

    try:
        # Get details of an analysis definition version by ID or URN.
        api_response = api_instance.get_analysis_version_definition_by_id_or_urn(analysis_version_definition_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->get_analysis_version_definition_by_id_or_urn: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.AnalysisVersionDefinitionsApi(api_client)
    analysis_version_definition_id = 'analysis_version_definition_id_example' # str | 
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)

    try:
        # Get details of an analysis definition version by ID or URN.
        api_response = api_instance.get_analysis_version_definition_by_id_or_urn(analysis_version_definition_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->get_analysis_version_definition_by_id_or_urn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_version_definition_id** | **str**|  | 
 **include** | [**list[str]**](str.md)| Include flags to specify what is included in the response | [optional] 

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
> AnalysisVersionDefinitionCompactAnalysisVersionDefinitionSortFieldsPagedItems list_analysis_version_definitions(analysis_definition_id, instrument_platform=instrument_platform, instrument_type=instrument_type, include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)

Get a list of analysis definition versions.

Get a list of analysis definition versions accessible by the current request token.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.AnalysisVersionDefinitionsApi(api_client)
    analysis_definition_id = 'analysis_definition_id_example' # str | ID of the analysis definition
instrument_platform = 'instrument_platform_example' # str | Instrument platform (optional)
instrument_type = 'instrument_type_example' # str | Instrument type (optional)
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)
tenant_ids = ['tenant_ids_example'] # list[str] | Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to 'timeCreated asc')

    try:
        # Get a list of analysis definition versions.
        api_response = api_instance.list_analysis_version_definitions(analysis_definition_id, instrument_platform=instrument_platform, instrument_type=instrument_type, include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->list_analysis_version_definitions: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.AnalysisVersionDefinitionsApi(api_client)
    analysis_definition_id = 'analysis_definition_id_example' # str | ID of the analysis definition
instrument_platform = 'instrument_platform_example' # str | Instrument platform (optional)
instrument_type = 'instrument_type_example' # str | Instrument type (optional)
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)
tenant_ids = ['tenant_ids_example'] # list[str] | Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to 'timeCreated asc')

    try:
        # Get a list of analysis definition versions.
        api_response = api_instance.list_analysis_version_definitions(analysis_definition_id, instrument_platform=instrument_platform, instrument_type=instrument_type, include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->list_analysis_version_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_definition_id** | **str**| ID of the analysis definition | 
 **instrument_platform** | **str**| Instrument platform | [optional] 
 **instrument_type** | **str**| Instrument type | [optional] 
 **include** | [**list[str]**](str.md)| Include flags to specify what is included in the response | [optional] 
 **tenant_ids** | [**list[str]**](str.md)| Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids | [optional] 
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] [default to 10]
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional] 
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] [default to &#39;timeCreated asc&#39;]

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
> AnalysisVersionDefinition merge_analysis_version_definition_acl(analysis_version_definition_id, body=body)

Merge the access control list of an analysis version definition with the input access control list.

Merge the access control list of an analysis version definition with the input access control list, and return information about that analysis definition.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.AnalysisVersionDefinitionsApi(api_client)
    analysis_version_definition_id = 'analysis_version_definition_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Merge the access control list of an analysis version definition with the input access control list.
        api_response = api_instance.merge_analysis_version_definition_acl(analysis_version_definition_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->merge_analysis_version_definition_acl: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.AnalysisVersionDefinitionsApi(api_client)
    analysis_version_definition_id = 'analysis_version_definition_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Merge the access control list of an analysis version definition with the input access control list.
        api_response = api_instance.merge_analysis_version_definition_acl(analysis_version_definition_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
> AnalysisVersionDefinition remove_analysis_version_definition_acl(analysis_version_definition_id, body=body)

Remove the access control list of an analysis version definition.

Remove the access control list of an analysis version definition, and return information about that analysis definition.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.AnalysisVersionDefinitionsApi(api_client)
    analysis_version_definition_id = 'analysis_version_definition_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Remove the access control list of an analysis version definition.
        api_response = api_instance.remove_analysis_version_definition_acl(analysis_version_definition_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->remove_analysis_version_definition_acl: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.AnalysisVersionDefinitionsApi(api_client)
    analysis_version_definition_id = 'analysis_version_definition_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Remove the access control list of an analysis version definition.
        api_response = api_instance.remove_analysis_version_definition_acl(analysis_version_definition_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
> RenderAnalysisVersionDefinitionResponse render_analysis_version_definition_by_id_or_urn(analysis_version_definition_id, body=body)

Dynamically render an analysis definition version by ID or URN.

For a given ID or URN, get details of an analysis definition version accessible by the current request token.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.AnalysisVersionDefinitionsApi(api_client)
    analysis_version_definition_id = 'analysis_version_definition_id_example' # str | 
body = ICA_SDK.RenderAnalysisVersionDefinitionRequest() # RenderAnalysisVersionDefinitionRequest |  (optional)

    try:
        # Dynamically render an analysis definition version by ID or URN.
        api_response = api_instance.render_analysis_version_definition_by_id_or_urn(analysis_version_definition_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->render_analysis_version_definition_by_id_or_urn: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.AnalysisVersionDefinitionsApi(api_client)
    analysis_version_definition_id = 'analysis_version_definition_id_example' # str | 
body = ICA_SDK.RenderAnalysisVersionDefinitionRequest() # RenderAnalysisVersionDefinitionRequest |  (optional)

    try:
        # Dynamically render an analysis definition version by ID or URN.
        api_response = api_instance.render_analysis_version_definition_by_id_or_urn(analysis_version_definition_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
> AnalysisVersionDefinition replace_analysis_version_definition_acl(analysis_version_definition_id, body=body)

Replace the access control list of an analysis version definition with the input access control list.

Replace the access control list of an analysis version definition with the input access control list, and return information about that analysis definition.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.AnalysisVersionDefinitionsApi(api_client)
    analysis_version_definition_id = 'analysis_version_definition_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Replace the access control list of an analysis version definition with the input access control list.
        api_response = api_instance.replace_analysis_version_definition_acl(analysis_version_definition_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->replace_analysis_version_definition_acl: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.AnalysisVersionDefinitionsApi(api_client)
    analysis_version_definition_id = 'analysis_version_definition_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Replace the access control list of an analysis version definition with the input access control list.
        api_response = api_instance.replace_analysis_version_definition_acl(analysis_version_definition_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.AnalysisVersionDefinitionsApi(api_client)
    analysis_version_definition_id = 'analysis_version_definition_id_example' # str | 

    try:
        # Unarchive the given Analysis Version Definition.
        api_response = api_instance.unarchive_analysis_version_definition(analysis_version_definition_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->unarchive_analysis_version_definition: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.AnalysisVersionDefinitionsApi(api_client)
    analysis_version_definition_id = 'analysis_version_definition_id_example' # str | 

    try:
        # Unarchive the given Analysis Version Definition.
        api_response = api_instance.unarchive_analysis_version_definition(analysis_version_definition_id)
        pprint(api_response)
    except ApiException as e:
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
> AnalysisVersionDefinition update_analysis_version_definition(analysis_definition_id, version_name, body=body)

Update an analysis version definition.

Update an analysis version definition, and return information about that analysis definition.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.AnalysisVersionDefinitionsApi(api_client)
    analysis_definition_id = 'analysis_definition_id_example' # str | 
version_name = 'version_name_example' # str | 
body = ICA_SDK.UpdateAnalysisVersionDefinitionRequest() # UpdateAnalysisVersionDefinitionRequest |  (optional)

    try:
        # Update an analysis version definition.
        api_response = api_instance.update_analysis_version_definition(analysis_definition_id, version_name, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisVersionDefinitionsApi->update_analysis_version_definition: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.AnalysisVersionDefinitionsApi(api_client)
    analysis_definition_id = 'analysis_definition_id_example' # str | 
version_name = 'version_name_example' # str | 
body = ICA_SDK.UpdateAnalysisVersionDefinitionRequest() # UpdateAnalysisVersionDefinitionRequest |  (optional)

    try:
        # Update an analysis version definition.
        api_response = api_instance.update_analysis_version_definition(analysis_definition_id, version_name, body=body)
        pprint(api_response)
    except ApiException as e:
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

