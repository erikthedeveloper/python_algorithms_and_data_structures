import unittest
from bst import Bst


class TestBst(unittest.TestCase):
    def test_container_size_is_represented(self):
        bst = Bst()
        self.assertEqual(0, bst.size())
        bst.insert({'foo': 'bar'})
        self.assertEqual(1, bst.size())
        bst.insert({'bar': 'foo'})
        self.assertEqual(2, bst.size())

    # def test_inserting_item_into_empty_container(self):
    #     bst = Bst()
    #     some_item = {'foo': 'bar'}
    #     bst.insert(some_item)
    #     self.assertEqual(some_item, bst.get_first().item)
    #
    # def test_finding_an_existing_element(self):
    #     bst = Bst()
    #     the_item = {'foo': 'bar'}
    #     self.assertFalse(bst.exists(the_item))
    #     bst.insert(the_item)
    #     self.assertTrue(bst.exists(the_item))
    #
    # def test_deleting_an_item(self):
    #     bst = Bst()
    #
    #     delete_me = {'foo4': 'bar'}
    #     bst.insert({'foo2': 'bar'})
    #     bst.insert({'foo3': 'bar'})
    #
    #     self.assertFalse(bst.delete(delete_me))
    #
    #     bst.insert(delete_me)
    #     bst.insert({'foo5': 'bar'})
    #
    #     self.assertTrue(bst.delete(delete_me))
    #
    # def test_traverse_method(self):
    #     bst = Bst()
    #
    #     characters = ["a", "b", "c"]
    #     for c in characters:
    #         bst.insert(c)
    #
    #     the_traversed_string = ""
    #     # bst.traverse(lambda current_item: the_traversed_string)
    #     self.assertEqual("abc", the_traversed_string)
    #
    # def test_exists_method(self):
    #     bst = Bst()
    #     find_me = {'foo4': 'bar', 'bar': 123}
    #
    #     self.assertFalse(bst.exists(find_me))
    #
    #     bst.insert(find_me)
    #     self.assertTrue(bst.exists(find_me))
    #
    # def test_retrieve_method(self):
    #     bst = Bst()
    #     find_me = {'foo4': 'bar', 'bar': 123}
    #
    #     self.assertFalse(bst.retrieve(find_me))
    #
    #     bst.insert(find_me)
    #     self.assertEqual(find_me, bst.retrieve(find_me))




if __name__ == '__main__':
    unittest.main()