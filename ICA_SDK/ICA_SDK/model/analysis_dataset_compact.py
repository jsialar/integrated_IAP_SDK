"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ICA_SDK.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from ICA_SDK.model.analysis_dataset_type_compact import AnalysisDatasetTypeCompact
    from ICA_SDK.model.sample_compact import SampleCompact
    from ICA_SDK.model.sequencing_analysis_run_compact import SequencingAnalysisRunCompact
    globals()['AnalysisDatasetTypeCompact'] = AnalysisDatasetTypeCompact
    globals()['SampleCompact'] = SampleCompact
    globals()['SequencingAnalysisRunCompact'] = SequencingAnalysisRunCompact


class AnalysisDatasetCompact(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (str,),  # noqa: E501
            'urn': (str,),  # noqa: E501
            'href': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'display_name': (str,),  # noqa: E501
            'analysis_run': (SequencingAnalysisRunCompact,),  # noqa: E501
            'task_run_id': (str,),  # noqa: E501
            'workflow_run_id': (str,),  # noqa: E501
            'lane_number': (int,),  # noqa: E501
            'data_folder_urn': (str,),  # noqa: E501
            'data_folder_volume_path': (str,),  # noqa: E501
            'attributes': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'analysis_dataset_type': (AnalysisDatasetTypeCompact,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'qc_status': (str,),  # noqa: E501
            'qc_status_summary': (str,),  # noqa: E501
            'file_urns': ([str],),  # noqa: E501
            'external_id': (str,),  # noqa: E501
            'input_samples': ([SampleCompact],),  # noqa: E501
            'tenant_id': (str,),  # noqa: E501
            'sub_tenant_id': (str,),  # noqa: E501
            'acl': ([str],),  # noqa: E501
            'created_by_client_id': (str,),  # noqa: E501
            'created_by': (str,),  # noqa: E501
            'modified_by': (str,),  # noqa: E501
            'time_created': (datetime,),  # noqa: E501
            'time_modified': (datetime,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'urn': 'urn',  # noqa: E501
        'href': 'href',  # noqa: E501
        'name': 'name',  # noqa: E501
        'display_name': 'displayName',  # noqa: E501
        'analysis_run': 'analysisRun',  # noqa: E501
        'task_run_id': 'taskRunId',  # noqa: E501
        'workflow_run_id': 'workflowRunId',  # noqa: E501
        'lane_number': 'laneNumber',  # noqa: E501
        'data_folder_urn': 'dataFolderUrn',  # noqa: E501
        'data_folder_volume_path': 'dataFolderVolumePath',  # noqa: E501
        'attributes': 'attributes',  # noqa: E501
        'analysis_dataset_type': 'analysisDatasetType',  # noqa: E501
        'type': 'type',  # noqa: E501
        'qc_status': 'qcStatus',  # noqa: E501
        'qc_status_summary': 'qcStatusSummary',  # noqa: E501
        'file_urns': 'fileUrns',  # noqa: E501
        'external_id': 'externalId',  # noqa: E501
        'input_samples': 'inputSamples',  # noqa: E501
        'tenant_id': 'tenantId',  # noqa: E501
        'sub_tenant_id': 'subTenantId',  # noqa: E501
        'acl': 'acl',  # noqa: E501
        'created_by_client_id': 'createdByClientId',  # noqa: E501
        'created_by': 'createdBy',  # noqa: E501
        'modified_by': 'modifiedBy',  # noqa: E501
        'time_created': 'timeCreated',  # noqa: E501
        'time_modified': 'timeModified',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """AnalysisDatasetCompact - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): Unique object ID. [optional]  # noqa: E501
            urn (str): URN of the object. [optional]  # noqa: E501
            href (str): HREF to the object. [optional]  # noqa: E501
            name (str): Name of the analysis dataset. [optional]  # noqa: E501
            display_name (str): Display name of the analysis dataset. [optional]  # noqa: E501
            analysis_run (SequencingAnalysisRunCompact): [optional]  # noqa: E501
            task_run_id (str): Task run id of the analysis dataset. [optional]  # noqa: E501
            workflow_run_id (str): Workflow run id of the analysis dataset. [optional]  # noqa: E501
            lane_number (int): Lane number associated with the analysis dataset. [optional]  # noqa: E501
            data_folder_urn (str): Data folder urn of the analysis dataset. [optional]  # noqa: E501
            data_folder_volume_path (str): Data folder volume path of the analysis dataset. [optional]  # noqa: E501
            attributes ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Attributes of the analysis dataset. [optional]  # noqa: E501
            analysis_dataset_type (AnalysisDatasetTypeCompact): [optional]  # noqa: E501
            type (str): Type of the analysis dataset. [optional]  # noqa: E501
            qc_status (str): QC status of the analysis dataset. [optional]  # noqa: E501
            qc_status_summary (str): QC summary of the analysis dataset. [optional]  # noqa: E501
            file_urns ([str]): FileUrns of the AnalysisDataset resource. [optional]  # noqa: E501
            external_id (str): External ID of the dataset. [optional]  # noqa: E501
            input_samples ([SampleCompact]): Input samples of the analysis dataset. [optional]  # noqa: E501
            tenant_id (str): Unique identifier for the resource tenant. [optional]  # noqa: E501
            sub_tenant_id (str): Organizational or Workgroup ID. If neither are present, User ID.. [optional]  # noqa: E501
            acl ([str]): Access control list of the object. [optional]  # noqa: E501
            created_by_client_id (str): ClientId that created the resource (bssh, stratus...). [optional]  # noqa: E501
            created_by (str): User that created the resource. [optional]  # noqa: E501
            modified_by (str): User that last modified the resource. [optional]  # noqa: E501
            time_created (datetime): Time (in UTC) the resource was created. [optional]  # noqa: E501
            time_modified (datetime): Time (in UTC) the resource was modified. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
