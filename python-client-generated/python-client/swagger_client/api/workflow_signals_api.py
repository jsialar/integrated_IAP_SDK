# coding: utf-8

"""
    Workflow Execution Service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class WorkflowSignalsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fail_signal(self, signal_id, **kwargs):  # noqa: E501
        """Fail a workflow signal  # noqa: E501

        Responds to a pending workflow signal with a failure result.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fail_signal(signal_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str signal_id: ID of the workflow signal (required)
        :param FailWorkflowSignalRequest body:
        :return: WorkflowSignal
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fail_signal_with_http_info(signal_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fail_signal_with_http_info(signal_id, **kwargs)  # noqa: E501
            return data

    def fail_signal_with_http_info(self, signal_id, **kwargs):  # noqa: E501
        """Fail a workflow signal  # noqa: E501

        Responds to a pending workflow signal with a failure result.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fail_signal_with_http_info(signal_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str signal_id: ID of the workflow signal (required)
        :param FailWorkflowSignalRequest body:
        :return: WorkflowSignal
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['signal_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fail_signal" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'signal_id' is set
        if ('signal_id' not in params or
                params['signal_id'] is None):
            raise ValueError("Missing the required parameter `signal_id` when calling `fail_signal`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'signal_id' in params:
            path_params['signalId'] = params['signal_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/workflows/signals/{signalId}:fail', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowSignal',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_signal(self, signal_id, **kwargs):  # noqa: E501
        """Get the details of a workflow signal  # noqa: E501

        Gets the details of a workflow signal with a given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_signal(signal_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str signal_id: ID of the workflow signal (required)
        :return: WorkflowSignal
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_signal_with_http_info(signal_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_signal_with_http_info(signal_id, **kwargs)  # noqa: E501
            return data

    def get_signal_with_http_info(self, signal_id, **kwargs):  # noqa: E501
        """Get the details of a workflow signal  # noqa: E501

        Gets the details of a workflow signal with a given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_signal_with_http_info(signal_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str signal_id: ID of the workflow signal (required)
        :return: WorkflowSignal
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['signal_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_signal" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'signal_id' is set
        if ('signal_id' not in params or
                params['signal_id'] is None):
            raise ValueError("Missing the required parameter `signal_id` when calling `get_signal`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'signal_id' in params:
            path_params['signalId'] = params['signal_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/workflows/signals/{signalId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowSignal',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_signals(self, **kwargs):  # noqa: E501
        """Get a list of workflow signals  # noqa: E501

        Gets a list of workflow signals.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_signals(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: ID of the tenant
        :param list[str] include: Comma-separated list of properties to include in the response
        :param int page_size: Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified.
        :param str page_token: Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified.
        :param str sort: Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending).
        :return: WorkflowSignalList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_signals_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_signals_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_signals_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of workflow signals  # noqa: E501

        Gets a list of workflow signals.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_signals_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: ID of the tenant
        :param list[str] include: Comma-separated list of properties to include in the response
        :param int page_size: Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified.
        :param str page_token: Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified.
        :param str sort: Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending).
        :return: WorkflowSignalList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id', 'include', 'page_size', 'page_token', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_signals" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tenant_id' in params:
            query_params.append(('tenantId', params['tenant_id']))  # noqa: E501
        if 'include' in params:
            query_params.append(('include', params['include']))  # noqa: E501
            collection_formats['include'] = 'multi'  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page_token' in params:
            query_params.append(('pageToken', params['page_token']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/workflows/signals', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowSignalList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def succeed_signal(self, signal_id, **kwargs):  # noqa: E501
        """Succeed a workflow signal  # noqa: E501

        Responds to a pending workflow signal with a successful result.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.succeed_signal(signal_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str signal_id: ID of the workflow signal (required)
        :param SucceedWorkflowSignalRequest body:
        :return: WorkflowSignal
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.succeed_signal_with_http_info(signal_id, **kwargs)  # noqa: E501
        else:
            (data) = self.succeed_signal_with_http_info(signal_id, **kwargs)  # noqa: E501
            return data

    def succeed_signal_with_http_info(self, signal_id, **kwargs):  # noqa: E501
        """Succeed a workflow signal  # noqa: E501

        Responds to a pending workflow signal with a successful result.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.succeed_signal_with_http_info(signal_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str signal_id: ID of the workflow signal (required)
        :param SucceedWorkflowSignalRequest body:
        :return: WorkflowSignal
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['signal_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method succeed_signal" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'signal_id' is set
        if ('signal_id' not in params or
                params['signal_id'] is None):
            raise ValueError("Missing the required parameter `signal_id` when calling `succeed_signal`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'signal_id' in params:
            path_params['signalId'] = params['signal_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/workflows/signals/{signalId}:succeed', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowSignal',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)