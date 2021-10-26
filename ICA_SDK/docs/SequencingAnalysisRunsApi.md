# ICA_SDK.SequencingAnalysisRunsApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sequencing_analysis_run**](SequencingAnalysisRunsApi.md#get_sequencing_analysis_run) | **GET** /v1/sequencing/analysisRuns/{analysisRunId} | Get SequencingAnalysisRun details.
[**list_sequencing_analysis_runs**](SequencingAnalysisRunsApi.md#list_sequencing_analysis_runs) | **GET** /v1/sequencing/analysisRuns | Get a list of analysis runs.
[**sync_sequencing_analysis_run**](SequencingAnalysisRunsApi.md#sync_sequencing_analysis_run) | **POST** /v1/sequencing/analysisRuns/{analysisRunId}:sync | Sync A SequencingAnalysisRun.


# **get_sequencing_analysis_run**
> SequencingAnalysisRun get_sequencing_analysis_run(analysis_run_id, include=include)

Get SequencingAnalysisRun details.

For a given ID, return information about that SequencingAnalysisRun.

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
    api_instance = ICA_SDK.SequencingAnalysisRunsApi(api_client)
    analysis_run_id = 'analysis_run_id_example' # str | ID of the analysis run
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)

    try:
        # Get SequencingAnalysisRun details.
        api_response = api_instance.get_sequencing_analysis_run(analysis_run_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingAnalysisRunsApi->get_sequencing_analysis_run: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingAnalysisRunsApi(api_client)
    analysis_run_id = 'analysis_run_id_example' # str | ID of the analysis run
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)

    try:
        # Get SequencingAnalysisRun details.
        api_response = api_instance.get_sequencing_analysis_run(analysis_run_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingAnalysisRunsApi->get_sequencing_analysis_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_run_id** | **str**| ID of the analysis run | 
 **include** | [**list[str]**](str.md)| Include flags to specify what is included in the response | [optional] 

### Return type

[**SequencingAnalysisRun**](SequencingAnalysisRun.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SequencingAnalysisRun details returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No SequencingAnalysisRun found for given SequencingAnalysisRun ID. |  -  |
**410** | The SequencingAnalysisRun with the given SequencingAnalysisRun ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sequencing_analysis_runs**
> SequencingAnalysisRunCompactSequencingAnalysisRunSortFieldsPagedItems list_sequencing_analysis_runs(include=include, status=status, sequencing_run_id=sequencing_run_id, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)

Get a list of analysis runs.

Get a list of analysis runs accessible by the request token.

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
    api_instance = ICA_SDK.SequencingAnalysisRunsApi(api_client)
    include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)
status = ['status_example'] # list[str] | Optional parameter. Set to filter the analysis run list and only include analysis runs with the specified status. (optional)
sequencing_run_id = ['sequencing_run_id_example'] # list[str] | Optional parameter. Set to filter the analysis run and only include analysis runs associated with the specific sequencing runs (optional)
tenant_ids = ['tenant_ids_example'] # list[str] | Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to 'timeCreated asc')

    try:
        # Get a list of analysis runs.
        api_response = api_instance.list_sequencing_analysis_runs(include=include, status=status, sequencing_run_id=sequencing_run_id, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingAnalysisRunsApi->list_sequencing_analysis_runs: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingAnalysisRunsApi(api_client)
    include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)
status = ['status_example'] # list[str] | Optional parameter. Set to filter the analysis run list and only include analysis runs with the specified status. (optional)
sequencing_run_id = ['sequencing_run_id_example'] # list[str] | Optional parameter. Set to filter the analysis run and only include analysis runs associated with the specific sequencing runs (optional)
tenant_ids = ['tenant_ids_example'] # list[str] | Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to 'timeCreated asc')

    try:
        # Get a list of analysis runs.
        api_response = api_instance.list_sequencing_analysis_runs(include=include, status=status, sequencing_run_id=sequencing_run_id, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingAnalysisRunsApi->list_sequencing_analysis_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**list[str]**](str.md)| Include flags to specify what is included in the response | [optional] 
 **status** | [**list[str]**](str.md)| Optional parameter. Set to filter the analysis run list and only include analysis runs with the specified status. | [optional] 
 **sequencing_run_id** | [**list[str]**](str.md)| Optional parameter. Set to filter the analysis run and only include analysis runs associated with the specific sequencing runs | [optional] 
 **tenant_ids** | [**list[str]**](str.md)| Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids | [optional] 
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] [default to 10]
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional] 
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] [default to &#39;timeCreated asc&#39;]

### Return type

[**SequencingAnalysisRunCompactSequencingAnalysisRunSortFieldsPagedItems**](SequencingAnalysisRunCompactSequencingAnalysisRunSortFieldsPagedItems.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SequencingAnalysisRun list returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_sequencing_analysis_run**
> SequencingAnalysisRun sync_sequencing_analysis_run(analysis_run_id)

Sync A SequencingAnalysisRun.

For a given ID, sync the SequencingAnalysisRun.

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
    api_instance = ICA_SDK.SequencingAnalysisRunsApi(api_client)
    analysis_run_id = 'analysis_run_id_example' # str | 

    try:
        # Sync A SequencingAnalysisRun.
        api_response = api_instance.sync_sequencing_analysis_run(analysis_run_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingAnalysisRunsApi->sync_sequencing_analysis_run: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingAnalysisRunsApi(api_client)
    analysis_run_id = 'analysis_run_id_example' # str | 

    try:
        # Sync A SequencingAnalysisRun.
        api_response = api_instance.sync_sequencing_analysis_run(analysis_run_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingAnalysisRunsApi->sync_sequencing_analysis_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_run_id** | **str**|  | 

### Return type

[**SequencingAnalysisRun**](SequencingAnalysisRun.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SequencingAnalysisRun is synced successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No SequencingAnalysisRun found for given SequencingAnalysisRun ID. |  -  |
**409** | Sync SequencingAnalysisRun failed due to conflict. |  -  |
**410** | The SequencingAnalysisRun with the given SequencingAnalysisRun ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

