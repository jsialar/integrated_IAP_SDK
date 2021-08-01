# ICA_SDK.SampleSheetsApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_sample_sheet**](SampleSheetsApi.md#generate_sample_sheet) | **POST** /v1/sequencing:generateSampleSheet | Generate a sample sheet.
[**parse_sample_sheet**](SampleSheetsApi.md#parse_sample_sheet) | **POST** /v1/sequencing:parseSampleSheet | Parse a sample sheet.


# **generate_sample_sheet**
> SampleSheet generate_sample_sheet()

Generate a sample sheet.

Generate a sample sheet, and return information about that sample sheet.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sample_sheets_api
from ICA_SDK.model.generate_sample_sheet_request import GenerateSampleSheetRequest
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.sample_sheet import SampleSheet
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
    api_instance = sample_sheets_api.SampleSheetsApi(api_client)
    body = GenerateSampleSheetRequest(
        run_configuration=CreateSequencingRunConfigurationRequest(
            instrument_type="instrument_type_example",
            instrument_platform="instrument_platform_example",
            run_name="run_name_example",
            description="description_example",
            regulatory_mode="RUO",
            num_cycles_read1=0,
            num_cycles_read2=0,
            read_type="Single",
            num_cycles_index1=0,
            num_cycles_index2=0,
            use_custom_primer_for_read1=True,
            use_custom_primer_for_read2=True,
            use_custom_primer_for_index1=True,
            use_custom_primer_for_index2=True,
            input_container_identifier="input_container_identifier_example",
        ),
        run_contents=UpdateSequencingRunContentsRequest(
            allow_index_updates=True,
            lane_contents=[
                LaneContent(
                    lane_number=1,
                    same_as_lane_number=1,
                    adapter_sequence_read1="adapter_sequence_read1_example",
                    adapter_sequence_read2="adapter_sequence_read2_example",
                    lane_libraries=[
                        LaneLibrary(
                            sample_name="sample_name_example",
                            sample_urn="sample_urn_example",
                            project_name="project_name_example",
                            library_name="library_name_example",
                            library_urn="library_urn_example",
                            adapter_sequence_read1="adapter_sequence_read1_example",
                            adapter_sequence_read2="adapter_sequence_read2_example",
                            index1_sequence="index1_sequence_example",
                            index2_sequence="index2_sequence_example",
                            index_container_position="index_container_position_example",
                            index1_name="index1_name_example",
                            index2_name="index2_name_example",
                            library_prep_kit_urn="library_prep_kit_urn_example",
                            index_adapter_kit_urn="index_adapter_kit_urn_example",
                        ),
                    ],
                ),
            ],
        ),
        run_analysis_configurations=[
            CreateSequencingRunAnalysisConfigurationRequest(
                name="name_example",
                description="description_example",
                analysis_version_definition_id="analysis_version_definition_id_example",
                settings={},
                sample_settings=[
                    SampleSettingEntry(
                        sample_id="sample_id_example",
                        settings={},
                    ),
                ],
            ),
        ],
        include=[
            "IncludeFileReferences",
        ],
        exclude_kit_urns=True,
    ) # GenerateSampleSheetRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate a sample sheet.
        api_response = api_instance.generate_sample_sheet(body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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
> ParseSampleSheetResponse parse_sample_sheet()

Parse a sample sheet.

Parse a sample sheet, and return information about that run.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sample_sheets_api
from ICA_SDK.model.parse_sample_sheet_request import ParseSampleSheetRequest
from ICA_SDK.model.parse_sample_sheet_response import ParseSampleSheetResponse
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
    api_instance = sample_sheets_api.SampleSheetsApi(api_client)
    body = ParseSampleSheetRequest(
        include=[
            "PrepKitInfo",
        ],
        sample_sheet_content="sample_sheet_content_example",
        resolve_prep_kits=True,
        resolve_prep_kits_by_name=True,
        resolve_index_sequence_info=True,
        enable_warnings_for_missing_cloud_sections=True,
    ) # ParseSampleSheetRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Parse a sample sheet.
        api_response = api_instance.parse_sample_sheet(body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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

