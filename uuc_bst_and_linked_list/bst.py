# https://gist.github.com/erikthedeveloper/f7d9e115537339fcceb6

from uuc import UnorderedUniqueContainer


class Bst(UnorderedUniqueContainer):
    def __init__(self):
        self._root = None

    def empty(self):
        return self._root is None

    def insert(self, item):
        if self.empty():
            self._root = BstNode(item)
            return True
        return self._root.insert(item)

    def retrieve(self, dummy_item):
        if self.empty():
            return False
        return self._root.retrieve(dummy_item)

    def delete(self, dummy_item):
        if not self.exists(dummy_item):
            return False
        if self._root.item == dummy_item:
            # Create a temporary "root" to encompass tree to accommodate for deleting root node as target
            temp_node = BstNode("foo")
            temp_node.left = self._root

            delete_success = self._root.delete(dummy_item, temp_node)

            # Set the "copied and altered" tree back to self._root
            self._root = temp_node.left
            return delete_success

        return self._root.delete(dummy_item, self._root)

    def traverse(self, callback):
        if self.empty():
            return False
        return self._root.traverse(callback)

    def exists(self, dummy_item):
        if self.empty():
            return False
        return bool(self._root.exists(dummy_item))

    def size(self):
        if self.empty():
            return 0
        return self._root.size()


class BstNode:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item

    def insert(self, item):
        if item < self.item:
            if self.left:
                return self.left.insert(item)
            self.left = BstNode(item)
            return True
        elif item > self.item:
            if self.right:
                return self.right.insert(item)
            self.right = BstNode(item)
            return True
        return False

    def retrieve_node(self, dummy_item):
        if dummy_item < self.item and self.left:
            return self.left.retrieve_node(dummy_item)
        elif dummy_item > self.item and self.right:
            return self.right.retrieve_node(dummy_item)
        elif dummy_item == self.item:
            return self
        return False

    def retrieve(self, dummy_item):
        result_node = self.retrieve_node(dummy_item)
        if result_node:
            return result_node.item
        return False

    def delete(self, dummy_item, parent):
        if self.item == dummy_item:
            if self.left and self.right:
                # TODO - Refactor: Always using the "least of the greater than" will lead to an unbalanced tree.
                self.item = self.right.smallest_child_node().item
                self.right.delete(self.item, self)
            elif parent.left == self:
                parent.left = self.left if self.left else self.right
            elif parent.right == self:
                parent.right = self.left if self.left else self.right
            # Leaf node case implicitly covered in above 2 cases (assigning parent.left to self.left when self.left = None)
            return True
        elif dummy_item < self.item and self.left:
            return self.left.delete(dummy_item, self)
        elif dummy_item > self.item and self.right:
            return self.right.delete(dummy_item, self)
        return False

    def traverse(self, callable_method):
        """
        Traversals
            In Order
                left, self, right
            Pre Order
                self, left, right
            Post Order
                left, right, self
        """
        # In order traversal
        if self.left:
            self.left.traverse(callable_method)
        callable_method(self.item)
        if self.right:
            self.right.traverse(callable_method)
        return True

    def smallest_child_node(self):
        if self.left:
            return self.left.smallest_child_node()
        return self

    def exists(self, dummy_item):
        return bool(self.retrieve_node(dummy_item))

    def size(self):
        size = 1
        if self.left:
            size += self.left.size()
        if self.right:
            size += self.right.size()
        return size

    def is_leaf_node(self):
        return self.left is None and self.right is None
