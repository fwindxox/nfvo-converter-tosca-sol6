from tosca_model import ToscaElement
from tools import PathFormatter
from tools.dict_utils import *

class Compute(ToscaElement):
    def __init__(self, elem_type, parent_elem=None):
        super().__init__(elem_type, "VDU_COMPUTE", parent_elem=parent_elem)
        self.name                           = None
        self.description                    = None
        self.boot_order                     = None
        self.nfvi_constraints               = None
        self.monitoring_parameters          = None
        self.configurable_properties        = None
        self.boot_data                      = None
        self.vdu_profile                    = None
        self.sw_image_data                  = None
        self.virtual_storage                = None
        self.virtual_compute                = None
        self.virtual_binding                = None
        self.all_vars = list(vars(self).keys())

    def read_data_from_input(self, input_data):
        # Strip the top element, because it's not super important
        self.dict_name = get_dict_key(input_data)
        input_stripped = input_data[self.dict_name]
        # Make this shorter
        val = lambda x: get_path_value(PathFormatter.path(x), input_stripped, must_exist=PathFormatter.req(x),
                                       no_msg=PathFormatter.no_msg(x) or self.suppress_notfound)

        self.name                           = val(VNFPaths.name)
        self.description                    = val(VNFPaths.description)
        self.boot_order                     = val(VNFPaths.boot_order)
        self.nfvi_constraints               = val(VNFPaths.nfvi_constraints)
        self.monitoring_parameters          = val(VNFPaths.monitoring_parameters)
        self.configurable_properties        = val(VNFPaths.configurable_properties)
        self.boot_data                      = val(VNFPaths.boot_data)
        self.vdu_profile                    = val(VNFPaths.vdu_profile)
        self.sw_image_data                  = val(VNFPaths.sw_image_data)
        self.virtual_storage                = val(VNFPaths.virtual_storage)
        self.virtual_compute                = val(VNFPaths.virtual_compute)
        self.virtual_binding                = val(VNFPaths.virtual_binding)

    def __str__(self):
        # Just do a stupid loop through and get all the variables
        res = super().__str__()
        for var in self.all_vars:
            res = "{}, {}: {}".format(res, var, self.__dict__[var])
        return res


class VNFPaths:
    formatter = PathFormatter()
    fmt = formatter.fmt_last
    set_root = formatter.set_root

    set_root("properties")
    # Name                                  = Path                              Req     No message on missing
    name                                    = fmt("name"),                      True
    description                             = fmt("description"),               True
    boot_order                              = fmt("boot_order"),                False
    nfvi_constraints                        = fmt("nfvi_constraints"),          False
    monitoring_parameters                   = fmt("monitoring_parameters"),     False
    configurable_properties                 = fmt("configurable_properties"),   False
    boot_data                               = fmt("boot_data"),                 False
    vdu_profile                             = fmt("vdu_profile"),               True
    sw_image_data                           = fmt("sw_image_data"),             False

    set_root("requirements")
    virtual_storage                         = fmt("virtual_storage"),           False

    set_root("capabilities")
    virtual_compute                         = fmt("virtual_compute"),           False
    virtual_binding                         = fmt("virtual_binding"),           False
