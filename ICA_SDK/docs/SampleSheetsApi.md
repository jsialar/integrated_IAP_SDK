# ICA_SDK.SampleSheetsApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_sample_sheet**](SampleSheetsApi.md#generate_sample_sheet) | **POST** /v1/sequencing:generateSampleSheet | Generate a sample sheet.
[**parse_sample_sheet**](SampleSheetsApi.md#parse_sample_sheet) | **POST** /v1/sequencing:parseSampleSheet | Parse a sample sheet.


# **generate_sample_sheet**
> SampleSheet generate_sample_sheet(body=body)

Generate a sample sheet.

Generate a sample sheet, and return information about that sample sheet.

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
    api_instance = ICA_SDK.SampleSheetsApi(api_client)
    body = ICA_SDK.GenerateSampleSheetRequest() # GenerateSampleSheetRequest |  (optional)

    try:
        # Generate a sample sheet.
        api_response = api_instance.generate_sample_sheet(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SampleSheetsApi->generate_sample_sheet: %s\n" % e)
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
    api_instance = ICA_SDK.SampleSheetsApi(api_client)
    body = ICA_SDK.GenerateSampleSheetRequest() # GenerateSampleSheetRequest |  (optional)

    try:
        # Generate a sample sheet.
        api_response = api_instance.generate_sample_sheet(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SampleSheetsApi->generate_sample_sheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenerateSampleSheetRequest**](GenerateSampleSheetRequest.md)|  | [optional] 

### Return type

[**SampleSheet**](SampleSheet.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sample sheet generated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**409** | Conflict. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_sample_sheet**
> ParseSampleSheetResponse parse_sample_sheet(body=body)

Parse a sample sheet.

Parse a sample sheet, and return information about that run.

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
    api_instance = ICA_SDK.SampleSheetsApi(api_client)
    body = ICA_SDK.ParseSampleSheetRequest() # ParseSampleSheetRequest |  (optional)

    try:
        # Parse a sample sheet.
        api_response = api_instance.parse_sample_sheet(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SampleSheetsApi->parse_sample_sheet: %s\n" % e)
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
    api_instance = ICA_SDK.SampleSheetsApi(api_client)
    body = ICA_SDK.ParseSampleSheetRequest() # ParseSampleSheetRequest |  (optional)

    try:
        # Parse a sample sheet.
        api_response = api_instance.parse_sample_sheet(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SampleSheetsApi->parse_sample_sheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ParseSampleSheetRequest**](ParseSampleSheetRequest.md)|  | [optional] 

### Return type

[**ParseSampleSheetResponse**](ParseSampleSheetResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sample sheet parsed successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

