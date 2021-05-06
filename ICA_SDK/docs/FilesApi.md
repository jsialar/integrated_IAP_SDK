# ICA_SDK.FilesApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_file**](FilesApi.md#archive_file) | **POST** /v1/files/{fileId}:archive | Archive a file
[**create_file**](FilesApi.md#create_file) | **POST** /v1/files | Create a file entry in GDS and get temporary credentials for upload
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /v1/files/{fileId} | Permanently delete a file
[**get_file**](FilesApi.md#get_file) | **GET** /v1/files/{fileId} | Get details about a file, including a pre-signed URL for download
[**list_files**](FilesApi.md#list_files) | **GET** /v1/files | Get a list of files
[**unarchive_file**](FilesApi.md#unarchive_file) | **POST** /v1/files/{fileId}:unarchive | Unarchive a file
[**update_file**](FilesApi.md#update_file) | **PATCH** /v1/files/{fileId} | Update a file entry in GDS and get temporary credentials for upload


# **archive_file**
> FileResponse archive_file(file_id, body)

Archive a file

Archives a file to a lower storage cost tier.

### Example

* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import files_api
from ICA_SDK.model.file_response import FileResponse
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.file_archive_request import FileArchiveRequest
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    file_id = "fileId_example" # str | Unique identifier for the file to be archived.
    body = FileArchiveRequest(
        storage_tier=FileArchiveStorageTier("Archive"),
    ) # FileArchiveRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Archive a file
        api_response = api_instance.archive_file(file_id, body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling FilesApi->archive_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Unique identifier for the file to be archived. |
 **body** | [**FileArchiveRequest**](FileArchiveRequest.md)|  |

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | File not found. |  -  |
**409** | Conflict. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file**
> FileWriteableResponse create_file(body)

Create a file entry in GDS and get temporary credentials for upload

Create a file entry in GDS. Returns temporary credentials for file upload directly to S3 when the include=objectStoreAccess parameter is used. Volume ID or volume name is required for file creation. If a folder path is provided and does not exist, GDS creates the folder path in the appropriate account automatically.

### Example

* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import files_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.create_file_request import CreateFileRequest
from ICA_SDK.model.file_writeable_response import FileWriteableResponse
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    body = CreateFileRequest(
        name="k",
        volume_id="volume_id_example",
        folder_path="folder_path_example",
        type="type_example",
        volume_name="volume_name_example",
    ) # CreateFileRequest | 
    include = "include_example" # str | Optionally include additional fields in the response.              Possible values: ObjectStoreAccess (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a file entry in GDS and get temporary credentials for upload
        api_response = api_instance.create_file(body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling FilesApi->create_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a file entry in GDS and get temporary credentials for upload
        api_response = api_instance.create_file(body, include=include)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling FilesApi->create_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateFileRequest**](CreateFileRequest.md)|  |
 **include** | **str**| Optionally include additional fields in the response.              Possible values: ObjectStoreAccess | [optional]

### Return type

[**FileWriteableResponse**](FileWriteableResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created new File. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**409** | A conflict was found. Make sure the new File doesn&#39;t already exist. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> delete_file(file_id)

Permanently delete a file

Permanently delete a file entry and its underlying content

### Example

* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import files_api
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    file_id = "fileId_example" # str | Unique identifier for the file to delete.

    # example passing only required values which don't have defaults set
    try:
        # Permanently delete a file
        api_instance.delete_file(file_id)
    except ICA_SDK.ApiException as e:
        print("Exception when calling FilesApi->delete_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Unique identifier for the file to delete. |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | File not found. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> FileResponse get_file(file_id)

Get details about a file, including a pre-signed URL for download

Get information and details for the specified file ID, including metadata and a pre-signed URL for file download. The URL can be used as a curl command or directly with S3.

### Example

* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import files_api
from ICA_SDK.model.file_response import FileResponse
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    file_id = "fileId_example" # str | Unique identifier for the file to retrieve.
    tenant_id = "tenantId_example" # str | Optional parameter to see shared data in another tenant (optional)
    metadata_include = "metadata.include_example" # str | Optional parameter to specify comma separated patterns to include metadata by their field names. (optional)
    metadata_exclude = "metadata.exclude_example" # str | Optional parameter to specify comma separated patterns to exclude metadata by their field names. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details about a file, including a pre-signed URL for download
        api_response = api_instance.get_file(file_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling FilesApi->get_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details about a file, including a pre-signed URL for download
        api_response = api_instance.get_file(file_id, tenant_id=tenant_id, metadata_include=metadata_include, metadata_exclude=metadata_exclude)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling FilesApi->get_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Unique identifier for the file to retrieve. |
 **tenant_id** | **str**| Optional parameter to see shared data in another tenant | [optional]
 **metadata_include** | **str**| Optional parameter to specify comma separated patterns to include metadata by their field names. | [optional]
 **metadata_exclude** | **str**| Optional parameter to specify comma separated patterns to exclude metadata by their field names. | [optional]

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

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
**404** | File not found. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_files**
> FileListResponse list_files()

Get a list of files

Given a volumeId or volume name, get a list of files accessible by the JWT. The default sort returned is alphabetical, ascending. The default page size is 10 items

### Example

* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import files_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.file_list_response import FileListResponse
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    volume_id = [
        "volume.id_example",
    ] # [str] | Optional field that specifies comma-separated volume IDs to include in the list (optional)
    volume_name = [
        "volume.name_example",
    ] # [str] | Optional field that specifies comma-separated volume names to include in the list (optional)
    path = [
        "path_example",
    ] # [str] | Optional field that specifies comma-separated paths to include in the list. Value can use wildcards (e.g. /a/b/c/*) or exact matches (e.g. /a/b/c/d/). (optional)
    is_uploaded = True # bool | Optional field to filter by Uploaded files (optional)
    archive_status = "archiveStatus_example" # str | Optional field that specifies comma-separated Archive Statuses to include in the list (optional)
    recursive = True # bool | Optional field to specify if files should be returned recursively in and under the specified paths, or only directly in the specified paths (optional)
    include = "include_example" # str | Optionally include additional fields in the response. Multiple fields can be included by comma-separation.  Possible values: TotalItemCount, PresignedUrl, InheritedAcl (optional)
    page_size = 0 # int | START_DESC END_DESC (optional)
    page_token = "pageToken_example" # str | START_DESC END_DESC (optional)
    tenant_id = "tenantId_example" # str | Optional parameter to see shared data in another tenant (optional)
    metadata_include = "metadata.include_example" # str | Optional parameter to specify comma separated patterns to include metadata by their field names. (optional)
    metadata_exclude = "metadata.exclude_example" # str | Optional parameter to specify comma separated patterns to exclude metadata by their field names. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of files
        api_response = api_instance.list_files(volume_id=volume_id, volume_name=volume_name, path=path, is_uploaded=is_uploaded, archive_status=archive_status, recursive=recursive, include=include, page_size=page_size, page_token=page_token, tenant_id=tenant_id, metadata_include=metadata_include, metadata_exclude=metadata_exclude)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling FilesApi->list_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_id** | **[str]**| Optional field that specifies comma-separated volume IDs to include in the list | [optional]
 **volume_name** | **[str]**| Optional field that specifies comma-separated volume names to include in the list | [optional]
 **path** | **[str]**| Optional field that specifies comma-separated paths to include in the list. Value can use wildcards (e.g. /a/b/c/*) or exact matches (e.g. /a/b/c/d/). | [optional]
 **is_uploaded** | **bool**| Optional field to filter by Uploaded files | [optional]
 **archive_status** | **str**| Optional field that specifies comma-separated Archive Statuses to include in the list | [optional]
 **recursive** | **bool**| Optional field to specify if files should be returned recursively in and under the specified paths, or only directly in the specified paths | [optional]
 **include** | **str**| Optionally include additional fields in the response. Multiple fields can be included by comma-separation.  Possible values: TotalItemCount, PresignedUrl, InheritedAcl | [optional]
 **page_size** | **int**| START_DESC END_DESC | [optional]
 **page_token** | **str**| START_DESC END_DESC | [optional]
 **tenant_id** | **str**| Optional parameter to see shared data in another tenant | [optional]
 **metadata_include** | **str**| Optional parameter to specify comma separated patterns to include metadata by their field names. | [optional]
 **metadata_exclude** | **str**| Optional parameter to specify comma separated patterns to exclude metadata by their field names. | [optional]

### Return type

[**FileListResponse**](FileListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **unarchive_file**
> FileResponse unarchive_file(file_id, body)

Unarchive a file

Unarchive a file from a lower storage cost tier.

### Example

* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import files_api
from ICA_SDK.model.file_response import FileResponse
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.file_unarchive_request import FileUnarchiveRequest
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    file_id = "fileId_example" # str | Unique identifier for the file to be unarchived.
    body = FileUnarchiveRequest(
        restore_speed="restore_speed_example",
    ) # FileUnarchiveRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Unarchive a file
        api_response = api_instance.unarchive_file(file_id, body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling FilesApi->unarchive_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Unique identifier for the file to be unarchived. |
 **body** | [**FileUnarchiveRequest**](FileUnarchiveRequest.md)|  |

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | File not found. |  -  |
**409** | Conflict. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file**
> FileWriteableResponse update_file(file_id)

Update a file entry in GDS and get temporary credentials for upload

Update a file entry in GDS. Returns temporary credentials for file upload directly to S3 when the include=objectStoreAccess parameter is used. Note that the currently supported changes to the file resource are updating the file type and the underlying content.

### Example

* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import files_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_file_request import UpdateFileRequest
from ICA_SDK.model.file_writeable_response import FileWriteableResponse
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    file_id = "fileId_example" # str | Unique identifier for the file to be updated.
    include = "include_example" # str | Optionally include additional fields in the response.              Possible values: ObjectStoreAccess (optional)
    body = UpdateFileRequest(
        type="type_example",
    ) # UpdateFileRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a file entry in GDS and get temporary credentials for upload
        api_response = api_instance.update_file(file_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling FilesApi->update_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a file entry in GDS and get temporary credentials for upload
        api_response = api_instance.update_file(file_id, include=include, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling FilesApi->update_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Unique identifier for the file to be updated. |
 **include** | **str**| Optionally include additional fields in the response.              Possible values: ObjectStoreAccess | [optional]
 **body** | [**UpdateFileRequest**](UpdateFileRequest.md)|  | [optional]

### Return type

[**FileWriteableResponse**](FileWriteableResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | File not found. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

