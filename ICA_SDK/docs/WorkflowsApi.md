# ICA_SDK.WorkflowsApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workflow**](WorkflowsApi.md#create_workflow) | **POST** /v1/workflows | Create a workflow
[**get_workflow**](WorkflowsApi.md#get_workflow) | **GET** /v1/workflows/{workflowId} | Get the details of a workflow
[**list_workflows**](WorkflowsApi.md#list_workflows) | **GET** /v1/workflows | Get a list of workflows
[**update_workflow**](WorkflowsApi.md#update_workflow) | **PATCH** /v1/workflows/{workflowId} | Update an existing workflow


# **create_workflow**
> Workflow create_workflow()

Create a workflow

Creates a new workflow and version (if provided).

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import workflows_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.workflow import Workflow
from ICA_SDK.model.create_workflow_request import CreateWorkflowRequest
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    body = CreateWorkflowRequest(
        name="name_example",
        description="description_example",
        organization="organization_example",
        workflow_version=CreateWorkflowVersionRequest(
            version="version_example",
            description="description_example",
            language=WorkflowLanguage(
                name="name_example",
                version="version_example",
            ),
            definition={},
            acl=[
                "acl_example",
            ],
            status="draft",
        ),
        tool_class="workflow",
        acl=[
            "acl_example",
        ],
        categories=[
            "categories_example",
        ],
    ) # CreateWorkflowRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a workflow
        api_response = api_instance.create_workflow(body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import workflows_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.workflow import Workflow
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    workflow_id = "workflowId_example" # str | ID of the workflow

    # example passing only required values which don't have defaults set
    try:
        # Get the details of a workflow
        api_response = api_instance.get_workflow(workflow_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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
> WorkflowList list_workflows()

Get a list of workflows

Gets a list of workflows.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import workflows_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.workflow_list import WorkflowList
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    tenant_id = "tenantId_example" # str | ID of the tenant (optional)
    name = "name_example" # str |  (optional)
    categories = [
        "categories_example",
    ] # [str] |  (optional)
    include = [
        "totalItemCount",
    ] # [str] | Comma-separated list of properties to include in the response (optional)
    page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) if omitted the server will use the default value of 10
    page_token = "pageToken_example" # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
    sort = "timeCreated asc" # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) if omitted the server will use the default value of "timeCreated asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of workflows
        api_response = api_instance.list_workflows(tenant_id=tenant_id, name=name, categories=categories, include=include, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling WorkflowsApi->list_workflows: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| ID of the tenant | [optional]
 **name** | **str**|  | [optional]
 **categories** | **[str]**|  | [optional]
 **include** | **[str]**| Comma-separated list of properties to include in the response | [optional]
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] if omitted the server will use the default value of 10
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional]
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] if omitted the server will use the default value of "timeCreated asc"

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
> Workflow update_workflow(workflow_id)

Update an existing workflow

Updates the workflow with a given ID.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import workflows_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.workflow import Workflow
from ICA_SDK.model.update_workflow_request import UpdateWorkflowRequest
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    workflow_id = "workflowId_example" # str | ID of the workflow
    body = UpdateWorkflowRequest(
        name="name_example",
        description="description_example",
        organization="organization_example",
        acl=[
            "acl_example",
        ],
        categories=[
            "categories_example",
        ],
    ) # UpdateWorkflowRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an existing workflow
        api_response = api_instance.update_workflow(workflow_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling WorkflowsApi->update_workflow: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an existing workflow
        api_response = api_instance.update_workflow(workflow_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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

