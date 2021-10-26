# ICA_SDK.WorkflowsApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workflow**](WorkflowsApi.md#create_workflow) | **POST** /v1/workflows | Create a workflow
[**get_workflow**](WorkflowsApi.md#get_workflow) | **GET** /v1/workflows/{workflowId} | Get the details of a workflow
[**list_workflows**](WorkflowsApi.md#list_workflows) | **GET** /v1/workflows | Get a list of workflows
[**update_workflow**](WorkflowsApi.md#update_workflow) | **PATCH** /v1/workflows/{workflowId} | Update an existing workflow


# **create_workflow**
> Workflow create_workflow(body=body)

Create a workflow

Creates a new workflow and version (if provided).

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
    api_instance = ICA_SDK.WorkflowsApi(api_client)
    body = ICA_SDK.CreateWorkflowRequest() # CreateWorkflowRequest |  (optional)

    try:
        # Create a workflow
        api_response = api_instance.create_workflow(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow: %s\n" % e)
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
    api_instance = ICA_SDK.WorkflowsApi(api_client)
    body = ICA_SDK.CreateWorkflowRequest() # CreateWorkflowRequest |  (optional)

    try:
        # Create a workflow
        api_response = api_instance.create_workflow(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWorkflowRequest**](CreateWorkflowRequest.md)|  | [optional] 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Details of the newly created workflow. |  -  |
**400** | Invalid request. |  -  |
**401** | Unauthorized |  -  |
**403** | Permission denied. |  -  |
**409** | A conflict was found. Ensure the workflow name is unique. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow**
> Workflow get_workflow(workflow_id)

Get the details of a workflow

Gets the details of a workflow with a given ID.

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
    api_instance = ICA_SDK.WorkflowsApi(api_client)
    workflow_id = 'workflow_id_example' # str | ID of the workflow

    try:
        # Get the details of a workflow
        api_response = api_instance.get_workflow(workflow_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowsApi->get_workflow: %s\n" % e)
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
    api_instance = ICA_SDK.WorkflowsApi(api_client)
    workflow_id = 'workflow_id_example' # str | ID of the workflow

    try:
        # Get the details of a workflow
        api_response = api_instance.get_workflow(workflow_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowsApi->get_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| ID of the workflow | 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of the workflow. |  -  |
**400** | Invalid request. |  -  |
**401** | Unauthorized |  -  |
**403** | Permission denied. |  -  |
**404** | The workflow with the specified ID was not found. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflows**
> WorkflowList list_workflows(tenant_id=tenant_id, name=name, categories=categories, include=include, page_size=page_size, page_token=page_token, sort=sort)

Get a list of workflows

Gets a list of workflows.

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
    api_instance = ICA_SDK.WorkflowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | ID of the tenant (optional)
name = 'name_example' # str |  (optional)
categories = ['categories_example'] # list[str] |  (optional)
include = ['include_example'] # list[str] | Comma-separated list of properties to include in the response (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to 'timeCreated asc')

    try:
        # Get a list of workflows
        api_response = api_instance.list_workflows(tenant_id=tenant_id, name=name, categories=categories, include=include, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowsApi->list_workflows: %s\n" % e)
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
    api_instance = ICA_SDK.WorkflowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | ID of the tenant (optional)
name = 'name_example' # str |  (optional)
categories = ['categories_example'] # list[str] |  (optional)
include = ['include_example'] # list[str] | Comma-separated list of properties to include in the response (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to 'timeCreated asc')

    try:
        # Get a list of workflows
        api_response = api_instance.list_workflows(tenant_id=tenant_id, name=name, categories=categories, include=include, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowsApi->list_workflows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| ID of the tenant | [optional] 
 **name** | **str**|  | [optional] 
 **categories** | [**list[str]**](str.md)|  | [optional] 
 **include** | [**list[str]**](str.md)| Comma-separated list of properties to include in the response | [optional] 
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] [default to 10]
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional] 
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] [default to &#39;timeCreated asc&#39;]

### Return type

[**WorkflowList**](WorkflowList.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paged list of workflows. |  -  |
**400** | Invalid request. |  -  |
**401** | Unauthorized |  -  |
**403** | Permission denied. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workflow**
> Workflow update_workflow(workflow_id, body=body)

Update an existing workflow

Updates the workflow with a given ID.

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
    api_instance = ICA_SDK.WorkflowsApi(api_client)
    workflow_id = 'workflow_id_example' # str | ID of the workflow
body = ICA_SDK.UpdateWorkflowRequest() # UpdateWorkflowRequest |  (optional)

    try:
        # Update an existing workflow
        api_response = api_instance.update_workflow(workflow_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowsApi->update_workflow: %s\n" % e)
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
    api_instance = ICA_SDK.WorkflowsApi(api_client)
    workflow_id = 'workflow_id_example' # str | ID of the workflow
body = ICA_SDK.UpdateWorkflowRequest() # UpdateWorkflowRequest |  (optional)

    try:
        # Update an existing workflow
        api_response = api_instance.update_workflow(workflow_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowsApi->update_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| ID of the workflow | 
 **body** | [**UpdateWorkflowRequest**](UpdateWorkflowRequest.md)|  | [optional] 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns updated workflow. |  -  |
**400** | Invalid request. |  -  |
**401** | Unauthorized |  -  |
**403** | Permission denied. |  -  |
**404** | The workflow with the specified ID was not found. |  -  |
**409** | A conflict was found. Ensure the workflow name is unique. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

