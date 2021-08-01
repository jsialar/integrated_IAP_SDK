# ICA_SDK.LibrariesApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_library**](LibrariesApi.md#create_library) | **POST** /v1/sequencing/samples/{sampleId}/libraries | Create library.
[**disassociate_library_prep_kit_from_library**](LibrariesApi.md#disassociate_library_prep_kit_from_library) | **POST** /v1/sequencing/libraries/{libraryId}:disassociateLibraryPrepKit | Disassociate library prep kit and index adapter kit from library.
[**get_library**](LibrariesApi.md#get_library) | **GET** /v1/sequencing/libraries/{libraryId} | Get library details.
[**list_libraries**](LibrariesApi.md#list_libraries) | **GET** /v1/sequencing/libraries | Get a list of libraries.
[**merge_library_acl**](LibrariesApi.md#merge_library_acl) | **PATCH** /v1/sequencing/libraries/{libraryId}/acl | Merge the access control list of a library.
[**remove_library_acl**](LibrariesApi.md#remove_library_acl) | **DELETE** /v1/sequencing/libraries/{libraryId}/acl | Remove the access control list of a library.
[**replace_library_acl**](LibrariesApi.md#replace_library_acl) | **PUT** /v1/sequencing/libraries/{libraryId}/acl | Replace the access control list of a library.
[**update_library**](LibrariesApi.md#update_library) | **PATCH** /v1/sequencing/libraries/{libraryId} | Update library.


# **create_library**
> Library create_library(sample_id)

Create library.

Create a library, and return information about that library.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import libraries_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.create_library_request import CreateLibraryRequest
from ICA_SDK.model.library import Library
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
    api_instance = libraries_api.LibrariesApi(api_client)
    sample_id = "sampleId_example" # str | 
    body = CreateLibraryRequest(
        name="name_example",
        description="description_example",
        status="Active",
        library_prep_kit_id="library_prep_kit_id_example",
        index_adapter_kit_id="index_adapter_kit_id_example",
        index_container_position="index_container_position_example",
        index1_sequence="index1_sequence_example",
        index2_sequence="index2_sequence_example",
        index1_name="index1_name_example",
        index2_name="index2_name_example",
        adapter_sequence_read1="adapter_sequence_read1_example",
        adapter_sequence_read2="adapter_sequence_read2_example",
        acl=[
            "acl_example",
        ],
    ) # CreateLibraryRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create library.
        api_response = api_instance.create_library(sample_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibrariesApi->create_library: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create library.
        api_response = api_instance.create_library(sample_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibrariesApi->create_library: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **str**|  |
 **body** | [**CreateLibraryRequest**](CreateLibraryRequest.md)|  | [optional]

### Return type

[**Library**](Library.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Library created successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**409** | Unable to create library. Conflict found (e.g. invalid sample ID, or library with the same name already exists). |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disassociate_library_prep_kit_from_library**
> Library disassociate_library_prep_kit_from_library(library_id)

Disassociate library prep kit and index adapter kit from library.

For a given library ID, disassociate the library prep kit and index adapter kit.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import libraries_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.library import Library
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
    api_instance = libraries_api.LibrariesApi(api_client)
    library_id = "libraryId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Disassociate library prep kit and index adapter kit from library.
        api_response = api_instance.disassociate_library_prep_kit_from_library(library_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibrariesApi->disassociate_library_prep_kit_from_library: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**|  |

### Return type

[**Library**](Library.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Disassociation completed successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No library found for given library ID. |  -  |
**409** | No associated library prep kit found for given library ID. |  -  |
**410** | The library with given library ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library**
> Library get_library(library_id)

Get library details.

For a given library ID, get the details of the library.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import libraries_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.library import Library
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
    api_instance = libraries_api.LibrariesApi(api_client)
    library_id = "libraryId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get library details.
        api_response = api_instance.get_library(library_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibrariesApi->get_library: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**|  |

### Return type

[**Library**](Library.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Library returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No library found for given library ID. |  -  |
**410** | The library with given library ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_libraries**
> LibraryCompactLibrarySortFieldsPagedItems list_libraries()

Get a list of libraries.

Get a list of libraries accessible by the request token.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import libraries_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.library_compact_library_sort_fields_paged_items import LibraryCompactLibrarySortFieldsPagedItems
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
    api_instance = libraries_api.LibrariesApi(api_client)
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
        # Get a list of libraries.
        api_response = api_instance.list_libraries(include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibrariesApi->list_libraries: %s\n" % e)
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

[**LibraryCompactLibrarySortFieldsPagedItems**](LibraryCompactLibrarySortFieldsPagedItems.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Libraries returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_library_acl**
> Library merge_library_acl(library_id)

Merge the access control list of a library.

Merge the access control list of a library, and return information about that library.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import libraries_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_acl_request import UpdateAclRequest
from ICA_SDK.model.library import Library
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
    api_instance = libraries_api.LibrariesApi(api_client)
    library_id = "libraryId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Merge the access control list of a library.
        api_response = api_instance.merge_library_acl(library_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibrariesApi->merge_library_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Merge the access control list of a library.
        api_response = api_instance.merge_library_acl(library_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibrariesApi->merge_library_acl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**|  |
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional]

### Return type

[**Library**](Library.md)

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
**404** | No library found with the given ID. |  -  |
**410** | The library with the given ID has been disabled. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_library_acl**
> Library remove_library_acl(library_id)

Remove the access control list of a library.

Remove the access control list of a library, and return information about that library.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import libraries_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_acl_request import UpdateAclRequest
from ICA_SDK.model.library import Library
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
    api_instance = libraries_api.LibrariesApi(api_client)
    library_id = "libraryId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove the access control list of a library.
        api_response = api_instance.remove_library_acl(library_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibrariesApi->remove_library_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove the access control list of a library.
        api_response = api_instance.remove_library_acl(library_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibrariesApi->remove_library_acl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**|  |
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional]

### Return type

[**Library**](Library.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Input access control list of the library removed successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No library found with the given ID. |  -  |
**410** | The library with the given ID has been disabled. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_library_acl**
> Library replace_library_acl(library_id)

Replace the access control list of a library.

Replace the access control list of a library, and return information about that library.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import libraries_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_acl_request import UpdateAclRequest
from ICA_SDK.model.library import Library
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
    api_instance = libraries_api.LibrariesApi(api_client)
    library_id = "libraryId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Replace the access control list of a library.
        api_response = api_instance.replace_library_acl(library_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibrariesApi->replace_library_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Replace the access control list of a library.
        api_response = api_instance.replace_library_acl(library_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibrariesApi->replace_library_acl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**|  |
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional]

### Return type

[**Library**](Library.md)

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
**404** | No library found with the given ID. |  -  |
**410** | The library with the given ID has been disabled. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_library**
> Library update_library(library_id)

Update library.

For a given library ID, update the library.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import libraries_api
from ICA_SDK.model.update_library_request import UpdateLibraryRequest
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.library import Library
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
    api_instance = libraries_api.LibrariesApi(api_client)
    library_id = "libraryId_example" # str | The id of the requested library.
    body = UpdateLibraryRequest(
        name="name_example",
        description="description_example",
        status="Active",
        library_prep_kit_id="library_prep_kit_id_example",
        index_adapter_kit_id="index_adapter_kit_id_example",
        index_container_position="index_container_position_example",
        index1_name="index1_name_example",
        index2_name="index2_name_example",
        index1_sequence="index1_sequence_example",
        index2_sequence="index2_sequence_example",
        adapter_sequence_read1="adapter_sequence_read1_example",
        adapter_sequence_read2="adapter_sequence_read2_example",
        acl=[
            "acl_example",
        ],
    ) # UpdateLibraryRequest | The update request for the library (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update library.
        api_response = api_instance.update_library(library_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibrariesApi->update_library: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update library.
        api_response = api_instance.update_library(library_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling LibrariesApi->update_library: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**| The id of the requested library. |
 **body** | [**UpdateLibraryRequest**](UpdateLibraryRequest.md)| The update request for the library | [optional]

### Return type

[**Library**](Library.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Library updated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | \&quot;Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No library found for given library ID. |  -  |
**409** | Unable to update library. Conflict found (e.g. library with same name already exists). |  -  |
**410** | The library with the given library ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

