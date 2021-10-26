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


class UpdateSampleRequest(object):
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
        'description': 'str',
        'status': 'str',
        'lab_status': 'str',
        'project_name': 'str',
        'acl': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'lab_status': 'labStatus',
        'project_name': 'projectName',
        'acl': 'acl'
    }

    def __init__(self, name=None, description=None, status=None, lab_status=None, project_name=None, acl=None, local_vars_configuration=None):  # noqa: E501
        """UpdateSampleRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._status = None
        self._lab_status = None
        self._project_name = None
        self._acl = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if lab_status is not None:
            self.lab_status = lab_status
        if project_name is not None:
            self.project_name = project_name
        if acl is not None:
            self.acl = acl

    @property
    def name(self):
        """Gets the name of this UpdateSampleRequest.  # noqa: E501

        Name of the sample. This field is case-insensitive.  # noqa: E501

        :return: The name of this UpdateSampleRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateSampleRequest.

        Name of the sample. This field is case-insensitive.  # noqa: E501

        :param name: The name of this UpdateSampleRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 100):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateSampleRequest.  # noqa: E501

        Description of the sample  # noqa: E501

        :return: The description of this UpdateSampleRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateSampleRequest.

        Description of the sample  # noqa: E501

        :param description: The description of this UpdateSampleRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 8192):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `8192`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def status(self):
        """Gets the status of this UpdateSampleRequest.  # noqa: E501

        Status of the sample in the lab process  # noqa: E501

        :return: The status of this UpdateSampleRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateSampleRequest.

        Status of the sample in the lab process  # noqa: E501

        :param status: The status of this UpdateSampleRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["New", "Active", "Done", "Canceled", "QcFailed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def lab_status(self):
        """Gets the lab_status of this UpdateSampleRequest.  # noqa: E501

        User-customizable value that indicates the status of the sample  # noqa: E501

        :return: The lab_status of this UpdateSampleRequest.  # noqa: E501
        :rtype: str
        """
        return self._lab_status

    @lab_status.setter
    def lab_status(self, lab_status):
        """Sets the lab_status of this UpdateSampleRequest.

        User-customizable value that indicates the status of the sample  # noqa: E501

        :param lab_status: The lab_status of this UpdateSampleRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                lab_status is not None and len(lab_status) > 255):
            raise ValueError("Invalid value for `lab_status`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                lab_status is not None and len(lab_status) < 0):
            raise ValueError("Invalid value for `lab_status`, length must be greater than or equal to `0`")  # noqa: E501

        self._lab_status = lab_status

    @property
    def project_name(self):
        """Gets the project_name of this UpdateSampleRequest.  # noqa: E501

        ProjectName. This field is case-insensitive.  Note: This field is an alias of DataAggregationGroup field until DataAggregationGroups is deprecated.  # noqa: E501

        :return: The project_name of this UpdateSampleRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this UpdateSampleRequest.

        ProjectName. This field is case-insensitive.  Note: This field is an alias of DataAggregationGroup field until DataAggregationGroups is deprecated.  # noqa: E501

        :param project_name: The project_name of this UpdateSampleRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                project_name is not None and len(project_name) > 255):
            raise ValueError("Invalid value for `project_name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                project_name is not None and len(project_name) < 0):
            raise ValueError("Invalid value for `project_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._project_name = project_name

    @property
    def acl(self):
        """Gets the acl of this UpdateSampleRequest.  # noqa: E501


        :return: The acl of this UpdateSampleRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this UpdateSampleRequest.


        :param acl: The acl of this UpdateSampleRequest.  # noqa: E501
        :type: list[str]
        """

        self._acl = acl

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
        if not isinstance(other, UpdateSampleRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateSampleRequest):
            return True

        return self.to_dict() != other.to_dict()