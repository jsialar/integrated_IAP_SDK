"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ICA_SDK.api_client import ApiClient, Endpoint as _Endpoint
from ICA_SDK.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ICA_SDK.model.analysis_definition import AnalysisDefinition
from ICA_SDK.model.analysis_definition_compact_analysis_definition_sort_fields_paged_items import AnalysisDefinitionCompactAnalysisDefinitionSortFieldsPagedItems
from ICA_SDK.model.create_analysis_definition_request import CreateAnalysisDefinitionRequest
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.update_acl_request import UpdateAclRequest
from ICA_SDK.model.update_analysis_definition_request import UpdateAnalysisDefinitionRequest


class AnalysisDefinitionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_analysis_definition(
            self,
            **kwargs
        ):
            """Create an analysis definition.  # noqa: E501

            Create an analysis definition, and return information about that analysis definition.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_analysis_definition(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                body (CreateAnalysisDefinitionRequest): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AnalysisDefinition
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.create_analysis_definition = _Endpoint(
            settings={
                'response_type': (AnalysisDefinition,),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/v1/sequencing/analysisdefinitions',
                'operation_id': 'create_analysis_definition',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'body',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'body':
                        (CreateAnalysisDefinitionRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__create_analysis_definition
        )

        def __get_analysis_definition(
            self,
            analysis_definition_id,
            **kwargs
        ):
            """Get analysis definition details.  # noqa: E501

            For a given analysis definition ID, get the analysis definition details.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_analysis_definition(analysis_definition_id, async_req=True)
            >>> result = thread.get()

            Args:
                analysis_definition_id (str): ID of the analysis definition

            Keyword Args:
                include ([str]): Include flags to specify what is included in the response. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AnalysisDefinition
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['analysis_definition_id'] = \
                analysis_definition_id
            return self.call_with_http_info(**kwargs)

        self.get_analysis_definition = _Endpoint(
            settings={
                'response_type': (AnalysisDefinition,),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/v1/sequencing/analysisdefinitions/{analysisDefinitionId}',
                'operation_id': 'get_analysis_definition',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'analysis_definition_id',
                    'include',
                ],
                'required': [
                    'analysis_definition_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'include',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('include',): {

                        "COMPATIBLELIBRARYPREPKITS": "CompatibleLibraryPrepKits",
                        "ANALYSISVERSIONS": "AnalysisVersions"
                    },
                },
                'openapi_types': {
                    'analysis_definition_id':
                        (str,),
                    'include':
                        ([str],),
                },
                'attribute_map': {
                    'analysis_definition_id': 'analysisDefinitionId',
                    'include': 'include',
                },
                'location_map': {
                    'analysis_definition_id': 'path',
                    'include': 'query',
                },
                'collection_format_map': {
                    'include': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_analysis_definition
        )

        def __list_analysis_definitions(
            self,
            **kwargs
        ):
            """Get a list of analysis definitions.  # noqa: E501

            Get a list of analysis definitions accessible by the request token.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_analysis_definitions(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                analysis_location (str): Filter parameter to only show Local/Cloud analysis version definitions. [optional]
                regulatory_mode ([str]): Filter by regulatory modes using comma separated values, e.g <example>RUO,IVD,IUO</example>. [optional]
                instrument_platform (str): Instrument platform. [optional]
                instrument_type (str): Instrument type. [optional]
                include ([str]): Include flags to specify what is included in the response. [optional]
                tenant_ids ([str]): Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids. [optional]
                page_size (int): Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified.. [optional] if omitted the server will use the default value of 10
                page_token (str): Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified.. [optional]
                sort (str): Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending).. [optional] if omitted the server will use the default value of "timeCreated asc"
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AnalysisDefinitionCompactAnalysisDefinitionSortFieldsPagedItems
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.list_analysis_definitions = _Endpoint(
            settings={
                'response_type': (AnalysisDefinitionCompactAnalysisDefinitionSortFieldsPagedItems,),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/v1/sequencing/analysisdefinitions',
                'operation_id': 'list_analysis_definitions',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'analysis_location',
                    'regulatory_mode',
                    'instrument_platform',
                    'instrument_type',
                    'include',
                    'tenant_ids',
                    'page_size',
                    'page_token',
                    'sort',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'analysis_location',
                    'regulatory_mode',
                    'include',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('analysis_location',): {

                        "LOCAL": "Local",
                        "CLOUD": "Cloud",
                        "EDGE": "Edge"
                    },
                    ('regulatory_mode',): {

                        "RUO": "RUO",
                        "IVD": "IVD",
                        "IUO": "IUO"
                    },
                    ('include',): {

                        "TOTALITEMCOUNT": "TotalItemCount",
                        "ANALYSISVERSIONS": "AnalysisVersions"
                    },
                },
                'openapi_types': {
                    'analysis_location':
                        (str,),
                    'regulatory_mode':
                        ([str],),
                    'instrument_platform':
                        (str,),
                    'instrument_type':
                        (str,),
                    'include':
                        ([str],),
                    'tenant_ids':
                        ([str],),
                    'page_size':
                        (int,),
                    'page_token':
                        (str,),
                    'sort':
                        (str,),
                },
                'attribute_map': {
                    'analysis_location': 'analysisLocation',
                    'regulatory_mode': 'regulatoryMode',
                    'instrument_platform': 'instrumentPlatform',
                    'instrument_type': 'instrumentType',
                    'include': 'include',
                    'tenant_ids': 'tenantIds',
                    'page_size': 'pageSize',
                    'page_token': 'pageToken',
                    'sort': 'sort',
                },
                'location_map': {
                    'analysis_location': 'query',
                    'regulatory_mode': 'query',
                    'instrument_platform': 'query',
                    'instrument_type': 'query',
                    'include': 'query',
                    'tenant_ids': 'query',
                    'page_size': 'query',
                    'page_token': 'query',
                    'sort': 'query',
                },
                'collection_format_map': {
                    'regulatory_mode': 'csv',
                    'include': 'csv',
                    'tenant_ids': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_analysis_definitions
        )

        def __merge_analysis_definition_acl(
            self,
            analysis_definition_id,
            **kwargs
        ):
            """Merge the access control list of an analysis definition with the input access control list.  # noqa: E501

            Merge the access control list of an analysis definition with the input access control list, and return information about that analysis definition.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.merge_analysis_definition_acl(analysis_definition_id, async_req=True)
            >>> result = thread.get()

            Args:
                analysis_definition_id (str):

            Keyword Args:
                body (UpdateAclRequest): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AnalysisDefinition
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['analysis_definition_id'] = \
                analysis_definition_id
            return self.call_with_http_info(**kwargs)

        self.merge_analysis_definition_acl = _Endpoint(
            settings={
                'response_type': (AnalysisDefinition,),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/v1/sequencing/analysisdefinitions/{analysisDefinitionId}/acl',
                'operation_id': 'merge_analysis_definition_acl',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'analysis_definition_id',
                    'body',
                ],
                'required': [
                    'analysis_definition_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'analysis_definition_id':
                        (str,),
                    'body':
                        (UpdateAclRequest,),
                },
                'attribute_map': {
                    'analysis_definition_id': 'analysisDefinitionId',
                },
                'location_map': {
                    'analysis_definition_id': 'path',
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__merge_analysis_definition_acl
        )

        def __remove_analysis_definition_acl(
            self,
            analysis_definition_id,
            **kwargs
        ):
            """Remove the access control list of an analysis definition.  # noqa: E501

            Remove the access control list of an analysis definition, and return information about that analysis definition.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.remove_analysis_definition_acl(analysis_definition_id, async_req=True)
            >>> result = thread.get()

            Args:
                analysis_definition_id (str):

            Keyword Args:
                body (UpdateAclRequest): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AnalysisDefinition
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['analysis_definition_id'] = \
                analysis_definition_id
            return self.call_with_http_info(**kwargs)

        self.remove_analysis_definition_acl = _Endpoint(
            settings={
                'response_type': (AnalysisDefinition,),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/v1/sequencing/analysisdefinitions/{analysisDefinitionId}/acl',
                'operation_id': 'remove_analysis_definition_acl',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'analysis_definition_id',
                    'body',
                ],
                'required': [
                    'analysis_definition_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'analysis_definition_id':
                        (str,),
                    'body':
                        (UpdateAclRequest,),
                },
                'attribute_map': {
                    'analysis_definition_id': 'analysisDefinitionId',
                },
                'location_map': {
                    'analysis_definition_id': 'path',
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__remove_analysis_definition_acl
        )

        def __replace_analysis_definition_acl(
            self,
            analysis_definition_id,
            **kwargs
        ):
            """Replace the access control list of an analysis definition.  # noqa: E501

            Replace the access control list of an analysis definition, and return information about that analysis definition.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.replace_analysis_definition_acl(analysis_definition_id, async_req=True)
            >>> result = thread.get()

            Args:
                analysis_definition_id (str):

            Keyword Args:
                body (UpdateAclRequest): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AnalysisDefinition
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['analysis_definition_id'] = \
                analysis_definition_id
            return self.call_with_http_info(**kwargs)

        self.replace_analysis_definition_acl = _Endpoint(
            settings={
                'response_type': (AnalysisDefinition,),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/v1/sequencing/analysisdefinitions/{analysisDefinitionId}/acl',
                'operation_id': 'replace_analysis_definition_acl',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'analysis_definition_id',
                    'body',
                ],
                'required': [
                    'analysis_definition_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'analysis_definition_id':
                        (str,),
                    'body':
                        (UpdateAclRequest,),
                },
                'attribute_map': {
                    'analysis_definition_id': 'analysisDefinitionId',
                },
                'location_map': {
                    'analysis_definition_id': 'path',
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__replace_analysis_definition_acl
        )

        def __update_analysis_definition(
            self,
            analysis_definition_id,
            **kwargs
        ):
            """Update analysis definition details.  # noqa: E501

            For a given analysis definition ID, update the analysis definition details.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_analysis_definition(analysis_definition_id, async_req=True)
            >>> result = thread.get()

            Args:
                analysis_definition_id (str):

            Keyword Args:
                body (UpdateAnalysisDefinitionRequest): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AnalysisDefinition
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['analysis_definition_id'] = \
                analysis_definition_id
            return self.call_with_http_info(**kwargs)

        self.update_analysis_definition = _Endpoint(
            settings={
                'response_type': (AnalysisDefinition,),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/v1/sequencing/analysisdefinitions/{analysisDefinitionId}',
                'operation_id': 'update_analysis_definition',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'analysis_definition_id',
                    'body',
                ],
                'required': [
                    'analysis_definition_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'analysis_definition_id':
                        (str,),
                    'body':
                        (UpdateAnalysisDefinitionRequest,),
                },
                'attribute_map': {
                    'analysis_definition_id': 'analysisDefinitionId',
                },
                'location_map': {
                    'analysis_definition_id': 'path',
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__update_analysis_definition
        )
