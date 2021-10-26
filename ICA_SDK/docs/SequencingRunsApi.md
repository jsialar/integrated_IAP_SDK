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
> SequencingRun abort_sequencing_run(run_id, body=body)

Abort a sequencing run.

For a given sequencing run ID, abort the run.

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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.AbortSequencingRunRequest() # AbortSequencingRunRequest |  (optional)

    try:
        # Abort a sequencing run.
        api_response = api_instance.abort_sequencing_run(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->abort_sequencing_run: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.AbortSequencingRunRequest() # AbortSequencingRunRequest |  (optional)

    try:
        # Abort a sequencing run.
        api_response = api_instance.abort_sequencing_run(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 

    try:
        # Check whether the run is ready to upload.
        api_response = api_instance.can_upload(run_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->can_upload: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 

    try:
        # Check whether the run is ready to upload.
        api_response = api_instance.can_upload(run_id)
        pprint(api_response)
    except ApiException as e:
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
> CloseUploadSessionResponse close_upload_session(run_id, body=body)

Close an upload session for a sequencing run

For a given sequencing run ID, close an upload session.

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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.CloseRunUploadSessionRequest() # CloseRunUploadSessionRequest |  (optional)

    try:
        # Close an upload session for a sequencing run
        api_response = api_instance.close_upload_session(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->close_upload_session: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.CloseRunUploadSessionRequest() # CloseRunUploadSessionRequest |  (optional)

    try:
        # Close an upload session for a sequencing run
        api_response = api_instance.close_upload_session(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
> SequencingRun complete_upload(run_id, body=body)

Complete upload stage for a sequencing run.

For a given sequencing run ID, complete the upload stage and close the upload session if provided.

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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.CompleteSequencingRunUploadRequest() # CompleteSequencingRunUploadRequest |  (optional)

    try:
        # Complete upload stage for a sequencing run.
        api_response = api_instance.complete_upload(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->complete_upload: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.CompleteSequencingRunUploadRequest() # CompleteSequencingRunUploadRequest |  (optional)

    try:
        # Complete upload stage for a sequencing run.
        api_response = api_instance.complete_upload(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
> SequencingRunAnalysisConfiguration create_analysis_configuration(run_id, body=body)

Create an analysis configuration for a sequencing run.

For a given run ID, create an analysis configuration and return information about that analysis configuration.

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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.CreateSequencingRunAnalysisConfigurationRequest() # CreateSequencingRunAnalysisConfigurationRequest |  (optional)

    try:
        # Create an analysis configuration for a sequencing run.
        api_response = api_instance.create_analysis_configuration(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->create_analysis_configuration: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.CreateSequencingRunAnalysisConfigurationRequest() # CreateSequencingRunAnalysisConfigurationRequest |  (optional)

    try:
        # Create an analysis configuration for a sequencing run.
        api_response = api_instance.create_analysis_configuration(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete an analysis configuration for a sequencing run.
        api_instance.delete_analysis_configuration(id)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->delete_analysis_configuration: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete an analysis configuration for a sequencing run.
        api_instance.delete_analysis_configuration(id)
    except ApiException as e:
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | ID of the sequencing run

    try:
        # Delete sequencing run.
        api_response = api_instance.delete_sequencing_run(run_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->delete_sequencing_run: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | ID of the sequencing run

    try:
        # Delete sequencing run.
        api_response = api_instance.delete_sequencing_run(run_id)
        pprint(api_response)
    except ApiException as e:
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
> SampleSheet generate_sample_sheet_for_sequencing_run(run_id, body=body)

Generate sample sheet from a sequencing run.

Generate sample sheet from a sequencing run, and return the CSV string of sample sheet.

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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.GenerateSampleSheetForSequencingRunRequest() # GenerateSampleSheetForSequencingRunRequest |  (optional)

    try:
        # Generate sample sheet from a sequencing run.
        api_response = api_instance.generate_sample_sheet_for_sequencing_run(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->generate_sample_sheet_for_sequencing_run: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.GenerateSampleSheetForSequencingRunRequest() # GenerateSampleSheetForSequencingRunRequest |  (optional)

    try:
        # Generate sample sheet from a sequencing run.
        api_response = api_instance.generate_sample_sheet_for_sequencing_run(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 

    try:
        # Get sequencing run details.
        api_response = api_instance.get_sequencing_run(run_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->get_sequencing_run: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 

    try:
        # Get sequencing run details.
        api_response = api_instance.get_sequencing_run(run_id)
        pprint(api_response)
    except ApiException as e:
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
> SequencingRunContentsResponse get_sequencing_run_contents(run_id, include=include)

 Get the content of a sequencing run.

For a given a run ID, get the content of the sequencing run.

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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | ID of the sequencing run
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)

    try:
        #  Get the content of a sequencing run.
        api_response = api_instance.get_sequencing_run_contents(run_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->get_sequencing_run_contents: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | ID of the sequencing run
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)

    try:
        #  Get the content of a sequencing run.
        api_response = api_instance.get_sequencing_run_contents(run_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->get_sequencing_run_contents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| ID of the sequencing run | 
 **include** | [**list[str]**](str.md)| Include flags to specify what is included in the response | [optional] 

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
> SequencingStatsResponse get_sequencing_stats(run_id, include=include)

Get the sequencing stats of a sequencing run.

For a given a run ID, get the sequencing stats of a sequencing run.

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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | ID of the sequencing run
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)

    try:
        # Get the sequencing stats of a sequencing run.
        api_response = api_instance.get_sequencing_stats(run_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->get_sequencing_stats: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | ID of the sequencing run
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)

    try:
        # Get the sequencing stats of a sequencing run.
        api_response = api_instance.get_sequencing_stats(run_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->get_sequencing_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| ID of the sequencing run | 
 **include** | [**list[str]**](str.md)| Include flags to specify what is included in the response | [optional] 

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
> SequencingRunAnalysisConfigurationSequencingRunAnalysisConfigurationSortFieldsPagedItems list_analysis_configurations(run_id, include=include, page_size=page_size, page_token=page_token, sort=sort)

List analysis configurations for a sequencing run.

List analysis configurations for a given run ID.

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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
include = ['include_example'] # list[str] | Include flags to specify what is included in the request (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to 'timeCreated asc')

    try:
        # List analysis configurations for a sequencing run.
        api_response = api_instance.list_analysis_configurations(run_id, include=include, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->list_analysis_configurations: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
include = ['include_example'] # list[str] | Include flags to specify what is included in the request (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to 'timeCreated asc')

    try:
        # List analysis configurations for a sequencing run.
        api_response = api_instance.list_analysis_configurations(run_id, include=include, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->list_analysis_configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 
 **include** | [**list[str]**](str.md)| Include flags to specify what is included in the request | [optional] 
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] [default to 10]
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional] 
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] [default to &#39;timeCreated asc&#39;]

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
> SequencingRunCompactSequencingRunSortFieldsPagedItems list_sequencing_runs(is_planned=is_planned, is_locked=is_locked, is_favorite=is_favorite, instrument_type=instrument_type, run_origin=run_origin, aggregate_run_status=aggregate_run_status, include=include, flow_cell_barcode=flow_cell_barcode, input_container_identifier=input_container_identifier, regulatory_mode=regulatory_mode, requeued_from_run_id=requeued_from_run_id, run_name=run_name, is_completed=is_completed, include_completed_after_date=include_completed_after_date, include_completed_before_date=include_completed_before_date, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)

Get a list of sequencing runs.

Get a list of sequencing runs accessible by the request token.

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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    is_planned = True # bool | Optional parameter. Set to true to filter the run list and only include planned runs. (optional)
is_locked = True # bool | Optional parameter. Set to true to filter the run list and only include locked runs. (optional)
is_favorite = True # bool | Optional parameter. Set to true to filter the run list and only include favorite runs. (optional)
instrument_type = 'instrument_type_example' # str | Optional parameter. Set to true to filter the run list and only include runs performed by the specified instrument type. (optional)
run_origin = ['run_origin_example'] # list[str] | Optional field. Used to filter the sequencing runs list by comma-separated RunOrigins values, e.g.  <example>Instrument,Simulator</example> (optional)
aggregate_run_status = ['aggregate_run_status_example'] # list[str] | Optional field. Used to filter the sequencing runs list by comma-separated AggregateRunStatus values, e.g <example>Aborted,Deleted,Running</example> (optional)
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)
flow_cell_barcode = 'flow_cell_barcode_example' # str | Filter by flowcell barcode (optional)
input_container_identifier = 'input_container_identifier_example' # str | Filter by Input container identifier (optional)
regulatory_mode = ['regulatory_mode_example'] # list[str] | Filter by regulatory modes using comma separated values, e.g <example>RUO,IVD,IUO</example> (optional)
requeued_from_run_id = 'requeued_from_run_id_example' # str | Filter By Requeued Run Id (optional)
run_name = ['run_name_example'] # list[str] | Filter by name of the sequencing run (optional)
is_completed = True # bool | Optional parameter. Set to true to filter the run list and only include completed (failed, aborted, successfully completed) runs. (optional)
include_completed_after_date = '2013-10-20T19:20:30+01:00' # datetime | Optional parameter. Show runs that were completed after the provided Date as well as runs that are not completed (optional)
include_completed_before_date = '2013-10-20T19:20:30+01:00' # datetime | Optional parameter. Show runs that were completed before the provided Date as well as runs that are not completed (optional)
tenant_ids = ['tenant_ids_example'] # list[str] | Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to 'timeCreated asc')

    try:
        # Get a list of sequencing runs.
        api_response = api_instance.list_sequencing_runs(is_planned=is_planned, is_locked=is_locked, is_favorite=is_favorite, instrument_type=instrument_type, run_origin=run_origin, aggregate_run_status=aggregate_run_status, include=include, flow_cell_barcode=flow_cell_barcode, input_container_identifier=input_container_identifier, regulatory_mode=regulatory_mode, requeued_from_run_id=requeued_from_run_id, run_name=run_name, is_completed=is_completed, include_completed_after_date=include_completed_after_date, include_completed_before_date=include_completed_before_date, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->list_sequencing_runs: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    is_planned = True # bool | Optional parameter. Set to true to filter the run list and only include planned runs. (optional)
is_locked = True # bool | Optional parameter. Set to true to filter the run list and only include locked runs. (optional)
is_favorite = True # bool | Optional parameter. Set to true to filter the run list and only include favorite runs. (optional)
instrument_type = 'instrument_type_example' # str | Optional parameter. Set to true to filter the run list and only include runs performed by the specified instrument type. (optional)
run_origin = ['run_origin_example'] # list[str] | Optional field. Used to filter the sequencing runs list by comma-separated RunOrigins values, e.g.  <example>Instrument,Simulator</example> (optional)
aggregate_run_status = ['aggregate_run_status_example'] # list[str] | Optional field. Used to filter the sequencing runs list by comma-separated AggregateRunStatus values, e.g <example>Aborted,Deleted,Running</example> (optional)
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)
flow_cell_barcode = 'flow_cell_barcode_example' # str | Filter by flowcell barcode (optional)
input_container_identifier = 'input_container_identifier_example' # str | Filter by Input container identifier (optional)
regulatory_mode = ['regulatory_mode_example'] # list[str] | Filter by regulatory modes using comma separated values, e.g <example>RUO,IVD,IUO</example> (optional)
requeued_from_run_id = 'requeued_from_run_id_example' # str | Filter By Requeued Run Id (optional)
run_name = ['run_name_example'] # list[str] | Filter by name of the sequencing run (optional)
is_completed = True # bool | Optional parameter. Set to true to filter the run list and only include completed (failed, aborted, successfully completed) runs. (optional)
include_completed_after_date = '2013-10-20T19:20:30+01:00' # datetime | Optional parameter. Show runs that were completed after the provided Date as well as runs that are not completed (optional)
include_completed_before_date = '2013-10-20T19:20:30+01:00' # datetime | Optional parameter. Show runs that were completed before the provided Date as well as runs that are not completed (optional)
tenant_ids = ['tenant_ids_example'] # list[str] | Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to 'timeCreated asc')

    try:
        # Get a list of sequencing runs.
        api_response = api_instance.list_sequencing_runs(is_planned=is_planned, is_locked=is_locked, is_favorite=is_favorite, instrument_type=instrument_type, run_origin=run_origin, aggregate_run_status=aggregate_run_status, include=include, flow_cell_barcode=flow_cell_barcode, input_container_identifier=input_container_identifier, regulatory_mode=regulatory_mode, requeued_from_run_id=requeued_from_run_id, run_name=run_name, is_completed=is_completed, include_completed_after_date=include_completed_after_date, include_completed_before_date=include_completed_before_date, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->list_sequencing_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_planned** | **bool**| Optional parameter. Set to true to filter the run list and only include planned runs. | [optional] 
 **is_locked** | **bool**| Optional parameter. Set to true to filter the run list and only include locked runs. | [optional] 
 **is_favorite** | **bool**| Optional parameter. Set to true to filter the run list and only include favorite runs. | [optional] 
 **instrument_type** | **str**| Optional parameter. Set to true to filter the run list and only include runs performed by the specified instrument type. | [optional] 
 **run_origin** | [**list[str]**](str.md)| Optional field. Used to filter the sequencing runs list by comma-separated RunOrigins values, e.g.  &lt;example&gt;Instrument,Simulator&lt;/example&gt; | [optional] 
 **aggregate_run_status** | [**list[str]**](str.md)| Optional field. Used to filter the sequencing runs list by comma-separated AggregateRunStatus values, e.g &lt;example&gt;Aborted,Deleted,Running&lt;/example&gt; | [optional] 
 **include** | [**list[str]**](str.md)| Include flags to specify what is included in the response | [optional] 
 **flow_cell_barcode** | **str**| Filter by flowcell barcode | [optional] 
 **input_container_identifier** | **str**| Filter by Input container identifier | [optional] 
 **regulatory_mode** | [**list[str]**](str.md)| Filter by regulatory modes using comma separated values, e.g &lt;example&gt;RUO,IVD,IUO&lt;/example&gt; | [optional] 
 **requeued_from_run_id** | **str**| Filter By Requeued Run Id | [optional] 
 **run_name** | [**list[str]**](str.md)| Filter by name of the sequencing run | [optional] 
 **is_completed** | **bool**| Optional parameter. Set to true to filter the run list and only include completed (failed, aborted, successfully completed) runs. | [optional] 
 **include_completed_after_date** | **datetime**| Optional parameter. Show runs that were completed after the provided Date as well as runs that are not completed | [optional] 
 **include_completed_before_date** | **datetime**| Optional parameter. Show runs that were completed before the provided Date as well as runs that are not completed | [optional] 
 **tenant_ids** | [**list[str]**](str.md)| Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids | [optional] 
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] [default to 10]
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional] 
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] [default to &#39;timeCreated asc&#39;]

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
> SequencingRun merge_sequencing_run_acl(run_id, body=body)

Merge the access control list of a sequencing run with the input access control list.

For a given sequencing run, merge the access control list with the input access control list, and return information about the run.

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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Merge the access control list of a sequencing run with the input access control list.
        api_response = api_instance.merge_sequencing_run_acl(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->merge_sequencing_run_acl: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Merge the access control list of a sequencing run with the input access control list.
        api_response = api_instance.merge_sequencing_run_acl(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
> SequencingRun prepare_requeue(run_id, body=body)

Prepare requeue run.

Prepare requeue analysis of the same or different sequencing run with potentially different run content/analysis.

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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.RequeueSequencingRunAnalysisRequest() # RequeueSequencingRunAnalysisRequest |  (optional)

    try:
        # Prepare requeue run.
        api_response = api_instance.prepare_requeue(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->prepare_requeue: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.RequeueSequencingRunAnalysisRequest() # RequeueSequencingRunAnalysisRequest |  (optional)

    try:
        # Prepare requeue run.
        api_response = api_instance.prepare_requeue(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
> SequencingRun remove_sequencing_run_acl(run_id, body=body)

Remove the access control list of a sequencing run.

Remove the access control list of a given sequencing run, and return information about the run.

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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Remove the access control list of a sequencing run.
        api_response = api_instance.remove_sequencing_run_acl(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->remove_sequencing_run_acl: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Remove the access control list of a sequencing run.
        api_response = api_instance.remove_sequencing_run_acl(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
> SequencingRun replace_sequencing_run_acl(run_id, body=body)

 Replace the access control list of a sequencing run with the input access control list.

For a given sequencing run, replace the access control list with the input access control list, and return information about the run.

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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        #  Replace the access control list of a sequencing run with the input access control list.
        api_response = api_instance.replace_sequencing_run_acl(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->replace_sequencing_run_acl: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        #  Replace the access control list of a sequencing run with the input access control list.
        api_response = api_instance.replace_sequencing_run_acl(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
> SequencingStatsResponse replace_sequencing_stats(run_id, body=body)

Replace the sequencing stats of a sequencing run.

Replace the sequencing stats of a sequencing run. Any existing sequencing stats will be deleted and replaced with the new contents of this request.

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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.ReplaceSequencingStatsRequest() # ReplaceSequencingStatsRequest |  (optional)

    try:
        # Replace the sequencing stats of a sequencing run.
        api_response = api_instance.replace_sequencing_stats(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->replace_sequencing_stats: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.ReplaceSequencingStatsRequest() # ReplaceSequencingStatsRequest |  (optional)

    try:
        # Replace the sequencing stats of a sequencing run.
        api_response = api_instance.replace_sequencing_stats(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
> SequencingRunCompact run_direct_upload_info(run_id, body=body)

Provide information about an uploaded file or set of files.

For a given sequencing run ID, provide information about an uploaded file or set of files.

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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.RunDirectUploadInfoRequest() # RunDirectUploadInfoRequest |  (optional)

    try:
        # Provide information about an uploaded file or set of files.
        api_response = api_instance.run_direct_upload_info(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->run_direct_upload_info: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.RunDirectUploadInfoRequest() # RunDirectUploadInfoRequest |  (optional)

    try:
        # Provide information about an uploaded file or set of files.
        api_response = api_instance.run_direct_upload_info(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 

    try:
        # Start prepared requeue run.
        api_response = api_instance.start_requeue(run_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->start_requeue: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 

    try:
        # Start prepared requeue run.
        api_response = api_instance.start_requeue(run_id)
        pprint(api_response)
    except ApiException as e:
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
> RunVerificationResult start_run_verification(run_id, body=body)

Start verification for a run and return information about that run

Start run verification

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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.StartVerificationRequest() # StartVerificationRequest |  (optional)

    try:
        # Start verification for a run and return information about that run
        api_response = api_instance.start_run_verification(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->start_run_verification: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.StartVerificationRequest() # StartVerificationRequest |  (optional)

    try:
        # Start verification for a run and return information about that run
        api_response = api_instance.start_run_verification(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
> SequencingRunAnalysisConfiguration update_analysis_configuration(id, body=body)

Update an analysis configuration.

Update an analysis configuration, and return information about that analysis configuration.

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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    id = 'id_example' # str | 
body = ICA_SDK.UpdateSequencingRunAnalysisConfigurationRequest() # UpdateSequencingRunAnalysisConfigurationRequest |  (optional)

    try:
        # Update an analysis configuration.
        api_response = api_instance.update_analysis_configuration(id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->update_analysis_configuration: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    id = 'id_example' # str | 
body = ICA_SDK.UpdateSequencingRunAnalysisConfigurationRequest() # UpdateSequencingRunAnalysisConfigurationRequest |  (optional)

    try:
        # Update an analysis configuration.
        api_response = api_instance.update_analysis_configuration(id, body=body)
        pprint(api_response)
    except ApiException as e:
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
> SequencingRun update_sequencing_run(run_id, body=body)

Update information for an existing sequencing run.

Update information for an existing sequencing run. This may include metadata, status, progress (started/completed/failed), and flags.

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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.UpdateSequencingRunRequest() # UpdateSequencingRunRequest |  (optional)

    try:
        # Update information for an existing sequencing run.
        api_response = api_instance.update_sequencing_run(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->update_sequencing_run: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.UpdateSequencingRunRequest() # UpdateSequencingRunRequest |  (optional)

    try:
        # Update information for an existing sequencing run.
        api_response = api_instance.update_sequencing_run(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
> SequencingRunContentsResponse update_sequencing_run_contents(run_id, body=body)

Update the content of a sequencing run.

For a given a run ID, update the sequencing run content with the current tokenâ€™s tenant ID.

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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.UpdateSequencingRunContentsRequest() # UpdateSequencingRunContentsRequest |  (optional)

    try:
        # Update the content of a sequencing run.
        api_response = api_instance.update_sequencing_run_contents(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->update_sequencing_run_contents: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.UpdateSequencingRunContentsRequest() # UpdateSequencingRunContentsRequest |  (optional)

    try:
        # Update the content of a sequencing run.
        api_response = api_instance.update_sequencing_run_contents(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
> SequencingRun update_sequencing_run_status(run_id, body=body)

Update status information for an existing sequencing run.

Update status information for an existing sequencing run. This may include status, progress (started/completed/failed), and flags.

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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.UpdateSequencingRunStatusRequest() # UpdateSequencingRunStatusRequest |  (optional)

    try:
        # Update status information for an existing sequencing run.
        api_response = api_instance.update_sequencing_run_status(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencingRunsApi->update_sequencing_run_status: %s\n" % e)
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
    api_instance = ICA_SDK.SequencingRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.UpdateSequencingRunStatusRequest() # UpdateSequencingRunStatusRequest |  (optional)

    try:
        # Update status information for an existing sequencing run.
        api_response = api_instance.update_sequencing_run_status(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
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

