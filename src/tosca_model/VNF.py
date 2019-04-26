from tosca_model import ToscaElement


class VNF(ToscaElement):
    def __init__(self, elem_type):
        super().__init__(elem_type)

        self.id = None
        self.version = None
        self.provider = None
