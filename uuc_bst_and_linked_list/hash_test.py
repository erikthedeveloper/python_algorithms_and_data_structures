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
    def _jane_john_and_jake(self):
        some_students = {
            'jane': Student("Doe", "Jane", "123-123-1234", "jane@gmail.com", 23),
            'john': Student("Doe", "John", "223-123-1234", "john@gmail.com", 23),
            'jake': Student("Doe", "Jake", "323-123-1234", "john@gmail.com", 23)
        }
        return some_students

    def test_inserting_unique_and_duplicate_items(self):
        hash_table = HashTable(3)
        some_students = self._jane_john_and_jake()
        self.assertTrue(hash_table.insert(some_students['jane']))
        self.assertTrue(hash_table.insert(some_students['john']))
        self.assertFalse(hash_table.insert(some_students['john']))
        self.assertTrue(hash_table.insert(some_students['jake']))

    def test_container_size_is_maintained_during_insertions(self):
        hash_table = HashTable(3)
        some_students = self._jane_john_and_jake()
        self.assertEqual(0, hash_table.size())

        self.assertTrue(hash_table.insert(some_students['jane']))
        self.assertEqual(1, hash_table.size())

        self.assertTrue(hash_table.insert(some_students['john']))
        self.assertEqual(2, hash_table.size())

        self.assertTrue(hash_table.insert(some_students['jake']))
        self.assertEqual(3, hash_table.size())

    def test_finding_an_existing_element(self):
        hash_table = HashTable(3)
        some_students = self._jane_john_and_jake()

        dummy_john = StudentFactory.create_dummy_from_ssn(some_students['john'].ssn)

        hash_table.insert(some_students['jane'])
        hash_table.insert(some_students['john'])
        hash_table.insert(some_students['jake'])

        self.assertEqual(some_students['john'], hash_table.retrieve(dummy_john))

    def test_checking_if_an_item_exists(self):
        hash_table = HashTable(3)
        some_students = self._jane_john_and_jake()

        dummy_john = StudentFactory.create_dummy_from_ssn(some_students['john'].ssn)

        self.assertFalse(hash_table.exists(dummy_john))

        hash_table.insert(some_students['jane'])
        hash_table.insert(some_students['john'])
        hash_table.insert(some_students['jake'])

        self.assertTrue(hash_table.exists(dummy_john))

    def test_deleting_an_item(self):
        hash_table = HashTable(3)
        some_students = self._jane_john_and_jake()

        dummy_john = StudentFactory.create_dummy_from_ssn("223-123-1234")

        self.assertFalse(hash_table.delete(dummy_john))

        hash_table.insert(some_students['jane'])
        hash_table.insert(some_students['john'])
        hash_table.insert(some_students['jake'])

        self.assertEqual(3, hash_table.size())
        self.assertTrue(hash_table.delete(dummy_john))
        self.assertFalse(hash_table.exists(dummy_john))
        self.assertFalse(hash_table.delete(dummy_john))
        self.assertEqual(2, hash_table.size())

    def test_traverse_method_used_from_outside_collaborator(self):
        hash_table = HashTable(3)
        some_students = self._jane_john_and_jake()

        hash_table.insert(some_students['jane'])
        hash_table.insert(some_students['john'])
        hash_table.insert(some_students['jake'])

        class StudentCollaborator:
            def __init__(self):
                self.ssn_list = []

            def add_to(self, student):
                self.ssn_list.append(student.ssn)

        string_master = StudentCollaborator()

        hash_table.traverse(string_master.add_to)
        self.assertListEqual(
            sorted([some_students['jane'].ssn, some_students['john'].ssn, some_students['jake'].ssn]),
            sorted(string_master.ssn_list))


if __name__ == '__main__':
    unittest.main()