import tosca_model
import lxml.etree as etree
import sys


class Sol6Writer:
    def __init__(self, model):
        self.model = model  # type: tosca_model.ToscaModel

    def write(self, file_name):
        print("Write to {}...".format(file_name))

        ns_etsi = "http://tailf.com/ns/etsi-nfv-descriptors"

        # Create the base structure
        data = etree.Element("data", nsmap={None: "http://tail-f.com/ns/config/1.0"})
        nfv = etree.SubElement(data, "nfv", nsmap={None: "urn:etsi:nfv:yang:etsi-nfv-descriptors"})
        vnfd = etree.SubElement(nfv, "vnfd")

        VNF = self.model.VNF

        add_child(vnfd, "id", VNF.descriptor_id)
        add_child(vnfd, "provider", VNF.provider)
        add_child(vnfd, "product", VNF.product_name)
        add_child(vnfd, "software-version", VNF.software_version)
        add_child(vnfd, "version", VNF.descriptor_version)
        add_child(vnfd, "product-info-name", VNF.product_info_name)
        add_child(vnfd, "product-info-description", VNF.product_info_description)
        add_child(vnfd, "vnfm-info", VNF.vnfm_info)

        with open(file_name, 'wb') as f:
            f.write(etree.tostring(data, pretty_print=True, xml_declaration=True))


def add_child(parent, name, value=""):
    if not value and value is not 0:
        return
    temp = etree.SubElement(parent, name)
    temp.text = str(value)
