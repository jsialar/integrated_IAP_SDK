# ICA_SDK.AnalysisDatasetsApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_analysis_datasets**](AnalysisDatasetsApi.md#list_analysis_datasets) | **GET** /v1/sequencing/analysisDatasets | List analysis datasets.


# **list_analysis_datasets**
> AnalysisDatasetCompactAnalysisDatasetSortFieldsPagedItems list_analysis_datasets()

List analysis datasets.

Return a list of associated analysis datasets.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import analysis_datasets_api
from ICA_SDK.model.analysis_dataset_compact_analysis_dataset_sort_fields_paged_items import AnalysisDatasetCompactAnalysisDatasetSortFieldsPagedItems
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
    api_instance = analysis_datasets_api.AnalysisDatasetsApi(api_client)
    include = [
        "TotalItemCount",
    ] # [str] | Include flags to specify what is included in the response (optional)
    analysis_run_id = [
        "analysisRunId_example",
    ] # [str] | Optional parameter. Set to filter the analysis datasets list and only include analysis datasets associated with the provided analysis runs. (optional)
    tenant_ids = [
        "tenantIds_example",
    ] # [str] | Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids (optional)
    page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) if omitted the server will use the default value of 10
    page_token = "pageToken_example" # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
    sort = "timeCreated asc" # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) if omitted the server will use the default value of "timeCreated asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List analysis datasets.
        api_response = api_instance.list_analysis_datasets(include=include, analysis_run_id=analysis_run_id, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling AnalysisDatasetsApi->list_analysis_datasets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **[str]**| Include flags to specify what is included in the response | [optional]
 **analysis_run_id** | **[str]**| Optional parameter. Set to filter the analysis datasets list and only include analysis datasets associated with the provided analysis runs. | [optional]
 **tenant_ids** | **[str]**| Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids | [optional]
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] if omitted the server will use the default value of 10
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional]
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] if omitted the server will use the default value of "timeCreated asc"

### Return type

[**AnalysisDatasetCompactAnalysisDatasetSortFieldsPagedItems**](AnalysisDatasetCompactAnalysisDatasetSortFieldsPagedItems.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analysis datasets returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

