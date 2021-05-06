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
> TaskVersion create_task_version(task_id)

Create a task version

Creates a new task version within an existing task. Returns the ID associated with the new task version. Substitutions can be defined in the following format: \"{{string}}\", and specified at launch time.

### Example

* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import task_versions_api
from ICA_SDK.model.create_task_version_request import CreateTaskVersionRequest
from ICA_SDK.model.task_version import TaskVersion
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = task_versions_api.TaskVersionsApi(api_client)
    task_id = "taskId_example" # str | 
    body = CreateTaskVersionRequest(
        version="version_example",
        description="description_example",
        execution=Execution(
            image=Image(
                name="name_example",
                tag="tag_example",
                digest="digest_example",
                credentials=Credentials(
                    username="username_example",
                    password="password_example",
                ),
            ),
            command="command_example",
            args=[
                "args_example",
            ],
            inputs=[
                InputMountMappingWithCreds(
                    storage_provider="storage_provider_example",
                    credentials={
                        "key": "key_example",
                    },
                    path="path_example",
                    url="url_example",
                    urn="urn_example",
                    mode="mode_example",
                    type="File",
                ),
            ],
            outputs=[
                MountMappingWithCreds(
                    path="path_example",
                    url="url_example",
                    urn="urn_example",
                    type="type_example",
                    storage_provider="storage_provider_example",
                    credentials={
                        "key": "key_example",
                    },
                ),
            ],
            system_files=SystemFiles(
                url="url_example",
                urn="urn_example",
                storage_provider="storage_provider_example",
                credentials={
                    "key": "key_example",
                },
            ),
            environment=Environment(
                variables={
                    "key": "key_example",
                },
                resources=Resources(
                    type="type_example",
                    size="size_example",
                    cpu_cores=3.14,
                    memory_gb=3.14,
                    hardware=[
                        "hardware_example",
                    ],
                    tier="tier_example",
                ),
                input_stream_settings=InputStreamSettings(
                    access_pattern="sequential",
                    cache_size_gb=50,
                    block_size_mb=32.0,
                    prefetch_blocks=32,
                ),
            ),
            working_directory="working_directory_example",
            retry_limit=3,
            retry_count=0,
        ),
        acl=[
            "acl_example",
        ],
    ) # CreateTaskVersionRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a task version
        api_response = api_instance.create_task_version(task_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling TaskVersionsApi->create_task_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a task version
        api_response = api_instance.create_task_version(task_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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

[Bearer](../README.md#Bearer)

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

* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import task_versions_api
from ICA_SDK.model.task_version import TaskVersion
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = task_versions_api.TaskVersionsApi(api_client)
    task_id = "taskId_example" # str | 
    version_id = "versionId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the details of a task version
        api_response = api_instance.get_task_version(task_id, version_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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

[Bearer](../README.md#Bearer)

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
> TaskRun launch_task_run(task_id, version_id)

Launch a task version

Launches a task version for a given task version ID. Returns the ID associated with the new task run. Substitutions defined in the task version must be specified.

### Example

* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import task_versions_api
from ICA_SDK.model.task_run import TaskRun
from ICA_SDK.model.launch_task_request import LaunchTaskRequest
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = task_versions_api.TaskVersionsApi(api_client)
    task_id = "taskId_example" # str | 
    version_id = "versionId_example" # str | 
    body = LaunchTaskRequest(
        name="name_example",
        description="description_example",
        arguments={
            "key": "key_example",
        },
        acl=[
            "acl_example",
        ],
    ) # LaunchTaskRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Launch a task version
        api_response = api_instance.launch_task_run(task_id, version_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling TaskVersionsApi->launch_task_run: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Launch a task version
        api_response = api_instance.launch_task_run(task_id, version_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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

[Bearer](../README.md#Bearer)

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
> TaskVersionSummaryPagedItems list_task_versions(task_id)

Get a list of versions

Gets a list of task versions within the given task accessible by the current tenant ID.

### Example

* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import task_versions_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.task_version_summary_paged_items import TaskVersionSummaryPagedItems
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = task_versions_api.TaskVersionsApi(api_client)
    task_id = "taskId_example" # str | 
    sort = "sort_example" # str | Sort: Optional parameter to set the sort of the returned list. Valid fields include: name, version, timeCreated, timeModified.  The sort can be specified as asc or desc. (Default: asc.) (optional)
    versions = "versions_example" # str |  (optional)
    ids = "ids_example" # str |  (optional)
    acls = "acls_example" # str |  (optional)
    page_size = 10 # int | Optional parameter to define the page size returned. Valid inputs range from 1-1000. (optional) if omitted the server will use the default value of 10
    page_token = "pageToken_example" # str | pageToken: Optional parameter for navigation after initial listing. Valid values include firstPageToken,  nextPageToken, and previousPageToken (provided in the list response) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a list of versions
        api_response = api_instance.list_task_versions(task_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling TaskVersionsApi->list_task_versions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of versions
        api_response = api_instance.list_task_versions(task_id, sort=sort, versions=versions, ids=ids, acls=acls, page_size=page_size, page_token=page_token)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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
 **page_size** | **int**| Optional parameter to define the page size returned. Valid inputs range from 1-1000. | [optional] if omitted the server will use the default value of 10
 **page_token** | **str**| pageToken: Optional parameter for navigation after initial listing. Valid values include firstPageToken,  nextPageToken, and previousPageToken (provided in the list response) | [optional]

### Return type

[**TaskVersionSummaryPagedItems**](TaskVersionSummaryPagedItems.md)

### Authorization

[Bearer](../README.md#Bearer)

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
> TaskVersion update_task_version(task_id, version_id)

Update task version properties

Update details of a task version for a given task version ID.

### Example

* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import task_versions_api
from ICA_SDK.model.update_task_version_request import UpdateTaskVersionRequest
from ICA_SDK.model.task_version import TaskVersion
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = task_versions_api.TaskVersionsApi(api_client)
    task_id = "taskId_example" # str | 
    version_id = "versionId_example" # str | 
    body = UpdateTaskVersionRequest(
        version="version_example",
        description="description_example",
        execution=Execution(
            image=Image(
                name="name_example",
                tag="tag_example",
                digest="digest_example",
                credentials=Credentials(
                    username="username_example",
                    password="password_example",
                ),
            ),
            command="command_example",
            args=[
                "args_example",
            ],
            inputs=[
                InputMountMappingWithCreds(
                    storage_provider="storage_provider_example",
                    credentials={
                        "key": "key_example",
                    },
                    path="path_example",
                    url="url_example",
                    urn="urn_example",
                    mode="mode_example",
                    type="File",
                ),
            ],
            outputs=[
                MountMappingWithCreds(
                    path="path_example",
                    url="url_example",
                    urn="urn_example",
                    type="type_example",
                    storage_provider="storage_provider_example",
                    credentials={
                        "key": "key_example",
                    },
                ),
            ],
            system_files=SystemFiles(
                url="url_example",
                urn="urn_example",
                storage_provider="storage_provider_example",
                credentials={
                    "key": "key_example",
                },
            ),
            environment=Environment(
                variables={
                    "key": "key_example",
                },
                resources=Resources(
                    type="type_example",
                    size="size_example",
                    cpu_cores=3.14,
                    memory_gb=3.14,
                    hardware=[
                        "hardware_example",
                    ],
                    tier="tier_example",
                ),
                input_stream_settings=InputStreamSettings(
                    access_pattern="sequential",
                    cache_size_gb=50,
                    block_size_mb=32.0,
                    prefetch_blocks=32,
                ),
            ),
            working_directory="working_directory_example",
            retry_limit=3,
            retry_count=0,
        ),
        acl=[
            "acl_example",
        ],
    ) # UpdateTaskVersionRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update task version properties
        api_response = api_instance.update_task_version(task_id, version_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling TaskVersionsApi->update_task_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update task version properties
        api_response = api_instance.update_task_version(task_id, version_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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

[Bearer](../README.md#Bearer)

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

