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
> SequencingRun create_planned_run(body=body)

Create sequencing run plan.

Create sequencing run plan, with configuration required for an instrument to start the run.

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
    api_instance = ICA_SDK.PlannedRunsApi(api_client)
    body = ICA_SDK.CreatePlannedRunRequest() # CreatePlannedRunRequest |  (optional)

    try:
        # Create sequencing run plan.
        api_response = api_instance.create_planned_run(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlannedRunsApi->create_planned_run: %s\n" % e)
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
    api_instance = ICA_SDK.PlannedRunsApi(api_client)
    body = ICA_SDK.CreatePlannedRunRequest() # CreatePlannedRunRequest |  (optional)

    try:
        # Create sequencing run plan.
        api_response = api_instance.create_planned_run(body=body)
        pprint(api_response)
    except ApiException as e:
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
> ImportPlannedRunResponse import_planned_run(body=body)

Import a planned run from sample sheet.

Import a planned run based on sample sheet, return information of the import result.

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
    api_instance = ICA_SDK.PlannedRunsApi(api_client)
    body = ICA_SDK.ImportPlannedRunRequest() # ImportPlannedRunRequest |  (optional)

    try:
        # Import a planned run from sample sheet.
        api_response = api_instance.import_planned_run(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlannedRunsApi->import_planned_run: %s\n" % e)
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
    api_instance = ICA_SDK.PlannedRunsApi(api_client)
    body = ICA_SDK.ImportPlannedRunRequest() # ImportPlannedRunRequest |  (optional)

    try:
        # Import a planned run from sample sheet.
        api_response = api_instance.import_planned_run(body=body)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = ICA_SDK.PlannedRunsApi(api_client)
    run_id = 'run_id_example' # str | 

    try:
        # Lock a planned run.
        api_response = api_instance.lock_planned_run(run_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlannedRunsApi->lock_planned_run: %s\n" % e)
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
    api_instance = ICA_SDK.PlannedRunsApi(api_client)
    run_id = 'run_id_example' # str | 

    try:
        # Lock a planned run.
        api_response = api_instance.lock_planned_run(run_id)
        pprint(api_response)
    except ApiException as e:
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
> SequencingRun replace_planned_run(run_id, body=body)

Replace planned run configuration, contents, and analysis configurations.

For a given sequencing run ID, replace the existing planned run with user input. This may include run configuration, run contents, and analysis configurations. Only applicable to runs in planning stage.

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
    api_instance = ICA_SDK.PlannedRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.ReplacePlannedRunRequest() # ReplacePlannedRunRequest |  (optional)

    try:
        # Replace planned run configuration, contents, and analysis configurations.
        api_response = api_instance.replace_planned_run(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlannedRunsApi->replace_planned_run: %s\n" % e)
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
    api_instance = ICA_SDK.PlannedRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.ReplacePlannedRunRequest() # ReplacePlannedRunRequest |  (optional)

    try:
        # Replace planned run configuration, contents, and analysis configurations.
        api_response = api_instance.replace_planned_run(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
> SequencingRun start_planned_run(run_id, body=body)

Start a planned sequencing run.

Start a planned sequencing run, and return information about that run. Only applicable to planned runs.

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
    api_instance = ICA_SDK.PlannedRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.StartPlannedRunRequest() # StartPlannedRunRequest |  (optional)

    try:
        # Start a planned sequencing run.
        api_response = api_instance.start_planned_run(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlannedRunsApi->start_planned_run: %s\n" % e)
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
    api_instance = ICA_SDK.PlannedRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.StartPlannedRunRequest() # StartPlannedRunRequest |  (optional)

    try:
        # Start a planned sequencing run.
        api_response = api_instance.start_planned_run(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = ICA_SDK.PlannedRunsApi(api_client)
    run_id = 'run_id_example' # str | 

    try:
        # Unlock a planned run.
        api_response = api_instance.unlock_planned_run(run_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlannedRunsApi->unlock_planned_run: %s\n" % e)
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
    api_instance = ICA_SDK.PlannedRunsApi(api_client)
    run_id = 'run_id_example' # str | 

    try:
        # Unlock a planned run.
        api_response = api_instance.unlock_planned_run(run_id)
        pprint(api_response)
    except ApiException as e:
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
> SequencingRun update_planned_run_config(run_id, body=body)

Update planned run configuration.

For a given sequencing run ID, update the planned run configuration. Only applicable to runs in planning stage.

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
    api_instance = ICA_SDK.PlannedRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.UpdateSequencingRunConfigurationRequest() # UpdateSequencingRunConfigurationRequest |  (optional)

    try:
        # Update planned run configuration.
        api_response = api_instance.update_planned_run_config(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlannedRunsApi->update_planned_run_config: %s\n" % e)
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
    api_instance = ICA_SDK.PlannedRunsApi(api_client)
    run_id = 'run_id_example' # str | 
body = ICA_SDK.UpdateSequencingRunConfigurationRequest() # UpdateSequencingRunConfigurationRequest |  (optional)

    try:
        # Update planned run configuration.
        api_response = api_instance.update_planned_run_config(run_id, body=body)
        pprint(api_response)
    except ApiException as e:
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

