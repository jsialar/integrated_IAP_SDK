# ICA_SDK.WorkflowVersionsApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workflow_version**](WorkflowVersionsApi.md#create_workflow_version) | **POST** /v1/workflows/{workflowId}/versions | Create a new workflow version
[**get_workflow_version**](WorkflowVersionsApi.md#get_workflow_version) | **GET** /v1/workflows/{workflowId}/versions/{versionName} | Get the details of a workflow version
[**launch_workflow_version**](WorkflowVersionsApi.md#launch_workflow_version) | **POST** /v1/workflows/{workflowId}/versions/{versionName}:launch | Launch a workflow version
[**list_all_workflow_versions**](WorkflowVersionsApi.md#list_all_workflow_versions) | **GET** /v1/workflows/versions | Get a list of all workflow versions
[**list_workflow_versions**](WorkflowVersionsApi.md#list_workflow_versions) | **GET** /v1/workflows/{workflowId}/versions | Get a list of workflow versions
[**update_workflow_version**](WorkflowVersionsApi.md#update_workflow_version) | **PATCH** /v1/workflows/{workflowId}/versions/{versionName} | Update an existing workflow version


# **create_workflow_version**
> WorkflowVersion create_workflow_version(workflow_id)

Create a new workflow version

Creates a new workflow version with a given workflow ID.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import workflow_versions_api
from ICA_SDK.model.create_workflow_version_request import CreateWorkflowVersionRequest
from ICA_SDK.model.workflow_version import WorkflowVersion
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
    api_instance = workflow_versions_api.WorkflowVersionsApi(api_client)
    workflow_id = "workflowId_example" # str | ID of the workflow
    body = CreateWorkflowVersionRequest(
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
    ) # CreateWorkflowVersionRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new workflow version
        api_response = api_instance.create_workflow_version(workflow_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling WorkflowVersionsApi->create_workflow_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new workflow version
        api_response = api_instance.create_workflow_version(workflow_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling WorkflowVersionsApi->create_workflow_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| ID of the workflow |
 **body** | [**CreateWorkflowVersionRequest**](CreateWorkflowVersionRequest.md)|  | [optional]

### Return type

[**WorkflowVersion**](WorkflowVersion.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Details of the created workflow version. |  -  |
**400** | Invalid request. |  -  |
**401** | Unauthorized |  -  |
**403** | Permission denied. |  -  |
**409** | A conflict was found. Ensure the workflow version name is unique. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_version**
> WorkflowVersion get_workflow_version(workflow_id, version_name)

Get the details of a workflow version

Gets the details for a workflow version with a given workflow ID and version name.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import workflow_versions_api
from ICA_SDK.model.workflow_version import WorkflowVersion
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
    api_instance = workflow_versions_api.WorkflowVersionsApi(api_client)
    workflow_id = "workflowId_example" # str | ID of the workflow
    version_name = "versionName_example" # str | Name of the workflow version

    # example passing only required values which don't have defaults set
    try:
        # Get the details of a workflow version
        api_response = api_instance.get_workflow_version(workflow_id, version_name)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling WorkflowVersionsApi->get_workflow_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| ID of the workflow |
 **version_name** | **str**| Name of the workflow version |

### Return type

[**WorkflowVersion**](WorkflowVersion.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of the workflow version. |  -  |
**400** | Invalid request. |  -  |
**401** | Unauthorized |  -  |
**403** | Permission denied. |  -  |
**404** | The workflow ID or version name was not found. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launch_workflow_version**
> WorkflowRun launch_workflow_version(workflow_id, version_name)

Launch a workflow version

Launches a workflow version with a given workflow ID and version name.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import workflow_versions_api
from ICA_SDK.model.workflow_run import WorkflowRun
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.launch_workflow_version_request import LaunchWorkflowVersionRequest
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
    api_instance = workflow_versions_api.WorkflowVersionsApi(api_client)
    workflow_id = "workflowId_example" # str | ID of the workflow
    version_name = "versionName_example" # str | Name of the workflow version
    include = [
        "definition",
    ] # [str] | Comma-separated list of properties to include in the response (optional)
    body = LaunchWorkflowVersionRequest(
        name="+lYRGjjNSwg0_bs9ZayIMrKdgNvb6gvxmPb9GcsM61ate1RA89q3w1l4eH4XxEz.5awxoFZxHzs6ED.k",
        input={},
        engine_parameters={},
    ) # LaunchWorkflowVersionRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Launch a workflow version
        api_response = api_instance.launch_workflow_version(workflow_id, version_name)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling WorkflowVersionsApi->launch_workflow_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Launch a workflow version
        api_response = api_instance.launch_workflow_version(workflow_id, version_name, include=include, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling WorkflowVersionsApi->launch_workflow_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| ID of the workflow |
 **version_name** | **str**| Name of the workflow version |
 **include** | **[str]**| Comma-separated list of properties to include in the response | [optional]
 **body** | [**LaunchWorkflowVersionRequest**](LaunchWorkflowVersionRequest.md)|  | [optional]

### Return type

[**WorkflowRun**](WorkflowRun.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Details of the created workflow run. |  -  |
**400** | Invalid request. |  -  |
**401** | Unauthorized |  -  |
**403** | Permission denied. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_workflow_versions**
> WorkflowVersionList list_all_workflow_versions()

Get a list of all workflow versions

Gets a list of workflow versions across all workflows.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import workflow_versions_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.workflow_version_list import WorkflowVersionList
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
    api_instance = workflow_versions_api.WorkflowVersionsApi(api_client)
    tenant_id = "tenantId_example" # str | ID of the tenant (optional)
    include = [
        "totalItemCount",
    ] # [str] | Comma-separated list of properties to include in the response (optional)
    page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) if omitted the server will use the default value of 10
    page_token = "pageToken_example" # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
    sort = "timeCreated asc" # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) if omitted the server will use the default value of "timeCreated asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of all workflow versions
        api_response = api_instance.list_all_workflow_versions(tenant_id=tenant_id, include=include, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling WorkflowVersionsApi->list_all_workflow_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| ID of the tenant | [optional]
 **include** | **[str]**| Comma-separated list of properties to include in the response | [optional]
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] if omitted the server will use the default value of 10
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional]
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] if omitted the server will use the default value of "timeCreated asc"

### Return type

[**WorkflowVersionList**](WorkflowVersionList.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paged list of workflow versions across all workflows. |  -  |
**400** | Invalid request. |  -  |
**401** | Unauthorized |  -  |
**403** | Permission denied. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflow_versions**
> WorkflowVersionList list_workflow_versions(workflow_id)

Get a list of workflow versions

Gets a list of workflow versions with a given workflow ID.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import workflow_versions_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.workflow_version_list import WorkflowVersionList
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
    api_instance = workflow_versions_api.WorkflowVersionsApi(api_client)
    workflow_id = "workflowId_example" # str | ID of the workflow
    include = [
        "totalItemCount",
    ] # [str] | Comma-separated list of properties to include in the response (optional)
    page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) if omitted the server will use the default value of 10
    page_token = "pageToken_example" # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
    sort = "timeCreated asc" # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) if omitted the server will use the default value of "timeCreated asc"

    # example passing only required values which don't have defaults set
    try:
        # Get a list of workflow versions
        api_response = api_instance.list_workflow_versions(workflow_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling WorkflowVersionsApi->list_workflow_versions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of workflow versions
        api_response = api_instance.list_workflow_versions(workflow_id, include=include, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling WorkflowVersionsApi->list_workflow_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| ID of the workflow |
 **include** | **[str]**| Comma-separated list of properties to include in the response | [optional]
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] if omitted the server will use the default value of 10
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional]
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] if omitted the server will use the default value of "timeCreated asc"

### Return type

[**WorkflowVersionList**](WorkflowVersionList.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paged list of workflow versions that the user has access to. |  -  |
**400** | Invalid request. |  -  |
**401** | Unauthorized |  -  |
**403** | Permission denied. |  -  |
**404** | The workflow with the specified ID was not found. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workflow_version**
> WorkflowVersion update_workflow_version(workflow_id, version_name)

Update an existing workflow version

Updates an existing workflow version. Note: The Version, Definition, and Status cannot be changed simultaneously. Only one of these can be changed per API call.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import workflow_versions_api
from ICA_SDK.model.workflow_version import WorkflowVersion
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_workflow_version_request import UpdateWorkflowVersionRequest
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
    api_instance = workflow_versions_api.WorkflowVersionsApi(api_client)
    workflow_id = "workflowId_example" # str | ID of the workflow
    version_name = "versionName_example" # str | Name of the workflow version
    body = UpdateWorkflowVersionRequest(
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
    ) # UpdateWorkflowVersionRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an existing workflow version
        api_response = api_instance.update_workflow_version(workflow_id, version_name)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling WorkflowVersionsApi->update_workflow_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an existing workflow version
        api_response = api_instance.update_workflow_version(workflow_id, version_name, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling WorkflowVersionsApi->update_workflow_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| ID of the workflow |
 **version_name** | **str**| Name of the workflow version |
 **body** | [**UpdateWorkflowVersionRequest**](UpdateWorkflowVersionRequest.md)|  | [optional]

### Return type

[**WorkflowVersion**](WorkflowVersion.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of the created workflow run. |  -  |
**400** | Invalid request. |  -  |
**401** | Unauthorized |  -  |
**403** | Permission denied. |  -  |
**404** | The workflow ID or version name was not found. |  -  |
**409** | A conflict was found. Ensure the workflow version name is unique. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

