# ICA_SDK.GenomesApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_genome**](GenomesApi.md#create_genome) | **POST** /v1/sequencing/genomes | Create a reference genome.
[**delete_genome**](GenomesApi.md#delete_genome) | **DELETE** /v1/sequencing/genomes/{genomeId} | Delete genome.
[**get_genome**](GenomesApi.md#get_genome) | **GET** /v1/sequencing/genomes/{genomeId} | Get genome details.
[**list_genomes**](GenomesApi.md#list_genomes) | **GET** /v1/sequencing/genomes | Get a list of genomes.
[**merge_genome_acl**](GenomesApi.md#merge_genome_acl) | **PATCH** /v1/sequencing/genomes/{genomeId}/acl | Merge the access control list of a genome with the input access control list.
[**remove_genome_acl**](GenomesApi.md#remove_genome_acl) | **DELETE** /v1/sequencing/genomes/{genomeId}/acl | Remove the access control list of a genome.
[**replace_genome_acl**](GenomesApi.md#replace_genome_acl) | **PUT** /v1/sequencing/genomes/{genomeId}/acl | Replace the access control list of a genome with the input access control list.
[**update_genome**](GenomesApi.md#update_genome) | **PATCH** /v1/sequencing/genomes/{genomeId} | Update genome details.


# **create_genome**
> Genome create_genome(body=body)

Create a reference genome.

Create a reference genome, and return information about that reference genome.

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
    api_instance = ICA_SDK.GenomesApi(api_client)
    body = ICA_SDK.CreateGenomeRequest() # CreateGenomeRequest |  (optional)

    try:
        # Create a reference genome.
        api_response = api_instance.create_genome(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GenomesApi->create_genome: %s\n" % e)
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
    api_instance = ICA_SDK.GenomesApi(api_client)
    body = ICA_SDK.CreateGenomeRequest() # CreateGenomeRequest |  (optional)

    try:
        # Create a reference genome.
        api_response = api_instance.create_genome(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GenomesApi->create_genome: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateGenomeRequest**](CreateGenomeRequest.md)|  | [optional] 

### Return type

[**Genome**](Genome.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Genome created successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**409** | Unable to create genome. Conflict found (e.g. a genome with same name and version already exists). |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_genome**
> NoContentResult delete_genome(genome_id, force=force)

Delete genome.

For a given genome ID, delete the genome.

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
    api_instance = ICA_SDK.GenomesApi(api_client)
    genome_id = 'genome_id_example' # str | ID of the genome
force = True # bool | Force delete the genome (optional)

    try:
        # Delete genome.
        api_response = api_instance.delete_genome(genome_id, force=force)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GenomesApi->delete_genome: %s\n" % e)
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
    api_instance = ICA_SDK.GenomesApi(api_client)
    genome_id = 'genome_id_example' # str | ID of the genome
force = True # bool | Force delete the genome (optional)

    try:
        # Delete genome.
        api_response = api_instance.delete_genome(genome_id, force=force)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GenomesApi->delete_genome: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **genome_id** | **str**| ID of the genome | 
 **force** | **bool**| Force delete the genome | [optional] 

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
**204** | Genome deleted successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No genome found for given genome ID. |  -  |
**410** | Genome for the given genome ID has already been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_genome**
> Genome get_genome(genome_id)

Get genome details.

For a given genome ID, return information about that genome.

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
    api_instance = ICA_SDK.GenomesApi(api_client)
    genome_id = 'genome_id_example' # str | The ID of the requested genome.

    try:
        # Get genome details.
        api_response = api_instance.get_genome(genome_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GenomesApi->get_genome: %s\n" % e)
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
    api_instance = ICA_SDK.GenomesApi(api_client)
    genome_id = 'genome_id_example' # str | The ID of the requested genome.

    try:
        # Get genome details.
        api_response = api_instance.get_genome(genome_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GenomesApi->get_genome: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **genome_id** | **str**| The ID of the requested genome. | 

### Return type

[**Genome**](Genome.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Genome details returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No genome found for given genome ID. |  -  |
**410** | The genome with the given genome ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_genomes**
> GenomeCompactGenomeSortFieldsPagedItems list_genomes(analysis_version_definition_id=analysis_version_definition_id, dragen_version=dragen_version, name=name, include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)

Get a list of genomes.

Get a list of genomes accessible by the current request token.

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
    api_instance = ICA_SDK.GenomesApi(api_client)
    analysis_version_definition_id = 'analysis_version_definition_id_example' # str | Filter genomes by ID of AnalysisVersionDefinition (optional)
dragen_version = 'dragen_version_example' # str | Filter genomes by DragenVersion (optional)
name = ['name_example'] # list[str] | Filter genomes by comma-separated Name values (optional)
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)
tenant_ids = ['tenant_ids_example'] # list[str] | Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to 'timeCreated asc')

    try:
        # Get a list of genomes.
        api_response = api_instance.list_genomes(analysis_version_definition_id=analysis_version_definition_id, dragen_version=dragen_version, name=name, include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GenomesApi->list_genomes: %s\n" % e)
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
    api_instance = ICA_SDK.GenomesApi(api_client)
    analysis_version_definition_id = 'analysis_version_definition_id_example' # str | Filter genomes by ID of AnalysisVersionDefinition (optional)
dragen_version = 'dragen_version_example' # str | Filter genomes by DragenVersion (optional)
name = ['name_example'] # list[str] | Filter genomes by comma-separated Name values (optional)
include = ['include_example'] # list[str] | Include flags to specify what is included in the response (optional)
tenant_ids = ['tenant_ids_example'] # list[str] | Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to 'timeCreated asc')

    try:
        # Get a list of genomes.
        api_response = api_instance.list_genomes(analysis_version_definition_id=analysis_version_definition_id, dragen_version=dragen_version, name=name, include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GenomesApi->list_genomes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_version_definition_id** | **str**| Filter genomes by ID of AnalysisVersionDefinition | [optional] 
 **dragen_version** | **str**| Filter genomes by DragenVersion | [optional] 
 **name** | [**list[str]**](str.md)| Filter genomes by comma-separated Name values | [optional] 
 **include** | [**list[str]**](str.md)| Include flags to specify what is included in the response | [optional] 
 **tenant_ids** | [**list[str]**](str.md)| Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids | [optional] 
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] [default to 10]
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional] 
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] [default to &#39;timeCreated asc&#39;]

### Return type

[**GenomeCompactGenomeSortFieldsPagedItems**](GenomeCompactGenomeSortFieldsPagedItems.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Genomes returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_genome_acl**
> Genome merge_genome_acl(genome_id, body=body)

Merge the access control list of a genome with the input access control list.

Merge the access control list of a given genome with the input access control list, and return information about that genome.

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
    api_instance = ICA_SDK.GenomesApi(api_client)
    genome_id = 'genome_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Merge the access control list of a genome with the input access control list.
        api_response = api_instance.merge_genome_acl(genome_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GenomesApi->merge_genome_acl: %s\n" % e)
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
    api_instance = ICA_SDK.GenomesApi(api_client)
    genome_id = 'genome_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Merge the access control list of a genome with the input access control list.
        api_response = api_instance.merge_genome_acl(genome_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GenomesApi->merge_genome_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **genome_id** | **str**|  | 
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional] 

### Return type

[**Genome**](Genome.md)

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
**404** | No genome found for given genome ID. |  -  |
**410** | The genome with the given genome ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_genome_acl**
> Genome remove_genome_acl(genome_id, body=body)

Remove the access control list of a genome.

Remove the access control list of a given genome, and return information about that genome.

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
    api_instance = ICA_SDK.GenomesApi(api_client)
    genome_id = 'genome_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Remove the access control list of a genome.
        api_response = api_instance.remove_genome_acl(genome_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GenomesApi->remove_genome_acl: %s\n" % e)
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
    api_instance = ICA_SDK.GenomesApi(api_client)
    genome_id = 'genome_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Remove the access control list of a genome.
        api_response = api_instance.remove_genome_acl(genome_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GenomesApi->remove_genome_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **genome_id** | **str**|  | 
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional] 

### Return type

[**Genome**](Genome.md)

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
**404** | No genome found for given genome ID. |  -  |
**410** | The genome with the given genome ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_genome_acl**
> Genome replace_genome_acl(genome_id, body=body)

Replace the access control list of a genome with the input access control list.

Replace the access control list of a genome with the input access control list, and return information about that genome.

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
    api_instance = ICA_SDK.GenomesApi(api_client)
    genome_id = 'genome_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Replace the access control list of a genome with the input access control list.
        api_response = api_instance.replace_genome_acl(genome_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GenomesApi->replace_genome_acl: %s\n" % e)
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
    api_instance = ICA_SDK.GenomesApi(api_client)
    genome_id = 'genome_id_example' # str | 
body = ICA_SDK.UpdateAclRequest() # UpdateAclRequest |  (optional)

    try:
        # Replace the access control list of a genome with the input access control list.
        api_response = api_instance.replace_genome_acl(genome_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GenomesApi->replace_genome_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **genome_id** | **str**|  | 
 **body** | [**UpdateAclRequest**](UpdateAclRequest.md)|  | [optional] 

### Return type

[**Genome**](Genome.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Access control list of genome updated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No genome found for given genome ID. |  -  |
**410** | The genome with the given genome ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_genome**
> Genome update_genome(genome_id, body=body)

Update genome details.

For a given genome ID, update the genome details.

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
    api_instance = ICA_SDK.GenomesApi(api_client)
    genome_id = 'genome_id_example' # str | 
body = ICA_SDK.UpdateGenomeRequest() # UpdateGenomeRequest |  (optional)

    try:
        # Update genome details.
        api_response = api_instance.update_genome(genome_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GenomesApi->update_genome: %s\n" % e)
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
    api_instance = ICA_SDK.GenomesApi(api_client)
    genome_id = 'genome_id_example' # str | 
body = ICA_SDK.UpdateGenomeRequest() # UpdateGenomeRequest |  (optional)

    try:
        # Update genome details.
        api_response = api_instance.update_genome(genome_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GenomesApi->update_genome: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **genome_id** | **str**|  | 
 **body** | [**UpdateGenomeRequest**](UpdateGenomeRequest.md)|  | [optional] 

### Return type

[**Genome**](Genome.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Genome details updated successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | No genome found for given genome ID. |  -  |
**409** | Genome not updated due to conflict with input parameters. |  -  |
**410** | The genome for the given ID has been deleted. |  -  |
**0** | Unexpected issue. Try your request again. If problem persists, contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

