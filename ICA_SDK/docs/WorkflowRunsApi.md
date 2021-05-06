# ICA_SDK.WorkflowRunsApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_workflow_run**](WorkflowRunsApi.md#abort_workflow_run) | **PUT** /v1/workflows/runs/{runId}:abort | Abort a workflow run
[**get_workflow_run**](WorkflowRunsApi.md#get_workflow_run) | **GET** /v1/workflows/runs/{runId} | Get the details of a workflow run
[**list_workflow_run_history**](WorkflowRunsApi.md#list_workflow_run_history) | **GET** /v1/workflows/runs/{runId}/history | Get a list of workflow run history events
[**list_workflow_runs**](WorkflowRunsApi.md#list_workflow_runs) | **GET** /v1/workflows/runs | Get a list of workflow runs


# **abort_workflow_run**
> WorkflowRun abort_workflow_run(run_id)

Abort a workflow run

Aborts the workflow run with a given ID.

### Example

* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import workflow_runs_api
from ICA_SDK.model.workflow_run import WorkflowRun
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.abort_workflow_run_request import AbortWorkflowRunRequest
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
    api_instance = workflow_runs_api.WorkflowRunsApi(api_client)
    run_id = "runId_example" # str | ID of the workflow run
    include = [
        "definition",
    ] # [str] | Comma-separated list of properties to include in the response (optional)
    body = AbortWorkflowRunRequest(
        error="error_example",
        cause="cause_example",
    ) # AbortWorkflowRunRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Abort a workflow run
        api_response = api_instance.abort_workflow_run(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling WorkflowRunsApi->abort_workflow_run: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Abort a workflow run
        api_response = api_instance.abort_workflow_run(run_id, include=include, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling WorkflowRunsApi->abort_workflow_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| ID of the workflow run |
 **include** | **[str]**| Comma-separated list of properties to include in the response | [optional]
 **body** | [**AbortWorkflowRunRequest**](AbortWorkflowRunRequest.md)|  | [optional]

### Return type

[**WorkflowRun**](WorkflowRun.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of the aborted workflow run. |  -  |
**400** | Invalid request. |  -  |
**401** | Unauthorized |  -  |
**403** | Permission denied. |  -  |
**404** | The workflow run with the specified ID was not found. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_run**
> WorkflowRun get_workflow_run(run_id)

Get the details of a workflow run

Gets the details of a workflow run with a given ID.

### Example

* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import workflow_runs_api
from ICA_SDK.model.workflow_run import WorkflowRun
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
    api_instance = workflow_runs_api.WorkflowRunsApi(api_client)
    run_id = "runId_example" # str | ID of the workflow run
    include = [
        "definition",
    ] # [str] | Comma-separated list of properties to include in the response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the details of a workflow run
        api_response = api_instance.get_workflow_run(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling WorkflowRunsApi->get_workflow_run: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the details of a workflow run
        api_response = api_instance.get_workflow_run(run_id, include=include)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling WorkflowRunsApi->get_workflow_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| ID of the workflow run |
 **include** | **[str]**| Comma-separated list of properties to include in the response | [optional]

### Return type

[**WorkflowRun**](WorkflowRun.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of the workflow run. |  -  |
**400** | Invalid request. |  -  |
**401** | Unauthorized |  -  |
**403** | Permission denied. |  -  |
**404** | The workflow run with the specified ID was not found. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflow_run_history**
> WorkflowRunHistoryEventList list_workflow_run_history(run_id)

Get a list of workflow run history events

Gets a list of history events for a workflow run with a given ID.

### Example

* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import workflow_runs_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.workflow_run_history_event_list import WorkflowRunHistoryEventList
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
    api_instance = workflow_runs_api.WorkflowRunsApi(api_client)
    run_id = "runId_example" # str | ID of the workflow run
    sort = "eventId asc" # str |  (optional) if omitted the server will use the default value of "eventId asc"
    include = [
        "totalItemCount",
    ] # [str] | Comma-separated list of properties to include in the response (optional)
    page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) if omitted the server will use the default value of 10
    page_token = "pageToken_example" # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a list of workflow run history events
        api_response = api_instance.list_workflow_run_history(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling WorkflowRunsApi->list_workflow_run_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of workflow run history events
        api_response = api_instance.list_workflow_run_history(run_id, sort=sort, include=include, page_size=page_size, page_token=page_token)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling WorkflowRunsApi->list_workflow_run_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| ID of the workflow run |
 **sort** | **str**|  | [optional] if omitted the server will use the default value of "eventId asc"
 **include** | **[str]**| Comma-separated list of properties to include in the response | [optional]
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] if omitted the server will use the default value of 10
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional]

### Return type

[**WorkflowRunHistoryEventList**](WorkflowRunHistoryEventList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paged list of workflow run history events. |  -  |
**400** | Invalid request. |  -  |
**401** | Unauthorized |  -  |
**403** | Permission denied. |  -  |
**404** | The workflow run with the specified ID was not found. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflow_runs**
> WorkflowRunList list_workflow_runs()

Get a list of workflow runs

Gets a list of workflow runs.

### Example

* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import workflow_runs_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.workflow_run_list import WorkflowRunList
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
    api_instance = workflow_runs_api.WorkflowRunsApi(api_client)
    status = [
        "aborted",
    ] # [str] |  (optional)
    tenant_id = "tenantId_example" # str | ID of the tenant (optional)
    name = "name_example" # str |  (optional)
    include = [
        "totalItemCount",
    ] # [str] | Comma-separated list of properties to include in the response (optional)
    page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) if omitted the server will use the default value of 10
    page_token = "pageToken_example" # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
    sort = "timeCreated asc" # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) if omitted the server will use the default value of "timeCreated asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of workflow runs
        api_response = api_instance.list_workflow_runs(status=status, tenant_id=tenant_id, name=name, include=include, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling WorkflowRunsApi->list_workflow_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **[str]**|  | [optional]
 **tenant_id** | **str**| ID of the tenant | [optional]
 **name** | **str**|  | [optional]
 **include** | **[str]**| Comma-separated list of properties to include in the response | [optional]
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] if omitted the server will use the default value of 10
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional]
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] if omitted the server will use the default value of "timeCreated asc"

### Return type

[**WorkflowRunList**](WorkflowRunList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paged list of workflow runs that the user has access to. |  -  |
**400** | Invalid request. |  -  |
**401** | Unauthorized |  -  |
**403** | Permission denied. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

