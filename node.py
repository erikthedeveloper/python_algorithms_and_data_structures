class Node:
    """
    Node implementation
    """

    def __init__(self):
        self.item = None
        self.next = None

    def get_item(self):
        return self.item

    def set_item(self, item):
        self.item = item

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next