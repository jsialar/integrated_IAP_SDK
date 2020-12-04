# swagger_client.WorkflowVersionsApi

All URIs are relative to *https://aps1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workflow_version**](WorkflowVersionsApi.md#create_workflow_version) | **POST** /v1/workflows/{workflowId}/versions | Create a new workflow version
[**get_workflow_version**](WorkflowVersionsApi.md#get_workflow_version) | **GET** /v1/workflows/{workflowId}/versions/{versionName} | Get the details of a workflow version
[**launch_workflow_version**](WorkflowVersionsApi.md#launch_workflow_version) | **POST** /v1/workflows/{workflowId}/versions/{versionName}:launch | Launch a workflow version
[**list_all_workflow_versions**](WorkflowVersionsApi.md#list_all_workflow_versions) | **GET** /v1/workflows/versions | Get a list of all workflow versions
[**list_workflow_versions**](WorkflowVersionsApi.md#list_workflow_versions) | **GET** /v1/workflows/{workflowId}/versions | Get a list of workflow versions
[**update_workflow_version**](WorkflowVersionsApi.md#update_workflow_version) | **PATCH** /v1/workflows/{workflowId}/versions/{versionName} | Update an existing workflow version


# **create_workflow_version**
> WorkflowVersion create_workflow_version(workflow_id, body=body)

Create a new workflow version

Creates a new workflow version with a given workflow ID.

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
api_instance = swagger_client.WorkflowVersionsApi(swagger_client.ApiClient(configuration))
workflow_id = 'workflow_id_example' # str | ID of the workflow
body = swagger_client.CreateWorkflowVersionRequest() # CreateWorkflowVersionRequest |  (optional)

try:
    # Create a new workflow version
    api_response = api_instance.create_workflow_version(workflow_id, body=body)
    pprint(api_response)
except ApiException as e:
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_version**
> WorkflowVersion get_workflow_version(workflow_id, version_name)

Get the details of a workflow version

Gets the details for a workflow version with a given workflow ID and version name.

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
api_instance = swagger_client.WorkflowVersionsApi(swagger_client.ApiClient(configuration))
workflow_id = 'workflow_id_example' # str | ID of the workflow
version_name = 'version_name_example' # str | Name of the workflow version

try:
    # Get the details of a workflow version
    api_response = api_instance.get_workflow_version(workflow_id, version_name)
    pprint(api_response)
except ApiException as e:
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launch_workflow_version**
> WorkflowRun launch_workflow_version(workflow_id, version_name, include=include, body=body)

Launch a workflow version

Launches a workflow version with a given workflow ID and version name.

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
api_instance = swagger_client.WorkflowVersionsApi(swagger_client.ApiClient(configuration))
workflow_id = 'workflow_id_example' # str | ID of the workflow
version_name = 'version_name_example' # str | Name of the workflow version
include = ['include_example'] # list[str] | Comma-separated list of properties to include in the response (optional)
body = swagger_client.LaunchWorkflowVersionRequest() # LaunchWorkflowVersionRequest |  (optional)

try:
    # Launch a workflow version
    api_response = api_instance.launch_workflow_version(workflow_id, version_name, include=include, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowVersionsApi->launch_workflow_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| ID of the workflow | 
 **version_name** | **str**| Name of the workflow version | 
 **include** | [**list[str]**](str.md)| Comma-separated list of properties to include in the response | [optional] 
 **body** | [**LaunchWorkflowVersionRequest**](LaunchWorkflowVersionRequest.md)|  | [optional] 

### Return type

[**WorkflowRun**](WorkflowRun.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_workflow_versions**
> WorkflowVersionList list_all_workflow_versions(tenant_id=tenant_id, include=include, page_size=page_size, page_token=page_token, sort=sort)

Get a list of all workflow versions

Gets a list of workflow versions across all workflows.

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
api_instance = swagger_client.WorkflowVersionsApi(swagger_client.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | ID of the tenant (optional)
include = ['include_example'] # list[str] | Comma-separated list of properties to include in the response (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to timeCreated asc)

try:
    # Get a list of all workflow versions
    api_response = api_instance.list_all_workflow_versions(tenant_id=tenant_id, include=include, page_size=page_size, page_token=page_token, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowVersionsApi->list_all_workflow_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| ID of the tenant | [optional] 
 **include** | [**list[str]**](str.md)| Comma-separated list of properties to include in the response | [optional] 
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] [default to 10]
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional] 
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] [default to timeCreated asc]

### Return type

[**WorkflowVersionList**](WorkflowVersionList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflow_versions**
> WorkflowVersionList list_workflow_versions(workflow_id, include=include, page_size=page_size, page_token=page_token, sort=sort)

Get a list of workflow versions

Gets a list of workflow versions with a given workflow ID.

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
api_instance = swagger_client.WorkflowVersionsApi(swagger_client.ApiClient(configuration))
workflow_id = 'workflow_id_example' # str | ID of the workflow
include = ['include_example'] # list[str] | Comma-separated list of properties to include in the response (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to timeCreated asc)

try:
    # Get a list of workflow versions
    api_response = api_instance.list_workflow_versions(workflow_id, include=include, page_size=page_size, page_token=page_token, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowVersionsApi->list_workflow_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| ID of the workflow | 
 **include** | [**list[str]**](str.md)| Comma-separated list of properties to include in the response | [optional] 
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] [default to 10]
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional] 
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] [default to timeCreated asc]

### Return type

[**WorkflowVersionList**](WorkflowVersionList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workflow_version**
> WorkflowVersion update_workflow_version(workflow_id, version_name, body=body)

Update an existing workflow version

Updates an existing workflow version. Note: The Version, Definition, and Status cannot be changed simultaneously. Only one of these can be changed per API call.

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
api_instance = swagger_client.WorkflowVersionsApi(swagger_client.ApiClient(configuration))
workflow_id = 'workflow_id_example' # str | ID of the workflow
version_name = 'version_name_example' # str | Name of the workflow version
body = swagger_client.UpdateWorkflowVersionRequest() # UpdateWorkflowVersionRequest |  (optional)

try:
    # Update an existing workflow version
    api_response = api_instance.update_workflow_version(workflow_id, version_name, body=body)
    pprint(api_response)
except ApiException as e:
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
