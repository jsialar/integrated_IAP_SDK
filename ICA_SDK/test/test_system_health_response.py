"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ICA_SDK
from ICA_SDK.model.health_check_statuses import HealthCheckStatuses
from ICA_SDK.model.service_health_response import ServiceHealthResponse
globals()['HealthCheckStatuses'] = HealthCheckStatuses
globals()['ServiceHealthResponse'] = ServiceHealthResponse
from ICA_SDK.model.system_health_response import SystemHealthResponse


class TestSystemHealthResponse(unittest.TestCase):
    """SystemHealthResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSystemHealthResponse(self):
        """Test SystemHealthResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SystemHealthResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()