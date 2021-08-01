"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import unittest

import ICA_SDK
from ICA_SDK.api.sequencing_runs_api import SequencingRunsApi  # noqa: E501


class TestSequencingRunsApi(unittest.TestCase):
    """SequencingRunsApi unit test stubs"""

    def setUp(self):
        self.api = SequencingRunsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_abort_sequencing_run(self):
        """Test case for abort_sequencing_run

        Abort a sequencing run.  # noqa: E501
        """
        pass

    def test_can_upload(self):
        """Test case for can_upload

        Check whether the run is ready to upload.  # noqa: E501
        """
        pass

    def test_close_upload_session(self):
        """Test case for close_upload_session

        Close an upload session for a sequencing run  # noqa: E501
        """
        pass

    def test_complete_upload(self):
        """Test case for complete_upload

        Complete upload stage for a sequencing run.  # noqa: E501
        """
        pass

    def test_create_analysis_configuration(self):
        """Test case for create_analysis_configuration

        Create an analysis configuration for a sequencing run.  # noqa: E501
        """
        pass

    def test_delete_analysis_configuration(self):
        """Test case for delete_analysis_configuration

        Delete an analysis configuration for a sequencing run.  # noqa: E501
        """
        pass

    def test_delete_sequencing_run(self):
        """Test case for delete_sequencing_run

        Delete sequencing run.  # noqa: E501
        """
        pass

    def test_generate_sample_sheet_for_sequencing_run(self):
        """Test case for generate_sample_sheet_for_sequencing_run

        Generate sample sheet from a sequencing run.  # noqa: E501
        """
        pass

    def test_get_sequencing_run(self):
        """Test case for get_sequencing_run

        Get sequencing run details.  # noqa: E501
        """
        pass

    def test_get_sequencing_run_contents(self):
        """Test case for get_sequencing_run_contents

         Get the content of a sequencing run.  # noqa: E501
        """
        pass

    def test_get_sequencing_stats(self):
        """Test case for get_sequencing_stats

        Get the sequencing stats of a sequencing run.  # noqa: E501
        """
        pass

    def test_list_analysis_configurations(self):
        """Test case for list_analysis_configurations

        List analysis configurations for a sequencing run.  # noqa: E501
        """
        pass

    def test_list_sequencing_runs(self):
        """Test case for list_sequencing_runs

        Get a list of sequencing runs.  # noqa: E501
        """
        pass

    def test_merge_sequencing_run_acl(self):
        """Test case for merge_sequencing_run_acl

        Merge the access control list of a sequencing run with the input access control list.  # noqa: E501
        """
        pass

    def test_prepare_requeue(self):
        """Test case for prepare_requeue

        Prepare requeue run.  # noqa: E501
        """
        pass

    def test_remove_sequencing_run_acl(self):
        """Test case for remove_sequencing_run_acl

        Remove the access control list of a sequencing run.  # noqa: E501
        """
        pass

    def test_replace_sequencing_run_acl(self):
        """Test case for replace_sequencing_run_acl

         Replace the access control list of a sequencing run with the input access control list.  # noqa: E501
        """
        pass

    def test_replace_sequencing_stats(self):
        """Test case for replace_sequencing_stats

        Replace the sequencing stats of a sequencing run.  # noqa: E501
        """
        pass

    def test_run_direct_upload_info(self):
        """Test case for run_direct_upload_info

        Provide information about an uploaded file or set of files.  # noqa: E501
        """
        pass

    def test_start_requeue(self):
        """Test case for start_requeue

        Start prepared requeue run.  # noqa: E501
        """
        pass

    def test_start_run_verification(self):
        """Test case for start_run_verification

        Start verification for a run and return information about that run  # noqa: E501
        """
        pass

    def test_update_analysis_configuration(self):
        """Test case for update_analysis_configuration

        Update an analysis configuration.  # noqa: E501
        """
        pass

    def test_update_sequencing_run(self):
        """Test case for update_sequencing_run

        Update information for an existing sequencing run.  # noqa: E501
        """
        pass

    def test_update_sequencing_run_contents(self):
        """Test case for update_sequencing_run_contents

        Update the content of a sequencing run.  # noqa: E501
        """
        pass

    def test_update_sequencing_run_status(self):
        """Test case for update_sequencing_run_status

        Update status information for an existing sequencing run.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
