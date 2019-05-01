from tosca_model import ToscaElement


class Compute(ToscaElement):
    def __init__(self, elem_type):
        super().__init__(elem_type, "VDU_COMPUTE")

    def read_data_from_input(self, input_data):
        print("Compute read")
        print(input_data)

    def __str__(self):
        return super().__str__()
