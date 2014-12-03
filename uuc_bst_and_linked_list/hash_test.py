import unittest

from hash import HashTable, is_prime

from student import Student, StudentFactory


class TestIsPrime(unittest.TestCase):
    def test_is_prime_method(self):
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(13))


class TestHashTable(unittest.TestCase):
    def test_inserting_unique_and_duplicate_items(self):
        hash_table = HashTable(3)
        self.assertTrue(hash_table.insert(StudentFactory.create_dummy_from_ssn("123-123-1234")))
        self.assertTrue(hash_table.insert(StudentFactory.create_dummy_from_ssn("123-123-1235")))
        self.assertFalse(hash_table.insert(StudentFactory.create_dummy_from_ssn("123-123-1235")))
        self.assertTrue(hash_table.insert(StudentFactory.create_dummy_from_ssn("123-123-1236")))

    def test_container_size_is_maintained_during_insertions(self):
        hash_table = HashTable(3)
        self.assertEqual(0, hash_table.size())

        self.assertTrue(hash_table.insert(StudentFactory.create_dummy_from_ssn("123-123-1234")))
        self.assertEqual(1, hash_table.size())

        self.assertTrue(hash_table.insert(StudentFactory.create_dummy_from_ssn("123-123-1235")))
        self.assertEqual(2, hash_table.size())

        self.assertTrue(hash_table.insert(StudentFactory.create_dummy_from_ssn("123-123-1236")))
        self.assertEqual(3, hash_table.size())

    def test_finding_an_existing_element(self):
        hash_table = HashTable(3)
        jane = Student("Doe", "Jane", "123-123-1234", "jane@gmail.com", 23)
        john = Student("Doe", "John", "223-123-1234", "john@gmail.com", 23)
        jake = Student("Doe", "Jake", "323-123-1234", "john@gmail.com", 23)

        dummy_john = StudentFactory.create_dummy_from_ssn("223-123-1234")

        hash_table.insert(jane)
        hash_table.insert(john)
        hash_table.insert(jake)

        self.assertEqual(john, hash_table.retrieve(dummy_john))

    def test_checking_if_an_item_exists(self):
        hash_table = HashTable(3)
        jane = Student("Doe", "Jane", "123-123-1234", "jane@gmail.com", 23)
        john = Student("Doe", "John", "223-123-1234", "john@gmail.com", 23)
        jake = Student("Doe", "Jake", "323-123-1234", "john@gmail.com", 23)

        dummy_john = StudentFactory.create_dummy_from_ssn("223-123-1234")

        self.assertFalse(hash_table.exists(dummy_john))

        hash_table.insert(jane)
        hash_table.insert(john)
        hash_table.insert(jake)

        self.assertTrue(hash_table.exists(dummy_john))

    def test_deleting_an_item(self):
        hash_table = HashTable(3)
        jane = Student("Doe", "Jane", "123-123-1234", "jane@gmail.com", 23)
        john = Student("Doe", "John", "223-123-1234", "john@gmail.com", 23)
        jake = Student("Doe", "Jake", "323-123-1234", "john@gmail.com", 23)

        dummy_john = StudentFactory.create_dummy_from_ssn("223-123-1234")

        self.assertFalse(hash_table.delete(dummy_john))

        hash_table.insert(jane)
        hash_table.insert(john)
        hash_table.insert(jake)

        self.assertEqual(3, hash_table.size())
        self.assertTrue(hash_table.delete(dummy_john))
        self.assertFalse(hash_table.exists(dummy_john))
        self.assertFalse(hash_table.delete(dummy_john))
        self.assertEqual(2, hash_table.size())

    def test_traverse_method_used_from_outside_collaborator(self):
        hash_table = HashTable(3)
        jane = Student("Doe", "Jane", "123-123-1234", "jane@gmail.com", 23)
        john = Student("Doe", "John", "223-123-1234", "john@gmail.com", 23)
        jake = Student("Doe", "Jake", "323-123-1234", "john@gmail.com", 23)

        hash_table.insert(jane)
        hash_table.insert(john)
        hash_table.insert(jake)

        class StudentCollaborator:
            def __init__(self):
                self.ssn_list = []

            def add_to(self, student):
                self.ssn_list.append(student.ssn)

        string_master = StudentCollaborator()

        hash_table.traverse(string_master.add_to)
        self.assertListEqual(
            sorted([jane.ssn, john.ssn, jake.ssn]),
            sorted(string_master.ssn_list))


if __name__ == '__main__':
    unittest.main()