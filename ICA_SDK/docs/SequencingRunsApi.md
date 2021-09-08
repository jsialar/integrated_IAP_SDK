# ICA_SDK.SequencingRunsApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_sequencing_run**](SequencingRunsApi.md#abort_sequencing_run) | **POST** /v1/sequencing/runs/{runId}:abort | Abort a sequencing run.
[**can_upload**](SequencingRunsApi.md#can_upload) | **GET** /v1/sequencing/runs/{runId}:canUpload | Check whether the run is ready to upload.
[**close_upload_session**](SequencingRunsApi.md#close_upload_session) | **POST** /v1/sequencing/runs/{runId}:closeUploadSession | Close an upload session for a sequencing run
[**complete_upload**](SequencingRunsApi.md#complete_upload) | **POST** /v1/sequencing/runs/{runId}:completeUpload | Complete upload stage for a sequencing run.
[**create_analysis_configuration**](SequencingRunsApi.md#create_analysis_configuration) | **POST** /v1/sequencing/runs/{runId}/analyses | Create an analysis configuration for a sequencing run.
[**delete_analysis_configuration**](SequencingRunsApi.md#delete_analysis_configuration) | **DELETE** /v1/sequencing/runs/analyses/{id} | Delete an analysis configuration for a sequencing run.
[**delete_sequencing_run**](SequencingRunsApi.md#delete_sequencing_run) | **DELETE** /v1/sequencing/runs/{runId} | Delete sequencing run.
[**generate_sample_sheet_for_sequencing_run**](SequencingRunsApi.md#generate_sample_sheet_for_sequencing_run) | **POST** /v1/sequencing/runs/{runId}:generateSampleSheet | Generate sample sheet from a sequencing run.
[**get_sequencing_run**](SequencingRunsApi.md#get_sequencing_run) | **GET** /v1/sequencing/runs/{runId} | Get sequencing run details.
[**get_sequencing_run_contents**](SequencingRunsApi.md#get_sequencing_run_contents) | **GET** /v1/sequencing/runs/{runId}/contents |  Get the content of a sequencing run.
[**get_sequencing_stats**](SequencingRunsApi.md#get_sequencing_stats) | **GET** /v1/sequencing/runs/{runId}/sequencingStats | Get the sequencing stats of a sequencing run.
[**list_analysis_configurations**](SequencingRunsApi.md#list_analysis_configurations) | **GET** /v1/sequencing/runs/{runId}/analyses | List analysis configurations for a sequencing run.
[**list_sequencing_runs**](SequencingRunsApi.md#list_sequencing_runs) | **GET** /v1/sequencing/runs | Get a list of sequencing runs.
[**merge_sequencing_run_acl**](SequencingRunsApi.md#merge_sequencing_run_acl) | **PATCH** /v1/sequencing/runs/{runId}/acl | Merge the access control list of a sequencing run with the input access control list.
[**prepare_requeue**](SequencingRunsApi.md#prepare_requeue) | **POST** /v1/sequencing/runs/{runId}:prepareRequeue | Prepare requeue run.
[**remove_sequencing_run_acl**](SequencingRunsApi.md#remove_sequencing_run_acl) | **DELETE** /v1/sequencing/runs/{runId}/acl | Remove the access control list of a sequencing run.
[**replace_sequencing_run_acl**](SequencingRunsApi.md#replace_sequencing_run_acl) | **PUT** /v1/sequencing/runs/{runId}/acl |  Replace the access control list of a sequencing run with the input access control list.
[**replace_sequencing_stats**](SequencingRunsApi.md#replace_sequencing_stats) | **PUT** /v1/sequencing/runs/{runId}:replaceSequencingStats | Replace the sequencing stats of a sequencing run.
[**run_direct_upload_info**](SequencingRunsApi.md#run_direct_upload_info) | **POST** /v1/sequencing/runs/{runId}/directUploadInfo | Provide information about an uploaded file or set of files.
[**start_requeue**](SequencingRunsApi.md#start_requeue) | **POST** /v1/sequencing/runs/{runId}:startRequeue | Start prepared requeue run.
[**start_run_verification**](SequencingRunsApi.md#start_run_verification) | **POST** /v1/sequencing/runs/{runId}:startVerification | Start verification for a run and return information about that run
[**update_analysis_configuration**](SequencingRunsApi.md#update_analysis_configuration) | **PATCH** /v1/sequencing/runs/analyses/{id} | Update an analysis configuration.
[**update_sequencing_run**](SequencingRunsApi.md#update_sequencing_run) | **PATCH** /v1/sequencing/runs/{runId} | Update information for an existing sequencing run.
[**update_sequencing_run_contents**](SequencingRunsApi.md#update_sequencing_run_contents) | **PUT** /v1/sequencing/runs/{runId}/contents | Update the content of a sequencing run.
[**update_sequencing_run_status**](SequencingRunsApi.md#update_sequencing_run_status) | **POST** /v1/sequencing/runs/{runId}:updateStatus | Update status information for an existing sequencing run.


# **abort_sequencing_run**
> SequencingRun abort_sequencing_run(run_id)

Abort a sequencing run.

For a given sequencing run ID, abort the run.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
from ICA_SDK.model.abort_sequencing_run_request import AbortSequencingRunRequest
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    run_id = "runId_example" # str | 
    body = AbortSequencingRunRequest(
        instrument_run_status="instrument_run_status_example",
        instrument_run_status_summary="instrument_run_status_summary_example",
    ) # AbortSequencingRunRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Abort a sequencing run.
        api_response = api_instance.abort_sequencing_run(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->abort_sequencing_run: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Abort a sequencing run.
        api_response = api_instance.abort_sequencing_run(run_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->abort_sequencing_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |
 **body** | [**AbortSequencingRunRequest**](AbortSequencingRunRequest.md)|  | [optional]

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
**200** | Sequencing run aborted successfully.\&quot; |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sequencing run found for given sequencing run ID. |  -  |
**409** | Request is invalid due to current state of the sequencing run. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **can_upload**
> CanUploadResponse can_upload(run_id)

Check whether the run is ready to upload.

Check the status of the run and returns whether the run is ready to be uploaded.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
from ICA_SDK.model.can_upload_response import CanUploadResponse
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    run_id = "runId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Check whether the run is ready to upload.
        api_response = api_instance.can_upload(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->can_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |

### Return type

[**CanUploadResponse**](CanUploadResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sequencing run is ready to upload. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sequencing run found for given sequencing run ID. |  -  |
**409** | The sequencing run is not in a state where startUpload or refreshUpload is allowed |  -  |
**500** | Internal server error. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_upload_session**
> CloseUploadSessionResponse close_upload_session(run_id)

Close an upload session for a sequencing run

For a given sequencing run ID, close an upload session.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
from ICA_SDK.model.close_run_upload_session_request import CloseRunUploadSessionRequest
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.close_upload_session_response import CloseUploadSessionResponse
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    run_id = "runId_example" # str | 
    body = CloseRunUploadSessionRequest(
        session_id="session_id_example",
        expected_session_file_count=0,
    ) # CloseRunUploadSessionRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Close an upload session for a sequencing run
        api_response = api_instance.close_upload_session(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->close_upload_session: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Close an upload session for a sequencing run
        api_response = api_instance.close_upload_session(run_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->close_upload_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |
 **body** | [**CloseRunUploadSessionRequest**](CloseRunUploadSessionRequest.md)|  | [optional]

### Return type

[**CloseUploadSessionResponse**](CloseUploadSessionResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upload session is closed successfully |  -  |
**400** | An invalid or missing input parameter will result in a bad request. |  -  |
**401** | The acting identity cannot be authenticated and authorized. |  -  |
**403** | The acting identity is not authorized to subscribe to the given event type or deliver to the given delivery target. |  -  |
**404** | No run found for given run ID. |  -  |
**409** | Request is invalid based on the current state of the run. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_upload**
> SequencingRun complete_upload(run_id)

Complete upload stage for a sequencing run.

For a given sequencing run ID, complete the upload stage and close the upload session if provided.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
from ICA_SDK.model.sequencing_run import SequencingRun
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.complete_sequencing_run_upload_request import CompleteSequencingRunUploadRequest
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    run_id = "runId_example" # str | 
    body = CompleteSequencingRunUploadRequest(
        run_upload_status_summary="run_upload_status_summary_example",
        session_id="session_id_example",
        expected_session_file_count=0,
    ) # CompleteSequencingRunUploadRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Complete upload stage for a sequencing run.
        api_response = api_instance.complete_upload(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->complete_upload: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Complete upload stage for a sequencing run.
        api_response = api_instance.complete_upload(run_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->complete_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |
 **body** | [**CompleteSequencingRunUploadRequest**](CompleteSequencingRunUploadRequest.md)|  | [optional]

### Return type

[**SequencingRun**](SequencingRun.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sequencing run upload completed successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sequencing run found for given sequencing run ID. |  -  |
**409** | Request is invalid due to the current state of the sequencing run. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_analysis_configuration**
> SequencingRunAnalysisConfiguration create_analysis_configuration(run_id)

Create an analysis configuration for a sequencing run.

For a given run ID, create an analysis configuration and return information about that analysis configuration.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.create_sequencing_run_analysis_configuration_request import CreateSequencingRunAnalysisConfigurationRequest
from ICA_SDK.model.sequencing_run_analysis_configuration import SequencingRunAnalysisConfiguration
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    run_id = "runId_example" # str | 
    body = CreateSequencingRunAnalysisConfigurationRequest(
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
    ) # CreateSequencingRunAnalysisConfigurationRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an analysis configuration for a sequencing run.
        api_response = api_instance.create_analysis_configuration(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->create_analysis_configuration: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an analysis configuration for a sequencing run.
        api_response = api_instance.create_analysis_configuration(run_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->create_analysis_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |
 **body** | [**CreateSequencingRunAnalysisConfigurationRequest**](CreateSequencingRunAnalysisConfigurationRequest.md)|  | [optional]

### Return type

[**SequencingRunAnalysisConfiguration**](SequencingRunAnalysisConfiguration.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Analysis configuration created successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sequencing run found for given run ID. |  -  |
**409** | Unable to create analysis configuration. Conflict found. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_analysis_configuration**
> delete_analysis_configuration(id)

Delete an analysis configuration for a sequencing run.

For a given run ID, delete an analysis configuration and return information about that analysis configuration.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an analysis configuration for a sequencing run.
        api_instance.delete_analysis_configuration(id)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->delete_analysis_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Analysis configuration deleted successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sequencing run found for given run ID. |  -  |
**409** | Unable to delete analysis configuration. Conflict found. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sequencing_run**
> NoContentResult delete_sequencing_run(run_id)

Delete sequencing run.

For a given sequencing run ID, delete the sequencing run.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.no_content_result import NoContentResult
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    run_id = "runId_example" # str | ID of the sequencing run

    # example passing only required values which don't have defaults set
    try:
        # Delete sequencing run.
        api_response = api_instance.delete_sequencing_run(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->delete_sequencing_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| ID of the sequencing run |

### Return type

[**NoContentResult**](NoContentResult.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Sequencing run deleted successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sequencing run found for given sequencing run ID. |  -  |
**410** | Sequencing run for the given sequencing run ID has already been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_sample_sheet_for_sequencing_run**
> SampleSheet generate_sample_sheet_for_sequencing_run(run_id)

Generate sample sheet from a sequencing run.

Generate sample sheet from a sequencing run, and return the CSV string of sample sheet.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
from ICA_SDK.model.generate_sample_sheet_for_sequencing_run_request import GenerateSampleSheetForSequencingRunRequest
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    run_id = "runId_example" # str | 
    body = GenerateSampleSheetForSequencingRunRequest(
        include=[
            "IncludeFileReferences",
        ],
        exclude_kit_urns=True,
    ) # GenerateSampleSheetForSequencingRunRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Generate sample sheet from a sequencing run.
        api_response = api_instance.generate_sample_sheet_for_sequencing_run(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->generate_sample_sheet_for_sequencing_run: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate sample sheet from a sequencing run.
        api_response = api_instance.generate_sample_sheet_for_sequencing_run(run_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->generate_sample_sheet_for_sequencing_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |
 **body** | [**GenerateSampleSheetForSequencingRunRequest**](GenerateSampleSheetForSequencingRunRequest.md)|  | [optional]

### Return type

[**SampleSheet**](SampleSheet.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sample sheet generated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**409** | Conflict. |  -  |
**410** | Client Error |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sequencing_run**
> SequencingRun get_sequencing_run(run_id)

Get sequencing run details.

For a given sequencing run ID, get the associated run information.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    run_id = "runId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get sequencing run details.
        api_response = api_instance.get_sequencing_run(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->get_sequencing_run: %s\n" % e)
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
**200** | Sequencing run details returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sequencing run found for given sequencing run ID. |  -  |
**410** | The sequencing run for the given sequencing run ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sequencing_run_contents**
> SequencingRunContentsResponse get_sequencing_run_contents(run_id)

 Get the content of a sequencing run.

For a given a run ID, get the content of the sequencing run.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.sequencing_run_contents_response import SequencingRunContentsResponse
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    run_id = "runId_example" # str | ID of the sequencing run
    include = [
        "ReferencedResourceModels",
    ] # [str] | Include flags to specify what is included in the response (optional)

    # example passing only required values which don't have defaults set
    try:
        #  Get the content of a sequencing run.
        api_response = api_instance.get_sequencing_run_contents(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->get_sequencing_run_contents: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        #  Get the content of a sequencing run.
        api_response = api_instance.get_sequencing_run_contents(run_id, include=include)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->get_sequencing_run_contents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| ID of the sequencing run |
 **include** | **[str]**| Include flags to specify what is included in the response | [optional]

### Return type

[**SequencingRunContentsResponse**](SequencingRunContentsResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sequencing run content returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Sequencing run not found for given run ID. |  -  |
**409** | Conflict |  -  |
**410** | The sequencing run for the given run ID has been deleted. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sequencing_stats**
> SequencingStatsResponse get_sequencing_stats(run_id)

Get the sequencing stats of a sequencing run.

For a given a run ID, get the sequencing stats of a sequencing run.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
from ICA_SDK.model.sequencing_stats_response import SequencingStatsResponse
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    run_id = "runId_example" # str | ID of the sequencing run
    include = [
        "ReferencedResourceModels",
    ] # [str] | Include flags to specify what is included in the response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the sequencing stats of a sequencing run.
        api_response = api_instance.get_sequencing_stats(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->get_sequencing_stats: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the sequencing stats of a sequencing run.
        api_response = api_instance.get_sequencing_stats(run_id, include=include)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->get_sequencing_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| ID of the sequencing run |
 **include** | **[str]**| Include flags to specify what is included in the response | [optional]

### Return type

[**SequencingStatsResponse**](SequencingStatsResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sequencing run stats returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Sequencing run not found for given run ID. |  -  |
**410** | The sequencing run for the given run ID has been deleted. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_analysis_configurations**
> SequencingRunAnalysisConfigurationSequencingRunAnalysisConfigurationSortFieldsPagedItems list_analysis_configurations(run_id)

List analysis configurations for a sequencing run.

List analysis configurations for a given run ID.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.sequencing_run_analysis_configuration_sequencing_run_analysis_configuration_sort_fields_paged_items import SequencingRunAnalysisConfigurationSequencingRunAnalysisConfigurationSortFieldsPagedItems
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    run_id = "runId_example" # str | 
    include = [
        "TotalItemCount",
    ] # [str] | Include flags to specify what is included in the request (optional)
    page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) if omitted the server will use the default value of 10
    page_token = "pageToken_example" # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
    sort = "timeCreated asc" # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) if omitted the server will use the default value of "timeCreated asc"

    # example passing only required values which don't have defaults set
    try:
        # List analysis configurations for a sequencing run.
        api_response = api_instance.list_analysis_configurations(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->list_analysis_configurations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List analysis configurations for a sequencing run.
        api_response = api_instance.list_analysis_configurations(run_id, include=include, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->list_analysis_configurations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |
 **include** | **[str]**| Include flags to specify what is included in the request | [optional]
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] if omitted the server will use the default value of 10
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional]
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] if omitted the server will use the default value of "timeCreated asc"

### Return type

[**SequencingRunAnalysisConfigurationSequencingRunAnalysisConfigurationSortFieldsPagedItems**](SequencingRunAnalysisConfigurationSequencingRunAnalysisConfigurationSortFieldsPagedItems.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analysis configurations returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sequencing run found for given run ID. |  -  |
**409** | Unable to list analysis configurations. Conflict found. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sequencing_runs**
> SequencingRunCompactSequencingRunSortFieldsPagedItems list_sequencing_runs()

Get a list of sequencing runs.

Get a list of sequencing runs accessible by the request token.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.sequencing_run_compact_sequencing_run_sort_fields_paged_items import SequencingRunCompactSequencingRunSortFieldsPagedItems
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    is_planned = True # bool | Optional parameter. Set to true to filter the run list and only include planned runs. (optional)
    is_locked = True # bool | Optional parameter. Set to true to filter the run list and only include locked runs. (optional)
    is_favorite = True # bool | Optional parameter. Set to true to filter the run list and only include favorite runs. (optional)
    instrument_type = "instrumentType_example" # str | Optional parameter. Set to true to filter the run list and only include runs performed by the specified instrument type. (optional)
    run_origin = [
        "Instrument",
    ] # [str] | Optional field. Used to filter the sequencing runs list by comma-separated RunOrigins values, e.g.  <example>Instrument,Simulator</example> (optional)
    aggregate_run_status = [
        "Aborted",
    ] # [str] | Optional field. Used to filter the sequencing runs list by comma-separated AggregateRunStatus values, e.g <example>Aborted,Deleted,Running</example> (optional)
    include = [
        "TotalItemCount",
    ] # [str] | Include flags to specify what is included in the response (optional)
    flow_cell_barcode = "flowCellBarcode_example" # str | Filter by flowcell barcode (optional)
    input_container_identifier = "inputContainerIdentifier_example" # str | Filter by Input container identifier (optional)
    regulatory_mode = [
        "RUO",
    ] # [str] | Filter by regulatory modes using comma separated values, e.g <example>RUO,IVD,IUO</example> (optional)
    requeued_from_run_id = "requeuedFromRunId_example" # str | Filter By Requeued Run Id (optional)
    run_name = [
        "runName_example",
    ] # [str] | Filter by name of the sequencing run (optional)
    is_completed = True # bool | Optional parameter. Set to true to filter the run list and only include completed (failed, aborted, successfully completed) runs. (optional)
    include_completed_after_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Optional parameter. Show runs that were completed after the provided Date as well as runs that are not completed (optional)
    include_completed_before_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Optional parameter. Show runs that were completed before the provided Date as well as runs that are not completed (optional)
    tenant_ids = [
        "tenantIds_example",
    ] # [str] | Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids (optional)
    page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) if omitted the server will use the default value of 10
    page_token = "pageToken_example" # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
    sort = "timeCreated asc" # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) if omitted the server will use the default value of "timeCreated asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of sequencing runs.
        api_response = api_instance.list_sequencing_runs(is_planned=is_planned, is_locked=is_locked, is_favorite=is_favorite, instrument_type=instrument_type, run_origin=run_origin, aggregate_run_status=aggregate_run_status, include=include, flow_cell_barcode=flow_cell_barcode, input_container_identifier=input_container_identifier, regulatory_mode=regulatory_mode, requeued_from_run_id=requeued_from_run_id, run_name=run_name, is_completed=is_completed, include_completed_after_date=include_completed_after_date, include_completed_before_date=include_completed_before_date, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->list_sequencing_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_planned** | **bool**| Optional parameter. Set to true to filter the run list and only include planned runs. | [optional]
 **is_locked** | **bool**| Optional parameter. Set to true to filter the run list and only include locked runs. | [optional]
 **is_favorite** | **bool**| Optional parameter. Set to true to filter the run list and only include favorite runs. | [optional]
 **instrument_type** | **str**| Optional parameter. Set to true to filter the run list and only include runs performed by the specified instrument type. | [optional]
 **run_origin** | **[str]**| Optional field. Used to filter the sequencing runs list by comma-separated RunOrigins values, e.g.  &lt;example&gt;Instrument,Simulator&lt;/example&gt; | [optional]
 **aggregate_run_status** | **[str]**| Optional field. Used to filter the sequencing runs list by comma-separated AggregateRunStatus values, e.g &lt;example&gt;Aborted,Deleted,Running&lt;/example&gt; | [optional]
 **include** | **[str]**| Include flags to specify what is included in the response | [optional]
 **flow_cell_barcode** | **str**| Filter by flowcell barcode | [optional]
 **input_container_identifier** | **str**| Filter by Input container identifier | [optional]
 **regulatory_mode** | **[str]**| Filter by regulatory modes using comma separated values, e.g &lt;example&gt;RUO,IVD,IUO&lt;/example&gt; | [optional]
 **requeued_from_run_id** | **str**| Filter By Requeued Run Id | [optional]
 **run_name** | **[str]**| Filter by name of the sequencing run | [optional]
 **is_completed** | **bool**| Optional parameter. Set to true to filter the run list and only include completed (failed, aborted, successfully completed) runs. | [optional]
 **include_completed_after_date** | **datetime**| Optional parameter. Show runs that were completed after the provided Date as well as runs that are not completed | [optional]
 **include_completed_before_date** | **datetime**| Optional parameter. Show runs that were completed before the provided Date as well as runs that are not completed | [optional]
 **tenant_ids** | **[str]**| Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids | [optional]
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] if omitted the server will use the default value of 10
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional]
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] if omitted the server will use the default value of "timeCreated asc"

### Return type

[**SequencingRunCompactSequencingRunSortFieldsPagedItems**](SequencingRunCompactSequencingRunSortFieldsPagedItems.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of sequencing runs returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_sequencing_run_acl**
> SequencingRun merge_sequencing_run_acl(run_id)

Merge the access control list of a sequencing run with the input access control list.

For a given sequencing run, merge the access control list with the input access control list, and return information about the run.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
from ICA_SDK.model.sequencing_run import SequencingRun
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_acl_request import UpdateAclRequest
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    run_id = "runId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Merge the access control list of a sequencing run with the input access control list.
        api_response = api_instance.merge_sequencing_run_acl(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->merge_sequencing_run_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Merge the access control list of a sequencing run with the input access control list.
        api_response = api_instance.merge_sequencing_run_acl(run_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->merge_sequencing_run_acl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional]

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
**200** | Access control list updated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sequencing run found for given sequencing run ID. |  -  |
**410** | The sequencing run with the given sequencing run ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prepare_requeue**
> SequencingRun prepare_requeue(run_id)

Prepare requeue run.

Prepare requeue analysis of the same or different sequencing run with potentially different run content/analysis.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
from ICA_SDK.model.requeue_sequencing_run_analysis_request import RequeueSequencingRunAnalysisRequest
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    run_id = "runId_example" # str | 
    body = RequeueSequencingRunAnalysisRequest(
        run_name="run_name_example",
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
        requeue_reason="requeue_reason_example",
        replace_existing_run_requeue=True,
    ) # RequeueSequencingRunAnalysisRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Prepare requeue run.
        api_response = api_instance.prepare_requeue(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->prepare_requeue: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Prepare requeue run.
        api_response = api_instance.prepare_requeue(run_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->prepare_requeue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |
 **body** | [**RequeueSequencingRunAnalysisRequest**](RequeueSequencingRunAnalysisRequest.md)|  | [optional]

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
**201** | Prepared run requeue successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | NotFound. |  -  |
**409** | Conflict. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_sequencing_run_acl**
> SequencingRun remove_sequencing_run_acl(run_id)

Remove the access control list of a sequencing run.

Remove the access control list of a given sequencing run, and return information about the run.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
from ICA_SDK.model.sequencing_run import SequencingRun
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_acl_request import UpdateAclRequest
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    run_id = "runId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove the access control list of a sequencing run.
        api_response = api_instance.remove_sequencing_run_acl(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->remove_sequencing_run_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove the access control list of a sequencing run.
        api_response = api_instance.remove_sequencing_run_acl(run_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->remove_sequencing_run_acl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional]

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
**200** | Input access control list removed successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sequencing run found for given sequencing run ID. |  -  |
**410** | The sequencing run with the given sequencing run ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_sequencing_run_acl**
> SequencingRun replace_sequencing_run_acl(run_id)

 Replace the access control list of a sequencing run with the input access control list.

For a given sequencing run, replace the access control list with the input access control list, and return information about the run.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
from ICA_SDK.model.sequencing_run import SequencingRun
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_acl_request import UpdateAclRequest
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    run_id = "runId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        #  Replace the access control list of a sequencing run with the input access control list.
        api_response = api_instance.replace_sequencing_run_acl(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->replace_sequencing_run_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        #  Replace the access control list of a sequencing run with the input access control list.
        api_response = api_instance.replace_sequencing_run_acl(run_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->replace_sequencing_run_acl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional]

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
**200** | Access control list updated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sequencing run found for given sequencing run ID. |  -  |
**410** | The sequencing run with the given sequencing run ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_sequencing_stats**
> SequencingStatsResponse replace_sequencing_stats(run_id)

Replace the sequencing stats of a sequencing run.

Replace the sequencing stats of a sequencing run. Any existing sequencing stats will be deleted and replaced with the new contents of this request.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
from ICA_SDK.model.sequencing_stats_response import SequencingStatsResponse
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.replace_sequencing_stats_request import ReplaceSequencingStatsRequest
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    run_id = "runId_example" # str | 
    body = ReplaceSequencingStatsRequest(
        cycle_number=1,
        run_sequencing_stats=RunSequencingStats(
            num_cycles_index1=1,
            num_cycles_index2=1,
            num_cycles_read1=1,
            num_cycles_read2=1,
            num_lanes=1,
            num_reads=1,
            num_surfaces=1,
            num_swaths_per_lane=1,
            num_tiles_per_swath=1,
            error_rate=3.14,
            error_rate_r1=3.14,
            error_rate_r2=3.14,
            intensity_cycle1=3.14,
            is_indexed=True,
            max_cycle_called=1,
            max_cycle_extracted=1,
            max_cycle_scored=1,
            min_cycle_called=1,
            min_cycle_extracted=1,
            min_cycle_scored=1,
            non_indexed_error_rate=3.14,
            non_indexed_intensity_cycle1=3.14,
            non_indexed_percent_aligned=3.14,
            non_indexed_percent_gt_q30=3.14,
            non_indexed_projected_total_yield=3.14,
            non_indexed_yield_total=3.14,
            percent_aligned=3.14,
            percent_gt_q30=3.14,
            percent_gt_q30_last10_cycles=3.14,
            percent_gt_q30_r1=3.14,
            percent_gt_q30_r2=3.14,
            percent_pf=3.14,
            percent_resynthesis=3.14,
            phasing_r1=3.14,
            phasing_r2=3.14,
            pre_phasing_r1=3.14,
            pre_phasing_r2=3.14,
            projected_total_yield=3.14,
            reads_pf_total=1,
            reads_total=1,
            yield_total=3.14,
            clusters=1,
            clusters_pf=1,
            cluster_density=3.14,
            occupancy=3.14,
            percent_loading_concentration=3.14,
        ),
        lane_sequencing_stats=[
            LaneSequencingStats(
                lane_number=1,
                density=3.14,
                percent_pf=3.14,
                phasing=3.14,
                pre_phasing=3.14,
                reads=1,
                reads_pf=1,
                percent_gt_q30=3.14,
                percent_gt_q30_last10_cycles=3.14,
                _yield=3.14,
                max_cycle_called=1,
                percent_aligned=3.14,
                error_rate=3.14,
                error_rate35=3.14,
                error_rate50=3.14,
                error_rate75=3.14,
                error_rate100=3.14,
                intensity_cycle1=3.14,
                projected_yield_in_gbp=3.14,
                max_projected_yield_in_gbp=3.14,
                phasing_slope=3.14,
                phasing_offset=3.14,
                pre_phasing_slope=3.14,
                pre_phasing_offset=3.14,
            ),
        ],
        read_sequencing_stats=[
            ReadSequencingStats(
                read_number=1,
                is_indexed=True,
                total_cycles=1,
                yield_total=3.14,
                projected_total_yield=3.14,
                percent_aligned=3.14,
                error_rate=3.14,
                intensity_cycle1=3.14,
                percent_gt_q30=3.14,
                percent_gt_q30_last10_cycles=3.14,
            ),
        ],
        lane_by_read_sequencing_stats=[
            LaneByReadSequencingStats(
                lane_number=1,
                read_number=1,
                tile_count=1,
                density=3.14,
                density_deviation=3.14,
                percent_pf=3.14,
                percent_pf_deviation=3.14,
                phasing=3.14,
                pre_phasing=3.14,
                reads=1,
                reads_pf=1,
                percent_gt_q30=3.14,
                percent_gt_q30_last10_cycles=3.14,
                _yield=3.14,
                min_cycle_called=1,
                max_cycle_called=1,
                percent_aligned=3.14,
                percent_aligned_deviation=3.14,
                error_rate=3.14,
                error_rate_deviation=3.14,
                error_rate35=3.14,
                error_rate35_deviation=3.14,
                error_rate50=3.14,
                error_rate50_deviation=3.14,
                error_rate75=3.14,
                error_rate75_deviation=3.14,
                error_rate100=3.14,
                error_rate100_deviation=3.14,
                intensity_cycle1=3.14,
                intensity_cycle1_deviation=3.14,
                min_cycle_error=1,
                max_cycle_error=1,
                phasing_slope=3.14,
                phasing_offset=3.14,
                pre_phasing_slope=3.14,
                pre_phasing_offset=3.14,
                percent_no_calls=3.14,
                cluster_density=3.14,
                occupancy=3.14,
            ),
        ],
    ) # ReplaceSequencingStatsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Replace the sequencing stats of a sequencing run.
        api_response = api_instance.replace_sequencing_stats(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->replace_sequencing_stats: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Replace the sequencing stats of a sequencing run.
        api_response = api_instance.replace_sequencing_stats(run_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->replace_sequencing_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |
 **body** | [**ReplaceSequencingStatsRequest**](ReplaceSequencingStatsRequest.md)|  | [optional]

### Return type

[**SequencingStatsResponse**](SequencingStatsResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Sequencing stats replaced successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**409** | Conflict. |  -  |
**410** | The sequencing run for the given run ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_direct_upload_info**
> SequencingRunCompact run_direct_upload_info(run_id)

Provide information about an uploaded file or set of files.

For a given sequencing run ID, provide information about an uploaded file or set of files.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.run_direct_upload_info_request import RunDirectUploadInfoRequest
from ICA_SDK.model.sequencing_run_compact import SequencingRunCompact
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    run_id = "runId_example" # str | 
    body = RunDirectUploadInfoRequest(
        files=[
            DirectUploadFileInfo(
                file_name="file_name_example",
                relative_path="relative_path_example",
                file_id="file_id_example",
                file_urn="file_urn_example",
            ),
        ],
    ) # RunDirectUploadInfoRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Provide information about an uploaded file or set of files.
        api_response = api_instance.run_direct_upload_info(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->run_direct_upload_info: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Provide information about an uploaded file or set of files.
        api_response = api_instance.run_direct_upload_info(run_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->run_direct_upload_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |
 **body** | [**RunDirectUploadInfoRequest**](RunDirectUploadInfoRequest.md)|  | [optional]

### Return type

[**SequencingRunCompact**](SequencingRunCompact.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upload information captured successfully. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sequencing run found for given sequencing run ID. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_requeue**
> SequencingRun start_requeue(run_id)

Start prepared requeue run.

Starts previously prepared requeue run for analysis.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    run_id = "runId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Start prepared requeue run.
        api_response = api_instance.start_requeue(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->start_requeue: %s\n" % e)
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
**200** | Starts requeue run successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | NotFound. |  -  |
**409** | Conflict. |  -  |
**410** | Client Error |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_run_verification**
> RunVerificationResult start_run_verification(run_id)

Start verification for a run and return information about that run

Start run verification

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
from ICA_SDK.model.start_verification_request import StartVerificationRequest
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.run_verification_result import RunVerificationResult
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    run_id = "runId_example" # str | 
    body = StartVerificationRequest(
        flowcell_type="flowcell_type_example",
        sequencing_run_space_required_in_gb=3.14,
    ) # StartVerificationRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Start verification for a run and return information about that run
        api_response = api_instance.start_run_verification(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->start_run_verification: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start verification for a run and return information about that run
        api_response = api_instance.start_run_verification(run_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->start_run_verification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |
 **body** | [**StartVerificationRequest**](StartVerificationRequest.md)|  | [optional]

### Return type

[**RunVerificationResult**](RunVerificationResult.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Verification is started successfully |  -  |
**400** | An invalid or missing input parameter will result in a bad request. |  -  |
**401** | The acting identity cannot be authenticated and authorized. |  -  |
**403** | The acting identity is not authorized to perform the action. |  -  |
**409** | Request is invalid based on the current state of the run |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_analysis_configuration**
> SequencingRunAnalysisConfiguration update_analysis_configuration(id)

Update an analysis configuration.

Update an analysis configuration, and return information about that analysis configuration.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_sequencing_run_analysis_configuration_request import UpdateSequencingRunAnalysisConfigurationRequest
from ICA_SDK.model.sequencing_run_analysis_configuration import SequencingRunAnalysisConfiguration
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    id = "id_example" # str | 
    body = UpdateSequencingRunAnalysisConfigurationRequest(
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
    ) # UpdateSequencingRunAnalysisConfigurationRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an analysis configuration.
        api_response = api_instance.update_analysis_configuration(id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->update_analysis_configuration: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an analysis configuration.
        api_response = api_instance.update_analysis_configuration(id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->update_analysis_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **body** | [**UpdateSequencingRunAnalysisConfigurationRequest**](UpdateSequencingRunAnalysisConfigurationRequest.md)|  | [optional]

### Return type

[**SequencingRunAnalysisConfiguration**](SequencingRunAnalysisConfiguration.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analysis configuration updated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No analysis configuration found for given ID. |  -  |
**409** | Analysis configuration not updated due to conflict with input parameters. |  -  |
**410** | Client Error |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sequencing_run**
> SequencingRun update_sequencing_run(run_id)

Update information for an existing sequencing run.

Update information for an existing sequencing run. This may include metadata, status, progress (started/completed/failed), and flags.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
from ICA_SDK.model.sequencing_run import SequencingRun
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_sequencing_run_request import UpdateSequencingRunRequest
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    run_id = "runId_example" # str | 
    body = UpdateSequencingRunRequest(
        run_name="run_name_example",
        description="description_example",
        prep_kit_info=SequencingRunPrepKitInfo(
            library_prep_kit_names="library_prep_kit_names_example",
            num_samples=1,
            lanes=[
                LanePrepKitInfo(
                    lane_number=1,
                    kits=[
                        LibraryPrepKitAndIndexAdapterKitName(
                            library_prep_kit_name="library_prep_kit_name_example",
                            index_adapter_kit_name="index_adapter_kit_name_example",
                        ),
                    ],
                ),
            ],
        ),
        flow_cell_barcode="flow_cell_barcode_example",
        input_container_identifier="input_container_identifier_example",
        consumables={},
        sample_sheet_name="sample_sheet_name_example",
        is_favorite=True,
        acl=[
            "acl_example",
        ],
    ) # UpdateSequencingRunRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update information for an existing sequencing run.
        api_response = api_instance.update_sequencing_run(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->update_sequencing_run: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update information for an existing sequencing run.
        api_response = api_instance.update_sequencing_run(run_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->update_sequencing_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |
 **body** | [**UpdateSequencingRunRequest**](UpdateSequencingRunRequest.md)|  | [optional]

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
**200** | Sequencing run updated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sequencing run found for given sequencing run ID. |  -  |
**409** | Request is invalid due to current state of the sequencing run. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sequencing_run_contents**
> SequencingRunContentsResponse update_sequencing_run_contents(run_id)

Update the content of a sequencing run.

For a given a run ID, update the sequencing run content with the current tokenâ€™s tenant ID.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.sequencing_run_contents_response import SequencingRunContentsResponse
from ICA_SDK.model.update_sequencing_run_contents_request import UpdateSequencingRunContentsRequest
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    run_id = "runId_example" # str | 
    body = UpdateSequencingRunContentsRequest(
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
    ) # UpdateSequencingRunContentsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the content of a sequencing run.
        api_response = api_instance.update_sequencing_run_contents(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->update_sequencing_run_contents: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the content of a sequencing run.
        api_response = api_instance.update_sequencing_run_contents(run_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->update_sequencing_run_contents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |
 **body** | [**UpdateSequencingRunContentsRequest**](UpdateSequencingRunContentsRequest.md)|  | [optional]

### Return type

[**SequencingRunContentsResponse**](SequencingRunContentsResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SequencingRun content for the given runId is updated successfully. |  -  |
**400** | An invalid or missing input parameter will result in a bad request. |  -  |
**401** | The acting identity cannot be authenticated and authorized. |  -  |
**403** | The acting identity is not authorized to update the SequencingRun content for the given runId. |  -  |
**404** | Could not find a SequencingRun for the given runId. |  -  |
**409** | The sequencing run content update request is invalid based on the current state of the sequencing run |  -  |
**410** | The SequencingRun for the given runId has been deleted. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sequencing_run_status**
> SequencingRun update_sequencing_run_status(run_id)

Update status information for an existing sequencing run.

Update status information for an existing sequencing run. This may include status, progress (started/completed/failed), and flags.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import sequencing_runs_api
from ICA_SDK.model.update_sequencing_run_status_request import UpdateSequencingRunStatusRequest
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
    api_instance = sequencing_runs_api.SequencingRunsApi(api_client)
    run_id = "runId_example" # str | 
    body = UpdateSequencingRunStatusRequest(
        verification_status="verification_status_example",
        verification_status_summary="verification_status_summary_example",
        instrument_run_status="instrument_run_status_example",
        instrument_run_status_summary="instrument_run_status_summary_example",
        instrument_analysis_status="instrument_analysis_status_example",
        instrument_analysis_status_summary="instrument_analysis_status_summary_example",
        upload_status_summary="upload_status_summary_example",
        verification_progress="Started",
        instrument_progress="Started",
        sequencing_progress="Started",
        instrument_analysis_progress="Started",
        upload_progress="Started",
        failure_reason="failure_reason_example",
        needs_attention=True,
        needs_attention_reason="needs_attention_reason_example",
    ) # UpdateSequencingRunStatusRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update status information for an existing sequencing run.
        api_response = api_instance.update_sequencing_run_status(run_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->update_sequencing_run_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update status information for an existing sequencing run.
        api_response = api_instance.update_sequencing_run_status(run_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling SequencingRunsApi->update_sequencing_run_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |
 **body** | [**UpdateSequencingRunStatusRequest**](UpdateSequencingRunStatusRequest.md)|  | [optional]

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
**200** | Sequencing run status updated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No sequencing run found for given sequencing run ID. |  -  |
**409** | Request is invalid due to current state of the sequencing run. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

