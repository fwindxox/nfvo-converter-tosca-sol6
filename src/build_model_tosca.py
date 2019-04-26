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

        # Initialize the model where we're going to store everything
        self.tosca_model = ToscaModel()
        # Tell the model what the types of the varying elements are
        self.tosca_model.set_types_from_config(self.config["TOSCA_TYPES"])
        self.partition_raw_input()
        self.init_elements()

        # Start getting values from the input file

    def partition_raw_input(self):
        """
        Get the raw data and assign it to self.raw_type_input under it's own dict entry list
        """
        for t in list(self.tosca_model.types.keys()):
            self.raw_type_input[t] = list(dict_utils.get_roots_from_filter(self.input, child_key="type",
                                                                           child_value=self.tosca_model.types[t]))

    def init_elements(self):
        """
        Initialize all the base elements with empty objects other than their types
        """

        self.tosca_model.VNF = VNF(self.tosca_model.types["VNF"])
        # Figure out how many of each element array we need
        # Create as many VDU objects as there are instances in the input array
        for i in range(len(self.raw_type_input["VDU"])):
            self.tosca_model.VDU.append(VDU(self.tosca_model.types["VDU"]))

    @staticmethod
    def _read(file):
        # Read incoming yaml
        with open(file, "r") as f:
            try:
                return yaml.safe_load(f)
            except yaml.YAMLError as exc:
                logger.error(exc)
