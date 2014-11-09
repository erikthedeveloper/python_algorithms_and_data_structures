# https://gist.github.com/erikthedeveloper/f7d9e115537339fcceb6

from uuc import UnorderedUniqueContainer


class Bst(UnorderedUniqueContainer):
    def __init__(self):
        self._root = None
        pass

    def retrieve(self, dummy_item):
        if self._root is None:
            return False
        return self._root.retrieve(dummy_item)

    def size(self):
        if self._root:
            return self._root.size()
        return 0

    def exists(self, dummy_item):
        return bool(self.retrieve(dummy_item))

    def traverse(self, callback):
        pass

    def insert(self, item):
        if self._root is None:
            self._root = BstNode(item)
        else:
            self._root.insert(item)
        return True

    def delete(self, dummy_item):
        if not self.exists(dummy_item) or self.empty():
            return False

        if self._root.item == dummy_item:
            self._root = None
            # raise Exception("Found it! It was the root!")
            return True

        # TODO: Rethink size() ... pass bst into node... or track size() for each Node?
        delete_me = self._root.retrieve_node(dummy_item)
        return delete_me.delete()

    def empty(self):
        return self.size() == 0


class BstNode:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item

    def size(self):
        size = 1
        if self.left:
            size += self.left.size()
        if self.right:
            size += self.right.size()
        return size

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

    def retrieve_node(self, dummy_item):
        if dummy_item == self.item:
            return self
        if dummy_item < self.item:
            if self.left is None:
                return self
            else:
                return self.left.retrieve_node(dummy_item)
        elif dummy_item > self.item:
            if self.right is None:
                return self
            else:
                return self.right.retrieve_node(dummy_item)
        return False

    def retrieve(self, dummy_item):
        result_node = self.retrieve_node(dummy_item)
        if result_node:
            return result_node.item
        else:
            return False

    def delete(self, dummy_item):
        if self.is_leaf_node():
            raise Exception("Attempting to delete self (as leaf_node)!")
        # To delete self
            # Find successor and replace self.item with successor.item
            # Call delete successor
        return

    def is_leaf_node(self):
        return self.left is None and self.right is None

