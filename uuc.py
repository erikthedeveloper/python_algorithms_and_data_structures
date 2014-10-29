import abc

# TODO: http://broken.build/2011/07/21/private-protected-and-public-in-python/
# TODO: http://pymotw.com/2/abc/
# TODO: http://pymotw.com/2/unittest/
# TODO: http://chimera.labs.oreilly.com/books/1230000000393/ch09.html

class UnorderedUniqueContainer:

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def insert(self, item):
        return

    @abc.abstractmethod
    def delete(self, item):  # dummy_item
        return

    @abc.abstractmethod
    def retrieve(self, item):  # dummy_item
        return

    @abc.abstractmethod
    def traverse(self, callback):
        return

    @abc.abstractmethod
    def size(self):
        return

    @abc.abstractmethod
    def exists(self, item):  # dummy_item
        return
