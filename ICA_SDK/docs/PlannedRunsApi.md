# ICA_SDK.PlannedRunsApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_planned_run**](PlannedRunsApi.md#create_planned_run) | **POST** /v1/sequencing/runs:plan | Create sequencing run plan.
[**import_planned_run**](PlannedRunsApi.md#import_planned_run) | **POST** /v1/sequencing/runs:import | Import a planned run from sample sheet.
[**lock_planned_run**](PlannedRunsApi.md#lock_planned_run) | **POST** /v1/sequencing/runs/{runId}:lock | Lock a planned run.
[**replace_planned_run**](PlannedRunsApi.md#replace_planned_run) | **PUT** /v1/sequencing/runs/{runId}/plan | Replace planned run configuration, contents, and analysis configurations.
[**start_planned_run**](PlannedRunsApi.md#start_planned_run) | **POST** /v1/sequencing/runs/{runId}:start | Start a planned sequencing run.
[**unlock_planned_run**](PlannedRunsApi.md#unlock_planned_run) | **POST** /v1/sequencing/runs/{runId}:unlock | Unlock a planned run.
[**update_planned_run_config**](PlannedRunsApi.md#update_planned_run_config) | **PATCH** /v1/sequencing/runs/{runId}/config | Update planned run configuration.


# **create_planned_run**
> SequencingRun create_planned_run()

Create sequencing run plan.

Create sequencing run plan, with configuration required for an instrument to start the run.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import planned_runs_api
from ICA_SDK.model.sequencing_run import SequencingRun
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.create_planned_run_request import CreatePlannedRunRequest
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
    api_instance = planned_runs_api.PlannedRunsApi(api_client)
    body = CreatePlannedRunRequest(
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
        is_favorite=True,
        acl=[
            "acl_example",
        ],
    ) # CreatePlannedRunRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create sequencing run plan.
        api_response = api_instance.create_planned_run(body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling PlannedRunsApi->create_planned_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePlannedRunRequest**](CreatePlannedRunRequest.md)|  | [optional]

### Return type

[**SequencingRun**](SequencingRun.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Planned run created successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_planned_run**
> ImportPlannedRunResponse import_planned_run()

Import a planned run from sample sheet.

Import a planned run based on sample sheet, return information of the import result.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import planned_runs_api
from ICA_SDK.model.import_planned_run_request import ImportPlannedRunRequest
from ICA_SDK.model.import_planned_run_response import ImportPlannedRunResponse
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
    api_instance = planned_runs_api.PlannedRunsApi(api_client)
    body = ImportPlannedRunRequest(
        sample_sheet_content="sample_sheet_content_example",
        resolve_prep_kits=True,
        resolve_prep_kits_by_name=True,
        resolve_index_sequence_info=True,
        enable_warnings_for_missing_cloud_sections=True,
        default_kits=[
            DefaultKit(
                lane_number=1,
                library_prep_kit_id="library_prep_kit_id_example",
                index_adapter_kit_id="index_adapter_kit_id_example",
            ),
        ],
    ) # ImportPlannedRunRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import a planned run from sample sheet.
        api_response = api_instance.import_planned_run(body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling PlannedRunsApi->import_planned_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImportPlannedRunRequest**](ImportPlannedRunRequest.md)|  | [optional]

### Return type

[**ImportPlannedRunResponse**](ImportPlannedRunResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Planned run imported successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**409** | Conflict. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_planned_run**
> SequencingRun lock_planned_run(run_id)

Lock a planned run.

Lock the planned run associated with a given sequencing run ID.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import planned_runs_api
from ICA_SDK.model.sequencing_run import SequencingRun
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
    api_instance = planned_runs_api.PlannedRunsApi(api_client)
    run_id = "runId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Lock a planned run.
        api_response = api_instance.lock_planned_run(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling PlannedRunsApi->lock_planned_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |

### Return type

[**SequencingRun**](SequencingRun.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Planned run locked successfully.\&quot; |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No planned run found for given sequencing run ID.\&quot; |  -  |
**409** | Request is invalid due to the current state of the sequencing run. |  -  |
**410** | The planned run for the given sequencing run ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_planned_run**
> SequencingRun replace_planned_run(run_id)

Replace planned run configuration, contents, and analysis configurations.

For a given sequencing run ID, replace the existing planned run with user input. This may include run configuration, run contents, and analysis configurations. Only applicable to runs in planning stage.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import planned_runs_api
from ICA_SDK.model.sequencing_run import SequencingRun
from ICA_SDK.model.replace_planned_run_request import ReplacePlannedRunRequest
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
    api_instance = planned_runs_api.PlannedRunsApi(api_client)
    run_id = "runId_example" # str | 
    body = ReplacePlannedRunRequest(
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
        is_favorite=True,
    ) # ReplacePlannedRunRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Replace planned run configuration, contents, and analysis configurations.
        api_response = api_instance.replace_planned_run(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling PlannedRunsApi->replace_planned_run: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Replace planned run configuration, contents, and analysis configurations.
        api_response = api_instance.replace_planned_run(run_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling PlannedRunsApi->replace_planned_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |
 **body** | [**ReplacePlannedRunRequest**](ReplacePlannedRunRequest.md)|  | [optional]

### Return type

[**SequencingRun**](SequencingRun.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Planned run updated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sequencing run found for given sequencing run ID. |  -  |
**410** | Sequencing run with given sequencing run ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_planned_run**
> SequencingRun start_planned_run(run_id)

Start a planned sequencing run.

Start a planned sequencing run, and return information about that run. Only applicable to planned runs.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import planned_runs_api
from ICA_SDK.model.sequencing_run import SequencingRun
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.start_planned_run_request import StartPlannedRunRequest
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
    api_instance = planned_runs_api.PlannedRunsApi(api_client)
    run_id = "runId_example" # str | 
    body = StartPlannedRunRequest(
        instrument_run_id="instrument_run_id_example",
        instrument_run_status="instrument_run_status_example",
        flow_cell_barcode="flow_cell_barcode_example",
        consumables={},
        sample_sheet_name="sample_sheet_name_example",
        run_mode="InstrumentMetrics",
        run_name="run_name_example",
        run_parameters_xml="run_parameters_xml_example",
        run_info_xml="run_info_xml_example",
        instrument_run_number=0,
        description="description_example",
        instrument_software_version="instrument_software_version_example",
        external_location="external_location_example",
    ) # StartPlannedRunRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Start a planned sequencing run.
        api_response = api_instance.start_planned_run(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling PlannedRunsApi->start_planned_run: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start a planned sequencing run.
        api_response = api_instance.start_planned_run(run_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling PlannedRunsApi->start_planned_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |
 **body** | [**StartPlannedRunRequest**](StartPlannedRunRequest.md)|  | [optional]

### Return type

[**SequencingRun**](SequencingRun.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Planned sequencing run started successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Bad request. |  -  |
**409** | Request is invalid due to the current state of the sequencing run. |  -  |
**410** | The sequencing run for the given sequencing run ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlock_planned_run**
> SequencingRun unlock_planned_run(run_id)

Unlock a planned run.

For a given sequencing run ID, unlock the planned run for the current request token.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import planned_runs_api
from ICA_SDK.model.sequencing_run import SequencingRun
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
    api_instance = planned_runs_api.PlannedRunsApi(api_client)
    run_id = "runId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Unlock a planned run.
        api_response = api_instance.unlock_planned_run(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling PlannedRunsApi->unlock_planned_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |

### Return type

[**SequencingRun**](SequencingRun.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sequencing run unlocked successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sequencing run found for given sequencing run ID. |  -  |
**409** | Request is invalid due to current state of the sequencing run. |  -  |
**410** | Sequencing run for the given sequencing run ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_planned_run_config**
> SequencingRun update_planned_run_config(run_id)

Update planned run configuration.

For a given sequencing run ID, update the planned run configuration. Only applicable to runs in planning stage.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import planned_runs_api
from ICA_SDK.model.sequencing_run import SequencingRun
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_sequencing_run_configuration_request import UpdateSequencingRunConfigurationRequest
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
    api_instance = planned_runs_api.PlannedRunsApi(api_client)
    run_id = "runId_example" # str | 
    body = UpdateSequencingRunConfigurationRequest(
        run_name="run_name_example",
        description="description_example",
        regulatory_mode="RUO",
        instrument_type="instrument_type_example",
        instrument_platform="instrument_platform_example",
        num_cycles_read1=0,
        num_cycles_read2=0,
        read_type="Single",
        num_cycles_index1=0,
        num_cycles_index2=0,
        use_custom_primer_for_read1=True,
        use_custom_primer_for_read2=True,
        use_custom_primer_for_index1=True,
        use_custom_primer_for_index2=True,
    ) # UpdateSequencingRunConfigurationRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update planned run configuration.
        api_response = api_instance.update_planned_run_config(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling PlannedRunsApi->update_planned_run_config: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update planned run configuration.
        api_response = api_instance.update_planned_run_config(run_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling PlannedRunsApi->update_planned_run_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |
 **body** | [**UpdateSequencingRunConfigurationRequest**](UpdateSequencingRunConfigurationRequest.md)|  | [optional]

### Return type

[**SequencingRun**](SequencingRun.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Planned run updated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sequencing run found for given sequencing run ID. |  -  |
**410** | Sequencing run with given sequencing run ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

