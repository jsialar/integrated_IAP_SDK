# coding: utf-8

"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import illumina_iap_sdk
from illumina_iap_sdk.models.subscription_list_sort_fields import SubscriptionListSortFields  # noqa: E501
from illumina_iap_sdk.rest import ApiException

class TestSubscriptionListSortFields(unittest.TestCase):
    """SubscriptionListSortFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SubscriptionListSortFields
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = illumina_iap_sdk.models.subscription_list_sort_fields.SubscriptionListSortFields()  # noqa: E501
        if include_optional :
            return SubscriptionListSortFields(
            )
        else :
            return SubscriptionListSortFields(
        )

    def testSubscriptionListSortFields(self):
        """Test SubscriptionListSortFields"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()