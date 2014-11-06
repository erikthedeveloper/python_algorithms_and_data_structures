import unittest
from bst import Bst


class TestBst(unittest.TestCase):
    def test_inserting_item_into_empty_container(self):
        linked_list = Bst()
        some_item = {'foo': 'bar'}
        linked_list.insert(some_item)
        self.assertEqual(some_item, linked_list.get_first().item)

    def test_container_size_is_represented(self):
        linked_list = Bst()
        self.assertEqual(0, linked_list.size())
        linked_list.insert({'foo': 'bar'})
        self.assertEqual(1, linked_list.size())
        linked_list.insert({'bar': 'foo'})
        self.assertEqual(2, linked_list.size())

    def test_finding_an_existing_element(self):
        linked_list = Bst()
        the_item = {'foo': 'bar'}
        self.assertFalse(linked_list.exists(the_item))
        linked_list.insert(the_item)
        self.assertTrue(linked_list.exists(the_item))

    def test_deleting_an_item(self):
        linked_list = Bst()

        delete_me = {'foo4': 'bar'}
        linked_list.insert({'foo2': 'bar'})
        linked_list.insert({'foo3': 'bar'})

        self.assertFalse(linked_list.delete(delete_me))

        linked_list.insert(delete_me)
        linked_list.insert({'foo5': 'bar'})

        self.assertTrue(linked_list.delete(delete_me))

    def test_deleting_an_item_when_it_is_the_first_item(self):
        linked_list = Bst()
        delete_me = {'foo4': 'bar'}

        linked_list.insert({'foo2': 'bar'})
        linked_list.insert({'foo3': 'bar'})
        linked_list.insert({'foo5': 'bar'})
        linked_list.insert(delete_me)
        self.assertTrue(linked_list.delete(delete_me))

    def test_deleting_an_item_when_it_is_the_last_item(self):
        linked_list = Bst()
        delete_me = {'foo4': 'bar'}

        linked_list.insert(delete_me)
        linked_list.insert({'foo2': 'bar'})
        linked_list.insert({'foo3': 'bar'})
        linked_list.insert({'foo5': 'bar'})
        self.assertTrue(linked_list.delete(delete_me))

    def test_traverse_method(self):
        linked_list = Bst()

        the_string = "A nasty string   "
        linked_list.insert(the_string)
        self.assertEqual(the_string, linked_list.get_first().item)

        linked_list.traverse(lambda string_item: string_item.rstrip())

        self.assertEqual(the_string.rstrip(), linked_list.get_first().item)

    def test_exists_method(self):
        linked_list = Bst()
        find_me = {'foo4': 'bar', 'bar': 123}

        self.assertFalse(linked_list.exists(find_me))

        linked_list.insert(find_me)
        self.assertTrue(linked_list.exists(find_me))

    def test_retrieve_method(self):
        linked_list = Bst()
        find_me = {'foo4': 'bar', 'bar': 123}

        self.assertFalse(linked_list.retrieve(find_me))

        linked_list.insert(find_me)
        self.assertEqual(find_me, linked_list.retrieve(find_me))




if __name__ == '__main__':
    unittest.main()