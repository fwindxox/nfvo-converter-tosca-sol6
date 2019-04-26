from tosca_model import *
import yaml
import logging
logger = logging.getLogger(__name__)


class BuildModelTosca:

    def __init__(self, input_file, output_file, config_file):
        self.input_file = input_file
        self.output_file = output_file
        self.config_file = config_file
        self.input = None
        self.config = None
        self.tosca_model = None

    def build(self):
        # Read all the files we need to
        self.input = self._read(self.input_file)
        self.config = self._read(self.config_file)

        # Initialize the model where we're going to store everything
        self.tosca_model = ToscaModel()
        # Tell the model what the types of the varying elements are
        self.tosca_model.set_types_from_config(self.config["TOSCA_TYPES"])

    @staticmethod
    def _read(file):
        # Read incoming yaml
        with open(file, "r") as f:
            try:
                return yaml.safe_load(f)
            except yaml.YAMLError as exc:
                logger.error(exc)
