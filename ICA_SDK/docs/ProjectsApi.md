# ICA_SDK.ProjectsApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_projects**](ProjectsApi.md#list_projects) | **GET** /v1/projects | Get a list of available projects. Requires user authorization Bearer token.


# **list_projects**
> ProjectPagedItems list_projects()

Get a list of available projects. Requires user authorization Bearer token.

Get a list of available projects

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import projects_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.project_paged_items import ProjectPagedItems
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
    api_instance = projects_api.ProjectsApi(api_client)
    page_token = "pageToken_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of available projects. Requires user authorization Bearer token.
        api_response = api_instance.list_projects(page_token=page_token)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling ProjectsApi->list_projects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_token** | **str**|  | [optional]

### Return type

[**ProjectPagedItems**](ProjectPagedItems.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Projects returned successfully |  -  |
**400** | The provided page token is invalid. |  -  |
**401** | The provided access token is unauthorized. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

