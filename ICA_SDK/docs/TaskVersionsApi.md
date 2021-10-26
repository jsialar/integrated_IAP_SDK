# ICA_SDK.TaskVersionsApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task_version**](TaskVersionsApi.md#create_task_version) | **POST** /v1/tasks/{taskId}/versions | Create a task version
[**get_task_version**](TaskVersionsApi.md#get_task_version) | **GET** /v1/tasks/{taskId}/versions/{versionId} | Get the details of a task version
[**launch_task_run**](TaskVersionsApi.md#launch_task_run) | **POST** /v1/tasks/{taskId}/versions/{versionId}:launch | Launch a task version
[**list_task_versions**](TaskVersionsApi.md#list_task_versions) | **GET** /v1/tasks/{taskId}/versions | Get a list of versions
[**update_task_version**](TaskVersionsApi.md#update_task_version) | **PATCH** /v1/tasks/{taskId}/versions/{versionId} | Update task version properties


# **create_task_version**
> TaskVersion create_task_version(task_id, body=body)

Create a task version

Creates a new task version within an existing task. Returns the ID associated with the new task version. Substitutions can be defined in the following format: \"{{string}}\", and specified at launch time.

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
    api_instance = ICA_SDK.TaskVersionsApi(api_client)
    task_id = 'task_id_example' # str | 
body = ICA_SDK.CreateTaskVersionRequest() # CreateTaskVersionRequest |  (optional)

    try:
        # Create a task version
        api_response = api_instance.create_task_version(task_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskVersionsApi->create_task_version: %s\n" % e)
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
    api_instance = ICA_SDK.TaskVersionsApi(api_client)
    task_id = 'task_id_example' # str | 
body = ICA_SDK.CreateTaskVersionRequest() # CreateTaskVersionRequest |  (optional)

    try:
        # Create a task version
        api_response = api_instance.create_task_version(task_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskVersionsApi->create_task_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **body** | [**CreateTaskVersionRequest**](CreateTaskVersionRequest.md)|  | [optional] 

### Return type

[**TaskVersion**](TaskVersion.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Server Error |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_version**
> TaskVersion get_task_version(task_id, version_id)

Get the details of a task version

Gets details of a task version for a given task version ID.

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
    api_instance = ICA_SDK.TaskVersionsApi(api_client)
    task_id = 'task_id_example' # str | 
version_id = 'version_id_example' # str | 

    try:
        # Get the details of a task version
        api_response = api_instance.get_task_version(task_id, version_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskVersionsApi->get_task_version: %s\n" % e)
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
    api_instance = ICA_SDK.TaskVersionsApi(api_client)
    task_id = 'task_id_example' # str | 
version_id = 'version_id_example' # str | 

    try:
        # Get the details of a task version
        api_response = api_instance.get_task_version(task_id, version_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskVersionsApi->get_task_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **version_id** | **str**|  | 

### Return type

[**TaskVersion**](TaskVersion.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launch_task_run**
> TaskRun launch_task_run(task_id, version_id, body=body)

Launch a task version

Launches a task version for a given task version ID. Returns the ID associated with the new task run. Substitutions defined in the task version must be specified.

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
    api_instance = ICA_SDK.TaskVersionsApi(api_client)
    task_id = 'task_id_example' # str | 
version_id = 'version_id_example' # str | 
body = ICA_SDK.LaunchTaskRequest() # LaunchTaskRequest |  (optional)

    try:
        # Launch a task version
        api_response = api_instance.launch_task_run(task_id, version_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskVersionsApi->launch_task_run: %s\n" % e)
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
    api_instance = ICA_SDK.TaskVersionsApi(api_client)
    task_id = 'task_id_example' # str | 
version_id = 'version_id_example' # str | 
body = ICA_SDK.LaunchTaskRequest() # LaunchTaskRequest |  (optional)

    try:
        # Launch a task version
        api_response = api_instance.launch_task_run(task_id, version_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskVersionsApi->launch_task_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **version_id** | **str**|  | 
 **body** | [**LaunchTaskRequest**](LaunchTaskRequest.md)|  | [optional] 

### Return type

[**TaskRun**](TaskRun.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_task_versions**
> TaskVersionSummaryPagedItems list_task_versions(task_id, sort=sort, versions=versions, ids=ids, acls=acls, page_size=page_size, page_token=page_token)

Get a list of versions

Gets a list of task versions within the given task accessible by the current tenant ID.

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
    api_instance = ICA_SDK.TaskVersionsApi(api_client)
    task_id = 'task_id_example' # str | 
sort = 'sort_example' # str | Sort: Optional parameter to set the sort of the returned list. Valid fields include: name, version, timeCreated, timeModified.  The sort can be specified as asc or desc. (Default: asc.) (optional)
versions = 'versions_example' # str |  (optional)
ids = 'ids_example' # str |  (optional)
acls = 'acls_example' # str |  (optional)
page_size = 10 # int | Optional parameter to define the page size returned. Valid inputs range from 1-1000. (optional) (default to 10)
page_token = 'page_token_example' # str | pageToken: Optional parameter for navigation after initial listing. Valid values include firstPageToken,  nextPageToken, and previousPageToken (provided in the list response) (optional)

    try:
        # Get a list of versions
        api_response = api_instance.list_task_versions(task_id, sort=sort, versions=versions, ids=ids, acls=acls, page_size=page_size, page_token=page_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskVersionsApi->list_task_versions: %s\n" % e)
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
    api_instance = ICA_SDK.TaskVersionsApi(api_client)
    task_id = 'task_id_example' # str | 
sort = 'sort_example' # str | Sort: Optional parameter to set the sort of the returned list. Valid fields include: name, version, timeCreated, timeModified.  The sort can be specified as asc or desc. (Default: asc.) (optional)
versions = 'versions_example' # str |  (optional)
ids = 'ids_example' # str |  (optional)
acls = 'acls_example' # str |  (optional)
page_size = 10 # int | Optional parameter to define the page size returned. Valid inputs range from 1-1000. (optional) (default to 10)
page_token = 'page_token_example' # str | pageToken: Optional parameter for navigation after initial listing. Valid values include firstPageToken,  nextPageToken, and previousPageToken (provided in the list response) (optional)

    try:
        # Get a list of versions
        api_response = api_instance.list_task_versions(task_id, sort=sort, versions=versions, ids=ids, acls=acls, page_size=page_size, page_token=page_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskVersionsApi->list_task_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **sort** | **str**| Sort: Optional parameter to set the sort of the returned list. Valid fields include: name, version, timeCreated, timeModified.  The sort can be specified as asc or desc. (Default: asc.) | [optional] 
 **versions** | **str**|  | [optional] 
 **ids** | **str**|  | [optional] 
 **acls** | **str**|  | [optional] 
 **page_size** | **int**| Optional parameter to define the page size returned. Valid inputs range from 1-1000. | [optional] [default to 10]
 **page_token** | **str**| pageToken: Optional parameter for navigation after initial listing. Valid values include firstPageToken,  nextPageToken, and previousPageToken (provided in the list response) | [optional] 

### Return type

[**TaskVersionSummaryPagedItems**](TaskVersionSummaryPagedItems.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task_version**
> TaskVersion update_task_version(task_id, version_id, body=body)

Update task version properties

Update details of a task version for a given task version ID.

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
    api_instance = ICA_SDK.TaskVersionsApi(api_client)
    task_id = 'task_id_example' # str | 
version_id = 'version_id_example' # str | 
body = ICA_SDK.UpdateTaskVersionRequest() # UpdateTaskVersionRequest |  (optional)

    try:
        # Update task version properties
        api_response = api_instance.update_task_version(task_id, version_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskVersionsApi->update_task_version: %s\n" % e)
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
    api_instance = ICA_SDK.TaskVersionsApi(api_client)
    task_id = 'task_id_example' # str | 
version_id = 'version_id_example' # str | 
body = ICA_SDK.UpdateTaskVersionRequest() # UpdateTaskVersionRequest |  (optional)

    try:
        # Update task version properties
        api_response = api_instance.update_task_version(task_id, version_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskVersionsApi->update_task_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **version_id** | **str**|  | 
 **body** | [**UpdateTaskVersionRequest**](UpdateTaskVersionRequest.md)|  | [optional] 

### Return type

[**TaskVersion**](TaskVersion.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

