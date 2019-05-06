from tosca_model import ToscaElement
from tools import PathFormatter
from tools.dict_utils import *


class VDU(ToscaElement):
    def __init__(self, elem_type, vdu_id, parent_elem=None):
        super().__init__(elem_type, "VDU_COMPUTE", parent_elem=parent_elem)
        self.vdu_id = vdu_id
        self.compute = None
        self.storage = []
        self.connection_point = None

    def read_data_from_input(self, input_data):
        # Determine our place in the heirarchy
        # We have a vdu_id that is unique across all VDU comput elements,
        # but might not necessarily be connected to the same ordering of the other elements, such as storage
        # So we need to determine unambiguously what compute element is ours, and determine connectivity here before
        # we pass the data down to the components

        # Easy first step, just associate the vdu_id to the given element in the list
        self.assoc_data = input_data[self.elem_name][self.vdu_id]
        self.dict_name = get_dict_key(self.assoc_data)

        # The compute element is the *actual* node that will have the structure in it
        self.compute.read_data_from_input(self.assoc_data)

        self._init_subelems(input_data)

    def _init_subelems(self, input_data):
        # Determine linking
        # Get the array indexes of all the referenced storage volumes
        cur_storage_ids = self._get_linked_storage(input_data)

        # Since we start with only one storage object, we need to copy it
        to_copy = self.storage[0].copy()

        # Clear out the storage array, although I'm not sure if this is needed
        self.storage = []
        for cur_id in cur_storage_ids:
            self.storage.append(to_copy.copy())
            self.storage[-1].read_data_from_input(input_data[to_copy.elem_name][cur_id])

        # if self.connection_point and self.connection_point.elem_name in input_data:
        #    self.connection_point.read_data_from_input(input_data[self.connection_point.elem_name])

    def _get_linked_storage(self, input_data):
        """
        Return the index of the storage node that is used in the current compute node
        """
        res = []

        # Get all storage names
        # We can consider the first element as representative for all the names because we only support one name or type
        # per type of element
        storage_names = [get_dict_key(x) for x in input_data[self.storage[0].elem_name]]

        if not storage_names:
            return [-1]

        possible_storages = []
        # Do a dumb search across the compute node for storage names
        for s in storage_names:
            compute_refs = get_roots_from_filter(self.assoc_data, child_value=s)
            # Technically this storage volume *could* show up and not actually be a part of this compute
            # I don't think that's super likely, but handle it in the future
            if compute_refs:
                possible_storages.append(s)

        # Return a list of indexes from the main list
        for cur in possible_storages:
            res.append(storage_names.index(cur))

        log.debug("Storage {}: {}".format(self.dict_name, res))
        if res:
            return res
        return [-1]

    def _get_linked_connection_points(self, input_data):
        return -1

    def __str__(self):
        return str(self.compute)
