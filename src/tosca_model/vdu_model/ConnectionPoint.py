from tosca_model import ToscaElement


class ConnectionPoint(ToscaElement):
    def __init__(self, elem_type):
        super().__init__(elem_type, type(self).__name__)

    def read_data_from_input(self, input_data):
        pass

    def __str__(self):
        return super().__str__()
