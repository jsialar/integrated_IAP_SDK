"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import unittest

import ICA_SDK
from ICA_SDK.api.accounts_api import AccountsApi  # noqa: E501


class TestAccountsApi(unittest.TestCase):
    """AccountsApi unit test stubs"""

    def setUp(self):
        self.api = AccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_account(self):
        """Test case for get_account

        Get requested account id info require authorization Bearer token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()