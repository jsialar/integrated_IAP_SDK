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


class RenderMessage(object):
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
        'field_id': 'str',
        'sample_id': 'str',
        'message': 'str'
    }

    attribute_map = {
        'field_id': 'fieldId',
        'sample_id': 'sampleId',
        'message': 'message'
    }

    def __init__(self, field_id=None, sample_id=None, message=None, local_vars_configuration=None):  # noqa: E501
        """RenderMessage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._field_id = None
        self._sample_id = None
        self._message = None
        self.discriminator = None

        if field_id is not None:
            self.field_id = field_id
        if sample_id is not None:
            self.sample_id = sample_id
        if message is not None:
            self.message = message

    @property
    def field_id(self):
        """Gets the field_id of this RenderMessage.  # noqa: E501

        Field Id of the message  # noqa: E501

        :return: The field_id of this RenderMessage.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this RenderMessage.

        Field Id of the message  # noqa: E501

        :param field_id: The field_id of this RenderMessage.  # noqa: E501
        :type: str
        """

        self._field_id = field_id

    @property
    def sample_id(self):
        """Gets the sample_id of this RenderMessage.  # noqa: E501

        Sample Id of the message  # noqa: E501

        :return: The sample_id of this RenderMessage.  # noqa: E501
        :rtype: str
        """
        return self._sample_id

    @sample_id.setter
    def sample_id(self, sample_id):
        """Sets the sample_id of this RenderMessage.

        Sample Id of the message  # noqa: E501

        :param sample_id: The sample_id of this RenderMessage.  # noqa: E501
        :type: str
        """

        self._sample_id = sample_id

    @property
    def message(self):
        """Gets the message of this RenderMessage.  # noqa: E501

        The message content  # noqa: E501

        :return: The message of this RenderMessage.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this RenderMessage.

        The message content  # noqa: E501

        :param message: The message of this RenderMessage.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, RenderMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RenderMessage):
            return True

        return self.to_dict() != other.to_dict()