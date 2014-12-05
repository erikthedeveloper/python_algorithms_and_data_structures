"""
A basic test suite for the DSU CS2420 HashTable (UUC) Implementation
    This covers the basic functionality required by the course and should
    serve as a specification for the class(es) and method(s) to be implemented

To run: `python hash_test.py`

Requirements:
    Files present in same directory as hash_test.py
        hash.py with a is_prime(int) method and a HashTable class
        student.py with a Student class and StudentFactory class (to "generate dummy from SSN")

Note: Use `self.skipTest("Skip this test for now!")` to skip a test_*() method (to focus on one feature at a time).
"""
__author__ = "Erik Aybar <erikthedeveloper@gmail.com>"

import unittest
from hash import HashTable, is_prime
from student import Student, StudentFactory


class TestHashTableMethods(unittest.TestCase):
    def test_is_prime_method(self):
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(13))


class TestHashTable(unittest.TestCase):

    def _make_uuc(self, size):
        """
        This method should be overridden per UUC implementation (i.e. Hash requires size... for now at least)
        """
        # TODO: in that case the entire test suite should be extracted to a TestUuc and used as TestHashTable(TestUuc)...
        # TODO: ... hmmm would need to be generalized/converted into some type of UUC Factory to account for "size"...
        return HashTable(size)

    def _jane_john_and_jake(self):
        some_students = {
            'jane': Student("Johnson", "Jane", "123-123-1234", "jane@fakemail.com", 23),
            'john': Student("Doe", "John", "223-123-1234", "john@fakemail.com", 28),
            'jake': Student("Jerk", "Jake", "323-123-1234", "jake@fakemail.com", 47)
        }
        return some_students

    def test_inserting_unique_and_duplicate_items(self):
        uuc = self._make_uuc(3)
        some_students = self._jane_john_and_jake()
        self.assertTrue(uuc.insert(some_students['jane']))
        self.assertTrue(uuc.insert(some_students['john']))
        self.assertFalse(uuc.insert(some_students['john']))
        self.assertTrue(uuc.insert(some_students['jake']))

    def test_container_size_is_maintained_during_insertions(self):
        uuc = self._make_uuc(3)
        some_students = self._jane_john_and_jake()

        self.assertEqual(0, uuc.size())
        self.assertTrue(uuc.insert(some_students['jane']))
        self.assertEqual(1, uuc.size())
        self.assertTrue(uuc.insert(some_students['john']))
        self.assertEqual(2, uuc.size())
        self.assertTrue(uuc.insert(some_students['jake']))
        self.assertEqual(3, uuc.size())

    def test_finding_an_existing_element(self):
        uuc = self._make_uuc(3)
        some_students = self._jane_john_and_jake()

        dummy_john = StudentFactory.create_dummy_from_ssn(some_students['john'].ssn)

        uuc.insert(some_students['jane'])
        uuc.insert(some_students['john'])
        uuc.insert(some_students['jake'])

        self.assertEqual(some_students['john'], uuc.retrieve(dummy_john))

    def test_checking_if_an_item_exists(self):
        uuc = self._make_uuc(3)
        some_students = self._jane_john_and_jake()

        dummy_john = StudentFactory.create_dummy_from_ssn(some_students['john'].ssn)

        self.assertFalse(uuc.exists(dummy_john))
        uuc.insert(some_students['jane'])
        uuc.insert(some_students['john'])
        uuc.insert(some_students['jake'])
        self.assertTrue(uuc.exists(dummy_john))

    def test_deleting_an_item(self):
        uuc = self._make_uuc(3)
        some_students = self._jane_john_and_jake()

        dummy_john = StudentFactory.create_dummy_from_ssn("223-123-1234")

        self.assertFalse(uuc.delete(dummy_john))

        uuc.insert(some_students['jane'])
        uuc.insert(some_students['john'])
        uuc.insert(some_students['jake'])

        self.assertEqual(3, uuc.size())
        self.assertTrue(uuc.delete(dummy_john))
        self.assertFalse(uuc.exists(dummy_john))
        self.assertFalse(uuc.delete(dummy_john))
        self.assertEqual(2, uuc.size())

    def test_traverse_method_used_from_outside_collaborator(self):
        uuc = self._make_uuc(3)
        some_students = self._jane_john_and_jake()

        uuc.insert(some_students['jane'])
        uuc.insert(some_students['john'])
        uuc.insert(some_students['jake'])

        class StudentCollaborator:
            def __init__(self):
                self.ssn_list = []

            def add_to_ssn_list(self, student):
                self.ssn_list.append(student.ssn)

        string_master = StudentCollaborator()

        uuc.traverse(string_master.add_to_ssn_list)
        self.assertListEqual(
            sorted([some_students['jane'].ssn, some_students['john'].ssn, some_students['jake'].ssn]),
            sorted(string_master.ssn_list))

    def test_checking_if_an_item_exists_after_some_deletions(self):
        self.skipTest("Need to write test that fails (i.e. breaking the bridge by deleting... looking for friend in mall etc...")


if __name__ == '__main__':
    unittest.main()