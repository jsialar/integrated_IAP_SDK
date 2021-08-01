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
> LibraryPool create_library_pool()

Create library pool.

Create a library pool, and return information about that library pool.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import library_pools_api
from ICA_SDK.model.library_pool import LibraryPool
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.create_library_pool_request import CreateLibraryPoolRequest
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
    api_instance = library_pools_api.LibraryPoolsApi(api_client)
    body = CreateLibraryPoolRequest(
        name="name_example",
        library_ids=[
            "library_ids_example",
        ],
        description="description_example",
        status="Active",
        acl=[
            "acl_example",
        ],
    ) # CreateLibraryPoolRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create library pool.
        api_response = api_instance.create_library_pool(body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import library_pools_api
from ICA_SDK.model.library_pool import LibraryPool
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
    api_instance = library_pools_api.LibraryPoolsApi(api_client)
    library_pool_id = "libraryPoolId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get library pool details.
        api_response = api_instance.get_library_pool(library_pool_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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
> LibraryPoolCompactLibraryPoolSortFieldsPagedItems list_library_pools()

Get a list of library pools.

Get a list of library pools accessible by the request token.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import library_pools_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.library_pool_compact_library_pool_sort_fields_paged_items import LibraryPoolCompactLibraryPoolSortFieldsPagedItems
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
    api_instance = library_pools_api.LibraryPoolsApi(api_client)
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
        # Get a list of library pools.
        api_response = api_instance.list_library_pools(include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibraryPoolsApi->list_library_pools: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **[str]**| Include flags to specify what is included in the response | [optional]
 **tenant_ids** | **[str]**| Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids | [optional]
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] if omitted the server will use the default value of 10
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional]
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] if omitted the server will use the default value of "timeCreated asc"

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
> LibraryPool merge_library_pool_acl(library_pool_id)

Merge the access control list of a library pool with the input access control list.

Merge the access control list of a library pool with the input access control list, and return information about the library pool.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import library_pools_api
from ICA_SDK.model.library_pool import LibraryPool
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
    api_instance = library_pools_api.LibraryPoolsApi(api_client)
    library_pool_id = "libraryPoolId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Merge the access control list of a library pool with the input access control list.
        api_response = api_instance.merge_library_pool_acl(library_pool_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibraryPoolsApi->merge_library_pool_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Merge the access control list of a library pool with the input access control list.
        api_response = api_instance.merge_library_pool_acl(library_pool_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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
> LibraryPool remove_library_pool_acl(library_pool_id)

Remove the input access control list from a library pool.

Remove the input access control list from a library pool, and return information about the library pool.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import library_pools_api
from ICA_SDK.model.library_pool import LibraryPool
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
    api_instance = library_pools_api.LibraryPoolsApi(api_client)
    library_pool_id = "libraryPoolId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove the input access control list from a library pool.
        api_response = api_instance.remove_library_pool_acl(library_pool_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibraryPoolsApi->remove_library_pool_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove the input access control list from a library pool.
        api_response = api_instance.remove_library_pool_acl(library_pool_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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
> LibraryPool replace_library_pool_acl(library_pool_id)

Replace the access control list of a library pool with the input access control list.

Replace the access control list of a library pool with the input access control list, and return information about that library pool.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import library_pools_api
from ICA_SDK.model.library_pool import LibraryPool
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
    api_instance = library_pools_api.LibraryPoolsApi(api_client)
    library_pool_id = "libraryPoolId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Replace the access control list of a library pool with the input access control list.
        api_response = api_instance.replace_library_pool_acl(library_pool_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibraryPoolsApi->replace_library_pool_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Replace the access control list of a library pool with the input access control list.
        api_response = api_instance.replace_library_pool_acl(library_pool_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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
> LibraryPool update_library_pool(library_pool_id)

Update library pool.

Update a library pool, and return information about that library pool.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import library_pools_api
from ICA_SDK.model.library_pool import LibraryPool
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_library_pool_request import UpdateLibraryPoolRequest
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
    api_instance = library_pools_api.LibraryPoolsApi(api_client)
    library_pool_id = "libraryPoolId_example" # str | 
    body = UpdateLibraryPoolRequest(
        name="name_example",
        library_ids=[
            "library_ids_example",
        ],
        description="description_example",
        status="Active",
        acl=[
            "acl_example",
        ],
    ) # UpdateLibraryPoolRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update library pool.
        api_response = api_instance.update_library_pool(library_pool_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibraryPoolsApi->update_library_pool: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update library pool.
        api_response = api_instance.update_library_pool(library_pool_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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

