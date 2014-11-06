from uuc import UnorderedUniqueContainer


class Bst(UnorderedUniqueContainer):
    def __init__(self):
        self._size = 0
        pass

    def retrieve(self, item):
        pass

    def size(self):
        return self._size

    def exists(self, item):
        pass

    def traverse(self, callback):
        pass

    def insert(self, item):
        self._size += 1
        pass

    def delete(self, item):
        self._size -= 1
        pass


class BstNode:
    def __init__(self):
        pass