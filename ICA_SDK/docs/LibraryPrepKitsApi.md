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
> LibraryPrepKit create_library_prep_kit(body=body)

Create a library prep kit.

Create a library prep kit, and return information about that library prep kit.

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
    api_instance = ICA_SDK.LibraryPrepKitsApi(api_client)
    body = ICA_SDK.CreateLibraryPrepKitRequest() # CreateLibraryPrepKitRequest |  (optional)

    try:
        # Create a library prep kit.
        api_response = api_instance.create_library_prep_kit(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->create_library_prep_kit: %s\n" % e)
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
    api_instance = ICA_SDK.LibraryPrepKitsApi(api_client)
    body = ICA_SDK.CreateLibraryPrepKitRequest() # CreateLibraryPrepKitRequest |  (optional)

    try:
        # Create a library prep kit.
        api_response = api_instance.create_library_prep_kit(body=body)
        pprint(api_response)
    except ApiException as e:
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
> NoContentResult delete_library_prep_kit(library_prep_kit_id, force=force)

Delete library prep kit.

For a given library prep kit ID, delete the library prep kit.

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
    api_instance = ICA_SDK.LibraryPrepKitsApi(api_client)
    library_prep_kit_id = 'library_prep_kit_id_example' # str | ID of the library prep kit
force = True # bool | Force delete the library prep kit (optional)

    try:
        # Delete library prep kit.
        api_response = api_instance.delete_library_prep_kit(library_prep_kit_id, force=force)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->delete_library_prep_kit: %s\n" % e)
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
    api_instance = ICA_SDK.LibraryPrepKitsApi(api_client)
    library_prep_kit_id = 'library_prep_kit_id_example' # str | ID of the library prep kit
force = True # bool | Force delete the library prep kit (optional)

    try:
        # Delete library prep kit.
        api_response = api_instance.delete_library_prep_kit(library_prep_kit_id, force=force)
        pprint(api_response)
    except ApiException as e:
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
> LibraryPrepKit get_library_prep_kit(library_prep_kit_id, include=include)

Get library prep kit details.

For a given library prep kit ID, return information about that library prep kit.

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
    api_instance = ICA_SDK.LibraryPrepKitsApi(api_client)
    library_prep_kit_id = 'library_prep_kit_id_example' # str | ID of the library prep kit
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)

    try:
        # Get library prep kit details.
        api_response = api_instance.get_library_prep_kit(library_prep_kit_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->get_library_prep_kit: %s\n" % e)
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
    api_instance = ICA_SDK.LibraryPrepKitsApi(api_client)
    library_prep_kit_id = 'library_prep_kit_id_example' # str | ID of the library prep kit
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)

    try:
        # Get library prep kit details.
        api_response = api_instance.get_library_prep_kit(library_prep_kit_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->get_library_prep_kit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_prep_kit_id** | **str**| ID of the library prep kit | 
 **include** | [**list[str]**](str.md)| Include flags to specify what is included in the response | [optional] 

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
> LibraryPrepKitCompactLibraryPrepKitSortFieldsPagedItems list_library_prep_kits(include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)

Get a list of library prep kits.

Get a list of library prep kits accessible by the current request token.

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
    api_instance = ICA_SDK.LibraryPrepKitsApi(api_client)
    include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)
tenant_ids = ['tenant_ids_example'] # list[str] | Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to 'timeCreated asc')

    try:
        # Get a list of library prep kits.
        api_response = api_instance.list_library_prep_kits(include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->list_library_prep_kits: %s\n" % e)
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
    api_instance = ICA_SDK.LibraryPrepKitsApi(api_client)
    include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)
tenant_ids = ['tenant_ids_example'] # list[str] | Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to 'timeCreated asc')

    try:
        # Get a list of library prep kits.
        api_response = api_instance.list_library_prep_kits(include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->list_library_prep_kits: %s\n" % e)
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
> LibraryPrepKit merge_library_prep_kit_acl(library_prep_kit_id, body=body)

Merge the access control list of a library prep kit with the input access control list.

For a given library prep kit ID, merge the access control list with the input access control list, and return information about the library prep kit

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
    api_instance = ICA_SDK.LibraryPrepKitsApi(api_client)
    library_prep_kit_id = 'library_prep_kit_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Merge the access control list of a library prep kit with the input access control list.
        api_response = api_instance.merge_library_prep_kit_acl(library_prep_kit_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->merge_library_prep_kit_acl: %s\n" % e)
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
    api_instance = ICA_SDK.LibraryPrepKitsApi(api_client)
    library_prep_kit_id = 'library_prep_kit_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Merge the access control list of a library prep kit with the input access control list.
        api_response = api_instance.merge_library_prep_kit_acl(library_prep_kit_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
> LibraryPrepKit remove_library_prep_kit_acl(library_prep_kit_id, body=body)

Remove the access control list of a given library prep kit.

Remove the access control list of a given library prep kit, and return information about that library prep kit.

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
    api_instance = ICA_SDK.LibraryPrepKitsApi(api_client)
    library_prep_kit_id = 'library_prep_kit_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Remove the access control list of a given library prep kit.
        api_response = api_instance.remove_library_prep_kit_acl(library_prep_kit_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->remove_library_prep_kit_acl: %s\n" % e)
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
    api_instance = ICA_SDK.LibraryPrepKitsApi(api_client)
    library_prep_kit_id = 'library_prep_kit_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Remove the access control list of a given library prep kit.
        api_response = api_instance.remove_library_prep_kit_acl(library_prep_kit_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
> LibraryPrepKit replace_library_prep_kit_acl(library_prep_kit_id, body=body)

Replace the access control list of a library prep kit with the input access control list.

For a given library prep kit ID, replace the access control list with the input access control list, and return information about the library prep kit.

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
    api_instance = ICA_SDK.LibraryPrepKitsApi(api_client)
    library_prep_kit_id = 'library_prep_kit_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Replace the access control list of a library prep kit with the input access control list.
        api_response = api_instance.replace_library_prep_kit_acl(library_prep_kit_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->replace_library_prep_kit_acl: %s\n" % e)
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
    api_instance = ICA_SDK.LibraryPrepKitsApi(api_client)
    library_prep_kit_id = 'library_prep_kit_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Replace the access control list of a library prep kit with the input access control list.
        api_response = api_instance.replace_library_prep_kit_acl(library_prep_kit_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
> LibraryPrepKit update_library_prep_kit(library_prep_kit_id, body=body)

Update a library prep kit.

For a given library prep kit ID, update the associated library prep kit.

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
    api_instance = ICA_SDK.LibraryPrepKitsApi(api_client)
    library_prep_kit_id = 'library_prep_kit_id_example' # str | The id of the requested library prep kit.
body = ICA_SDK.UpdateLibraryPrepKitRequest() # UpdateLibraryPrepKitRequest | The update request for the library prep kit (optional)

    try:
        # Update a library prep kit.
        api_response = api_instance.update_library_prep_kit(library_prep_kit_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryPrepKitsApi->update_library_prep_kit: %s\n" % e)
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
    api_instance = ICA_SDK.LibraryPrepKitsApi(api_client)
    library_prep_kit_id = 'library_prep_kit_id_example' # str | The id of the requested library prep kit.
body = ICA_SDK.UpdateLibraryPrepKitRequest() # UpdateLibraryPrepKitRequest | The update request for the library prep kit (optional)

    try:
        # Update a library prep kit.
        api_response = api_instance.update_library_prep_kit(library_prep_kit_id, body=body)
        pprint(api_response)
    except ApiException as e:
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

