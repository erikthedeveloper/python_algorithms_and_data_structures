# https://gist.github.com/erikthedeveloper/f7d9e115537339fcceb6

from uuc import UnorderedUniqueContainer


class Bst(UnorderedUniqueContainer):
    def __init__(self):
        self._size = 0
        self._root = None
        pass

    def retrieve(self, dummy_item):
        if self._root is None:
            return False
        return self._root.retrieve(dummy_item)

    def size(self):
        return self._size

    def exists(self, dummy_item):
        return bool(self.retrieve(dummy_item))

    def traverse(self, callback):
        pass

    def insert(self, item):
        if self._root is None:
            self._root = BstNode(item)
        else:
            self._root.insert(item)
        self._size += 1
        return True

    def delete(self, item):
        self._size -= 1
        return True


class BstNode:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item

    def insert(self, item):
        # Enforce Uniqueness TODO: Use self.exists(item)
        if item == self.item:
            return False
        if item < self.item:
            if self.left is None:
                self.left = BstNode(item)
            else:
                self.left.insert(item)
        elif item > self.item:
            if self.right is None:
                self.right = BstNode(item)
            else:
                self.right.insert(item)

    def retrieve(self, dummy_item):
        if dummy_item == self.item:
            return self.item
        if dummy_item < self.item:
            if self.left is None:
                return self.item
            else:
                return self.left.retrieve(dummy_item)
        elif dummy_item > self.item:
            if self.right is None:
                return self.item
            else:
                return self.right.retrieve(dummy_item)
        return False

    def is_leaf(self):
        return self.left is None and self.right is None

