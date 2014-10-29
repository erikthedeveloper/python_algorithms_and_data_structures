import unittest
from linked_list import LinkedList


class TestMyStack(unittest.TestCase):
    def test_inserting_item_into_empty_container(self):
        linked_list = LinkedList()
        some_item = {'foo': 'bar'}
        linked_list.insert(some_item)
        self.assertEqual(some_item, linked_list.get_first().item)

    def test_container_size_is_represented(self):
        linked_list = LinkedList()
        self.assertEqual(0, linked_list.size())
        linked_list.insert({'foo': 'bar'})
        self.assertEqual(1, linked_list.size())
        linked_list.insert({'bar': 'foo'})
        self.assertEqual(2, linked_list.size())

    def test_finding_an_existing_element(self):
        linked_list = LinkedList()
        the_item = {'foo': 'bar'}
        self.assertFalse(linked_list.exists(the_item))
        linked_list.insert(the_item)
        self.assertTrue(linked_list.exists(the_item))

    def test_deleting_an_item(self):
        linked_list = LinkedList()

        delete_me = {'foo4': 'bar'}
        linked_list.insert({'foo2': 'bar'})
        linked_list.insert({'foo3': 'bar'})

        self.assertFalse(linked_list.delete(delete_me))

        linked_list.insert(delete_me)
        linked_list.insert({'foo5': 'bar'})

        self.assertTrue(linked_list.delete(delete_me))

    def test_deleting_an_item_when_it_is_the_first_item(self):
        linked_list = LinkedList()
        delete_me = {'foo4': 'bar'}

        linked_list.insert({'foo2': 'bar'})
        linked_list.insert({'foo3': 'bar'})
        linked_list.insert({'foo5': 'bar'})
        linked_list.insert(delete_me)
        self.assertTrue(linked_list.delete(delete_me))

    def test_deleting_an_item_when_it_is_the_last_item(self):
        linked_list = LinkedList()
        delete_me = {'foo4': 'bar'}

        linked_list.insert(delete_me)
        linked_list.insert({'foo2': 'bar'})
        linked_list.insert({'foo3': 'bar'})
        linked_list.insert({'foo5': 'bar'})
        self.assertTrue(linked_list.delete(delete_me))

    # TODO: test traverse(callback)

    # TODO: test_exists(self, item):

    # TODO: test_retrieve(self, item):




if __name__ == '__main__':
    unittest.main()