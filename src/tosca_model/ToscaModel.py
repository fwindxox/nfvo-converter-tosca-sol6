from tosca_model import *


class ToscaModel:

    def __init__(self):
        # Initialize names of types here
        self.types = {
            "VNF": None,
            "VDU": None
        }

        # Initialize the blank fields for parts
        # If there is only one, then it's going to be an instance of a class
        self.VNF = None
        # If there can be multiple, then it's going to be an array of classes
        self.VDU = []

    def set_types_from_config(self, config):
        for t in self.types:
            if t not in config:
                continue
            self.types[t] = config[t]
