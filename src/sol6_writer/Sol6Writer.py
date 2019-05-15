from tosca_model import *
import lxml.etree as etree
import logging
logger = logging.getLogger(__name__)


class Sol6Writer:
    def __init__(self, model):
        self.model = model  # type: ToscaModel

    def write(self, file_name):
        logger.info("Write to {}...".format(file_name))

        ns_etsi = "http://tailf.com/ns/etsi-nfv-descriptors"

        # Create the base structure
        data = etree.Element("data", nsmap={None: "http://tail-f.com/ns/config/1.0"})
        nfv = etree.SubElement(data, "nfv", nsmap={None: "urn:etsi:nfv:yang:etsi-nfv-descriptors"})
        vnfd = etree.SubElement(nfv, "vnfd")

        # *********
        # ** VNF **
        # *********
        vnf = self.model.VNF

        add_child(vnfd, "id", vnf.descriptor_id)
        add_child(vnfd, "provider", vnf.provider)
        add_child(vnfd, "product", vnf.product_name)
        add_child(vnfd, "software-version", vnf.software_version)
        add_child(vnfd, "version", vnf.descriptor_version)
        add_child(vnfd, "product-info-name", vnf.product_info_name)
        add_child(vnfd, "product-info-description", vnf.product_info_description)
        # This is always a list
        add_child_list(vnfd, "vnfm-info", vnf.vnfm_info)

        # **********
        # ** VDUs **
        # **********
        for vdu in self.model.VDU:
            cur_vdu = add_child(vnfd, "vdu")
            add_child(cur_vdu, "id", vdu.compute.dict_name)
            add_child(cur_vdu, "name", vdu.compute.name)
            add_child(cur_vdu, "sw-image-desc", vdu.compute.sw_image_data)


        # Do the actual pretty-printing writing
        with open(file_name, 'wb') as f:
            f.write(etree.tostring(data, pretty_print=True, xml_declaration=True))


def add_child(parent, name, value=""):
    """ """
    # We don't want to try to add data if none is given, but we do still want to create the element
    if not value and value is not 0:
        return add_child_empty(parent, name)

    logger.debug("add_child: {}, {}, {}".format(parent, name, value))
    if isinstance(value, ToscaElement):
        logger.debug("add_child: value is a ToscaElement, calling to_tree_structure")
        return value.to_tree_structure(parent, name)

    temp = etree.SubElement(parent, name)
    temp.text = str(value)
    return temp


def add_child_empty(parent, name):
    # Separate this out for future-proofing
    return etree.SubElement(parent, name)


def add_child_list(parent, name, list_values):
    """ """
    logger.debug("add_child_list")
    for item in list_values:
        add_child(parent, name, item)
