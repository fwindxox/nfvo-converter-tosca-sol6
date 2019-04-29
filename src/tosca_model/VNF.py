from tosca_model import ToscaElement
from tools import *


class VNF(ToscaElement):
    def __init__(self, elem_type):
        super().__init__(elem_type, type(self).__name__)

        self.descriptor_id                  = None
        self.descriptor_version             = None
        self.provider                       = None
        self.product_name                   = None
        self.software_version               = None
        self.product_info_name              = None
        self.product_info_description       = None
        self.vnfm_info                      = None
        self.localization_languages         = None
        self.default_localization_language  = None
        self.configurable_properties        = None
        self.modifiable_attributes          = None
        self.lcm_operations_configuration   = None
        self.monitoring_parameters          = None
        self.flavour_id                     = None
        self.flavour_description            = None
        self.vnf_profile                    = None

        self.all_vars = list(vars(self).keys())

    def read_data_from_input(self, input_data):
        # Strip the top element, because it's not super important
        input_stripped = input_data[get_dict_key(input_data)]
        # Make this shorter
        val = lambda x: get_path_value(PathFormatter.path(x), input_stripped, must_exist=PathFormatter.req(x),
                                       no_msg=PathFormatter.no_msg(x))

        self.descriptor_id                  = val(VNFPaths.descriptor_id)
        self.descriptor_version             = val(VNFPaths.descriptor_version)
        self.provider                       = val(VNFPaths.provider)
        self.product_name                   = val(VNFPaths.product_name)
        self.software_version               = val(VNFPaths.software_version)
        self.product_info_name              = val(VNFPaths.product_info_name)
        self.product_info_description       = val(VNFPaths.product_info_description)
        self.vnfm_info                      = val(VNFPaths.vnfm_info)
        self.localization_languages         = val(VNFPaths.localization_languages)
        self.default_localization_language  = val(VNFPaths.default_localization_language)
        self.configurable_properties        = val(VNFPaths.configurable_properties)
        self.modifiable_attributes          = val(VNFPaths.modifiable_attributes)
        self.lcm_operations_configuration   = val(VNFPaths.lcm_operations_configuration)
        self.monitoring_parameters          = val(VNFPaths.monitoring_parameters)
        self.flavour_id                     = val(VNFPaths.flavour_id)
        self.flavour_description            = val(VNFPaths.flavour_description)
        self.vnf_profile                    = val(VNFPaths.vnf_profile)

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

    properties                      = "properties"
    set_root(properties)

    # Name                          = Path                                      Req     No message on missing
    descriptor_id                   = fmt("descriptor_id"),                     True
    descriptor_version              = fmt("descriptor_version"),                True
    provider                        = fmt("provider"),                          True
    product_name                    = fmt("product_name"),                      True
    software_version                = fmt("software_version"),                  True
    product_info_name               = fmt("product_info_name"),                 False
    product_info_description        = fmt("product_info_description"),          False
    vnfm_info                       = fmt("vnfm_info"),                         True
    localization_languages          = fmt("localization_languages"),            False
    default_localization_language   = fmt("default_localization_language"),     False
    configurable_properties         = fmt("configurable_properties"),           False
    modifiable_attributes           = fmt("modifiable_attributes"),             False
    lcm_operations_configuration    = fmt("lcm_operations_configuration"),      False
    monitoring_parameters           = fmt("monitoring_parameters"),             False
    flavour_id                      = fmt("flavour_id"),                        True
    flavour_description             = fmt("flavour_description"),               True
    vnf_profile                     = fmt("vnf_profile"),                       False,  False
