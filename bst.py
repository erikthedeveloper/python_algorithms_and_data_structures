# https://gist.github.com/erikthedeveloper/f7d9e115537339fcceb6

from uuc import UnorderedUniqueContainer


class Bst(UnorderedUniqueContainer):
    def __init__(self):
        self._root = None

    def retrieve(self, dummy_item):
        if self.empty():
            return False
        return self._root.retrieve(dummy_item)

    def size(self):
        if self.empty():
            return 0
        return self._root.size()

    def exists(self, dummy_item):
        if self.empty():
            return False
        return bool(self._root.exists(dummy_item))

    def traverse(self, callback):
        pass

    def insert(self, item):
        if self.empty():
            self._root = BstNode(item)
            return True
        else:
            return self._root.insert(item)

    def delete(self, dummy_item):
        if not self.exists(dummy_item):
            return False

        if self._root.item == dummy_item:
            # Found it! It was the root!
            self._root = None
            return True

        # TODO: Delete that!
        delete_me = self._root.retrieve_node(dummy_item)
        return delete_me.delete()

    def empty(self):
        return self._root is None


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

    def exists(self, dummy_item):
        return bool(self.retrieve_node(dummy_item))

    def insert(self, item):
        # Enforce Uniqueness TODO: Use self.exists(item)
        if item == self.item:
            return False
        if item < self.item:
            if self.left is None:
                self.left = BstNode(item)
                return True
            else:
                return self.left.insert(item)
        elif item > self.item:
            if self.right is None:
                self.right = BstNode(item)
                return True
            else:
                return self.right.insert(item)

    def retrieve_node(self, dummy_item):
        if dummy_item == self.item:
            return self

        if dummy_item < self.item:
            if self.left is None:
                return False
            else:
                return self.left.retrieve_node(dummy_item)
        elif dummy_item > self.item:
            if self.right is None:
                return False
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

