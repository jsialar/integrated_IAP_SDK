# ICA_SDK.LibraryPrepKitsApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_library_prep_kit**](LibraryPrepKitsApi.md#create_library_prep_kit) | **POST** /v1/sequencing/libraryPrepKits | Create a library prep kit.
[**delete_library_prep_kit**](LibraryPrepKitsApi.md#delete_library_prep_kit) | **DELETE** /v1/sequencing/libraryPrepKits/{libraryPrepKitId} | Delete library prep kit.
[**get_library_prep_kit**](LibraryPrepKitsApi.md#get_library_prep_kit) | **GET** /v1/sequencing/libraryPrepKits/{libraryPrepKitId} | Get library prep kit details.
[**list_library_prep_kits**](LibraryPrepKitsApi.md#list_library_prep_kits) | **GET** /v1/sequencing/libraryPrepKits | Get a list of library prep kits.
[**merge_library_prep_kit_acl**](LibraryPrepKitsApi.md#merge_library_prep_kit_acl) | **PATCH** /v1/sequencing/libraryPrepKits/{libraryPrepKitId}/acl | Merge the access control list of a library prep kit with the input access control list.
[**remove_library_prep_kit_acl**](LibraryPrepKitsApi.md#remove_library_prep_kit_acl) | **DELETE** /v1/sequencing/libraryPrepKits/{libraryPrepKitId}/acl | Remove the access control list of a given library prep kit.
[**replace_library_prep_kit_acl**](LibraryPrepKitsApi.md#replace_library_prep_kit_acl) | **PUT** /v1/sequencing/libraryPrepKits/{libraryPrepKitId}/acl | Replace the access control list of a library prep kit with the input access control list.
[**update_library_prep_kit**](LibraryPrepKitsApi.md#update_library_prep_kit) | **PATCH** /v1/sequencing/libraryPrepKits/{libraryPrepKitId} | Update a library prep kit.


# **create_library_prep_kit**
> LibraryPrepKit create_library_prep_kit()

Create a library prep kit.

Create a library prep kit, and return information about that library prep kit.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import library_prep_kits_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.create_library_prep_kit_request import CreateLibraryPrepKitRequest
from ICA_SDK.model.library_prep_kit import LibraryPrepKit
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
    api_instance = library_prep_kits_api.LibraryPrepKitsApi(api_client)
    body = CreateLibraryPrepKitRequest(
        name="name_example",
        display_name="display_name_example",
        organization="organization_example",
        description="description_example",
        allowed_read_types=[
            "Single",
        ],
        default_read1_length=0,
        default_read2_length=0,
        is_application_specific=True,
        settings=LibraryPrepKitSettings(
            default_read_type="Single",
        ),
        checksum="checksum_example",
        index_adapter_kit_ids=[
            "index_adapter_kit_ids_example",
        ],
        acl=[
            "acl_example",
        ],
    ) # CreateLibraryPrepKitRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a library prep kit.
        api_response = api_instance.create_library_prep_kit(body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->create_library_prep_kit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLibraryPrepKitRequest**](CreateLibraryPrepKitRequest.md)|  | [optional]

### Return type

[**LibraryPrepKit**](LibraryPrepKit.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Library prep kit created successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**409** | Unable to create library prep kit. Conflict found (e.g. a library prep kit with same name and version already exists). |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_library_prep_kit**
> NoContentResult delete_library_prep_kit(library_prep_kit_id)

Delete library prep kit.

For a given library prep kit ID, delete the library prep kit.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import library_prep_kits_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.no_content_result import NoContentResult
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
    api_instance = library_prep_kits_api.LibraryPrepKitsApi(api_client)
    library_prep_kit_id = "libraryPrepKitId_example" # str | ID of the library prep kit
    force = True # bool | Force delete the library prep kit (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete library prep kit.
        api_response = api_instance.delete_library_prep_kit(library_prep_kit_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->delete_library_prep_kit: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete library prep kit.
        api_response = api_instance.delete_library_prep_kit(library_prep_kit_id, force=force)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->delete_library_prep_kit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_prep_kit_id** | **str**| ID of the library prep kit |
 **force** | **bool**| Force delete the library prep kit | [optional]

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
**204** | Library prep kit deleted successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No library prep kit found for given library prep kit ID. |  -  |
**410** | Library prep kit for the given library prep kit ID has already been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_prep_kit**
> LibraryPrepKit get_library_prep_kit(library_prep_kit_id)

Get library prep kit details.

For a given library prep kit ID, return information about that library prep kit.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import library_prep_kits_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.library_prep_kit import LibraryPrepKit
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
    api_instance = library_prep_kits_api.LibraryPrepKitsApi(api_client)
    library_prep_kit_id = "libraryPrepKitId_example" # str | ID of the library prep kit
    include = [
        "CanUpdate",
    ] # [str] | Include flags to specify what is included in the response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get library prep kit details.
        api_response = api_instance.get_library_prep_kit(library_prep_kit_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->get_library_prep_kit: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get library prep kit details.
        api_response = api_instance.get_library_prep_kit(library_prep_kit_id, include=include)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->get_library_prep_kit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_prep_kit_id** | **str**| ID of the library prep kit |
 **include** | **[str]**| Include flags to specify what is included in the response | [optional]

### Return type

[**LibraryPrepKit**](LibraryPrepKit.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Library prep kit found and details returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | \&quot;Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No library prep kit found for given library prep kit ID. |  -  |
**410** | The library prep kit with the given library prep kit ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_library_prep_kits**
> LibraryPrepKitCompactLibraryPrepKitSortFieldsPagedItems list_library_prep_kits()

Get a list of library prep kits.

Get a list of library prep kits accessible by the current request token.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import library_prep_kits_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.library_prep_kit_compact_library_prep_kit_sort_fields_paged_items import LibraryPrepKitCompactLibraryPrepKitSortFieldsPagedItems
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
    api_instance = library_prep_kits_api.LibraryPrepKitsApi(api_client)
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
        # Get a list of library prep kits.
        api_response = api_instance.list_library_prep_kits(include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->list_library_prep_kits: %s\n" % e)
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

[**LibraryPrepKitCompactLibraryPrepKitSortFieldsPagedItems**](LibraryPrepKitCompactLibraryPrepKitSortFieldsPagedItems.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Library prep kits found and returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_library_prep_kit_acl**
> LibraryPrepKit merge_library_prep_kit_acl(library_prep_kit_id)

Merge the access control list of a library prep kit with the input access control list.

For a given library prep kit ID, merge the access control list with the input access control list, and return information about the library prep kit

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import library_prep_kits_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_acl_request import UpdateAclRequest
from ICA_SDK.model.library_prep_kit import LibraryPrepKit
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
    api_instance = library_prep_kits_api.LibraryPrepKitsApi(api_client)
    library_prep_kit_id = "libraryPrepKitId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Merge the access control list of a library prep kit with the input access control list.
        api_response = api_instance.merge_library_prep_kit_acl(library_prep_kit_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->merge_library_prep_kit_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Merge the access control list of a library prep kit with the input access control list.
        api_response = api_instance.merge_library_prep_kit_acl(library_prep_kit_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->merge_library_prep_kit_acl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_prep_kit_id** | **str**|  |
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional]

### Return type

[**LibraryPrepKit**](LibraryPrepKit.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Library prep kit access control list updated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No library prep kit found for given library prep kit ID. |  -  |
**410** | The library prep kit with the given library prep kit ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_library_prep_kit_acl**
> LibraryPrepKit remove_library_prep_kit_acl(library_prep_kit_id)

Remove the access control list of a given library prep kit.

Remove the access control list of a given library prep kit, and return information about that library prep kit.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import library_prep_kits_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_acl_request import UpdateAclRequest
from ICA_SDK.model.library_prep_kit import LibraryPrepKit
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
    api_instance = library_prep_kits_api.LibraryPrepKitsApi(api_client)
    library_prep_kit_id = "libraryPrepKitId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove the access control list of a given library prep kit.
        api_response = api_instance.remove_library_prep_kit_acl(library_prep_kit_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->remove_library_prep_kit_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove the access control list of a given library prep kit.
        api_response = api_instance.remove_library_prep_kit_acl(library_prep_kit_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->remove_library_prep_kit_acl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_prep_kit_id** | **str**|  |
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional]

### Return type

[**LibraryPrepKit**](LibraryPrepKit.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Library prep kit access control list removed successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No library prep kit found for given library prep kit ID. |  -  |
**410** | The library prep kit with the given library prep kit ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_library_prep_kit_acl**
> LibraryPrepKit replace_library_prep_kit_acl(library_prep_kit_id)

Replace the access control list of a library prep kit with the input access control list.

For a given library prep kit ID, replace the access control list with the input access control list, and return information about the library prep kit.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import library_prep_kits_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_acl_request import UpdateAclRequest
from ICA_SDK.model.library_prep_kit import LibraryPrepKit
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
    api_instance = library_prep_kits_api.LibraryPrepKitsApi(api_client)
    library_prep_kit_id = "libraryPrepKitId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Replace the access control list of a library prep kit with the input access control list.
        api_response = api_instance.replace_library_prep_kit_acl(library_prep_kit_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->replace_library_prep_kit_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Replace the access control list of a library prep kit with the input access control list.
        api_response = api_instance.replace_library_prep_kit_acl(library_prep_kit_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->replace_library_prep_kit_acl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_prep_kit_id** | **str**|  |
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional]

### Return type

[**LibraryPrepKit**](LibraryPrepKit.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Library prep kit access control list updated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No library prep kit found for given library prep kit ID. |  -  |
**410** | The library prep kit with the given library prep kit ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_library_prep_kit**
> LibraryPrepKit update_library_prep_kit(library_prep_kit_id)

Update a library prep kit.

For a given library prep kit ID, update the associated library prep kit.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import library_prep_kits_api
from ICA_SDK.model.update_library_prep_kit_request import UpdateLibraryPrepKitRequest
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.library_prep_kit import LibraryPrepKit
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
    api_instance = library_prep_kits_api.LibraryPrepKitsApi(api_client)
    library_prep_kit_id = "libraryPrepKitId_example" # str | The id of the requested library prep kit.
    body = UpdateLibraryPrepKitRequest(
        name="name_example",
        display_name="display_name_example",
        organization="organization_example",
        description="description_example",
        allowed_read_types=[
            "Single",
        ],
        default_read1_length=0,
        default_read2_length=0,
        settings=LibraryPrepKitSettings(
            default_read_type="Single",
        ),
        checksum="checksum_example",
        is_application_specific=True,
        index_adapter_kit_ids=[
            "index_adapter_kit_ids_example",
        ],
        force=True,
        acl=[
            "acl_example",
        ],
    ) # UpdateLibraryPrepKitRequest | The update request for the library prep kit (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a library prep kit.
        api_response = api_instance.update_library_prep_kit(library_prep_kit_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->update_library_prep_kit: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a library prep kit.
        api_response = api_instance.update_library_prep_kit(library_prep_kit_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->update_library_prep_kit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_prep_kit_id** | **str**| The id of the requested library prep kit. |
 **body** | [**UpdateLibraryPrepKitRequest**](UpdateLibraryPrepKitRequest.md)| The update request for the library prep kit | [optional]

### Return type

[**LibraryPrepKit**](LibraryPrepKit.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Library prep kit updated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | \&quot;Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No library prep kit found for given library prep kit ID. |  -  |
**409** | Unable to update library prep kit. Conflict found (e.g. a library prep kit with same name and version already exists). |  -  |
**410** | The library prep kit with the given library prep kit ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

