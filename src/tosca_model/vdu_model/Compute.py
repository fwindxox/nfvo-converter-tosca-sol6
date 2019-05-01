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

    def read_data_from_input(self, input_data):
        print("Compute read")
        # Strip the top element, because it's not super important
        input_stripped = input_data[get_dict_key(input_data)]
        # Make this shorter
        val = lambda x: get_path_value(PathFormatter.path(x), input_stripped, must_exist=PathFormatter.req(x),
                                       no_msg=PathFormatter.no_msg(x))

        self.name                           = val(VNFPaths.name)

        print(self.name)

    def __str__(self):
        return super().__str__()


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
