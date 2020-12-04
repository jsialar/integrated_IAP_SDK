# coding: utf-8

"""
    Workflow Execution Service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class WorkflowList(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'items': 'list[WorkflowCompact]',
        'item_count': 'int',
        'first_page_token': 'str',
        'next_page_token': 'str',
        'prev_page_token': 'str',
        'last_page_token': 'str',
        'total_item_count': 'int',
        'total_page_count': 'int'
    }

    attribute_map = {
        'items': 'items',
        'item_count': 'itemCount',
        'first_page_token': 'firstPageToken',
        'next_page_token': 'nextPageToken',
        'prev_page_token': 'prevPageToken',
        'last_page_token': 'lastPageToken',
        'total_item_count': 'totalItemCount',
        'total_page_count': 'totalPageCount'
    }

    def __init__(self, items=None, item_count=None, first_page_token=None, next_page_token=None, prev_page_token=None, last_page_token=None, total_item_count=None, total_page_count=None):  # noqa: E501
        """WorkflowList - a model defined in Swagger"""  # noqa: E501

        self._items = None
        self._item_count = None
        self._first_page_token = None
        self._next_page_token = None
        self._prev_page_token = None
        self._last_page_token = None
        self._total_item_count = None
        self._total_page_count = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if item_count is not None:
            self.item_count = item_count
        if first_page_token is not None:
            self.first_page_token = first_page_token
        if next_page_token is not None:
            self.next_page_token = next_page_token
        if prev_page_token is not None:
            self.prev_page_token = prev_page_token
        if last_page_token is not None:
            self.last_page_token = last_page_token
        if total_item_count is not None:
            self.total_item_count = total_item_count
        if total_page_count is not None:
            self.total_page_count = total_page_count

    @property
    def items(self):
        """Gets the items of this WorkflowList.  # noqa: E501

        Items in paged list  # noqa: E501

        :return: The items of this WorkflowList.  # noqa: E501
        :rtype: list[WorkflowCompact]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this WorkflowList.

        Items in paged list  # noqa: E501

        :param items: The items of this WorkflowList.  # noqa: E501
        :type: list[WorkflowCompact]
        """

        self._items = items

    @property
    def item_count(self):
        """Gets the item_count of this WorkflowList.  # noqa: E501

        Number of items included in the page  # noqa: E501

        :return: The item_count of this WorkflowList.  # noqa: E501
        :rtype: int
        """
        return self._item_count

    @item_count.setter
    def item_count(self, item_count):
        """Sets the item_count of this WorkflowList.

        Number of items included in the page  # noqa: E501

        :param item_count: The item_count of this WorkflowList.  # noqa: E501
        :type: int
        """

        self._item_count = item_count

    @property
    def first_page_token(self):
        """Gets the first_page_token of this WorkflowList.  # noqa: E501

        PageToken for first paged list  # noqa: E501

        :return: The first_page_token of this WorkflowList.  # noqa: E501
        :rtype: str
        """
        return self._first_page_token

    @first_page_token.setter
    def first_page_token(self, first_page_token):
        """Sets the first_page_token of this WorkflowList.

        PageToken for first paged list  # noqa: E501

        :param first_page_token: The first_page_token of this WorkflowList.  # noqa: E501
        :type: str
        """

        self._first_page_token = first_page_token

    @property
    def next_page_token(self):
        """Gets the next_page_token of this WorkflowList.  # noqa: E501

        PageToken for the next paged list  # noqa: E501

        :return: The next_page_token of this WorkflowList.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this WorkflowList.

        PageToken for the next paged list  # noqa: E501

        :param next_page_token: The next_page_token of this WorkflowList.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

    @property
    def prev_page_token(self):
        """Gets the prev_page_token of this WorkflowList.  # noqa: E501

        PageToken for the previous paged list  # noqa: E501

        :return: The prev_page_token of this WorkflowList.  # noqa: E501
        :rtype: str
        """
        return self._prev_page_token

    @prev_page_token.setter
    def prev_page_token(self, prev_page_token):
        """Sets the prev_page_token of this WorkflowList.

        PageToken for the previous paged list  # noqa: E501

        :param prev_page_token: The prev_page_token of this WorkflowList.  # noqa: E501
        :type: str
        """

        self._prev_page_token = prev_page_token

    @property
    def last_page_token(self):
        """Gets the last_page_token of this WorkflowList.  # noqa: E501

        PageToken for the last paged list. Only included when totalItemCount is listed  # noqa: E501

        :return: The last_page_token of this WorkflowList.  # noqa: E501
        :rtype: str
        """
        return self._last_page_token

    @last_page_token.setter
    def last_page_token(self, last_page_token):
        """Sets the last_page_token of this WorkflowList.

        PageToken for the last paged list. Only included when totalItemCount is listed  # noqa: E501

        :param last_page_token: The last_page_token of this WorkflowList.  # noqa: E501
        :type: str
        """

        self._last_page_token = last_page_token

    @property
    def total_item_count(self):
        """Gets the total_item_count of this WorkflowList.  # noqa: E501

        Total number of items in all pages. Only included when requested  # noqa: E501

        :return: The total_item_count of this WorkflowList.  # noqa: E501
        :rtype: int
        """
        return self._total_item_count

    @total_item_count.setter
    def total_item_count(self, total_item_count):
        """Sets the total_item_count of this WorkflowList.

        Total number of items in all pages. Only included when requested  # noqa: E501

        :param total_item_count: The total_item_count of this WorkflowList.  # noqa: E501
        :type: int
        """

        self._total_item_count = total_item_count

    @property
    def total_page_count(self):
        """Gets the total_page_count of this WorkflowList.  # noqa: E501

        Total number of pages. Only included when totalItemCount is listed  # noqa: E501

        :return: The total_page_count of this WorkflowList.  # noqa: E501
        :rtype: int
        """
        return self._total_page_count

    @total_page_count.setter
    def total_page_count(self, total_page_count):
        """Sets the total_page_count of this WorkflowList.

        Total number of pages. Only included when totalItemCount is listed  # noqa: E501

        :param total_page_count: The total_page_count of this WorkflowList.  # noqa: E501
        :type: int
        """

        self._total_page_count = total_page_count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(WorkflowList, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WorkflowList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other