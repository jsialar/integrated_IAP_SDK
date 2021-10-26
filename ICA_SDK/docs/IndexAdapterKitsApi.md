# ICA_SDK.IndexAdapterKitsApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_index_adapter_kit**](IndexAdapterKitsApi.md#create_index_adapter_kit) | **POST** /v1/sequencing/indexadapterkits | Create an index adapter kit.
[**create_index_adapter_kit_by_definition**](IndexAdapterKitsApi.md#create_index_adapter_kit_by_definition) | **POST** /v1/sequencing/indexadapterkits/definition | Create an index adapter kit using a definition string.
[**delete_index_adapter_kit**](IndexAdapterKitsApi.md#delete_index_adapter_kit) | **DELETE** /v1/sequencing/indexadapterkits/{indexAdapterKitId} | Delete index adapter kit.
[**get_index_adapter_kit**](IndexAdapterKitsApi.md#get_index_adapter_kit) | **GET** /v1/sequencing/indexadapterkits/{indexAdapterKitId} | Get index adapter kit details.
[**list_index_adapter_kits**](IndexAdapterKitsApi.md#list_index_adapter_kits) | **GET** /v1/sequencing/indexadapterkits | Get a list of index adapter kits.
[**merge_index_adapter_kit_acl**](IndexAdapterKitsApi.md#merge_index_adapter_kit_acl) | **PATCH** /v1/sequencing/indexadapterkits/{indexAdapterKitId}/acl | Merge the access control list of an index adapter kit with the input access control list.
[**remove_index_adapter_kit_acl**](IndexAdapterKitsApi.md#remove_index_adapter_kit_acl) | **DELETE** /v1/sequencing/indexadapterkits/{indexAdapterKitId}/acl | Remove the access control list of an index adapter kit.
[**replace_index_adapter_kit_acl**](IndexAdapterKitsApi.md#replace_index_adapter_kit_acl) | **PUT** /v1/sequencing/indexadapterkits/{indexAdapterKitId}/acl | Replace the access control list of an index adapter kit with the input access control list.
[**update_index_adapter_kit**](IndexAdapterKitsApi.md#update_index_adapter_kit) | **PATCH** /v1/sequencing/indexadapterkits/{indexAdapterKitId} | Update an index adapter kit.
[**update_index_adapter_kit_by_definition**](IndexAdapterKitsApi.md#update_index_adapter_kit_by_definition) | **PATCH** /v1/sequencing/indexadapterkits/{indexAdapterKitId}/definition | Update an index adapter kit using a definition string.


# **create_index_adapter_kit**
> IndexAdapterKit create_index_adapter_kit(body=body)

Create an index adapter kit.

Create an index adapter kit, and return information about that index adapter kit.

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
    api_instance = ICA_SDK.IndexAdapterKitsApi(api_client)
    body = ICA_SDK.CreateIndexAdapterKitRequest() # CreateIndexAdapterKitRequest |  (optional)

    try:
        # Create an index adapter kit.
        api_response = api_instance.create_index_adapter_kit(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndexAdapterKitsApi->create_index_adapter_kit: %s\n" % e)
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
    api_instance = ICA_SDK.IndexAdapterKitsApi(api_client)
    body = ICA_SDK.CreateIndexAdapterKitRequest() # CreateIndexAdapterKitRequest |  (optional)

    try:
        # Create an index adapter kit.
        api_response = api_instance.create_index_adapter_kit(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndexAdapterKitsApi->create_index_adapter_kit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateIndexAdapterKitRequest**](CreateIndexAdapterKitRequest.md)|  | [optional] 

### Return type

[**IndexAdapterKit**](IndexAdapterKit.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Index adapter kit created successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**409** | Unable to create index adapter kit. Conflict found (e.g. an index adapter kit with same name and version already exists). |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_index_adapter_kit_by_definition**
> IndexAdapterKit create_index_adapter_kit_by_definition(body=body)

Create an index adapter kit using a definition string.

Create an index adapter kit, and return information about that index adapter kit.

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
    api_instance = ICA_SDK.IndexAdapterKitsApi(api_client)
    body = ICA_SDK.CreateIndexAdapterKitByDefinitionRequest() # CreateIndexAdapterKitByDefinitionRequest |  (optional)

    try:
        # Create an index adapter kit using a definition string.
        api_response = api_instance.create_index_adapter_kit_by_definition(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndexAdapterKitsApi->create_index_adapter_kit_by_definition: %s\n" % e)
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
    api_instance = ICA_SDK.IndexAdapterKitsApi(api_client)
    body = ICA_SDK.CreateIndexAdapterKitByDefinitionRequest() # CreateIndexAdapterKitByDefinitionRequest |  (optional)

    try:
        # Create an index adapter kit using a definition string.
        api_response = api_instance.create_index_adapter_kit_by_definition(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndexAdapterKitsApi->create_index_adapter_kit_by_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateIndexAdapterKitByDefinitionRequest**](CreateIndexAdapterKitByDefinitionRequest.md)|  | [optional] 

### Return type

[**IndexAdapterKit**](IndexAdapterKit.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Index adapter kit created successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**409** | Unable to create index adapter kit. Conflict found (e.g. an index adapter kit with same name and version already exists). |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_index_adapter_kit**
> NoContentResult delete_index_adapter_kit(index_adapter_kit_id, force=force)

Delete index adapter kit.

For a given index adapter kit ID, delete the index adapter kit.

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
    api_instance = ICA_SDK.IndexAdapterKitsApi(api_client)
    index_adapter_kit_id = 'index_adapter_kit_id_example' # str | ID of the index adapter kit
force = True # bool | Force delete the index adapter kit (optional)

    try:
        # Delete index adapter kit.
        api_response = api_instance.delete_index_adapter_kit(index_adapter_kit_id, force=force)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndexAdapterKitsApi->delete_index_adapter_kit: %s\n" % e)
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
    api_instance = ICA_SDK.IndexAdapterKitsApi(api_client)
    index_adapter_kit_id = 'index_adapter_kit_id_example' # str | ID of the index adapter kit
force = True # bool | Force delete the index adapter kit (optional)

    try:
        # Delete index adapter kit.
        api_response = api_instance.delete_index_adapter_kit(index_adapter_kit_id, force=force)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndexAdapterKitsApi->delete_index_adapter_kit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_adapter_kit_id** | **str**| ID of the index adapter kit | 
 **force** | **bool**| Force delete the index adapter kit | [optional] 

### Return type

[**NoContentResult**](NoContentResult.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Index adapter kit deleted successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No index adapter kit found for given index adapter kit ID. |  -  |
**410** | Index adapter kit for the given index adapter kit ID has already been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_index_adapter_kit**
> IndexAdapterKit get_index_adapter_kit(index_adapter_kit_id, include=include)

Get index adapter kit details.

For a given index adapter kit ID, get the index adapter kit details.

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
    api_instance = ICA_SDK.IndexAdapterKitsApi(api_client)
    index_adapter_kit_id = 'index_adapter_kit_id_example' # str | ID of the index adapter kit
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)

    try:
        # Get index adapter kit details.
        api_response = api_instance.get_index_adapter_kit(index_adapter_kit_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndexAdapterKitsApi->get_index_adapter_kit: %s\n" % e)
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
    api_instance = ICA_SDK.IndexAdapterKitsApi(api_client)
    index_adapter_kit_id = 'index_adapter_kit_id_example' # str | ID of the index adapter kit
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)

    try:
        # Get index adapter kit details.
        api_response = api_instance.get_index_adapter_kit(index_adapter_kit_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndexAdapterKitsApi->get_index_adapter_kit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_adapter_kit_id** | **str**| ID of the index adapter kit | 
 **include** | [**list[str]**](str.md)| Include flags to specify what is included in the response | [optional] 

### Return type

[**IndexAdapterKit**](IndexAdapterKit.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Index adapter kit details returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No index adapter kit found for given index adapter kit ID. |  -  |
**410** | The index adapter kit for the given ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_index_adapter_kits**
> IndexAdapterKitCompactIndexAdapterKitSortFieldPagedItems list_index_adapter_kits(include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)

Get a list of index adapter kits.

Get a list of index adapter kits accessible by the current request token.

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
    api_instance = ICA_SDK.IndexAdapterKitsApi(api_client)
    include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)
tenant_ids = ['tenant_ids_example'] # list[str] | Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to 'timeCreated asc')

    try:
        # Get a list of index adapter kits.
        api_response = api_instance.list_index_adapter_kits(include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndexAdapterKitsApi->list_index_adapter_kits: %s\n" % e)
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
    api_instance = ICA_SDK.IndexAdapterKitsApi(api_client)
    include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)
tenant_ids = ['tenant_ids_example'] # list[str] | Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to 'timeCreated asc')

    try:
        # Get a list of index adapter kits.
        api_response = api_instance.list_index_adapter_kits(include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndexAdapterKitsApi->list_index_adapter_kits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**list[str]**](str.md)| Include flags to specify what is included in the response | [optional] 
 **tenant_ids** | [**list[str]**](str.md)| Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids | [optional] 
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] [default to 10]
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional] 
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] [default to &#39;timeCreated asc&#39;]

### Return type

[**IndexAdapterKitCompactIndexAdapterKitSortFieldPagedItems**](IndexAdapterKitCompactIndexAdapterKitSortFieldPagedItems.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Index adapter kits returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_index_adapter_kit_acl**
> IndexAdapterKit merge_index_adapter_kit_acl(index_adapter_kit_id, body=body)

Merge the access control list of an index adapter kit with the input access control list.

Merge the access control list of an index adapter kit with the input access control list, and return information about that index adapter kit.

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
    api_instance = ICA_SDK.IndexAdapterKitsApi(api_client)
    index_adapter_kit_id = 'index_adapter_kit_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Merge the access control list of an index adapter kit with the input access control list.
        api_response = api_instance.merge_index_adapter_kit_acl(index_adapter_kit_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndexAdapterKitsApi->merge_index_adapter_kit_acl: %s\n" % e)
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
    api_instance = ICA_SDK.IndexAdapterKitsApi(api_client)
    index_adapter_kit_id = 'index_adapter_kit_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Merge the access control list of an index adapter kit with the input access control list.
        api_response = api_instance.merge_index_adapter_kit_acl(index_adapter_kit_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndexAdapterKitsApi->merge_index_adapter_kit_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_adapter_kit_id** | **str**|  | 
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional] 

### Return type

[**IndexAdapterKit**](IndexAdapterKit.md)

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
**404** | No index adapter kit found for the given index adapter kit ID. |  -  |
**410** | The index adapter kit with the given ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_index_adapter_kit_acl**
> IndexAdapterKit remove_index_adapter_kit_acl(index_adapter_kit_id, body=body)

Remove the access control list of an index adapter kit.

Remove the access control list of a given index adapter kit, and return information about that index adapter kit.

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
    api_instance = ICA_SDK.IndexAdapterKitsApi(api_client)
    index_adapter_kit_id = 'index_adapter_kit_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Remove the access control list of an index adapter kit.
        api_response = api_instance.remove_index_adapter_kit_acl(index_adapter_kit_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndexAdapterKitsApi->remove_index_adapter_kit_acl: %s\n" % e)
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
    api_instance = ICA_SDK.IndexAdapterKitsApi(api_client)
    index_adapter_kit_id = 'index_adapter_kit_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Remove the access control list of an index adapter kit.
        api_response = api_instance.remove_index_adapter_kit_acl(index_adapter_kit_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndexAdapterKitsApi->remove_index_adapter_kit_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_adapter_kit_id** | **str**|  | 
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional] 

### Return type

[**IndexAdapterKit**](IndexAdapterKit.md)

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
**404** | No index adapter kit found for given index adapter kit ID. |  -  |
**410** | The index adapter kit with the given ID has already been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_index_adapter_kit_acl**
> IndexAdapterKit replace_index_adapter_kit_acl(index_adapter_kit_id, body=body)

Replace the access control list of an index adapter kit with the input access control list.

Replace the access control list of an index adapter kit with the input access control list, and return information about that index adapter kit.

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
    api_instance = ICA_SDK.IndexAdapterKitsApi(api_client)
    index_adapter_kit_id = 'index_adapter_kit_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Replace the access control list of an index adapter kit with the input access control list.
        api_response = api_instance.replace_index_adapter_kit_acl(index_adapter_kit_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndexAdapterKitsApi->replace_index_adapter_kit_acl: %s\n" % e)
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
    api_instance = ICA_SDK.IndexAdapterKitsApi(api_client)
    index_adapter_kit_id = 'index_adapter_kit_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Replace the access control list of an index adapter kit with the input access control list.
        api_response = api_instance.replace_index_adapter_kit_acl(index_adapter_kit_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndexAdapterKitsApi->replace_index_adapter_kit_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_adapter_kit_id** | **str**|  | 
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional] 

### Return type

[**IndexAdapterKit**](IndexAdapterKit.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Index adapter kit access control list updated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No index adapter kit found for given index adapter kit ID. |  -  |
**410** | The index adapter kit with the given ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_index_adapter_kit**
> IndexAdapterKit update_index_adapter_kit(index_adapter_kit_id, body=body)

Update an index adapter kit.

Update an index adapter kit, and return information about that index adapter kit.

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
    api_instance = ICA_SDK.IndexAdapterKitsApi(api_client)
    index_adapter_kit_id = 'index_adapter_kit_id_example' # str | 
body = ICA_SDK.UpdateIndexAdapterKitRequest() # UpdateIndexAdapterKitRequest |  (optional)

    try:
        # Update an index adapter kit.
        api_response = api_instance.update_index_adapter_kit(index_adapter_kit_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndexAdapterKitsApi->update_index_adapter_kit: %s\n" % e)
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
    api_instance = ICA_SDK.IndexAdapterKitsApi(api_client)
    index_adapter_kit_id = 'index_adapter_kit_id_example' # str | 
body = ICA_SDK.UpdateIndexAdapterKitRequest() # UpdateIndexAdapterKitRequest |  (optional)

    try:
        # Update an index adapter kit.
        api_response = api_instance.update_index_adapter_kit(index_adapter_kit_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndexAdapterKitsApi->update_index_adapter_kit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_adapter_kit_id** | **str**|  | 
 **body** | [**UpdateIndexAdapterKitRequest**](UpdateIndexAdapterKitRequest.md)|  | [optional] 

### Return type

[**IndexAdapterKit**](IndexAdapterKit.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Index adapter kit updated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No index adapter kit found for given index adapter kit ID. |  -  |
**409** | Unable to update index adapter kit. Conflict found (e.g. an index adapter kit with same name and version already exists). |  -  |
**410** | The index adapter kit with the given ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_index_adapter_kit_by_definition**
> IndexAdapterKit update_index_adapter_kit_by_definition(index_adapter_kit_id, body=body)

Update an index adapter kit using a definition string.

Update an index adapter kit, and return information about that index adapter kit.

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
    api_instance = ICA_SDK.IndexAdapterKitsApi(api_client)
    index_adapter_kit_id = 'index_adapter_kit_id_example' # str | 
body = ICA_SDK.UpdateIndexAdapterKitByDefinitionRequest() # UpdateIndexAdapterKitByDefinitionRequest |  (optional)

    try:
        # Update an index adapter kit using a definition string.
        api_response = api_instance.update_index_adapter_kit_by_definition(index_adapter_kit_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndexAdapterKitsApi->update_index_adapter_kit_by_definition: %s\n" % e)
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
    api_instance = ICA_SDK.IndexAdapterKitsApi(api_client)
    index_adapter_kit_id = 'index_adapter_kit_id_example' # str | 
body = ICA_SDK.UpdateIndexAdapterKitByDefinitionRequest() # UpdateIndexAdapterKitByDefinitionRequest |  (optional)

    try:
        # Update an index adapter kit using a definition string.
        api_response = api_instance.update_index_adapter_kit_by_definition(index_adapter_kit_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndexAdapterKitsApi->update_index_adapter_kit_by_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_adapter_kit_id** | **str**|  | 
 **body** | [**UpdateIndexAdapterKitByDefinitionRequest**](UpdateIndexAdapterKitByDefinitionRequest.md)|  | [optional] 

### Return type

[**IndexAdapterKit**](IndexAdapterKit.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Index adapter kit updated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No index adapter kit found for given index adapter kit ID. |  -  |
**409** | Unable to update index adapter kit. Conflict found (e.g. an index adapter kit with same name and version already exists). |  -  |
**410** | The index adapter kit with the given ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

