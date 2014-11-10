# https://gist.github.com/erikthedeveloper/f7d9e115537339fcceb6

import unittest

from bst import Bst, BstNode

from student import Student, StudentFactory


class TestBst(unittest.TestCase):
    def test_container_size_is_represented(self):
        bst = Bst()
        self.assertEqual(0, bst.size())
        bst.insert(Student("Doe", "Jane", "123-123-1234", "jane@gmail.com", 23))
        self.assertEqual(1, bst.size())
        bst.insert(Student("Doe", "John", "223-123-1234", "john@gmail.com", 23))
        self.assertEqual(2, bst.size())

    def test_inserting_unique_and_duplicate_items(self):
        bst = Bst()
        self.assertTrue(bst.insert("a"))
        self.assertTrue(bst.insert("b"))
        self.assertFalse(bst.insert("b"))
        self.assertTrue(bst.insert("c"))
        self.assertFalse(bst.insert("a"))
        self.assertEqual(3, bst.size())

    def test_finding_an_existing_element(self):
        bst = Bst()
        jane = Student("Doe", "Jane", "123-123-1234", "jane@gmail.com", 23)
        john = Student("Doe", "John", "223-123-1234", "john@gmail.com", 23)
        jake = Student("Doe", "Jake", "323-123-1234", "john@gmail.com", 23)

        dummy_john = StudentFactory.create_dummy_from_ssn("223-123-1234")

        self.assertFalse(bst.exists(dummy_john))

        bst.insert(jane)
        bst.insert(john)
        bst.insert(jake)

        self.assertEqual(john, bst.retrieve(dummy_john))
        self.assertTrue(bst.exists(dummy_john))

    def test_checking_if_an_item_exists(self):
        bst = Bst()
        find_me = {'foo4': 'bar', 'bar': 123}
        self.assertFalse(bst.exists(find_me))
        bst.insert(find_me)
        self.assertTrue(bst.exists(find_me))

    def test_deleting_an_item(self):
        bst = Bst()
        jane = Student("Doe", "Jane", "123-123-1234", "jane@gmail.com", 23)
        john = Student("Doe", "John", "223-123-1234", "john@gmail.com", 23)
        jake = Student("Doe", "Jake", "323-123-1234", "john@gmail.com", 23)

        dummy_john = StudentFactory.create_dummy_from_ssn("223-123-1234")

        self.assertFalse(bst.delete(dummy_john))

        bst.insert(jane)
        bst.insert(john)
        bst.insert(jake)

        self.assertEqual(3, bst.size())
        self.assertTrue(bst.delete(dummy_john))
        self.assertFalse(bst.exists(dummy_john))
        self.assertEqual(2, bst.size())

    def test_delete_under_more_complex_example(self):
        bst = Bst()
        # Comment out below as desired. Experiment like hell!
        numbers = [
            5,
            2,
            -4,
            3,
            12,
            9,
            21,
            19,
            25
        ]

        for n in numbers:
            bst.insert(n)

        self.assertEqual(len(numbers), bst.size())
        self.assertTrue(bst.exists(12))

        self.assertTrue(bst.delete(12))
        self.assertFalse(bst.delete(12))

        self.assertFalse(bst.exists(12))
        self.assertEqual(len(numbers) - 1, bst.size())

    def test_deleting_with_no_children(self):
        bst = Bst()
        # Comment out below as desired. Experiment like hell!
        numbers = [
            5,  # 1
            12, # 2
            9,  # 1
            7,  # 0
            21, # 2
            19, # 0
            25  # 0
        ]

        for n in numbers:
            bst.insert(n)

        target = 7

        self.assertEqual(len(numbers), bst.size())
        self.assertTrue(bst.exists(target))

        self.assertTrue(bst.delete(target))
        self.assertFalse(bst.delete(target))

        self.assertFalse(bst.exists(target))
        self.assertEqual(len(numbers) - 1, bst.size())

    def test_deleting_with_one_child(self):
        bst = Bst()
        # Comment out below as desired. Experiment like hell!
        numbers = [
            5,  # 1
            12, # 2
            9,  # 1
            7,  # 0
            21, # 2
            19, # 0
            25  # 0
        ]

        for n in numbers:
            bst.insert(n)

        target = 9

        self.assertEqual(len(numbers), bst.size())
        self.assertTrue(bst.exists(target))

        self.assertTrue(bst.delete(target))
        self.assertFalse(bst.delete(target))

        self.assertFalse(bst.exists(target))
        self.assertEqual(len(numbers) - 1, bst.size())

    def test_deleting_with_two_children(self):
        bst = Bst()
        # Comment out below as desired. Experiment like hell!
        numbers = [
            5,  # 1
            12, # 2
            9,  # 1
            7,  # 0
            21, # 2
            19, # 0
            25  # 0
        ]

        for n in numbers:
            bst.insert(n)

        target = 12

        self.assertEqual(len(numbers), bst.size())
        self.assertTrue(bst.exists(target))

        self.assertTrue(bst.delete(target))
        self.assertFalse(bst.delete(target))

        self.assertFalse(bst.exists(target))
        self.assertEqual(len(numbers) - 1, bst.size())

    def test_deleting_as_the_root_node(self):
        first_bst = Bst()
        first_bst.insert(1)
        self.assertTrue(first_bst.delete(1))
        self.assertEqual(0, first_bst.size())

        bst = Bst()
        # Comment out below as desired. Experiment like hell!
        numbers = [
            5,  # 1
            12, # 2
            9,  # 1
            7,  # 0
            21, # 2
            19, # 0
            25  # 0
        ]

        for n in numbers:
            bst.insert(n)

        target = 5

        self.assertEqual(len(numbers), bst.size())
        self.assertTrue(bst.exists(target))

        self.assertTrue(bst.delete(target))
        self.assertFalse(bst.delete(target))

        self.assertFalse(bst.exists(target))
        self.assertEqual(len(numbers) - 1, bst.size())

    def test_traverse_method(self):
        self.skipTest("Not yet implemented! Need to write useful test.")

        bst = Bst()

        characters = ["a", "b", "c"]
        for c in characters:
            bst.insert(c)

        the_traversed_string = ""
        # def append_to(new_string):
        #     return string += new_string
        # bst.traverse(lambda current_item: the_traversed_string)
        self.assertEqual("abc", the_traversed_string)


# TODO: Write tests for BstNode or remove block
# class TestBstNode(unittest.TestCase):
#     def test_container_size_is_represented(self):
#         node = BstNode("Some Item")
#         self.assertIsInstance(node, BstNode)


if __name__ == '__main__':
    unittest.main()