# ICA_SDK.VolumesApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_volume**](VolumesApi.md#create_volume) | **POST** /v1/volumes | Create a volume in GDS and receive temporary credentials for upload
[**delete_volume**](VolumesApi.md#delete_volume) | **DELETE** /v1/volumes/{volumeId} | Deletes a volume by Id
[**get_volume**](VolumesApi.md#get_volume) | **GET** /v1/volumes/{volumeId} | Get information for the specified volume ID or volume name
[**list_volumes**](VolumesApi.md#list_volumes) | **GET** /v1/volumes | Get a list of volumes


# **create_volume**
> CreateVolumeResponse create_volume(body)

Create a volume in GDS and receive temporary credentials for upload

Create a volume in GDS to hold folders and files. Returns upload credentials to the root folder of the volume when the include=objectStoreAccess parameter is used. You must create a volume prior to uploading files or folders.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import volumes_api
from ICA_SDK.model.create_volume_request import CreateVolumeRequest
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.create_volume_response import CreateVolumeResponse
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
    api_instance = volumes_api.VolumesApi(api_client)
    body = CreateVolumeRequest(
        name="name_example",
        volume_configuration_name="volume_configuration_name_example",
        root_key_prefix="kR,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:/",
        metadata={},
        life_cycle=VolumeLifeCycleSettings(
            grace_period_days=1,
            grace_period_end_action=GracePeriodEndAction("None"),
        ),
    ) # CreateVolumeRequest | 
    include = "include_example" # str | Optionally include additional fields in the response.              Possible values: ObjectStoreAccess (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a volume in GDS and receive temporary credentials for upload
        api_response = api_instance.create_volume(body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling VolumesApi->create_volume: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a volume in GDS and receive temporary credentials for upload
        api_response = api_instance.create_volume(body, include=include)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling VolumesApi->create_volume: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateVolumeRequest**](CreateVolumeRequest.md)|  |
 **include** | **str**| Optionally include additional fields in the response.              Possible values: ObjectStoreAccess | [optional]

### Return type

[**CreateVolumeResponse**](CreateVolumeResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created new Volume. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**409** | A conflict was found. Make sure the new Volume doesn&#39;t already exist. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_volume**
> VolumeResponse delete_volume(volume_id)

Deletes a volume by Id

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import volumes_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.volume_response import VolumeResponse
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
    api_instance = volumes_api.VolumesApi(api_client)
    volume_id = "volumeId_example" # str | Unique identifier for the Volume to be deleted.
    purge_object_store_data = True # bool | Optional and for BYOB only. If true, the volume's data in object storage will be erased.              This field is ignored for non-BYOB volumes where the object store data is always removed upon deleting the volume. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletes a volume by Id
        api_response = api_instance.delete_volume(volume_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling VolumesApi->delete_volume: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletes a volume by Id
        api_response = api_instance.delete_volume(volume_id, purge_object_store_data=purge_object_store_data)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling VolumesApi->delete_volume: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_id** | **str**| Unique identifier for the Volume to be deleted. |
 **purge_object_store_data** | **bool**| Optional and for BYOB only. If true, the volume&#39;s data in object storage will be erased.              This field is ignored for non-BYOB volumes where the object store data is always removed upon deleting the volume. | [optional]

### Return type

[**VolumeResponse**](VolumeResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Volume not found. |  -  |
**409** | Conflict |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_volume**
> VolumeResponse get_volume(volume_id)

Get information for the specified volume ID or volume name

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import volumes_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.volume_response import VolumeResponse
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
    api_instance = volumes_api.VolumesApi(api_client)
    volume_id = "volumeId_example" # str | Unique identifier for the volume to retrieve information for.
    tenant_id = "tenantId_example" # str | Optional parameter to see shared data in another tenant (optional)
    metadata_include = "metadata.include_example" # str | Optional parameter to specify comma separated patterns to include metadata by their field names. (optional)
    metadata_exclude = "metadata.exclude_example" # str | Optional parameter to specify comma separated patterns to exclude metadata by their field names. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get information for the specified volume ID or volume name
        api_response = api_instance.get_volume(volume_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling VolumesApi->get_volume: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get information for the specified volume ID or volume name
        api_response = api_instance.get_volume(volume_id, tenant_id=tenant_id, metadata_include=metadata_include, metadata_exclude=metadata_exclude)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling VolumesApi->get_volume: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_id** | **str**| Unique identifier for the volume to retrieve information for. |
 **tenant_id** | **str**| Optional parameter to see shared data in another tenant | [optional]
 **metadata_include** | **str**| Optional parameter to specify comma separated patterns to include metadata by their field names. | [optional]
 **metadata_exclude** | **str**| Optional parameter to specify comma separated patterns to exclude metadata by their field names. | [optional]

### Return type

[**VolumeResponse**](VolumeResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Volume not found. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_volumes**
> VolumeListResponse list_volumes()

Get a list of volumes

Get a list of volumes accessible by the current JWT tokenâ€™s tenant ID in GDS. The default sort returned is alphabetical, ascending. The default page size is 10 items.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import volumes_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.volume_list_response import VolumeListResponse
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
    api_instance = volumes_api.VolumesApi(api_client)
    page_size = 0 # int | START_DESC END_DESC (optional)
    page_token = "pageToken_example" # str | START_DESC END_DESC (optional)
    include = "include_example" # str | Optionally include additional fields in the response. Multiple fields can be included by comma-separation.  Possible values: TotalItemCount, InheritedAcl (optional)
    tenant_id = "tenantId_example" # str | Optional parameter to see shared data in another tenant (optional)
    volume_configuration_name = "volumeConfigurationName_example" # str | Unique name of the volume configuration (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of volumes
        api_response = api_instance.list_volumes(page_size=page_size, page_token=page_token, include=include, tenant_id=tenant_id, volume_configuration_name=volume_configuration_name)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling VolumesApi->list_volumes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| START_DESC END_DESC | [optional]
 **page_token** | **str**| START_DESC END_DESC | [optional]
 **include** | **str**| Optionally include additional fields in the response. Multiple fields can be included by comma-separation.  Possible values: TotalItemCount, InheritedAcl | [optional]
 **tenant_id** | **str**| Optional parameter to see shared data in another tenant | [optional]
 **volume_configuration_name** | **str**| Unique name of the volume configuration | [optional]

### Return type

[**VolumeListResponse**](VolumeListResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

