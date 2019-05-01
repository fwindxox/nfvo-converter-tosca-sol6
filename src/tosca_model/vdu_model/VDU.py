from tosca_model import ToscaElement
from tools import PathFormatter


class VDU(ToscaElement):
    def __init__(self, elem_type, vdu_id, parent_elem=None):
        super().__init__(elem_type, "VDU_COMPUTE", parent_elem=parent_elem)
        self.vdu_id = vdu_id
        self.compute = None
        self.storage = None
        self.connection_point = None

    def read_data_from_input(self, input_data):
        # Determine our place in the heirarchy
        # We have a vdu_id that is unique across all VDU comput elements,
        # but might not necessarily be connected to the same ordering of the other elements, such as storage
        # So we need to determine unambiguously what compute element is ours, and determine connectivity here before
        # we pass the data down to the components

        # Easy first step, just associate the vdu_id to the given element in the list
        self.assoc_data = input_data[self.elem_name][self.vdu_id]

        # The compute element is the *actual* node that will have the structure in it
        self.compute.read_data_from_input(self.assoc_data)

        self._init_subelems(input_data)

    def _init_subelems(self, input_data):
        # Ensure our composite elements exst
        if self.storage and self.storage.elem_name in input_data:
            self.storage.read_data_from_input(input_data[self.storage.elem_name])
        if self.connection_point and self.connection_point.elem_name in input_data:
            self.connection_point.read_data_from_input(input_data[self.connection_point.elem_name])

    def __str__(self):
        return super().__str__()
