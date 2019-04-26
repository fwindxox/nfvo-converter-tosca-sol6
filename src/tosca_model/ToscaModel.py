
class ToscaModel:

    def __init__(self):
        self.type = None
        # Initialize names of types here
        self.types = {
            "VNF": None,
            "VDU": None
        }

    def set_types_from_config(self, config):
        for t in self.types:
            if t not in config:
                continue
            self.types[t] = config[t]
        print(self.types)
