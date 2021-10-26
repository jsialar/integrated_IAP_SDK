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


class DefaultKit(object):
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
        'lane_number': 'int',
        'library_prep_kit_id': 'str',
        'index_adapter_kit_id': 'str'
    }

    attribute_map = {
        'lane_number': 'laneNumber',
        'library_prep_kit_id': 'libraryPrepKitId',
        'index_adapter_kit_id': 'indexAdapterKitId'
    }

    def __init__(self, lane_number=None, library_prep_kit_id=None, index_adapter_kit_id=None, local_vars_configuration=None):  # noqa: E501
        """DefaultKit - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._lane_number = None
        self._library_prep_kit_id = None
        self._index_adapter_kit_id = None
        self.discriminator = None

        if lane_number is not None:
            self.lane_number = lane_number
        if library_prep_kit_id is not None:
            self.library_prep_kit_id = library_prep_kit_id
        if index_adapter_kit_id is not None:
            self.index_adapter_kit_id = index_adapter_kit_id

    @property
    def lane_number(self):
        """Gets the lane_number of this DefaultKit.  # noqa: E501

        Lane number. If not specified, it's the default for all lanes unless overriden for a specific lane via a separate entry.  # noqa: E501

        :return: The lane_number of this DefaultKit.  # noqa: E501
        :rtype: int
        """
        return self._lane_number

    @lane_number.setter
    def lane_number(self, lane_number):
        """Sets the lane_number of this DefaultKit.

        Lane number. If not specified, it's the default for all lanes unless overriden for a specific lane via a separate entry.  # noqa: E501

        :param lane_number: The lane_number of this DefaultKit.  # noqa: E501
        :type: int
        """

        self._lane_number = lane_number

    @property
    def library_prep_kit_id(self):
        """Gets the library_prep_kit_id of this DefaultKit.  # noqa: E501

        Default LibraryPrepKit Id in the given lane  # noqa: E501

        :return: The library_prep_kit_id of this DefaultKit.  # noqa: E501
        :rtype: str
        """
        return self._library_prep_kit_id

    @library_prep_kit_id.setter
    def library_prep_kit_id(self, library_prep_kit_id):
        """Sets the library_prep_kit_id of this DefaultKit.

        Default LibraryPrepKit Id in the given lane  # noqa: E501

        :param library_prep_kit_id: The library_prep_kit_id of this DefaultKit.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                library_prep_kit_id is not None and len(library_prep_kit_id) > 50):
            raise ValueError("Invalid value for `library_prep_kit_id`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                library_prep_kit_id is not None and len(library_prep_kit_id) < 0):
            raise ValueError("Invalid value for `library_prep_kit_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._library_prep_kit_id = library_prep_kit_id

    @property
    def index_adapter_kit_id(self):
        """Gets the index_adapter_kit_id of this DefaultKit.  # noqa: E501

        Default IndexAdapterKit Id in the given lane  # noqa: E501

        :return: The index_adapter_kit_id of this DefaultKit.  # noqa: E501
        :rtype: str
        """
        return self._index_adapter_kit_id

    @index_adapter_kit_id.setter
    def index_adapter_kit_id(self, index_adapter_kit_id):
        """Sets the index_adapter_kit_id of this DefaultKit.

        Default IndexAdapterKit Id in the given lane  # noqa: E501

        :param index_adapter_kit_id: The index_adapter_kit_id of this DefaultKit.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                index_adapter_kit_id is not None and len(index_adapter_kit_id) > 50):
            raise ValueError("Invalid value for `index_adapter_kit_id`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                index_adapter_kit_id is not None and len(index_adapter_kit_id) < 0):
            raise ValueError("Invalid value for `index_adapter_kit_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._index_adapter_kit_id = index_adapter_kit_id

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
        if not isinstance(other, DefaultKit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DefaultKit):
            return True

        return self.to_dict() != other.to_dict()