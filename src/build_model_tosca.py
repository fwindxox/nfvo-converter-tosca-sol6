from tosca_model import *
import yaml
import logging
from tools import dict_utils

logger = logging.getLogger(__name__)


class BuildModelTosca:

    def __init__(self, input_file, output_file, config_file):
        self.input_file = input_file
        self.output_file = output_file
        self.config_file = config_file
        self.input = None
        self.config = None
        self.tosca_model = None
        self.raw_type_input = {}

    def build(self):
        # Read all the files we need to
        self.input = self._read(self.input_file)
        self.config = self._read(self.config_file)

        # Try to figure out what the VNF type is automatically
        if "VNF" not in self.config["TOSCA_TYPES"]:
            # The 'vnf' type isn't required by tosca, so just try to do this
            try:
                self.config["TOSCA_TYPES"]["VNF"] = self.input["topology_template"]["node_templates"]["vnf"]["type"]
            except KeyError:
                # If we do get here then we can't continue because we require the VNF type
                raise ValueError("No type for 'VNF' found in config file")

        # Initialize the model where we're going to store everything
        self.tosca_model = ToscaModel()
        # Tell the model what the types of the varying elements are
        self.tosca_model.set_types_from_config(self.config["TOSCA_TYPES"])
        self.partition_raw_input()
        self.init_elements()
        self.process_input()

        # print(self.tosca_model)
        # Start getting values from the input file

    def partition_raw_input(self):
        """
        Get the raw data and assign it to self.raw_type_input under it's own dict entry list
        """
        for t in list(self.tosca_model.types.keys()):
            # Get all of the roots that have the type as a value
            self.raw_type_input[t] = list(dict_utils.get_roots_from_filter(self.input,
                                                                           child_value=self.tosca_model.types[t]))
            cur_input = self.raw_type_input[t]
            # We can't do just 'type': value because substitution mappings can have information in it that we
            # expect to be in node_templates
            if len(cur_input) == 1:
                continue
            # We have a list that has multiple elements
            # This can be a normal thing (for VDUs) or it can be something we need to handle
            # We want to merge the dict entries iff one of the elements has 'substitution_mapping' for the key
            for i, e in enumerate(cur_input):
                if "substitution_mappings" not in list(e.keys()):
                    continue
                # We have a substitution mapping we need to merge
                # Make sure we have somewhere to put the merged info
                # We want to put the the data into something that has "type":type
                self._partition_merge_substitution(dict(e), cur_input, t)

    def _partition_merge_substitution(self, e, cur_input, type_key):
        """
        We have found the element that has the data we need to merge into a singular other, non-same, element contianed
        inside cur_input that has "type":current_type
        """
        for i, elem in enumerate(cur_input):
            if e is elem:
                continue
            merge_target = dict_utils.get_roots_from_filter(elem, child_key="type",
                                                            child_value=self.tosca_model.types[type_key])
            if not merge_target:
                continue
            # The merge target should be valid, so let's merge the data
            # If there are multiple valid merge locations, then I have no idea what's going on, just pick the first one
            if len(merge_target) > 1:
                logger.warning("There are multiple merge targets for substitution_mappings type merging, and this isn't"
                               "handled.")
            if isinstance(merge_target, list):
                merge_target = merge_target[0]
            # Strip the top level from the target and e, snce we need to merge into the internals
            elem_key = dict_utils.get_dict_key(elem)
            merge_target_key = dict_utils.get_dict_key(merge_target)

            merge_target = merge_target[merge_target_key]
            strip_e = e[dict_utils.get_dict_key(e)]

            cur_input[i][elem_key] = dict_utils.merge_two_dicts(merge_target, strip_e)

        # Once we have merged all applicable instances into the VNFs, remove the substitution_mapping element
        cur_input.remove(e)

    def init_elements(self):
        """
        Initialize all the base elements with empty (other than their types) objects
        """

        self.tosca_model.VNF = VNF(self.tosca_model.types["VNF"])
        # Figure out how many of each element array we need
        # Create as many VDU objects as there are instances in the input array
        # Base this on the vdu compute nodes, since those are the "main" objects
        for i in range(len(self.raw_type_input["VDU_COMPUTE"])):
            cur_vdu = VDU(self.tosca_model.types["VDU"], i)

            cur_vdu.compute = Compute(self.tosca_model.types["VDU_COMPUTE"], parent_elem=cur_vdu)
            cur_vdu.storage = Storage(self.tosca_model.types["VDU_STORAGE"], parent_elem=cur_vdu)
            self.tosca_model.VDU.append(cur_vdu)

    def process_input(self):
        for elem in self.tosca_model.get_all_elements():
            if not elem:
                continue

            # Call the process method inherited from ToscaElement
            # Pass in the whole data because we can easily need the whole thing
            elem.read_data_from_input(self.raw_type_input)

    @staticmethod
    def _read(file):
        # Read incoming yaml
        with open(file, "r") as f:
            try:
                return yaml.safe_load(f)
            except yaml.YAMLError as exc:
                logger.error(exc)
