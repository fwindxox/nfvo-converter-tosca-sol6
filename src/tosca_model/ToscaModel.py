from tosca_model import *


class ToscaModel:

    def __init__(self):
        # Initialize names of types here
        self.types = {
            "VNF": None,
            "VDU": None,
            "VDU_COMPUTE": None,
            "VDU_STORAGE": None,
            "VDU_CONNECTION_POINT": None
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

    def get_all_elements(self):
        """
        Get a flat list of all the ToscaElement objects contained in the model
        """
        res = [self.VNF]
        for vdu in self.VDU:
            # Add the VDU, which probably won't have much information in it
            # and the VDU elements, which should have the information
            res.append(vdu)

        return res

    def __str__(self):
        res = "VNF\n\t{}\n".format(self.VNF)
        vdus = ""
        for vdu in self.VDU:
            vdus += "VDU\n\t{}".format(str(vdu))
        res += vdus
        return res
