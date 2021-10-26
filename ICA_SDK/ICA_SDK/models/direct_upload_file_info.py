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


class DirectUploadFileInfo(object):
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
        'file_name': 'str',
        'relative_path': 'str',
        'file_id': 'str',
        'file_urn': 'str'
    }

    attribute_map = {
        'file_name': 'fileName',
        'relative_path': 'relativePath',
        'file_id': 'fileId',
        'file_urn': 'fileUrn'
    }

    def __init__(self, file_name=None, relative_path=None, file_id=None, file_urn=None, local_vars_configuration=None):  # noqa: E501
        """DirectUploadFileInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file_name = None
        self._relative_path = None
        self._file_id = None
        self._file_urn = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if relative_path is not None:
            self.relative_path = relative_path
        if file_id is not None:
            self.file_id = file_id
        if file_urn is not None:
            self.file_urn = file_urn

    @property
    def file_name(self):
        """Gets the file_name of this DirectUploadFileInfo.  # noqa: E501

        Name of the file  # noqa: E501

        :return: The file_name of this DirectUploadFileInfo.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this DirectUploadFileInfo.

        Name of the file  # noqa: E501

        :param file_name: The file_name of this DirectUploadFileInfo.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                file_name is not None and len(file_name) > 255):
            raise ValueError("Invalid value for `file_name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                file_name is not None and len(file_name) < 0):
            raise ValueError("Invalid value for `file_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._file_name = file_name

    @property
    def relative_path(self):
        """Gets the relative_path of this DirectUploadFileInfo.  # noqa: E501

        Relative path of the file (relative to run folder)  # noqa: E501

        :return: The relative_path of this DirectUploadFileInfo.  # noqa: E501
        :rtype: str
        """
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path):
        """Sets the relative_path of this DirectUploadFileInfo.

        Relative path of the file (relative to run folder)  # noqa: E501

        :param relative_path: The relative_path of this DirectUploadFileInfo.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                relative_path is not None and len(relative_path) > 1024):
            raise ValueError("Invalid value for `relative_path`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                relative_path is not None and len(relative_path) < 0):
            raise ValueError("Invalid value for `relative_path`, length must be greater than or equal to `0`")  # noqa: E501

        self._relative_path = relative_path

    @property
    def file_id(self):
        """Gets the file_id of this DirectUploadFileInfo.  # noqa: E501

        DataStore file ID if known  # noqa: E501

        :return: The file_id of this DirectUploadFileInfo.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this DirectUploadFileInfo.

        DataStore file ID if known  # noqa: E501

        :param file_id: The file_id of this DirectUploadFileInfo.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                file_id is not None and len(file_id) > 1152):
            raise ValueError("Invalid value for `file_id`, length must be less than or equal to `1152`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                file_id is not None and len(file_id) < 0):
            raise ValueError("Invalid value for `file_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._file_id = file_id

    @property
    def file_urn(self):
        """Gets the file_urn of this DirectUploadFileInfo.  # noqa: E501

        DataStore file URN if known  # noqa: E501

        :return: The file_urn of this DirectUploadFileInfo.  # noqa: E501
        :rtype: str
        """
        return self._file_urn

    @file_urn.setter
    def file_urn(self, file_urn):
        """Sets the file_urn of this DirectUploadFileInfo.

        DataStore file URN if known  # noqa: E501

        :param file_urn: The file_urn of this DirectUploadFileInfo.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                file_urn is not None and len(file_urn) > 1152):
            raise ValueError("Invalid value for `file_urn`, length must be less than or equal to `1152`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                file_urn is not None and len(file_urn) < 0):
            raise ValueError("Invalid value for `file_urn`, length must be greater than or equal to `0`")  # noqa: E501

        self._file_urn = file_urn

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
        if not isinstance(other, DirectUploadFileInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DirectUploadFileInfo):
            return True

        return self.to_dict() != other.to_dict()