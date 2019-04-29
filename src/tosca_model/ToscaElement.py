from abc import abstractmethod


class ToscaElement:
    def __init__(self, elem_type, class_name):
        self.elem_type = elem_type
        self.elem_name = class_name

    @abstractmethod
    def read_data_from_input(self, input_data):
        pass

    def __str__(self):
        return "{}, {}".format(self.elem_name, self.elem_type)
