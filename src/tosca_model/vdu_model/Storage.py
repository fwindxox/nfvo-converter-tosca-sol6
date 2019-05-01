from tosca_model import ToscaElement


class Storage(ToscaElement):
    def __init__(self, elem_type, parent_elem=None):
        super().__init__(elem_type, "VDU_STORAGE", parent_elem=parent_elem)

    def read_data_from_input(self, input_data):
        print("Storage read")
        print(input_data)

    def __str__(self):
        return super().__str__()
