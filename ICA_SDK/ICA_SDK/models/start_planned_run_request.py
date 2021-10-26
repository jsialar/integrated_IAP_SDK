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


class StartPlannedRunRequest(object):
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
        'instrument_run_id': 'str',
        'instrument_run_status': 'str',
        'flow_cell_barcode': 'str',
        'consumables': 'object',
        'sample_sheet_name': 'str',
        'run_mode': 'str',
        'run_name': 'str',
        'run_parameters_xml': 'str',
        'run_info_xml': 'str',
        'instrument_run_number': 'int',
        'description': 'str',
        'instrument_software_version': 'str',
        'external_location': 'str'
    }

    attribute_map = {
        'instrument_run_id': 'instrumentRunId',
        'instrument_run_status': 'instrumentRunStatus',
        'flow_cell_barcode': 'flowCellBarcode',
        'consumables': 'consumables',
        'sample_sheet_name': 'sampleSheetName',
        'run_mode': 'runMode',
        'run_name': 'runName',
        'run_parameters_xml': 'runParametersXml',
        'run_info_xml': 'runInfoXml',
        'instrument_run_number': 'instrumentRunNumber',
        'description': 'description',
        'instrument_software_version': 'instrumentSoftwareVersion',
        'external_location': 'externalLocation'
    }

    def __init__(self, instrument_run_id=None, instrument_run_status=None, flow_cell_barcode=None, consumables=None, sample_sheet_name=None, run_mode=None, run_name=None, run_parameters_xml=None, run_info_xml=None, instrument_run_number=None, description=None, instrument_software_version=None, external_location=None, local_vars_configuration=None):  # noqa: E501
        """StartPlannedRunRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._instrument_run_id = None
        self._instrument_run_status = None
        self._flow_cell_barcode = None
        self._consumables = None
        self._sample_sheet_name = None
        self._run_mode = None
        self._run_name = None
        self._run_parameters_xml = None
        self._run_info_xml = None
        self._instrument_run_number = None
        self._description = None
        self._instrument_software_version = None
        self._external_location = None
        self.discriminator = None

        self.instrument_run_id = instrument_run_id
        self.instrument_run_status = instrument_run_status
        self.flow_cell_barcode = flow_cell_barcode
        self.consumables = consumables
        if sample_sheet_name is not None:
            self.sample_sheet_name = sample_sheet_name
        self.run_mode = run_mode
        if run_name is not None:
            self.run_name = run_name
        self.run_parameters_xml = run_parameters_xml
        if run_info_xml is not None:
            self.run_info_xml = run_info_xml
        self.instrument_run_number = instrument_run_number
        if description is not None:
            self.description = description
        self.instrument_software_version = instrument_software_version
        if external_location is not None:
            self.external_location = external_location

    @property
    def instrument_run_id(self):
        """Gets the instrument_run_id of this StartPlannedRunRequest.  # noqa: E501

        Run ID typically generated by instrument (not guaranteed to be unique for either request token or system)  # noqa: E501

        :return: The instrument_run_id of this StartPlannedRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._instrument_run_id

    @instrument_run_id.setter
    def instrument_run_id(self, instrument_run_id):
        """Sets the instrument_run_id of this StartPlannedRunRequest.

        Run ID typically generated by instrument (not guaranteed to be unique for either request token or system)  # noqa: E501

        :param instrument_run_id: The instrument_run_id of this StartPlannedRunRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_run_id is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_run_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_run_id is not None and len(instrument_run_id) > 255):
            raise ValueError("Invalid value for `instrument_run_id`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_run_id is not None and len(instrument_run_id) < 0):
            raise ValueError("Invalid value for `instrument_run_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._instrument_run_id = instrument_run_id

    @property
    def instrument_run_status(self):
        """Gets the instrument_run_status of this StartPlannedRunRequest.  # noqa: E501

        Instrument run status, provided by the instrument control software  # noqa: E501

        :return: The instrument_run_status of this StartPlannedRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._instrument_run_status

    @instrument_run_status.setter
    def instrument_run_status(self, instrument_run_status):
        """Sets the instrument_run_status of this StartPlannedRunRequest.

        Instrument run status, provided by the instrument control software  # noqa: E501

        :param instrument_run_status: The instrument_run_status of this StartPlannedRunRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_run_status is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_run_status`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_run_status is not None and len(instrument_run_status) > 40):
            raise ValueError("Invalid value for `instrument_run_status`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_run_status is not None and len(instrument_run_status) < 0):
            raise ValueError("Invalid value for `instrument_run_status`, length must be greater than or equal to `0`")  # noqa: E501

        self._instrument_run_status = instrument_run_status

    @property
    def flow_cell_barcode(self):
        """Gets the flow_cell_barcode of this StartPlannedRunRequest.  # noqa: E501

        Barcode of the flow cell used in the sequencing run  # noqa: E501

        :return: The flow_cell_barcode of this StartPlannedRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._flow_cell_barcode

    @flow_cell_barcode.setter
    def flow_cell_barcode(self, flow_cell_barcode):
        """Sets the flow_cell_barcode of this StartPlannedRunRequest.

        Barcode of the flow cell used in the sequencing run  # noqa: E501

        :param flow_cell_barcode: The flow_cell_barcode of this StartPlannedRunRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and flow_cell_barcode is None:  # noqa: E501
            raise ValueError("Invalid value for `flow_cell_barcode`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                flow_cell_barcode is not None and len(flow_cell_barcode) > 255):
            raise ValueError("Invalid value for `flow_cell_barcode`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                flow_cell_barcode is not None and len(flow_cell_barcode) < 0):
            raise ValueError("Invalid value for `flow_cell_barcode`, length must be greater than or equal to `0`")  # noqa: E501

        self._flow_cell_barcode = flow_cell_barcode

    @property
    def consumables(self):
        """Gets the consumables of this StartPlannedRunRequest.  # noqa: E501

        Information (e.g. barcodes) about consumables (e.g. reagents or buffers) used in the sequencing run  # noqa: E501

        :return: The consumables of this StartPlannedRunRequest.  # noqa: E501
        :rtype: object
        """
        return self._consumables

    @consumables.setter
    def consumables(self, consumables):
        """Sets the consumables of this StartPlannedRunRequest.

        Information (e.g. barcodes) about consumables (e.g. reagents or buffers) used in the sequencing run  # noqa: E501

        :param consumables: The consumables of this StartPlannedRunRequest.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and consumables is None:  # noqa: E501
            raise ValueError("Invalid value for `consumables`, must not be `None`")  # noqa: E501

        self._consumables = consumables

    @property
    def sample_sheet_name(self):
        """Gets the sample_sheet_name of this StartPlannedRunRequest.  # noqa: E501

        Name of the sample sheet file. Sample sheets are not always required for all instrument types  # noqa: E501

        :return: The sample_sheet_name of this StartPlannedRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._sample_sheet_name

    @sample_sheet_name.setter
    def sample_sheet_name(self, sample_sheet_name):
        """Sets the sample_sheet_name of this StartPlannedRunRequest.

        Name of the sample sheet file. Sample sheets are not always required for all instrument types  # noqa: E501

        :param sample_sheet_name: The sample_sheet_name of this StartPlannedRunRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                sample_sheet_name is not None and len(sample_sheet_name) > 255):
            raise ValueError("Invalid value for `sample_sheet_name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sample_sheet_name is not None and len(sample_sheet_name) < 0):
            raise ValueError("Invalid value for `sample_sheet_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._sample_sheet_name = sample_sheet_name

    @property
    def run_mode(self):
        """Gets the run_mode of this StartPlannedRunRequest.  # noqa: E501

        Method by which analysis data is uploaded and process in the cloud  # noqa: E501

        :return: The run_mode of this StartPlannedRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._run_mode

    @run_mode.setter
    def run_mode(self, run_mode):
        """Sets the run_mode of this StartPlannedRunRequest.

        Method by which analysis data is uploaded and process in the cloud  # noqa: E501

        :param run_mode: The run_mode of this StartPlannedRunRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and run_mode is None:  # noqa: E501
            raise ValueError("Invalid value for `run_mode`, must not be `None`")  # noqa: E501
        allowed_values = ["InstrumentMetrics", "InstrumentAndRunMetrics", "InstrumentAndRunMetricsAndRunOutput"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and run_mode not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `run_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(run_mode, allowed_values)
            )

        self._run_mode = run_mode

    @property
    def run_name(self):
        """Gets the run_name of this StartPlannedRunRequest.  # noqa: E501

        Name of the run  # noqa: E501

        :return: The run_name of this StartPlannedRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._run_name

    @run_name.setter
    def run_name(self, run_name):
        """Sets the run_name of this StartPlannedRunRequest.

        Name of the run  # noqa: E501

        :param run_name: The run_name of this StartPlannedRunRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                run_name is not None and len(run_name) > 255):
            raise ValueError("Invalid value for `run_name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                run_name is not None and len(run_name) < 0):
            raise ValueError("Invalid value for `run_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._run_name = run_name

    @property
    def run_parameters_xml(self):
        """Gets the run_parameters_xml of this StartPlannedRunRequest.  # noqa: E501

        Content of the instrument RunParameters.xml file, generated in XML format when sequencing run starts  # noqa: E501

        :return: The run_parameters_xml of this StartPlannedRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._run_parameters_xml

    @run_parameters_xml.setter
    def run_parameters_xml(self, run_parameters_xml):
        """Sets the run_parameters_xml of this StartPlannedRunRequest.

        Content of the instrument RunParameters.xml file, generated in XML format when sequencing run starts  # noqa: E501

        :param run_parameters_xml: The run_parameters_xml of this StartPlannedRunRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and run_parameters_xml is None:  # noqa: E501
            raise ValueError("Invalid value for `run_parameters_xml`, must not be `None`")  # noqa: E501

        self._run_parameters_xml = run_parameters_xml

    @property
    def run_info_xml(self):
        """Gets the run_info_xml of this StartPlannedRunRequest.  # noqa: E501

        Content of the instrument RunInfo.xml file, generated in XML format when sequencing run starts  # noqa: E501

        :return: The run_info_xml of this StartPlannedRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._run_info_xml

    @run_info_xml.setter
    def run_info_xml(self, run_info_xml):
        """Sets the run_info_xml of this StartPlannedRunRequest.

        Content of the instrument RunInfo.xml file, generated in XML format when sequencing run starts  # noqa: E501

        :param run_info_xml: The run_info_xml of this StartPlannedRunRequest.  # noqa: E501
        :type: str
        """

        self._run_info_xml = run_info_xml

    @property
    def instrument_run_number(self):
        """Gets the instrument_run_number of this StartPlannedRunRequest.  # noqa: E501

        Number that records the number of runs that have been performed on a specific instrument  # noqa: E501

        :return: The instrument_run_number of this StartPlannedRunRequest.  # noqa: E501
        :rtype: int
        """
        return self._instrument_run_number

    @instrument_run_number.setter
    def instrument_run_number(self, instrument_run_number):
        """Sets the instrument_run_number of this StartPlannedRunRequest.

        Number that records the number of runs that have been performed on a specific instrument  # noqa: E501

        :param instrument_run_number: The instrument_run_number of this StartPlannedRunRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and instrument_run_number is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_run_number`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_run_number is not None and instrument_run_number < 0):  # noqa: E501
            raise ValueError("Invalid value for `instrument_run_number`, must be a value greater than or equal to `0`")  # noqa: E501

        self._instrument_run_number = instrument_run_number

    @property
    def description(self):
        """Gets the description of this StartPlannedRunRequest.  # noqa: E501

        Description of the run  # noqa: E501

        :return: The description of this StartPlannedRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StartPlannedRunRequest.

        Description of the run  # noqa: E501

        :param description: The description of this StartPlannedRunRequest.  # noqa: E501
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
    def instrument_software_version(self):
        """Gets the instrument_software_version of this StartPlannedRunRequest.  # noqa: E501

        Version of instrument control software provided by the instrument when the run starts  # noqa: E501

        :return: The instrument_software_version of this StartPlannedRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._instrument_software_version

    @instrument_software_version.setter
    def instrument_software_version(self, instrument_software_version):
        """Sets the instrument_software_version of this StartPlannedRunRequest.

        Version of instrument control software provided by the instrument when the run starts  # noqa: E501

        :param instrument_software_version: The instrument_software_version of this StartPlannedRunRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_software_version is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_software_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_software_version is not None and len(instrument_software_version) > 20):
            raise ValueError("Invalid value for `instrument_software_version`, length must be less than or equal to `20`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_software_version is not None and len(instrument_software_version) < 0):
            raise ValueError("Invalid value for `instrument_software_version`, length must be greater than or equal to `0`")  # noqa: E501

        self._instrument_software_version = instrument_software_version

    @property
    def external_location(self):
        """Gets the external_location of this StartPlannedRunRequest.  # noqa: E501

        Stores the external location of the sequencing run  # noqa: E501

        :return: The external_location of this StartPlannedRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._external_location

    @external_location.setter
    def external_location(self, external_location):
        """Sets the external_location of this StartPlannedRunRequest.

        Stores the external location of the sequencing run  # noqa: E501

        :param external_location: The external_location of this StartPlannedRunRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                external_location is not None and len(external_location) > 4096):
            raise ValueError("Invalid value for `external_location`, length must be less than or equal to `4096`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                external_location is not None and len(external_location) < 0):
            raise ValueError("Invalid value for `external_location`, length must be greater than or equal to `0`")  # noqa: E501

        self._external_location = external_location

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
        if not isinstance(other, StartPlannedRunRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StartPlannedRunRequest):
            return True

        return self.to_dict() != other.to_dict()