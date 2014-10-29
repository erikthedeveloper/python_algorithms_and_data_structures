from uuc import UnorderedUniqueContainer
from node import Node


class LinkedList(UnorderedUniqueContainer):
    """
    :type first: Node
    """

    def __init__(self):
        self._first = None
        self._node_count = 0

    def get_first(self):
        return self._first

    def set_first(self, node):
        """
        :param node:
        :type node: Node
        """
        self._first = node

    def insert(self, item):
        # Returns False on duplicate
        new_node = Node()
        new_node.set_item(item)

        if self.get_first() is not None:
            new_node.set_next(self.get_first())
        self.set_first(new_node)
        self._node_count += 1

    def traverse(self, callback):
        current = self.get_first()
        while current:
            callback(current.item)
            current = current.get_next()

    def delete(self, dummy_item):
        current = self.get_first()
        if current.item == dummy_item:
            self.set_first(current.next)
            return True

        while current.next:
            if current.next.item == dummy_item:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def retrieve(self):
        pass

    def exists(self, item):
        current = self.get_first()
        while current:
            if current.item == item:
                return True
            current = current.get_next()
        return False

    def size(self):
        return self._node_count

