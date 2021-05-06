# ICA_SDK.TaskRunsApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_task_run**](TaskRunsApi.md#abort_task_run) | **PUT** /v1/tasks/runs/{runId}:abort | Abort a task run
[**create_task_run**](TaskRunsApi.md#create_task_run) | **POST** /v1/tasks/runs | Create and launch a task run
[**get_task_run**](TaskRunsApi.md#get_task_run) | **GET** /v1/tasks/runs/{runId} | Get the status of a task run
[**heartbeat_task_run**](TaskRunsApi.md#heartbeat_task_run) | **POST** /v1/tasks/runs/{runId}:heartbeat | Heartbeat for a task run
[**list_task_runs**](TaskRunsApi.md#list_task_runs) | **GET** /v1/tasks/runs | Get a list of task runs


# **abort_task_run**
> TaskRunSummary abort_task_run(run_id)

Abort a task run

Aborts a task run for a given task run ID. The task run is required to have a status of \"Pending\" or \"Running\".

### Example

* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import task_runs_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.task_run_summary import TaskRunSummary
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
    api_instance = task_runs_api.TaskRunsApi(api_client)
    run_id = "runId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Abort a task run
        api_response = api_instance.abort_task_run(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling TaskRunsApi->abort_task_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |

### Return type

[**TaskRunSummary**](TaskRunSummary.md)

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

# **create_task_run**
> TaskRun create_task_run()

Create and launch a task run

Creates and launches a task run. Returns the ID and status associated with the new task run.

### Example

* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import task_runs_api
from ICA_SDK.model.task_run import TaskRun
from ICA_SDK.model.create_task_run_request import CreateTaskRunRequest
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
    api_instance = task_runs_api.TaskRunsApi(api_client)
    body = CreateTaskRunRequest(
        name="name_example",
        description="description_example",
        acl=[
            "acl_example",
        ],
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
    ) # CreateTaskRunRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create and launch a task run
        api_response = api_instance.create_task_run(body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling TaskRunsApi->create_task_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTaskRunRequest**](CreateTaskRunRequest.md)|  | [optional]

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
**500** | Server Error |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_run**
> TaskRun get_task_run(run_id)

Get the status of a task run

Gets the status of a task run for a given task run ID.

### Example

* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import task_runs_api
from ICA_SDK.model.task_run import TaskRun
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
    api_instance = task_runs_api.TaskRunsApi(api_client)
    run_id = "runId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the status of a task run
        api_response = api_instance.get_task_run(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling TaskRunsApi->get_task_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |

### Return type

[**TaskRun**](TaskRun.md)

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

# **heartbeat_task_run**
> TaskRunHeartbeat heartbeat_task_run(run_id)

Heartbeat for a task run

Heartbeat a task run for a given task run ID. This notifies TES that a task run is executing.

### Example

* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import task_runs_api
from ICA_SDK.model.task_run_heartbeat import TaskRunHeartbeat
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.heartbeat_task_run_request import HeartbeatTaskRunRequest
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
    api_instance = task_runs_api.TaskRunsApi(api_client)
    run_id = "runId_example" # str | 
    body = HeartbeatTaskRunRequest(
        last_heartbeat=True,
        pod_name="pod_name_example",
        pod_uid="pod_uid_example",
        pod_hardware_details="pod_hardware_details_example",
        job_retry_count=1,
        nonce="nonce_example",
        container_status=[
            ContainerStatus(
                name="name_example",
                state=ContainerState(
                    waiting=ContainerStateWaiting(
                        reason="reason_example",
                        message="message_example",
                    ),
                    running=ContainerStateRunning(
                        started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    ),
                    terminated=ContainerStateTerminated(
                        exit_code=1,
                        signal=1,
                        reason="reason_example",
                        message="message_example",
                        started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        finished_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        container_id="container_id_example",
                    ),
                ),
            ),
        ],
    ) # HeartbeatTaskRunRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Heartbeat for a task run
        api_response = api_instance.heartbeat_task_run(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling TaskRunsApi->heartbeat_task_run: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Heartbeat for a task run
        api_response = api_instance.heartbeat_task_run(run_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling TaskRunsApi->heartbeat_task_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |
 **body** | [**HeartbeatTaskRunRequest**](HeartbeatTaskRunRequest.md)|  | [optional]

### Return type

[**TaskRunHeartbeat**](TaskRunHeartbeat.md)

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

# **list_task_runs**
> TaskRunSummaryPagedItems list_task_runs()

Get a list of task runs

Get a list of task runs accessible by the current tenant ID.

### Example

* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import task_runs_api
from ICA_SDK.model.task_run_summary_paged_items import TaskRunSummaryPagedItems
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
    api_instance = task_runs_api.TaskRunsApi(api_client)
    sort = "sort_example" # str | Sort: Optional parameter to set the sort of the returned list. Valid fields include: name, status, timeCreated, timeModified.  The sort can be specified as asc or desc. (Default: asc.) (optional)
    names = "names_example" # str |  (optional)
    status = "status_example" # str |  (optional)
    versions = "versions_example" # str |  (optional)
    acls = "acls_example" # str |  (optional)
    page_size = 10 # int | Optional parameter to define the page size returned. Valid inputs range from 1-1000. (optional) if omitted the server will use the default value of 10
    page_token = "pageToken_example" # str | pageToken: Optional parameter for navigation after initial listing. Valid values include firstPageToken,  nextPageToken, and previousPageToken (provided in the list response) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of task runs
        api_response = api_instance.list_task_runs(sort=sort, names=names, status=status, versions=versions, acls=acls, page_size=page_size, page_token=page_token)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling TaskRunsApi->list_task_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| Sort: Optional parameter to set the sort of the returned list. Valid fields include: name, status, timeCreated, timeModified.  The sort can be specified as asc or desc. (Default: asc.) | [optional]
 **names** | **str**|  | [optional]
 **status** | **str**|  | [optional]
 **versions** | **str**|  | [optional]
 **acls** | **str**|  | [optional]
 **page_size** | **int**| Optional parameter to define the page size returned. Valid inputs range from 1-1000. | [optional] if omitted the server will use the default value of 10
 **page_token** | **str**| pageToken: Optional parameter for navigation after initial listing. Valid values include firstPageToken,  nextPageToken, and previousPageToken (provided in the list response) | [optional]

### Return type

[**TaskRunSummaryPagedItems**](TaskRunSummaryPagedItems.md)

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
**500** | Server Error |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

