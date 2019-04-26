from abc import abstractmethod


class ToscaElement:
    def __init__(self, elem_type):
        self.elem_type = elem_type

    @abstractmethod
    def read_data_from_input(self, input_data):
        pass
