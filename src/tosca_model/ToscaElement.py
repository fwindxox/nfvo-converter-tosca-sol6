from abc import abstractmethod


class ToscaElement:
    def __init__(self, elem_type, class_name, parent_elem=None):
        self.elem_type = elem_type
        self.elem_name = class_name
        self.assoc_data = None
        # We want to be able to access the full model from inside any part, so structuring it
        # as a tree makes sense, especially since we deal with locations in a very relational way
        self.parent_elem = parent_elem
        # We usually strip this out when we process input, but save it before that
        self.dict_name = None
        self.suppress_notfound = False

    @abstractmethod
    def read_data_from_input(self, input_data):
        pass

    def __str__(self):
        return "{}, {}".format(self.elem_name, self.elem_type)

    def copy(self, copy_to=None):
        if not copy_to:
            copy_to = ToscaElement(self.elem_type, self.elem_name, parent_elem=self.parent_elem)
        copy_to.assoc_data = self.assoc_data
        copy_to.dict_name = self.dict_name
        copy_to.suppress_notfound = self.suppress_notfound

        return copy_to
