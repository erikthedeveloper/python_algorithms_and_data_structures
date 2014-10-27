import unittest
from linked_list import LinkedList


class TestMyStack(unittest.TestCase):
    def test_inserting_item_into_empty_container(self):
        linked_list = LinkedList()
        some_item = {'foo': 'bar'}
        linked_list.insert(some_item)
        self.assertEqual(some_item, linked_list.get_first().item)

    # # TODO: test_delete(self, item):

    ## TODO: test_retrieve(self, item):

    ## TODO: test_traverse(self, callback):

    def test_container_size_is_represented(self):
        linked_list = LinkedList()
        self.assertEqual(0, linked_list.size())
        linked_list.insert({'foo': 'bar'})
        self.assertEqual(1, linked_list.size())
        linked_list.insert({'bar': 'foo'})
        self.assertEqual(2, linked_list.size())

        ## TODO: test_exists(self, item):


if __name__ == '__main__':
    unittest.main()