# ICA_SDK.SubscriptionsApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription**](SubscriptionsApi.md#create_subscription) | **POST** /v1/subscriptions | Creates a subscription to an event type and defines how those events get delivered.
[**disable_subscription**](SubscriptionsApi.md#disable_subscription) | **DELETE** /v1/subscriptions/{subscriptionId} | Given a subscription id, disables the specified subscription.
[**get_subscription**](SubscriptionsApi.md#get_subscription) | **GET** /v1/subscriptions/{subscriptionId} | Given a subscription id, returns information about that subscription.
[**list_subscriptions**](SubscriptionsApi.md#list_subscriptions) | **GET** /v1/subscriptions | Get a list of subscriptions.


# **create_subscription**
> Subscription create_subscription(body=body)

Creates a subscription to an event type and defines how those events get delivered.

Events can be delivered to AWS SQS, AWS SNS, or can be used to launch a WES workflow.

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
    api_instance = ICA_SDK.SubscriptionsApi(api_client)
    body = ICA_SDK.CreateSubscriptionRequest() # CreateSubscriptionRequest |  (optional)

    try:
        # Creates a subscription to an event type and defines how those events get delivered.
        api_response = api_instance.create_subscription(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubscriptionsApi->create_subscription: %s\n" % e)
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
    api_instance = ICA_SDK.SubscriptionsApi(api_client)
    body = ICA_SDK.CreateSubscriptionRequest() # CreateSubscriptionRequest |  (optional)

    try:
        # Creates a subscription to an event type and defines how those events get delivered.
        api_response = api_instance.create_subscription(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubscriptionsApi->create_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSubscriptionRequest**](CreateSubscriptionRequest.md)|  | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The subscription is created successfully. |  -  |
**400** | An invalid or missing input parameter will result in a bad request. |  -  |
**401** | The acting identity cannot be authenticated and authorized. |  -  |
**403** | The acting identity is not authorized to subscribe to the given event type or deliver to the given delivery target. |  -  |
**409** | The given delivery target is not valid or cannot be delivered to. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_subscription**
> Subscription disable_subscription(subscription_id)

Given a subscription id, disables the specified subscription.

Given a subscription id, disables that subscription with the current JWT tokenâ€™s tenant Id.

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
    api_instance = ICA_SDK.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | Id of the subscription to be disabled

    try:
        # Given a subscription id, disables the specified subscription.
        api_response = api_instance.disable_subscription(subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubscriptionsApi->disable_subscription: %s\n" % e)
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
    api_instance = ICA_SDK.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | Id of the subscription to be disabled

    try:
        # Given a subscription id, disables the specified subscription.
        api_response = api_instance.disable_subscription(subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubscriptionsApi->disable_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of the subscription to be disabled | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription for the given ID is disabled successfully. |  -  |
**400** | An invalid or missing input parameter will result in a bad request. |  -  |
**401** | The acting identity cannot be authenticated and authorized. |  -  |
**403** | The acting identity is not authorized to disable the subscription for the given ID. |  -  |
**404** | Could not find a subscription for the given ID. |  -  |
**410** | The subscription for the given ID has been disabled. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription**
> Subscription get_subscription(subscription_id)

Given a subscription id, returns information about that subscription.

Given a subscription id, returns information about that subscription accessible by the current JWT tokenâ€™s tenant Id.

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
    api_instance = ICA_SDK.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | Id of the subscription to return

    try:
        # Given a subscription id, returns information about that subscription.
        api_response = api_instance.get_subscription(subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubscriptionsApi->get_subscription: %s\n" % e)
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
    api_instance = ICA_SDK.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | Id of the subscription to return

    try:
        # Given a subscription id, returns information about that subscription.
        api_response = api_instance.get_subscription(subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubscriptionsApi->get_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of the subscription to return | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription for the given ID is found and returned successfully. |  -  |
**400** | An invalid or missing input parameter will result in a bad request. |  -  |
**401** | The acting identity cannot be authenticated and authorized. |  -  |
**403** | The acting identity is not authorized to access the subscription for the given ID. |  -  |
**404** | Could not find a subscription for the given ID. |  -  |
**410** | The subscription for the given ID has been disabled. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_subscriptions**
> SubscriptionList list_subscriptions(event_type=event_type, page_size=page_size, page_token=page_token)

Get a list of subscriptions.

Get a list of subscriptions accessible by the current JWT tokenâ€™s tenant Id.

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
    api_instance = ICA_SDK.SubscriptionsApi(api_client)
    event_type = 'event_type_example' # str | Optional event type for filtering returned subscriptions (optional)
page_size = 56 # int | Optional parameter to define the page size returned. Valid inputs range from 1-1000. (optional)
page_token = 'page_token_example' # str | Utilized for navigation after initial listing. Valid values include those of  firstPageToken, nextPageToken, and previousPageToken in the list response.  When there are no more pages, the nextPageToken will be null. (optional)

    try:
        # Get a list of subscriptions.
        api_response = api_instance.list_subscriptions(event_type=event_type, page_size=page_size, page_token=page_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubscriptionsApi->list_subscriptions: %s\n" % e)
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
    api_instance = ICA_SDK.SubscriptionsApi(api_client)
    event_type = 'event_type_example' # str | Optional event type for filtering returned subscriptions (optional)
page_size = 56 # int | Optional parameter to define the page size returned. Valid inputs range from 1-1000. (optional)
page_token = 'page_token_example' # str | Utilized for navigation after initial listing. Valid values include those of  firstPageToken, nextPageToken, and previousPageToken in the list response.  When there are no more pages, the nextPageToken will be null. (optional)

    try:
        # Get a list of subscriptions.
        api_response = api_instance.list_subscriptions(event_type=event_type, page_size=page_size, page_token=page_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubscriptionsApi->list_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_type** | **str**| Optional event type for filtering returned subscriptions | [optional] 
 **page_size** | **int**| Optional parameter to define the page size returned. Valid inputs range from 1-1000. | [optional] 
 **page_token** | **str**| Utilized for navigation after initial listing. Valid values include those of  firstPageToken, nextPageToken, and previousPageToken in the list response.  When there are no more pages, the nextPageToken will be null. | [optional] 

### Return type

[**SubscriptionList**](SubscriptionList.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscriptions found and returned successfully. |  -  |
**400** | An invalid or missing input parameter will result in a bad request. |  -  |
**401** | The acting identity cannot be authenticated and authorized. |  -  |
**403** | The acting identity is not authorized to access subscriptions. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

