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


class SampleSheet(object):
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
        'sample_sheet_content': 'str',
        'file_references': 'list[FileReferenceCompact]',
        'auxiliary_file_references': 'list[AuxiliaryFileReferenceCompact]'
    }

    attribute_map = {
        'sample_sheet_content': 'sampleSheetContent',
        'file_references': 'fileReferences',
        'auxiliary_file_references': 'auxiliaryFileReferences'
    }

    def __init__(self, sample_sheet_content=None, file_references=None, auxiliary_file_references=None, local_vars_configuration=None):  # noqa: E501
        """SampleSheet - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sample_sheet_content = None
        self._file_references = None
        self._auxiliary_file_references = None
        self.discriminator = None

        if sample_sheet_content is not None:
            self.sample_sheet_content = sample_sheet_content
        if file_references is not None:
            self.file_references = file_references
        if auxiliary_file_references is not None:
            self.auxiliary_file_references = auxiliary_file_references

    @property
    def sample_sheet_content(self):
        """Gets the sample_sheet_content of this SampleSheet.  # noqa: E501

        Sample sheet string in csv format  # noqa: E501

        :return: The sample_sheet_content of this SampleSheet.  # noqa: E501
        :rtype: str
        """
        return self._sample_sheet_content

    @sample_sheet_content.setter
    def sample_sheet_content(self, sample_sheet_content):
        """Sets the sample_sheet_content of this SampleSheet.

        Sample sheet string in csv format  # noqa: E501

        :param sample_sheet_content: The sample_sheet_content of this SampleSheet.  # noqa: E501
        :type: str
        """

        self._sample_sheet_content = sample_sheet_content

    @property
    def file_references(self):
        """Gets the file_references of this SampleSheet.  # noqa: E501

        File references  # noqa: E501

        :return: The file_references of this SampleSheet.  # noqa: E501
        :rtype: list[FileReferenceCompact]
        """
        return self._file_references

    @file_references.setter
    def file_references(self, file_references):
        """Sets the file_references of this SampleSheet.

        File references  # noqa: E501

        :param file_references: The file_references of this SampleSheet.  # noqa: E501
        :type: list[FileReferenceCompact]
        """

        self._file_references = file_references

    @property
    def auxiliary_file_references(self):
        """Gets the auxiliary_file_references of this SampleSheet.  # noqa: E501

        Auxiliary file references  # noqa: E501

        :return: The auxiliary_file_references of this SampleSheet.  # noqa: E501
        :rtype: list[AuxiliaryFileReferenceCompact]
        """
        return self._auxiliary_file_references

    @auxiliary_file_references.setter
    def auxiliary_file_references(self, auxiliary_file_references):
        """Sets the auxiliary_file_references of this SampleSheet.

        Auxiliary file references  # noqa: E501

        :param auxiliary_file_references: The auxiliary_file_references of this SampleSheet.  # noqa: E501
        :type: list[AuxiliaryFileReferenceCompact]
        """

        self._auxiliary_file_references = auxiliary_file_references

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
        if not isinstance(other, SampleSheet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SampleSheet):
            return True

        return self.to_dict() != other.to_dict()