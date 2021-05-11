# ICA_SDK.WorkgroupsApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_workgroups**](WorkgroupsApi.md#list_workgroups) | **GET** /v1/workgroups | Get a list of available workgroups. Requires session token (psToken) authorization Bearer token


# **list_workgroups**
> WorkgroupResponse list_workgroups()

Get a list of available workgroups. Requires session token (psToken) authorization Bearer token

Get a list of available workgroups

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import workgroups_api
from ICA_SDK.model.workgroup_response import WorkgroupResponse
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
    api_instance = workgroups_api.WorkgroupsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a list of available workgroups. Requires session token (psToken) authorization Bearer token
        api_response = api_instance.list_workgroups()
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling WorkgroupsApi->list_workgroups: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**WorkgroupResponse**](WorkgroupResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workgroups returned successfully |  -  |
**401** | The provided session token is unauthorized. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

