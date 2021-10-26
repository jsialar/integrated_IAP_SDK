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


class ParseSampleSheetResponse(object):
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
        'sequencing_run': 'ParsedSequencingRun',
        'warnings': 'list[SampleSheetParsingWarning]'
    }

    attribute_map = {
        'sequencing_run': 'sequencingRun',
        'warnings': 'warnings'
    }

    def __init__(self, sequencing_run=None, warnings=None, local_vars_configuration=None):  # noqa: E501
        """ParseSampleSheetResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sequencing_run = None
        self._warnings = None
        self.discriminator = None

        if sequencing_run is not None:
            self.sequencing_run = sequencing_run
        if warnings is not None:
            self.warnings = warnings

    @property
    def sequencing_run(self):
        """Gets the sequencing_run of this ParseSampleSheetResponse.  # noqa: E501


        :return: The sequencing_run of this ParseSampleSheetResponse.  # noqa: E501
        :rtype: ParsedSequencingRun
        """
        return self._sequencing_run

    @sequencing_run.setter
    def sequencing_run(self, sequencing_run):
        """Sets the sequencing_run of this ParseSampleSheetResponse.


        :param sequencing_run: The sequencing_run of this ParseSampleSheetResponse.  # noqa: E501
        :type: ParsedSequencingRun
        """

        self._sequencing_run = sequencing_run

    @property
    def warnings(self):
        """Gets the warnings of this ParseSampleSheetResponse.  # noqa: E501

        The warnings during parsing  # noqa: E501

        :return: The warnings of this ParseSampleSheetResponse.  # noqa: E501
        :rtype: list[SampleSheetParsingWarning]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this ParseSampleSheetResponse.

        The warnings during parsing  # noqa: E501

        :param warnings: The warnings of this ParseSampleSheetResponse.  # noqa: E501
        :type: list[SampleSheetParsingWarning]
        """

        self._warnings = warnings

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
        if not isinstance(other, ParseSampleSheetResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParseSampleSheetResponse):
            return True

        return self.to_dict() != other.to_dict()