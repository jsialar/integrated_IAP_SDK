# ICA_SDK.AccountsApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account**](AccountsApi.md#get_account) | **GET** /v1/accounts/{accountId} | Get requested account id info require authorization Bearer token


# **get_account**
> AccountResponse get_account(account_id)

Get requested account id info require authorization Bearer token

Get requested account id info

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
    api_instance = ICA_SDK.AccountsApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # Get requested account id info require authorization Bearer token
        api_response = api_instance.get_account(account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_account: %s\n" % e)
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
    api_instance = ICA_SDK.AccountsApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # Get requested account id info require authorization Bearer token
        api_response = api_instance.get_account(account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The account information returned successfully |  -  |
**401** | The provided token is unauthorized. |  -  |
**403** | You do not have permission to access this resource. |  -  |
**404** | The resource was not found at the given path. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

