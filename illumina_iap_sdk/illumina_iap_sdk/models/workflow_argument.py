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

from illumina_iap_sdk.configuration import Configuration


class WorkflowArgument(object):
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
        'name': 'str',
        'value': 'str',
        'json': 'object',
        'options': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'json': 'json',
        'options': 'options'
    }

    def __init__(self, name=None, value=None, json=None, options=None, local_vars_configuration=None):  # noqa: E501
        """WorkflowArgument - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._value = None
        self._json = None
        self._options = None
        self.discriminator = None

        self.name = name
        if value is not None:
            self.value = value
        if json is not None:
            self.json = json
        if options is not None:
            self.options = options

    @property
    def name(self):
        """Gets the name of this WorkflowArgument.  # noqa: E501

        Name of the argument key  # noqa: E501

        :return: The name of this WorkflowArgument.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkflowArgument.

        Name of the argument key  # noqa: E501

        :param name: The name of this WorkflowArgument.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 128):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def value(self):
        """Gets the value of this WorkflowArgument.  # noqa: E501

        A simple string value for the argument. Cannot provide both Value and Json at the same time.  # noqa: E501

        :return: The value of this WorkflowArgument.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this WorkflowArgument.

        A simple string value for the argument. Cannot provide both Value and Json at the same time.  # noqa: E501

        :param value: The value of this WorkflowArgument.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def json(self):
        """Gets the json of this WorkflowArgument.  # noqa: E501

        A JSON value for the argument. Cannot provide both Value and Json at the same time.  # noqa: E501

        :return: The json of this WorkflowArgument.  # noqa: E501
        :rtype: object
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this WorkflowArgument.

        A JSON value for the argument. Cannot provide both Value and Json at the same time.  # noqa: E501

        :param json: The json of this WorkflowArgument.  # noqa: E501
        :type: object
        """

        self._json = json

    @property
    def options(self):
        """Gets the options of this WorkflowArgument.  # noqa: E501

        Comma separated list of options for the argument: Required, Overridable, Writable, Json, Optional, ReadOnly, Final  Some combinations of options are considered errors, like Required/Optional, Overridable/Final, Writable/ReadOnly, etc.  # noqa: E501

        :return: The options of this WorkflowArgument.  # noqa: E501
        :rtype: str
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this WorkflowArgument.

        Comma separated list of options for the argument: Required, Overridable, Writable, Json, Optional, ReadOnly, Final  Some combinations of options are considered errors, like Required/Optional, Overridable/Final, Writable/ReadOnly, etc.  # noqa: E501

        :param options: The options of this WorkflowArgument.  # noqa: E501
        :type: str
        """

        self._options = options

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
        if not isinstance(other, WorkflowArgument):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowArgument):
            return True

        return self.to_dict() != other.to_dict()