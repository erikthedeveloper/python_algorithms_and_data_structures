import abc


class UnorderedUniqueContainer:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    def insert(self, item):
        raise Exception('Not yet implemented!')

    def delete(self, item):
        # dummy_item
        raise Exception('Not yet implemented!')

    def retrieve(self, item):
        # dummy_item
        raise Exception('Not yet implemented!')

    def traverse(self, callback):
        """
        This method should do something great!
        """
        return

    @abc.abstractmethod
    def size(self):
        """
        This method should do something great!
        """
        return

    def exists(self, item):
        # dummy_item
        raise Exception('Not yet implemented!')
