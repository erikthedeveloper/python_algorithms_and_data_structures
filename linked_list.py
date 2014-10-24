from uuc import UnorderedUniqueContainer
from node import Node


class LinkedList(UnorderedUniqueContainer):
    """
    :type first: Node
    """

    def __init__(self):
        self.first = None
        self.node_count = 0

    def get_first(self):
        return self.first

    def set_first(self, node):
        """
        :param node:
        :type node: Node
        """
        self.first = node

    def insert(self, item):
        new_node = Node()
        new_node.set_item(item)

        if self.first is not None:
            new_node.set_next(self.first)
        self.set_first(new_node)
        self.node_count += 1

    def size(self):
        return self.node_count