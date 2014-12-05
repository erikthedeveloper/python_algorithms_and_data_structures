"""
Table Size ~= 2 * Data Set Size

"""

from uuc import UnorderedUniqueContainer
import math


def is_prime(n):
    """
    :type n: int
    :rtype: bool
    """
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    square_root = int(math.sqrt(n))
    for i in range(3, square_root + 1, 2):
        if n % i == 0:
            return False
    return True


class HashTable(UnorderedUniqueContainer):
    def __init__(self, data_size):
        """
        :param data_size: The size of the data to be stored
        :type data_size: int
        """
        self._item_count = 0

        table_size = data_size * 2 + 1
        while not is_prime(table_size):
            table_size += 2
        self.table_size = table_size
        self.table = [None] * self.table_size

    def size(self):
        return self._item_count

    def insert(self, item):
        the_index = self._index_from_int_able(item)
        while self.table[the_index] is not None:
            if self.table[the_index] == item:
                return False
            the_index = (the_index + 1) + (the_index % self.table_size)

        self.table[the_index] = item
        self._item_count += 1
        return True

    def traverse(self, callable_method):
        for i in range(self.table_size):
            if self.table[i]:
                callable_method(self.table[i])
        return True

    def delete(self, dummy_item):
        the_index = self._index_from_int_able(dummy_item)
        while self.table[the_index] is not None:
            if self.table[the_index] == dummy_item:
                self.table[the_index] = None
                self._item_count -= 1
                return True
            the_index = (the_index + 1) + (the_index % self.table_size)
        return False

    def retrieve(self, dummy_item):
        the_index = self._index_from_int_able(dummy_item)
        while self.table[the_index] is not None:
            if self.table[the_index] == dummy_item:
                return self.table[the_index]
            the_index = (the_index + 1) + (the_index % self.table_size)
        return False

    def exists(self, dummy_item):
        return self.retrieve(dummy_item) is not False

    def _index_from_int_able(self, dummy_item):
        the_index = int(dummy_item) % self.table_size
        return the_index
