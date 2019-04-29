from .dict_utils import SPLIT_CHAR


class PathFormatter:
    """
    Path formatting tool
    """
    def __init__(self):
        self.last_root = None

    # Do the parsing of the paths in a less verbose way
    @staticmethod
    def fmt(last, new):
        return "{}{}{}".format(last, SPLIT_CHAR, new)

    def fmt_last(self, new):
        return self.fmt(self.last_root, new)

    def set_root(self, r):
        self.last_root = r

    @staticmethod
    def path(tup):
        return tup[0]

    @staticmethod
    def req(tup):
        return tup[1]

    @staticmethod
    def no_msg(tup):
        return False if len(tup) < 3 else tup[2]
