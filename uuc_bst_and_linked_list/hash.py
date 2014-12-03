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
        :return:
        """
        table_size = data_size * 2 + 1
        while not is_prime(table_size):
            table_size += 2
        self.table_size = table_size

        self.table = []

    def exists(self, item):
        pass

    def size(self):
        pass

    def insert(self, key, item):
        index = self.key_to_hash(key)
        while self.table[index] is not None:
            # Duplicate Insert - Bad!!!
            if self.table[index] == item:
                return False
            index += 1
        self.table[index] = item
        return True

    def traverse(self, callback):
        pass

    def delete(self, item):
        pass

    def retrieve(self, item):
        pass

    def key_to_hash(self, key):
        return key % self.table_size
