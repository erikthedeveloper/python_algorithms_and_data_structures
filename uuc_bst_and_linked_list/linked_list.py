from uuc import UnorderedUniqueContainer


class LinkedList(UnorderedUniqueContainer):

    def __init__(self):
        self._first = None
        self._node_count = 0

    def insert(self, item):
        if self.exists(item):
            return False

        new_node = Node(item)

        if self._first is not None:
            new_node.next = self._first
        self._first = new_node
        self._node_count += 1
        return True

    def traverse(self, callback):
        current = self._first
        while current:
            callback(current.item)
            current = current.next

    def delete(self, dummy_item):
        if self._first is None:
            return False

        current = self._first
        if current.item == dummy_item:
            self._first = current.next
            self._node_count -= 1
            return True

        while current.next:
            if current.next.item == dummy_item:
                current.next = current.next.next
                self._node_count -= 1
                return True
            current = current.next
        return False

    def retrieve(self, dummy_item):
        if not self.exists(dummy_item):
            return False

        retrieved_item = False
        current = self._first
        while current:
            if current.item == dummy_item:
                retrieved_item = current.item
                break
            current = current.next
        return retrieved_item

    def exists(self, item):
        current = self._first
        while current:
            if current.item == item:
                return True
            current = current.next
        return False

    def size(self):
        return self._node_count


class Node:
    """
    Node implementation
    """

    def __init__(self, item):
        self.item = item
        self.next = None