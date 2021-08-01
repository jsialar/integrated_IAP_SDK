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


class RunSequencingStats(ModelNormal):
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
        return {
            'num_cycles_index1': (int,),  # noqa: E501
            'num_cycles_index2': (int,),  # noqa: E501
            'num_cycles_read1': (int,),  # noqa: E501
            'num_cycles_read2': (int,),  # noqa: E501
            'num_lanes': (int,),  # noqa: E501
            'num_reads': (int,),  # noqa: E501
            'num_surfaces': (int,),  # noqa: E501
            'num_swaths_per_lane': (int,),  # noqa: E501
            'num_tiles_per_swath': (int,),  # noqa: E501
            'error_rate': (float,),  # noqa: E501
            'error_rate_r1': (float,),  # noqa: E501
            'error_rate_r2': (float,),  # noqa: E501
            'intensity_cycle1': (float,),  # noqa: E501
            'is_indexed': (bool,),  # noqa: E501
            'max_cycle_called': (int,),  # noqa: E501
            'max_cycle_extracted': (int,),  # noqa: E501
            'max_cycle_scored': (int,),  # noqa: E501
            'min_cycle_called': (int,),  # noqa: E501
            'min_cycle_extracted': (int,),  # noqa: E501
            'min_cycle_scored': (int,),  # noqa: E501
            'non_indexed_error_rate': (float,),  # noqa: E501
            'non_indexed_intensity_cycle1': (float,),  # noqa: E501
            'non_indexed_percent_aligned': (float,),  # noqa: E501
            'non_indexed_percent_gt_q30': (float,),  # noqa: E501
            'non_indexed_projected_total_yield': (float,),  # noqa: E501
            'non_indexed_yield_total': (float,),  # noqa: E501
            'percent_aligned': (float,),  # noqa: E501
            'percent_gt_q30': (float,),  # noqa: E501
            'percent_gt_q30_last10_cycles': (float,),  # noqa: E501
            'percent_gt_q30_r1': (float,),  # noqa: E501
            'percent_gt_q30_r2': (float,),  # noqa: E501
            'percent_pf': (float,),  # noqa: E501
            'percent_resynthesis': (float,),  # noqa: E501
            'phasing_r1': (float,),  # noqa: E501
            'phasing_r2': (float,),  # noqa: E501
            'pre_phasing_r1': (float,),  # noqa: E501
            'pre_phasing_r2': (float,),  # noqa: E501
            'projected_total_yield': (float,),  # noqa: E501
            'reads_pf_total': (int,),  # noqa: E501
            'reads_total': (int,),  # noqa: E501
            'yield_total': (float,),  # noqa: E501
            'clusters': (int,),  # noqa: E501
            'clusters_pf': (int,),  # noqa: E501
            'cluster_density': (float,),  # noqa: E501
            'occupancy': (float,),  # noqa: E501
            'percent_loading_concentration': (float,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'num_cycles_index1': 'numCyclesIndex1',  # noqa: E501
        'num_cycles_index2': 'numCyclesIndex2',  # noqa: E501
        'num_cycles_read1': 'numCyclesRead1',  # noqa: E501
        'num_cycles_read2': 'numCyclesRead2',  # noqa: E501
        'num_lanes': 'numLanes',  # noqa: E501
        'num_reads': 'numReads',  # noqa: E501
        'num_surfaces': 'numSurfaces',  # noqa: E501
        'num_swaths_per_lane': 'numSwathsPerLane',  # noqa: E501
        'num_tiles_per_swath': 'numTilesPerSwath',  # noqa: E501
        'error_rate': 'errorRate',  # noqa: E501
        'error_rate_r1': 'errorRateR1',  # noqa: E501
        'error_rate_r2': 'errorRateR2',  # noqa: E501
        'intensity_cycle1': 'intensityCycle1',  # noqa: E501
        'is_indexed': 'isIndexed',  # noqa: E501
        'max_cycle_called': 'maxCycleCalled',  # noqa: E501
        'max_cycle_extracted': 'maxCycleExtracted',  # noqa: E501
        'max_cycle_scored': 'maxCycleScored',  # noqa: E501
        'min_cycle_called': 'minCycleCalled',  # noqa: E501
        'min_cycle_extracted': 'minCycleExtracted',  # noqa: E501
        'min_cycle_scored': 'minCycleScored',  # noqa: E501
        'non_indexed_error_rate': 'nonIndexedErrorRate',  # noqa: E501
        'non_indexed_intensity_cycle1': 'nonIndexedIntensityCycle1',  # noqa: E501
        'non_indexed_percent_aligned': 'nonIndexedPercentAligned',  # noqa: E501
        'non_indexed_percent_gt_q30': 'nonIndexedPercentGtQ30',  # noqa: E501
        'non_indexed_projected_total_yield': 'nonIndexedProjectedTotalYield',  # noqa: E501
        'non_indexed_yield_total': 'nonIndexedYieldTotal',  # noqa: E501
        'percent_aligned': 'percentAligned',  # noqa: E501
        'percent_gt_q30': 'percentGtQ30',  # noqa: E501
        'percent_gt_q30_last10_cycles': 'percentGtQ30Last10Cycles',  # noqa: E501
        'percent_gt_q30_r1': 'percentGtQ30R1',  # noqa: E501
        'percent_gt_q30_r2': 'percentGtQ30R2',  # noqa: E501
        'percent_pf': 'percentPf',  # noqa: E501
        'percent_resynthesis': 'percentResynthesis',  # noqa: E501
        'phasing_r1': 'phasingR1',  # noqa: E501
        'phasing_r2': 'phasingR2',  # noqa: E501
        'pre_phasing_r1': 'prePhasingR1',  # noqa: E501
        'pre_phasing_r2': 'prePhasingR2',  # noqa: E501
        'projected_total_yield': 'projectedTotalYield',  # noqa: E501
        'reads_pf_total': 'readsPfTotal',  # noqa: E501
        'reads_total': 'readsTotal',  # noqa: E501
        'yield_total': 'yieldTotal',  # noqa: E501
        'clusters': 'clusters',  # noqa: E501
        'clusters_pf': 'clustersPf',  # noqa: E501
        'cluster_density': 'clusterDensity',  # noqa: E501
        'occupancy': 'occupancy',  # noqa: E501
        'percent_loading_concentration': 'percentLoadingConcentration',  # noqa: E501
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
    def __init__(self, num_cycles_index1, num_cycles_index2, num_cycles_read1, num_cycles_read2, num_lanes, num_reads, num_surfaces, num_swaths_per_lane, num_tiles_per_swath, *args, **kwargs):  # noqa: E501
        """RunSequencingStats - a model defined in OpenAPI

        Args:
            num_cycles_index1 (int):
            num_cycles_index2 (int):
            num_cycles_read1 (int):
            num_cycles_read2 (int):
            num_lanes (int):
            num_reads (int):
            num_surfaces (int):
            num_swaths_per_lane (int):
            num_tiles_per_swath (int):

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
            error_rate (float): [optional]  # noqa: E501
            error_rate_r1 (float): [optional]  # noqa: E501
            error_rate_r2 (float): [optional]  # noqa: E501
            intensity_cycle1 (float): [optional]  # noqa: E501
            is_indexed (bool): [optional]  # noqa: E501
            max_cycle_called (int): [optional]  # noqa: E501
            max_cycle_extracted (int): [optional]  # noqa: E501
            max_cycle_scored (int): [optional]  # noqa: E501
            min_cycle_called (int): [optional]  # noqa: E501
            min_cycle_extracted (int): [optional]  # noqa: E501
            min_cycle_scored (int): [optional]  # noqa: E501
            non_indexed_error_rate (float): [optional]  # noqa: E501
            non_indexed_intensity_cycle1 (float): [optional]  # noqa: E501
            non_indexed_percent_aligned (float): [optional]  # noqa: E501
            non_indexed_percent_gt_q30 (float): [optional]  # noqa: E501
            non_indexed_projected_total_yield (float): [optional]  # noqa: E501
            non_indexed_yield_total (float): [optional]  # noqa: E501
            percent_aligned (float): [optional]  # noqa: E501
            percent_gt_q30 (float): [optional]  # noqa: E501
            percent_gt_q30_last10_cycles (float): [optional]  # noqa: E501
            percent_gt_q30_r1 (float): [optional]  # noqa: E501
            percent_gt_q30_r2 (float): [optional]  # noqa: E501
            percent_pf (float): [optional]  # noqa: E501
            percent_resynthesis (float): [optional]  # noqa: E501
            phasing_r1 (float): [optional]  # noqa: E501
            phasing_r2 (float): [optional]  # noqa: E501
            pre_phasing_r1 (float): [optional]  # noqa: E501
            pre_phasing_r2 (float): [optional]  # noqa: E501
            projected_total_yield (float): [optional]  # noqa: E501
            reads_pf_total (int): [optional]  # noqa: E501
            reads_total (int): [optional]  # noqa: E501
            yield_total (float): [optional]  # noqa: E501
            clusters (int): [optional]  # noqa: E501
            clusters_pf (int): [optional]  # noqa: E501
            cluster_density (float): [optional]  # noqa: E501
            occupancy (float): [optional]  # noqa: E501
            percent_loading_concentration (float): [optional]  # noqa: E501
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

        self.num_cycles_index1 = num_cycles_index1
        self.num_cycles_index2 = num_cycles_index2
        self.num_cycles_read1 = num_cycles_read1
        self.num_cycles_read2 = num_cycles_read2
        self.num_lanes = num_lanes
        self.num_reads = num_reads
        self.num_surfaces = num_surfaces
        self.num_swaths_per_lane = num_swaths_per_lane
        self.num_tiles_per_swath = num_tiles_per_swath
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
