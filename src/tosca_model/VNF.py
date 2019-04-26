from tosca_model import ToscaModel


class VNF(ToscaModel):
    def __init__(self):
        super()
        self.type = "cisco.1VDU.1_0.1_0"
        self.id = None
        self.version = None
        self.provider = None
