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
    api_instance = ICA_SDK.WorkgroupsApi(api_client)
    
    try:
        # Get a list of available workgroups. Requires session token (psToken) authorization Bearer token
        api_response = api_instance.list_workgroups()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkgroupsApi->list_workgroups: %s\n" % e)
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
    api_instance = ICA_SDK.WorkgroupsApi(api_client)
    
    try:
        # Get a list of available workgroups. Requires session token (psToken) authorization Bearer token
        api_response = api_instance.list_workgroups()
        pprint(api_response)
    except ApiException as e:
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

