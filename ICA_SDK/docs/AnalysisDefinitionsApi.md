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
> AnalysisDefinition create_analysis_definition(body=body)

Create an analysis definition.

Create an analysis definition, and return information about that analysis definition.

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
    api_instance = ICA_SDK.AnalysisDefinitionsApi(api_client)
    body = ICA_SDK.CreateAnalysisDefinitionRequest() # CreateAnalysisDefinitionRequest |  (optional)

    try:
        # Create an analysis definition.
        api_response = api_instance.create_analysis_definition(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisDefinitionsApi->create_analysis_definition: %s\n" % e)
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
    api_instance = ICA_SDK.AnalysisDefinitionsApi(api_client)
    body = ICA_SDK.CreateAnalysisDefinitionRequest() # CreateAnalysisDefinitionRequest |  (optional)

    try:
        # Create an analysis definition.
        api_response = api_instance.create_analysis_definition(body=body)
        pprint(api_response)
    except ApiException as e:
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
> AnalysisDefinition get_analysis_definition(analysis_definition_id, include=include)

Get analysis definition details.

For a given analysis definition ID, get the analysis definition details.

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
    api_instance = ICA_SDK.AnalysisDefinitionsApi(api_client)
    analysis_definition_id = 'analysis_definition_id_example' # str | ID of the analysis definition
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)

    try:
        # Get analysis definition details.
        api_response = api_instance.get_analysis_definition(analysis_definition_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisDefinitionsApi->get_analysis_definition: %s\n" % e)
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
    api_instance = ICA_SDK.AnalysisDefinitionsApi(api_client)
    analysis_definition_id = 'analysis_definition_id_example' # str | ID of the analysis definition
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)

    try:
        # Get analysis definition details.
        api_response = api_instance.get_analysis_definition(analysis_definition_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisDefinitionsApi->get_analysis_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_definition_id** | **str**| ID of the analysis definition | 
 **include** | [**list[str]**](str.md)| Include flags to specify what is included in the response | [optional] 

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
> AnalysisDefinitionCompactAnalysisDefinitionSortFieldsPagedItems list_analysis_definitions(analysis_location=analysis_location, regulatory_mode=regulatory_mode, instrument_platform=instrument_platform, instrument_type=instrument_type, include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)

Get a list of analysis definitions.

Get a list of analysis definitions accessible by the request token.

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
    api_instance = ICA_SDK.AnalysisDefinitionsApi(api_client)
    analysis_location = 'analysis_location_example' # str | Filter parameter to only show Local/Cloud analysis version definitions (optional)
regulatory_mode = ['regulatory_mode_example'] # list[str] | Filter by regulatory modes using comma separated values, e.g <example>RUO,IVD,IUO</example> (optional)
instrument_platform = 'instrument_platform_example' # str | Instrument platform (optional)
instrument_type = 'instrument_type_example' # str | Instrument type (optional)
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)
tenant_ids = ['tenant_ids_example'] # list[str] | Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to 'timeCreated asc')

    try:
        # Get a list of analysis definitions.
        api_response = api_instance.list_analysis_definitions(analysis_location=analysis_location, regulatory_mode=regulatory_mode, instrument_platform=instrument_platform, instrument_type=instrument_type, include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisDefinitionsApi->list_analysis_definitions: %s\n" % e)
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
    api_instance = ICA_SDK.AnalysisDefinitionsApi(api_client)
    analysis_location = 'analysis_location_example' # str | Filter parameter to only show Local/Cloud analysis version definitions (optional)
regulatory_mode = ['regulatory_mode_example'] # list[str] | Filter by regulatory modes using comma separated values, e.g <example>RUO,IVD,IUO</example> (optional)
instrument_platform = 'instrument_platform_example' # str | Instrument platform (optional)
instrument_type = 'instrument_type_example' # str | Instrument type (optional)
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)
tenant_ids = ['tenant_ids_example'] # list[str] | Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to 'timeCreated asc')

    try:
        # Get a list of analysis definitions.
        api_response = api_instance.list_analysis_definitions(analysis_location=analysis_location, regulatory_mode=regulatory_mode, instrument_platform=instrument_platform, instrument_type=instrument_type, include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisDefinitionsApi->list_analysis_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_location** | **str**| Filter parameter to only show Local/Cloud analysis version definitions | [optional] 
 **regulatory_mode** | [**list[str]**](str.md)| Filter by regulatory modes using comma separated values, e.g &lt;example&gt;RUO,IVD,IUO&lt;/example&gt; | [optional] 
 **instrument_platform** | **str**| Instrument platform | [optional] 
 **instrument_type** | **str**| Instrument type | [optional] 
 **include** | [**list[str]**](str.md)| Include flags to specify what is included in the response | [optional] 
 **tenant_ids** | [**list[str]**](str.md)| Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids | [optional] 
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] [default to 10]
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional] 
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] [default to &#39;timeCreated asc&#39;]

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
> AnalysisDefinition merge_analysis_definition_acl(analysis_definition_id, body=body)

Merge the access control list of an analysis definition with the input access control list.

Merge the access control list of an analysis definition with the input access control list, and return information about that analysis definition.

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
    api_instance = ICA_SDK.AnalysisDefinitionsApi(api_client)
    analysis_definition_id = 'analysis_definition_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Merge the access control list of an analysis definition with the input access control list.
        api_response = api_instance.merge_analysis_definition_acl(analysis_definition_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisDefinitionsApi->merge_analysis_definition_acl: %s\n" % e)
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
    api_instance = ICA_SDK.AnalysisDefinitionsApi(api_client)
    analysis_definition_id = 'analysis_definition_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Merge the access control list of an analysis definition with the input access control list.
        api_response = api_instance.merge_analysis_definition_acl(analysis_definition_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
> AnalysisDefinition remove_analysis_definition_acl(analysis_definition_id, body=body)

Remove the access control list of an analysis definition.

Remove the access control list of an analysis definition, and return information about that analysis definition.

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
    api_instance = ICA_SDK.AnalysisDefinitionsApi(api_client)
    analysis_definition_id = 'analysis_definition_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Remove the access control list of an analysis definition.
        api_response = api_instance.remove_analysis_definition_acl(analysis_definition_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisDefinitionsApi->remove_analysis_definition_acl: %s\n" % e)
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
    api_instance = ICA_SDK.AnalysisDefinitionsApi(api_client)
    analysis_definition_id = 'analysis_definition_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Remove the access control list of an analysis definition.
        api_response = api_instance.remove_analysis_definition_acl(analysis_definition_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
> AnalysisDefinition replace_analysis_definition_acl(analysis_definition_id, body=body)

Replace the access control list of an analysis definition.

Replace the access control list of an analysis definition, and return information about that analysis definition.

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
    api_instance = ICA_SDK.AnalysisDefinitionsApi(api_client)
    analysis_definition_id = 'analysis_definition_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Replace the access control list of an analysis definition.
        api_response = api_instance.replace_analysis_definition_acl(analysis_definition_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisDefinitionsApi->replace_analysis_definition_acl: %s\n" % e)
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
    api_instance = ICA_SDK.AnalysisDefinitionsApi(api_client)
    analysis_definition_id = 'analysis_definition_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Replace the access control list of an analysis definition.
        api_response = api_instance.replace_analysis_definition_acl(analysis_definition_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
> AnalysisDefinition update_analysis_definition(analysis_definition_id, body=body)

Update analysis definition details.

For a given analysis definition ID, update the analysis definition details.

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
    api_instance = ICA_SDK.AnalysisDefinitionsApi(api_client)
    analysis_definition_id = 'analysis_definition_id_example' # str | 
body = ICA_SDK.UpdateAnalysisDefinitionRequest() # UpdateAnalysisDefinitionRequest |  (optional)

    try:
        # Update analysis definition details.
        api_response = api_instance.update_analysis_definition(analysis_definition_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysisDefinitionsApi->update_analysis_definition: %s\n" % e)
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
    api_instance = ICA_SDK.AnalysisDefinitionsApi(api_client)
    analysis_definition_id = 'analysis_definition_id_example' # str | 
body = ICA_SDK.UpdateAnalysisDefinitionRequest() # UpdateAnalysisDefinitionRequest |  (optional)

    try:
        # Update analysis definition details.
        api_response = api_instance.update_analysis_definition(analysis_definition_id, body=body)
        pprint(api_response)
    except ApiException as e:
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

