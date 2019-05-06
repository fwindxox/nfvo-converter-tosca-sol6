from xml.dom import minidom


class Sol6Writer:
    def __init__(self, tosca_model):
        self.tosca_model = tosca_model

    def write(self, file_name):
        print("Write to {}...".format(file_name))
