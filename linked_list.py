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
        new_node = Node()
        new_node.set_item(item)

        if self.get_first() is not None:
            new_node.set_next(self.first)
        self.set_first(new_node)
        self._node_count += 1

    def size(self):
        return self._node_count