# coding: utf-8

"""
    Workflow Execution Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import integrated_sdk
from integrated_sdk.models.workflow_compact import WorkflowCompact  # noqa: E501
from integrated_sdk.rest import ApiException

class TestWorkflowCompact(unittest.TestCase):
    """WorkflowCompact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WorkflowCompact
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = integrated_sdk.models.workflow_compact.WorkflowCompact()  # noqa: E501
        if include_optional :
            return WorkflowCompact(
                id = '0', 
                urn = '0', 
                href = '0', 
                name = '0', 
                organization = '0', 
                description = '0', 
                tool_class = '0', 
                categories = [
                    '0'
                    ], 
                created_by_client_id = '0', 
                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created_by = '0', 
                modified_by = '0', 
                tenant_id = '0', 
                acl = [
                    '0'
                    ]
            )
        else :
            return WorkflowCompact(
        )

    def testWorkflowCompact(self):
        """Test WorkflowCompact"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()