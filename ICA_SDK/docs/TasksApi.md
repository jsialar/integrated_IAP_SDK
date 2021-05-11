# ICA_SDK.TasksApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task**](TasksApi.md#create_task) | **POST** /v1/tasks | Create a Task
[**get_task**](TasksApi.md#get_task) | **GET** /v1/tasks/{taskId} | Get the details of a Task
[**list_tasks**](TasksApi.md#list_tasks) | **GET** /v1/tasks | Get a list of tasks
[**update_task**](TasksApi.md#update_task) | **PATCH** /v1/tasks/{taskId} | Update an existing task.


# **create_task**
> Task create_task()

Create a Task

Creates a task. Returns the ID associated with the new task. Also returns the task version ID associated with the new task, if provided. Substitutions can be defined in the following format: \"{{string}}\", and specified at launch time.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import tasks_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.task import Task
from ICA_SDK.model.create_task_request import CreateTaskRequest
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
    api_instance = tasks_api.TasksApi(api_client)
    body = CreateTaskRequest(
        name="name_example",
        description="description_example",
        acl=[
            "acl_example",
        ],
        task_versions=[
            CreateTaskVersionRequest(
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
            ),
        ],
    ) # CreateTaskRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Task
        api_response = api_instance.create_task(body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling TasksApi->create_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTaskRequest**](CreateTaskRequest.md)|  | [optional]

### Return type

[**Task**](Task.md)

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

# **get_task**
> TaskSummary get_task(task_id)

Get the details of a Task

Gets the details of a Task for a given task ID.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import tasks_api
from ICA_SDK.model.task_summary import TaskSummary
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
    api_instance = tasks_api.TasksApi(api_client)
    task_id = "taskId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the details of a Task
        api_response = api_instance.get_task(task_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling TasksApi->get_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  |

### Return type

[**TaskSummary**](TaskSummary.md)

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

# **list_tasks**
> TaskSummaryPagedItems list_tasks()

Get a list of tasks

Gets a list of tasks accessible by the current tenant ID.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import tasks_api
from ICA_SDK.model.task_summary_paged_items import TaskSummaryPagedItems
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
    api_instance = tasks_api.TasksApi(api_client)
    names = "names_example" # str | Name: Optional parameter to filter the returned list. Case-Sensitive (optional)
    acls = "acls_example" # str | Name: Optional parameter to filter the returned list. Case-Sensitive (optional)
    page_size = 10 # int | Optional parameter to define the page size returned. Valid inputs range from 1-1000. (optional) if omitted the server will use the default value of 10
    sort = "timeCreated asc" # str | Sort: Optional parameter to set the sort of the returned list. Valid fields include: name, timeCreated, timeModified.  The sort can be specified as asc or desc. (Default: asc.) (optional) if omitted the server will use the default value of "timeCreated asc"
    page_token = "pageToken_example" # str | pageToken: Optional parameter for navigation after initial listing. Valid values include firstPageToken,  nextPageToken, and previousPageToken (provided in the list response) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of tasks
        api_response = api_instance.list_tasks(names=names, acls=acls, page_size=page_size, sort=sort, page_token=page_token)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling TasksApi->list_tasks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | **str**| Name: Optional parameter to filter the returned list. Case-Sensitive | [optional]
 **acls** | **str**| Name: Optional parameter to filter the returned list. Case-Sensitive | [optional]
 **page_size** | **int**| Optional parameter to define the page size returned. Valid inputs range from 1-1000. | [optional] if omitted the server will use the default value of 10
 **sort** | **str**| Sort: Optional parameter to set the sort of the returned list. Valid fields include: name, timeCreated, timeModified.  The sort can be specified as asc or desc. (Default: asc.) | [optional] if omitted the server will use the default value of "timeCreated asc"
 **page_token** | **str**| pageToken: Optional parameter for navigation after initial listing. Valid values include firstPageToken,  nextPageToken, and previousPageToken (provided in the list response) | [optional]

### Return type

[**TaskSummaryPagedItems**](TaskSummaryPagedItems.md)

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

# **update_task**
> Task update_task(task_id)

Update an existing task.

Updates the task with a given ID. The task's name, description can be updated. The task's name must remain unique.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import tasks_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.task import Task
from ICA_SDK.model.update_task_request import UpdateTaskRequest
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
    api_instance = tasks_api.TasksApi(api_client)
    task_id = "taskId_example" # str | 
    body = UpdateTaskRequest(
        name="name_example",
        description="description_example",
        acl=[
            "acl_example",
        ],
    ) # UpdateTaskRequest | Details of the task to be updated. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an existing task.
        api_response = api_instance.update_task(task_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling TasksApi->update_task: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an existing task.
        api_response = api_instance.update_task(task_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling TasksApi->update_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  |
 **body** | [**UpdateTaskRequest**](UpdateTaskRequest.md)| Details of the task to be updated. | [optional]

### Return type

[**Task**](Task.md)

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
**409** | Conflict |  -  |
**500** | Server Error |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

