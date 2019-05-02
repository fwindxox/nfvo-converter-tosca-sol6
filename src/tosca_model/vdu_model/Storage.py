from tosca_model import ToscaElement
from tools import PathFormatter
from tools.dict_utils import *


class Storage(ToscaElement):
    def __init__(self, elem_type, parent_elem=None):
        super().__init__(elem_type, "VDU_STORAGE", parent_elem=parent_elem)
        self.virtual_block_storage_data     = None
        self.sw_image_data                  = None
        self.virtual_storage                = None

        self.all_vars = list(vars(self).keys())

    def read_data_from_input(self, input_data):
        # Strip the top element, because it's not super important
        self.dict_name = get_dict_key(input_data)
        input_stripped = input_data[self.dict_name]
        # Make this shorter
        val = lambda x: get_path_value(PathFormatter.path(x), input_stripped, must_exist=PathFormatter.req(x),
                                       no_msg=PathFormatter.no_msg(x) or self.suppress_notfound)

        self.virtual_block_storage_data     = val(VNFPaths.virtual_block_storage_data)
        self.sw_image_data                  = val(VNFPaths.sw_image_data)
        self.virtual_storage                = val(VNFPaths.virtual_storage)

    def __str__(self):
        # Just do a stupid loop through and get all the variables
        res = super().__str__()
        for var in self.all_vars:
            res = "{}, {}: {}".format(res, var, self.__dict__[var])
        return res

    def copy(self, copy_to=None):
        if not copy_to:
            copy_to = Storage(self.elem_type, parent_elem=self.parent_elem)
            copy_to = super().copy(copy_to=copy_to)

        copy_to.virtual_block_storage_data = self.virtual_block_storage_data
        copy_to.sw_image_data = self.sw_image_data
        copy_to.virtual_storage = self.virtual_storage
        copy_to.all_vars = self.all_vars
        return copy_to


class VNFPaths:
    formatter = PathFormatter()
    fmt = formatter.fmt_last
    set_root = formatter.set_root

    set_root("properties")
    # Name                                  = Path                                  Req     No message on missing
    virtual_block_storage_data              = fmt("virtual_block_storage_data"),    True
    sw_image_data                           = fmt("sw_image_data"),                 False

    set_root("capabilities")
    virtual_storage                         = fmt("virtual_storage"),               False
