# swagger_client.WorkflowRunsApi

All URIs are relative to *https://aps1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_workflow_run**](WorkflowRunsApi.md#abort_workflow_run) | **PUT** /v1/workflows/runs/{runId}:abort | Abort a workflow run
[**get_workflow_run**](WorkflowRunsApi.md#get_workflow_run) | **GET** /v1/workflows/runs/{runId} | Get the details of a workflow run
[**list_workflow_run_history**](WorkflowRunsApi.md#list_workflow_run_history) | **GET** /v1/workflows/runs/{runId}/history | Get a list of workflow run history events
[**list_workflow_runs**](WorkflowRunsApi.md#list_workflow_runs) | **GET** /v1/workflows/runs | Get a list of workflow runs


# **abort_workflow_run**
> WorkflowRun abort_workflow_run(run_id, include=include, body=body)

Abort a workflow run

Aborts the workflow run with a given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WorkflowRunsApi(swagger_client.ApiClient(configuration))
run_id = 'run_id_example' # str | ID of the workflow run
include = ['include_example'] # list[str] | Comma-separated list of properties to include in the response (optional)
body = swagger_client.AbortWorkflowRunRequest() # AbortWorkflowRunRequest |  (optional)

try:
    # Abort a workflow run
    api_response = api_instance.abort_workflow_run(run_id, include=include, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowRunsApi->abort_workflow_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| ID of the workflow run | 
 **include** | [**list[str]**](str.md)| Comma-separated list of properties to include in the response | [optional] 
 **body** | [**AbortWorkflowRunRequest**](AbortWorkflowRunRequest.md)|  | [optional] 

### Return type

[**WorkflowRun**](WorkflowRun.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_run**
> WorkflowRun get_workflow_run(run_id, include=include)

Get the details of a workflow run

Gets the details of a workflow run with a given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WorkflowRunsApi(swagger_client.ApiClient(configuration))
run_id = 'run_id_example' # str | ID of the workflow run
include = ['include_example'] # list[str] | Comma-separated list of properties to include in the response (optional)

try:
    # Get the details of a workflow run
    api_response = api_instance.get_workflow_run(run_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowRunsApi->get_workflow_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| ID of the workflow run | 
 **include** | [**list[str]**](str.md)| Comma-separated list of properties to include in the response | [optional] 

### Return type

[**WorkflowRun**](WorkflowRun.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflow_run_history**
> WorkflowRunHistoryEventList list_workflow_run_history(run_id, sort=sort, include=include, page_size=page_size, page_token=page_token)

Get a list of workflow run history events

Gets a list of history events for a workflow run with a given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WorkflowRunsApi(swagger_client.ApiClient(configuration))
run_id = 'run_id_example' # str | ID of the workflow run
sort = 'eventId asc' # str |  (optional) (default to eventId asc)
include = ['include_example'] # list[str] | Comma-separated list of properties to include in the response (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)

try:
    # Get a list of workflow run history events
    api_response = api_instance.list_workflow_run_history(run_id, sort=sort, include=include, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowRunsApi->list_workflow_run_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| ID of the workflow run | 
 **sort** | **str**|  | [optional] [default to eventId asc]
 **include** | [**list[str]**](str.md)| Comma-separated list of properties to include in the response | [optional] 
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] [default to 10]
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional] 

### Return type

[**WorkflowRunHistoryEventList**](WorkflowRunHistoryEventList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflow_runs**
> WorkflowRunList list_workflow_runs(status=status, tenant_id=tenant_id, name=name, include=include, page_size=page_size, page_token=page_token, sort=sort)

Get a list of workflow runs

Gets a list of workflow runs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WorkflowRunsApi(swagger_client.ApiClient(configuration))
status = ['status_example'] # list[str] |  (optional)
tenant_id = 'tenant_id_example' # str | ID of the tenant (optional)
name = 'name_example' # str |  (optional)
include = ['include_example'] # list[str] | Comma-separated list of properties to include in the response (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to timeCreated asc)

try:
    # Get a list of workflow runs
    api_response = api_instance.list_workflow_runs(status=status, tenant_id=tenant_id, name=name, include=include, page_size=page_size, page_token=page_token, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowRunsApi->list_workflow_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**list[str]**](str.md)|  | [optional] 
 **tenant_id** | **str**| ID of the tenant | [optional] 
 **name** | **str**|  | [optional] 
 **include** | [**list[str]**](str.md)| Comma-separated list of properties to include in the response | [optional] 
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] [default to 10]
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional] 
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] [default to timeCreated asc]

### Return type

[**WorkflowRunList**](WorkflowRunList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
