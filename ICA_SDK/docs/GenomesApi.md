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
> Genome create_genome()

Create a reference genome.

Create a reference genome, and return information about that reference genome.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import genomes_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.genome import Genome
from ICA_SDK.model.create_genome_request import CreateGenomeRequest
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
    api_instance = genomes_api.GenomesApi(api_client)
    body = CreateGenomeRequest(
        acl=[
            "acl_example",
        ],
        name="name_example",
        display_name="display_name_example",
        order=-2147483648,
        is_application_specific=True,
        build="build_example",
        organization="organization_example",
        description="description_example",
        status="Active",
        species="species_example",
        source="source_example",
        dragen_version="dragen_version_example",
        data_location_urn="data_location_urn_example",
        genome_format="Dragen",
        settings={},
        source_file_metadata={},
        fasta_file_urn="fasta_file_urn_example",
        checksum="checksum_example",
    ) # CreateGenomeRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a reference genome.
        api_response = api_instance.create_genome(body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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
> NoContentResult delete_genome(genome_id)

Delete genome.

For a given genome ID, delete the genome.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import genomes_api
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
    api_instance = genomes_api.GenomesApi(api_client)
    genome_id = "genomeId_example" # str | ID of the genome
    force = True # bool | Force delete the genome (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete genome.
        api_response = api_instance.delete_genome(genome_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling GenomesApi->delete_genome: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete genome.
        api_response = api_instance.delete_genome(genome_id, force=force)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import genomes_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.genome import Genome
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
    api_instance = genomes_api.GenomesApi(api_client)
    genome_id = "genomeId_example" # str | The ID of the requested genome.

    # example passing only required values which don't have defaults set
    try:
        # Get genome details.
        api_response = api_instance.get_genome(genome_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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
> GenomeCompactGenomeSortFieldsPagedItems list_genomes()

Get a list of genomes.

Get a list of genomes accessible by the current request token.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import genomes_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.genome_compact_genome_sort_fields_paged_items import GenomeCompactGenomeSortFieldsPagedItems
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
    api_instance = genomes_api.GenomesApi(api_client)
    analysis_version_definition_id = "analysisVersionDefinitionId_example" # str | Filter genomes by ID of AnalysisVersionDefinition (optional)
    dragen_version = "dragenVersion_example" # str | Filter genomes by DragenVersion (optional)
    name = [
        "name_example",
    ] # [str] | Filter genomes by comma-separated Name values (optional)
    include = [
        "TotalItemCount",
    ] # [str] | Include flags to specify what is included in the response (optional)
    tenant_ids = [
        "tenantIds_example",
    ] # [str] | Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids (optional)
    page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) if omitted the server will use the default value of 10
    page_token = "pageToken_example" # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
    sort = "timeCreated asc" # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) if omitted the server will use the default value of "timeCreated asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of genomes.
        api_response = api_instance.list_genomes(analysis_version_definition_id=analysis_version_definition_id, dragen_version=dragen_version, name=name, include=include, tenant_ids=tenant_ids, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling GenomesApi->list_genomes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_version_definition_id** | **str**| Filter genomes by ID of AnalysisVersionDefinition | [optional]
 **dragen_version** | **str**| Filter genomes by DragenVersion | [optional]
 **name** | **[str]**| Filter genomes by comma-separated Name values | [optional]
 **include** | **[str]**| Include flags to specify what is included in the response | [optional]
 **tenant_ids** | **[str]**| Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids | [optional]
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] if omitted the server will use the default value of 10
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional]
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] if omitted the server will use the default value of "timeCreated asc"

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
> Genome merge_genome_acl(genome_id)

Merge the access control list of a genome with the input access control list.

Merge the access control list of a given genome with the input access control list, and return information about that genome.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import genomes_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_acl_request import UpdateAclRequest
from ICA_SDK.model.genome import Genome
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
    api_instance = genomes_api.GenomesApi(api_client)
    genome_id = "genomeId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Merge the access control list of a genome with the input access control list.
        api_response = api_instance.merge_genome_acl(genome_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling GenomesApi->merge_genome_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Merge the access control list of a genome with the input access control list.
        api_response = api_instance.merge_genome_acl(genome_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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
> Genome remove_genome_acl(genome_id)

Remove the access control list of a genome.

Remove the access control list of a given genome, and return information about that genome.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import genomes_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_acl_request import UpdateAclRequest
from ICA_SDK.model.genome import Genome
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
    api_instance = genomes_api.GenomesApi(api_client)
    genome_id = "genomeId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove the access control list of a genome.
        api_response = api_instance.remove_genome_acl(genome_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling GenomesApi->remove_genome_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove the access control list of a genome.
        api_response = api_instance.remove_genome_acl(genome_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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
> Genome replace_genome_acl(genome_id)

Replace the access control list of a genome with the input access control list.

Replace the access control list of a genome with the input access control list, and return information about that genome.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import genomes_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_acl_request import UpdateAclRequest
from ICA_SDK.model.genome import Genome
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
    api_instance = genomes_api.GenomesApi(api_client)
    genome_id = "genomeId_example" # str | 
    body = UpdateAclRequest(
        acl=[
            "acl_example",
        ],
    ) # UpdateAclRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Replace the access control list of a genome with the input access control list.
        api_response = api_instance.replace_genome_acl(genome_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling GenomesApi->replace_genome_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Replace the access control list of a genome with the input access control list.
        api_response = api_instance.replace_genome_acl(genome_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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
> Genome update_genome(genome_id)

Update genome details.

For a given genome ID, update the genome details.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Bearer):
```python
import time
import ICA_SDK
from ICA_SDK.api import genomes_api
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.genome import Genome
from ICA_SDK.model.update_genome_request import UpdateGenomeRequest
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
    api_instance = genomes_api.GenomesApi(api_client)
    genome_id = "genomeId_example" # str | 
    body = UpdateGenomeRequest(
        name="name_example",
        display_name="display_name_example",
        order=-2147483648,
        is_application_specific=True,
        build="build_example",
        organization="organization_example",
        description="description_example",
        status="Active",
        species="species_example",
        source="source_example",
        dragen_version="dragen_version_example",
        data_location_urn="data_location_urn_example",
        genome_format="Dragen",
        settings={},
        source_file_metadata={},
        acl=[
            "acl_example",
        ],
        fasta_file_urn="fasta_file_urn_example",
        checksum="checksum_example",
    ) # UpdateGenomeRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update genome details.
        api_response = api_instance.update_genome(genome_id)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
        print("Exception when calling GenomesApi->update_genome: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update genome details.
        api_response = api_instance.update_genome(genome_id, body=body)
        pprint(api_response)
    except ICA_SDK.ApiException as e:
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

