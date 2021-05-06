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
from ICA_SDK.model.create_file_request import CreateFileRequest
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.file_archive_request import FileArchiveRequest
from ICA_SDK.model.file_list_response import FileListResponse
from ICA_SDK.model.file_response import FileResponse
from ICA_SDK.model.file_unarchive_request import FileUnarchiveRequest
from ICA_SDK.model.file_writeable_response import FileWriteableResponse
from ICA_SDK.model.update_file_request import UpdateFileRequest


class FilesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __archive_file(
            self,
            file_id,
            body,
            **kwargs
        ):
            """Archive a file  # noqa: E501

            Archives a file to a lower storage cost tier.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.archive_file(file_id, body, async_req=True)
            >>> result = thread.get()

            Args:
                file_id (str): Unique identifier for the file to be archived.
                body (FileArchiveRequest):

            Keyword Args:
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
                FileResponse
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
            kwargs['file_id'] = \
                file_id
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.archive_file = _Endpoint(
            settings={
                'response_type': (FileResponse,),
                'auth': [
                    'Bearer'
                ],
                'endpoint_path': '/v1/files/{fileId}:archive',
                'operation_id': 'archive_file',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_id',
                    'body',
                ],
                'required': [
                    'file_id',
                    'body',
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
                    'file_id':
                        (str,),
                    'body':
                        (FileArchiveRequest,),
                },
                'attribute_map': {
                    'file_id': 'fileId',
                },
                'location_map': {
                    'file_id': 'path',
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
                    'application/json-patch+json',
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            callable=__archive_file
        )

        def __create_file(
            self,
            body,
            **kwargs
        ):
            """Create a file entry in GDS and get temporary credentials for upload  # noqa: E501

            Create a file entry in GDS. Returns temporary credentials for file upload directly to S3 when the include=objectStoreAccess parameter is used. Volume ID or volume name is required for file creation. If a folder path is provided and does not exist, GDS creates the folder path in the appropriate account automatically.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_file(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (CreateFileRequest):

            Keyword Args:
                include (str): Optionally include additional fields in the response.              Possible values: ObjectStoreAccess. [optional]
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
                FileWriteableResponse
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
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.create_file = _Endpoint(
            settings={
                'response_type': (FileWriteableResponse,),
                'auth': [
                    'Bearer'
                ],
                'endpoint_path': '/v1/files',
                'operation_id': 'create_file',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'body',
                    'include',
                ],
                'required': [
                    'body',
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
                    'body':
                        (CreateFileRequest,),
                    'include':
                        (str,),
                },
                'attribute_map': {
                    'include': 'include',
                },
                'location_map': {
                    'body': 'body',
                    'include': 'query',
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
            callable=__create_file
        )

        def __delete_file(
            self,
            file_id,
            **kwargs
        ):
            """Permanently delete a file  # noqa: E501

            Permanently delete a file entry and its underlying content  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_file(file_id, async_req=True)
            >>> result = thread.get()

            Args:
                file_id (str): Unique identifier for the file to delete.

            Keyword Args:
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
                None
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
            kwargs['file_id'] = \
                file_id
            return self.call_with_http_info(**kwargs)

        self.delete_file = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'Bearer'
                ],
                'endpoint_path': '/v1/files/{fileId}',
                'operation_id': 'delete_file',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_id',
                ],
                'required': [
                    'file_id',
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
                    'file_id':
                        (str,),
                },
                'attribute_map': {
                    'file_id': 'fileId',
                },
                'location_map': {
                    'file_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_file
        )

        def __get_file(
            self,
            file_id,
            **kwargs
        ):
            """Get details about a file, including a pre-signed URL for download  # noqa: E501

            Get information and details for the specified file ID, including metadata and a pre-signed URL for file download. The URL can be used as a curl command or directly with S3.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_file(file_id, async_req=True)
            >>> result = thread.get()

            Args:
                file_id (str): Unique identifier for the file to retrieve.

            Keyword Args:
                tenant_id (str): Optional parameter to see shared data in another tenant. [optional]
                metadata_include (str): Optional parameter to specify comma separated patterns to include metadata by their field names.. [optional]
                metadata_exclude (str): Optional parameter to specify comma separated patterns to exclude metadata by their field names.. [optional]
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
                FileResponse
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
            kwargs['file_id'] = \
                file_id
            return self.call_with_http_info(**kwargs)

        self.get_file = _Endpoint(
            settings={
                'response_type': (FileResponse,),
                'auth': [
                    'Bearer'
                ],
                'endpoint_path': '/v1/files/{fileId}',
                'operation_id': 'get_file',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_id',
                    'tenant_id',
                    'metadata_include',
                    'metadata_exclude',
                ],
                'required': [
                    'file_id',
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
                    'file_id':
                        (str,),
                    'tenant_id':
                        (str,),
                    'metadata_include':
                        (str,),
                    'metadata_exclude':
                        (str,),
                },
                'attribute_map': {
                    'file_id': 'fileId',
                    'tenant_id': 'tenantId',
                    'metadata_include': 'metadata.include',
                    'metadata_exclude': 'metadata.exclude',
                },
                'location_map': {
                    'file_id': 'path',
                    'tenant_id': 'query',
                    'metadata_include': 'query',
                    'metadata_exclude': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_file
        )

        def __list_files(
            self,
            **kwargs
        ):
            """Get a list of files  # noqa: E501

            Given a volumeId or volume name, get a list of files accessible by the JWT. The default sort returned is alphabetical, ascending. The default page size is 10 items  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_files(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                volume_id ([str]): Optional field that specifies comma-separated volume IDs to include in the list. [optional]
                volume_name ([str]): Optional field that specifies comma-separated volume names to include in the list. [optional]
                path ([str]): Optional field that specifies comma-separated paths to include in the list. Value can use wildcards (e.g. /a/b/c/*) or exact matches (e.g. /a/b/c/d/).. [optional]
                is_uploaded (bool): Optional field to filter by Uploaded files. [optional]
                archive_status (str): Optional field that specifies comma-separated Archive Statuses to include in the list. [optional]
                recursive (bool): Optional field to specify if files should be returned recursively in and under the specified paths, or only directly in the specified paths. [optional]
                include (str): Optionally include additional fields in the response. Multiple fields can be included by comma-separation.  Possible values: TotalItemCount, PresignedUrl, InheritedAcl. [optional]
                page_size (int): START_DESC END_DESC. [optional]
                page_token (str): START_DESC END_DESC. [optional]
                tenant_id (str): Optional parameter to see shared data in another tenant. [optional]
                metadata_include (str): Optional parameter to specify comma separated patterns to include metadata by their field names.. [optional]
                metadata_exclude (str): Optional parameter to specify comma separated patterns to exclude metadata by their field names.. [optional]
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
                FileListResponse
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

        self.list_files = _Endpoint(
            settings={
                'response_type': (FileListResponse,),
                'auth': [
                    'Bearer'
                ],
                'endpoint_path': '/v1/files',
                'operation_id': 'list_files',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'volume_id',
                    'volume_name',
                    'path',
                    'is_uploaded',
                    'archive_status',
                    'recursive',
                    'include',
                    'page_size',
                    'page_token',
                    'tenant_id',
                    'metadata_include',
                    'metadata_exclude',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page_size',
                ]
            },
            root_map={
                'validations': {
                    ('page_size',): {

                        'inclusive_maximum': 10000,
                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'volume_id':
                        ([str],),
                    'volume_name':
                        ([str],),
                    'path':
                        ([str],),
                    'is_uploaded':
                        (bool,),
                    'archive_status':
                        (str,),
                    'recursive':
                        (bool,),
                    'include':
                        (str,),
                    'page_size':
                        (int,),
                    'page_token':
                        (str,),
                    'tenant_id':
                        (str,),
                    'metadata_include':
                        (str,),
                    'metadata_exclude':
                        (str,),
                },
                'attribute_map': {
                    'volume_id': 'volume.id',
                    'volume_name': 'volume.name',
                    'path': 'path',
                    'is_uploaded': 'isUploaded',
                    'archive_status': 'archiveStatus',
                    'recursive': 'recursive',
                    'include': 'include',
                    'page_size': 'pageSize',
                    'page_token': 'pageToken',
                    'tenant_id': 'tenantId',
                    'metadata_include': 'metadata.include',
                    'metadata_exclude': 'metadata.exclude',
                },
                'location_map': {
                    'volume_id': 'query',
                    'volume_name': 'query',
                    'path': 'query',
                    'is_uploaded': 'query',
                    'archive_status': 'query',
                    'recursive': 'query',
                    'include': 'query',
                    'page_size': 'query',
                    'page_token': 'query',
                    'tenant_id': 'query',
                    'metadata_include': 'query',
                    'metadata_exclude': 'query',
                },
                'collection_format_map': {
                    'volume_id': 'csv',
                    'volume_name': 'csv',
                    'path': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_files
        )

        def __unarchive_file(
            self,
            file_id,
            body,
            **kwargs
        ):
            """Unarchive a file  # noqa: E501

            Unarchive a file from a lower storage cost tier.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.unarchive_file(file_id, body, async_req=True)
            >>> result = thread.get()

            Args:
                file_id (str): Unique identifier for the file to be unarchived.
                body (FileUnarchiveRequest):

            Keyword Args:
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
                FileResponse
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
            kwargs['file_id'] = \
                file_id
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.unarchive_file = _Endpoint(
            settings={
                'response_type': (FileResponse,),
                'auth': [
                    'Bearer'
                ],
                'endpoint_path': '/v1/files/{fileId}:unarchive',
                'operation_id': 'unarchive_file',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_id',
                    'body',
                ],
                'required': [
                    'file_id',
                    'body',
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
                    'file_id':
                        (str,),
                    'body':
                        (FileUnarchiveRequest,),
                },
                'attribute_map': {
                    'file_id': 'fileId',
                },
                'location_map': {
                    'file_id': 'path',
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
                    'application/json-patch+json',
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            callable=__unarchive_file
        )

        def __update_file(
            self,
            file_id,
            **kwargs
        ):
            """Update a file entry in GDS and get temporary credentials for upload  # noqa: E501

            Update a file entry in GDS. Returns temporary credentials for file upload directly to S3 when the include=objectStoreAccess parameter is used. Note that the currently supported changes to the file resource are updating the file type and the underlying content.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_file(file_id, async_req=True)
            >>> result = thread.get()

            Args:
                file_id (str): Unique identifier for the file to be updated.

            Keyword Args:
                include (str): Optionally include additional fields in the response.              Possible values: ObjectStoreAccess. [optional]
                body (UpdateFileRequest): [optional]
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
                FileWriteableResponse
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
            kwargs['file_id'] = \
                file_id
            return self.call_with_http_info(**kwargs)

        self.update_file = _Endpoint(
            settings={
                'response_type': (FileWriteableResponse,),
                'auth': [
                    'Bearer'
                ],
                'endpoint_path': '/v1/files/{fileId}',
                'operation_id': 'update_file',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_id',
                    'include',
                    'body',
                ],
                'required': [
                    'file_id',
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
                    'file_id':
                        (str,),
                    'include':
                        (str,),
                    'body':
                        (UpdateFileRequest,),
                },
                'attribute_map': {
                    'file_id': 'fileId',
                    'include': 'include',
                },
                'location_map': {
                    'file_id': 'path',
                    'include': 'query',
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
            callable=__update_file
        )
