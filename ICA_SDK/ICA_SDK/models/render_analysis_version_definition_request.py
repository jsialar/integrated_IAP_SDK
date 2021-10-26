# coding: utf-8

"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ICA_SDK.configuration import Configuration


class RenderAnalysisVersionDefinitionRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'context': 'str',
        'field_id': 'str',
        'run_configuration': 'CreateSequencingRunConfigurationRequest',
        'run_contents': 'UpdateSequencingRunContentsRequest',
        'run_analysis_configuration': 'CreateSequencingRunAnalysisConfigurationRequest',
        'current_analysis_settings': 'object',
        'current_analysis_sample_settings': 'object'
    }

    attribute_map = {
        'context': 'context',
        'field_id': 'fieldId',
        'run_configuration': 'runConfiguration',
        'run_contents': 'runContents',
        'run_analysis_configuration': 'runAnalysisConfiguration',
        'current_analysis_settings': 'currentAnalysisSettings',
        'current_analysis_sample_settings': 'currentAnalysisSampleSettings'
    }

    def __init__(self, context=None, field_id=None, run_configuration=None, run_contents=None, run_analysis_configuration=None, current_analysis_settings=None, current_analysis_sample_settings=None, local_vars_configuration=None):  # noqa: E501
        """RenderAnalysisVersionDefinitionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._context = None
        self._field_id = None
        self._run_configuration = None
        self._run_contents = None
        self._run_analysis_configuration = None
        self._current_analysis_settings = None
        self._current_analysis_sample_settings = None
        self.discriminator = None

        self.context = context
        if field_id is not None:
            self.field_id = field_id
        if run_configuration is not None:
            self.run_configuration = run_configuration
        if run_contents is not None:
            self.run_contents = run_contents
        if run_analysis_configuration is not None:
            self.run_analysis_configuration = run_analysis_configuration
        if current_analysis_settings is not None:
            self.current_analysis_settings = current_analysis_settings
        if current_analysis_sample_settings is not None:
            self.current_analysis_sample_settings = current_analysis_sample_settings

    @property
    def context(self):
        """Gets the context of this RenderAnalysisVersionDefinitionRequest.  # noqa: E501

        Render context  # noqa: E501

        :return: The context of this RenderAnalysisVersionDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this RenderAnalysisVersionDefinitionRequest.

        Render context  # noqa: E501

        :param context: The context of this RenderAnalysisVersionDefinitionRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and context is None:  # noqa: E501
            raise ValueError("Invalid value for `context`, must not be `None`")  # noqa: E501
        allowed_values = ["Initial", "FieldChanged", "Edited"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and context not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `context` ({0}), must be one of {1}"  # noqa: E501
                .format(context, allowed_values)
            )

        self._context = context

    @property
    def field_id(self):
        """Gets the field_id of this RenderAnalysisVersionDefinitionRequest.  # noqa: E501

        The id of the field changed by user.  # noqa: E501

        :return: The field_id of this RenderAnalysisVersionDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this RenderAnalysisVersionDefinitionRequest.

        The id of the field changed by user.  # noqa: E501

        :param field_id: The field_id of this RenderAnalysisVersionDefinitionRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                field_id is not None and len(field_id) > 255):
            raise ValueError("Invalid value for `field_id`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                field_id is not None and len(field_id) < 0):
            raise ValueError("Invalid value for `field_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._field_id = field_id

    @property
    def run_configuration(self):
        """Gets the run_configuration of this RenderAnalysisVersionDefinitionRequest.  # noqa: E501


        :return: The run_configuration of this RenderAnalysisVersionDefinitionRequest.  # noqa: E501
        :rtype: CreateSequencingRunConfigurationRequest
        """
        return self._run_configuration

    @run_configuration.setter
    def run_configuration(self, run_configuration):
        """Sets the run_configuration of this RenderAnalysisVersionDefinitionRequest.


        :param run_configuration: The run_configuration of this RenderAnalysisVersionDefinitionRequest.  # noqa: E501
        :type: CreateSequencingRunConfigurationRequest
        """

        self._run_configuration = run_configuration

    @property
    def run_contents(self):
        """Gets the run_contents of this RenderAnalysisVersionDefinitionRequest.  # noqa: E501


        :return: The run_contents of this RenderAnalysisVersionDefinitionRequest.  # noqa: E501
        :rtype: UpdateSequencingRunContentsRequest
        """
        return self._run_contents

    @run_contents.setter
    def run_contents(self, run_contents):
        """Sets the run_contents of this RenderAnalysisVersionDefinitionRequest.


        :param run_contents: The run_contents of this RenderAnalysisVersionDefinitionRequest.  # noqa: E501
        :type: UpdateSequencingRunContentsRequest
        """

        self._run_contents = run_contents

    @property
    def run_analysis_configuration(self):
        """Gets the run_analysis_configuration of this RenderAnalysisVersionDefinitionRequest.  # noqa: E501


        :return: The run_analysis_configuration of this RenderAnalysisVersionDefinitionRequest.  # noqa: E501
        :rtype: CreateSequencingRunAnalysisConfigurationRequest
        """
        return self._run_analysis_configuration

    @run_analysis_configuration.setter
    def run_analysis_configuration(self, run_analysis_configuration):
        """Sets the run_analysis_configuration of this RenderAnalysisVersionDefinitionRequest.


        :param run_analysis_configuration: The run_analysis_configuration of this RenderAnalysisVersionDefinitionRequest.  # noqa: E501
        :type: CreateSequencingRunAnalysisConfigurationRequest
        """

        self._run_analysis_configuration = run_analysis_configuration

    @property
    def current_analysis_settings(self):
        """Gets the current_analysis_settings of this RenderAnalysisVersionDefinitionRequest.  # noqa: E501

        Current analysis version definition settings  # noqa: E501

        :return: The current_analysis_settings of this RenderAnalysisVersionDefinitionRequest.  # noqa: E501
        :rtype: object
        """
        return self._current_analysis_settings

    @current_analysis_settings.setter
    def current_analysis_settings(self, current_analysis_settings):
        """Sets the current_analysis_settings of this RenderAnalysisVersionDefinitionRequest.

        Current analysis version definition settings  # noqa: E501

        :param current_analysis_settings: The current_analysis_settings of this RenderAnalysisVersionDefinitionRequest.  # noqa: E501
        :type: object
        """

        self._current_analysis_settings = current_analysis_settings

    @property
    def current_analysis_sample_settings(self):
        """Gets the current_analysis_sample_settings of this RenderAnalysisVersionDefinitionRequest.  # noqa: E501

        Current analysis version definition sample settings  # noqa: E501

        :return: The current_analysis_sample_settings of this RenderAnalysisVersionDefinitionRequest.  # noqa: E501
        :rtype: object
        """
        return self._current_analysis_sample_settings

    @current_analysis_sample_settings.setter
    def current_analysis_sample_settings(self, current_analysis_sample_settings):
        """Sets the current_analysis_sample_settings of this RenderAnalysisVersionDefinitionRequest.

        Current analysis version definition sample settings  # noqa: E501

        :param current_analysis_sample_settings: The current_analysis_sample_settings of this RenderAnalysisVersionDefinitionRequest.  # noqa: E501
        :type: object
        """

        self._current_analysis_sample_settings = current_analysis_sample_settings

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RenderAnalysisVersionDefinitionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RenderAnalysisVersionDefinitionRequest):
            return True

        return self.to_dict() != other.to_dict()