import unittest
from student import Student


class TestStudent(unittest.TestCase):
    def test___int__(self):
        joe = Student("Schmoe", "Joe", "123-123-1234", "joe@schmoe.com", 35)
        self.assertEqual(1231231234, int(joe))


if __name__ == '__main__':
    unittest.main()