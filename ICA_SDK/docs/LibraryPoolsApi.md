# ICA_SDK.LibraryPoolsApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_library_pool**](LibraryPoolsApi.md#create_library_pool) | **POST** /v1/sequencing/librarypools | Create library pool.
[**get_library_pool**](LibraryPoolsApi.md#get_library_pool) | **GET** /v1/sequencing/librarypools/{libraryPoolId} | Get library pool details.
[**list_library_pools**](LibraryPoolsApi.md#list_library_pools) | **GET** /v1/sequencing/librarypools | Get a list of library pools.
[**merge_library_pool_acl**](LibraryPoolsApi.md#merge_library_pool_acl) | **PATCH** /v1/sequencing/librarypools/{libraryPoolId}/acl | Merge the access control list of a library pool with the input access control list.
[**remove_library_pool_acl**](LibraryPoolsApi.md#remove_library_pool_acl) | **DELETE** /v1/sequencing/librarypools/{libraryPoolId}/acl | Remove the input access control list from a library pool.
[**replace_library_pool_acl**](LibraryPoolsApi.md#replace_library_pool_acl) | **PUT** /v1/sequencing/librarypools/{libraryPoolId}/acl | Replace the access control list of a library pool with the input access control list.
[**update_library_pool**](LibraryPoolsApi.md#update_library_pool) | **PATCH** /v1/sequencing/librarypools/{libraryPoolId} | Update library pool.


# **create_library_pool**
> LibraryPool create_library_pool(body=body)

Create library pool.

Create a library pool, and return information about that library pool.

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
    api_instance = ICA_SDK.LibraryPoolsApi(api_client)
    body = ICA_SDK.CreateLibraryPoolRequest() # CreateLibraryPoolRequest |  (optional)

    try:
        # Create library pool.
        api_response = api_instance.create_library_pool(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPoolsApi->create_library_pool: %s\n" % e)
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
    api_instance = ICA_SDK.LibraryPoolsApi(api_client)
    body = ICA_SDK.CreateLibraryPoolRequest() # CreateLibraryPoolRequest |  (optional)

    try:
        # Create library pool.
        api_response = api_instance.create_library_pool(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPoolsApi->create_library_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLibraryPoolRequest**](CreateLibraryPoolRequest.md)|  | [optional] 

### Return type

[**LibraryPool**](LibraryPool.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Library pool created successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**409** | Unable to create library pool due to conflict with input parameters. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_pool**
> LibraryPool get_library_pool(library_pool_id)

Get library pool details.

For a given library pool ID, get the library pool details accessible by the request token.

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
    api_instance = ICA_SDK.LibraryPoolsApi(api_client)
    library_pool_id = 'library_pool_id_example' # str | 

    try:
        # Get library pool details.
        api_response = api_instance.get_library_pool(library_pool_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPoolsApi->get_library_pool: %s\n" % e)
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
    api_instance = ICA_SDK.LibraryPoolsApi(api_client)
    library_pool_id = 'library_pool_id_example' # str | 

    try:
        # Get library pool details.
        api_response = api_instance.get_library_pool(library_pool_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPoolsApi->get_library_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_pool_id** | **str**|  | 

### Return type

[**LibraryPool**](LibraryPool.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Library pool details returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No library pool found for given library pool ID. |  -  |
**410** | The library pool with the given library pool ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_library_pools**
> LibraryPoolCompactLibraryPoolSortFieldsPagedItems list_library_pools(include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)

Get a list of library pools.

Get a list of library pools accessible by the request token.

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
    api_instance = ICA_SDK.LibraryPoolsApi(api_client)
    include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)
tenant_ids = ['tenant_ids_example'] # list[str] | Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to 'timeCreated asc')

    try:
        # Get a list of library pools.
        api_response = api_instance.list_library_pools(include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPoolsApi->list_library_pools: %s\n" % e)
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
    api_instance = ICA_SDK.LibraryPoolsApi(api_client)
    include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)
tenant_ids = ['tenant_ids_example'] # list[str] | Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to 'timeCreated asc')

    try:
        # Get a list of library pools.
        api_response = api_instance.list_library_pools(include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPoolsApi->list_library_pools: %s\n" % e)
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

[**LibraryPoolCompactLibraryPoolSortFieldsPagedItems**](LibraryPoolCompactLibraryPoolSortFieldsPagedItems.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Library pools list returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_library_pool_acl**
> LibraryPool merge_library_pool_acl(library_pool_id, body=body)

Merge the access control list of a library pool with the input access control list.

Merge the access control list of a library pool with the input access control list, and return information about the library pool.

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
    api_instance = ICA_SDK.LibraryPoolsApi(api_client)
    library_pool_id = 'library_pool_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Merge the access control list of a library pool with the input access control list.
        api_response = api_instance.merge_library_pool_acl(library_pool_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPoolsApi->merge_library_pool_acl: %s\n" % e)
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
    api_instance = ICA_SDK.LibraryPoolsApi(api_client)
    library_pool_id = 'library_pool_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Merge the access control list of a library pool with the input access control list.
        api_response = api_instance.merge_library_pool_acl(library_pool_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPoolsApi->merge_library_pool_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_pool_id** | **str**|  | 
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional] 

### Return type

[**LibraryPool**](LibraryPool.md)

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
**404** | No library pool found for given library pool ID. |  -  |
**410** | The library pool with the given library pool ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_library_pool_acl**
> LibraryPool remove_library_pool_acl(library_pool_id, body=body)

Remove the input access control list from a library pool.

Remove the input access control list from a library pool, and return information about the library pool.

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
    api_instance = ICA_SDK.LibraryPoolsApi(api_client)
    library_pool_id = 'library_pool_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Remove the input access control list from a library pool.
        api_response = api_instance.remove_library_pool_acl(library_pool_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPoolsApi->remove_library_pool_acl: %s\n" % e)
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
    api_instance = ICA_SDK.LibraryPoolsApi(api_client)
    library_pool_id = 'library_pool_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Remove the input access control list from a library pool.
        api_response = api_instance.remove_library_pool_acl(library_pool_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPoolsApi->remove_library_pool_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_pool_id** | **str**|  | 
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional] 

### Return type

[**LibraryPool**](LibraryPool.md)

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
**404** | No library pool found for given library pool ID. |  -  |
**410** | The library pool with the given library pool ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_library_pool_acl**
> LibraryPool replace_library_pool_acl(library_pool_id, body=body)

Replace the access control list of a library pool with the input access control list.

Replace the access control list of a library pool with the input access control list, and return information about that library pool.

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
    api_instance = ICA_SDK.LibraryPoolsApi(api_client)
    library_pool_id = 'library_pool_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Replace the access control list of a library pool with the input access control list.
        api_response = api_instance.replace_library_pool_acl(library_pool_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPoolsApi->replace_library_pool_acl: %s\n" % e)
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
    api_instance = ICA_SDK.LibraryPoolsApi(api_client)
    library_pool_id = 'library_pool_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Replace the access control list of a library pool with the input access control list.
        api_response = api_instance.replace_library_pool_acl(library_pool_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPoolsApi->replace_library_pool_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_pool_id** | **str**|  | 
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional] 

### Return type

[**LibraryPool**](LibraryPool.md)

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
**404** | No library pool found for given library pool ID. |  -  |
**410** | The library pool with the given library pool ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_library_pool**
> LibraryPool update_library_pool(library_pool_id, body=body)

Update library pool.

Update a library pool, and return information about that library pool.

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
    api_instance = ICA_SDK.LibraryPoolsApi(api_client)
    library_pool_id = 'library_pool_id_example' # str | 
body = ICA_SDK.UpdateLibraryPoolRequest() # UpdateLibraryPoolRequest |  (optional)

    try:
        # Update library pool.
        api_response = api_instance.update_library_pool(library_pool_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPoolsApi->update_library_pool: %s\n" % e)
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
    api_instance = ICA_SDK.LibraryPoolsApi(api_client)
    library_pool_id = 'library_pool_id_example' # str | 
body = ICA_SDK.UpdateLibraryPoolRequest() # UpdateLibraryPoolRequest |  (optional)

    try:
        # Update library pool.
        api_response = api_instance.update_library_pool(library_pool_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPoolsApi->update_library_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_pool_id** | **str**|  | 
 **body** | [**UpdateLibraryPoolRequest**](UpdateLibraryPoolRequest.md)|  | [optional] 

### Return type

[**LibraryPool**](LibraryPool.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Library pool updated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No library pool found for given library pool ID. |  -  |
**409** | Unable to update library pool due to conflict with input parameters. |  -  |
**410** | The library pool with the given library pool ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

