__author__ = "Erik Aybar"

import urllib2


class Student:
    def __init__(self, last_name, first_name, ssn, email, age):
        self.last_name = last_name
        self.first_name = first_name
        self.ssn = ssn
        self.email = email
        self.age = age

    def __str__(self):
        return "{ssn} - ({last_name}, {first_name})".format(
            **{'last_name': self.last_name, 'first_name': self.first_name, 'ssn': self.ssn})

    def __int__(self):
        return int(self.ssn.replace("-", ""))

    def __eq__(self, other):
        return self.ssn == other.ssn

    def __ne__(self, other):
        return self.ssn != other.ssn

    def __lt__(self, other):
        return self.ssn < other.ssn

    def __le__(self, other):
        return self.ssn <= other.ssn

    def __gt__(self, other):
        return self.ssn > other.ssn

    def __ge__(self, other):
        return self.ssn >= other.ssn


class StudentFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_from_insert_row_string(row_string):
        split = row_string.split(" ")
        if len(split) != 5:
            raise Exception("Could not properly split and create student from ", row_string)
        last_name = split[0]
        first_name = split[1]
        ssn = split[2]
        email = split[3]
        age = split[4]
        student = Student(last_name, first_name, ssn, email, age)
        return student

    @staticmethod
    def create_dummy_from_ssn(ssn):
        student = Student("Faker", "Fake", ssn, "fake@faker.com", 99)
        return student


class StudentListFetcher:
    def __init__(self):
        pass

    def get_list_of_lines(self, filename):
        return self.read_url_data_into_lines_as_array(filename)

    def read_local_file_into_lines_as_array(self, endpoint):
        # TODO: Implement for use with local filesystem
        # file = open(endpoint)
        # data = opened.read().replace("\r", "")
        # lines = data.split("\n")
        # opened.close()
        # return lines[:-1]
        return

    def read_url_data_into_lines_as_array(self, endpoint):
        data_url = "http://cit.cs.dixie.edu/cs/2420/ssn/{0}".format(endpoint)
        opened = urllib2.urlopen(data_url)

        data = opened.read().replace("\r", "")
        lines = data.split("\n")
        opened.close()
        return lines[:-1]