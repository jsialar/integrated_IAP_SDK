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
from ICA_SDK.model.analysis_dataset_compact_analysis_dataset_sort_fields_paged_items import AnalysisDatasetCompactAnalysisDatasetSortFieldsPagedItems
from ICA_SDK.model.error_response import ErrorResponse


class AnalysisDatasetsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __list_analysis_datasets(
            self,
            **kwargs
        ):
            """List analysis datasets.  # noqa: E501

            Return a list of associated analysis datasets.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_analysis_datasets(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                include ([str]): Include flags to specify what is included in the response. [optional]
                analysis_run_id ([str]): Optional parameter. Set to filter the analysis datasets list and only include analysis datasets associated with the provided analysis runs.. [optional]
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
                AnalysisDatasetCompactAnalysisDatasetSortFieldsPagedItems
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

        self.list_analysis_datasets = _Endpoint(
            settings={
                'response_type': (AnalysisDatasetCompactAnalysisDatasetSortFieldsPagedItems,),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/v1/sequencing/analysisDatasets',
                'operation_id': 'list_analysis_datasets',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'include',
                    'analysis_run_id',
                    'tenant_ids',
                    'page_size',
                    'page_token',
                    'sort',
                ],
                'required': [],
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

                        "TOTALITEMCOUNT": "TotalItemCount",
                        "INPUTSAMPLES": "InputSamples"
                    },
                },
                'openapi_types': {
                    'include':
                        ([str],),
                    'analysis_run_id':
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
                    'include': 'include',
                    'analysis_run_id': 'analysisRunId',
                    'tenant_ids': 'tenantIds',
                    'page_size': 'pageSize',
                    'page_token': 'pageToken',
                    'sort': 'sort',
                },
                'location_map': {
                    'include': 'query',
                    'analysis_run_id': 'query',
                    'tenant_ids': 'query',
                    'page_size': 'query',
                    'page_token': 'query',
                    'sort': 'query',
                },
                'collection_format_map': {
                    'include': 'csv',
                    'analysis_run_id': 'csv',
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
            callable=__list_analysis_datasets
        )