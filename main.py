from student import Student, StudentFactory, StudentListFetcher
from uuc import UnorderedUniqueContainer
from linked_list import LinkedList
from bst import Bst
import time

def do_insert(uuc):
    pass

def do_traverse(uuc):
    pass

def do_delete(uuc):
    pass

def do_retrieve(uuc):
    pass

class Student:
    def __init__(self, name):
        self.name = name


def output_header(contents, pad_deep = 15):
    header_format = "\n" + "=" * pad_deep + " {0}\n"
    return header_format.format(contents)


def main():
    print output_header("Student List Fun (Assignment Part 02)", 20)
    time_master_start = time.time()
    list_fetcher = StudentListFetcher()
    lines_list = list_fetcher.get_list_of_lines('InsertNames.txt')

    section_timing_template = "Execution time for section: {0:.3f} seconds"

    # - - - -  Insert - Detect any duplicate objects. That is, if a student has the same SSN as a previous student, do not add that student. Instead, print an error message.
    # Assignment Part 01 (Passed Off)
    print output_header("Insert")
    time_start = time.time()
    students_list = []
    ssn_list = []

    for line in lines_list:
        try:
            new_student = StudentFactory.create_from_insert_row_string(line)
        except Exception:
            print "Could not process line: \"{0}\"".format(line)
            continue

        if new_student.ssn in ssn_list:
            print "Duplicate SSN ({1}) for {0}".format(new_student, new_student.ssn)
            continue

        ssn_list.append(new_student.ssn)
        students_list.append(new_student)

    print "Read Length: {0:,d} | Results Length: {1:,d}".format(len(lines_list), len(students_list))
    print section_timing_template.format(time.time() - time_start)
    # - - - -

    # - - - - Traverse all students in the pythonList, and print their average age (as a Float, not an Int). Print how many seconds that took.
    print output_header("Traverse")
    time_start = time.time()
    age_sum = 0
    for student in students_list:
        age_sum += int(student.age)
    average_age = age_sum / float(len(lines_list))

    print "Average age for {0:,d} students: {1:.4f}".format(len(students_list), average_age)
    print section_timing_template.format(time.time() - time_start)
    # - - - -

    # - - - - Delete all students in DeleteNames.txt, and print how long that took.
    print output_header("Delete")
    time_start = time.time()
    delete_names_ssn_list = list_fetcher.get_list_of_lines('DeleteNames.txt')
    for delete_ssn in delete_names_ssn_list:
        temp_student = StudentFactory.create_dummy_from_ssn(delete_ssn)
        found = False
        for i in range(len(students_list)):
            if students_list[i] == temp_student:
                students_list.pop(i)
                found = True
                break
        if not found:
            print "Could not find {ssn} for delete!!".format(**{'ssn': delete_ssn})

    print section_timing_template.format(time.time() - time_start)
    # - - - -

    # - - - - Retrieve all students in RetrieveNames.txt, print their average age (again, with decimal accuracy), and how long that took.
    print output_header("Retrieve")
    time_start = time.time()
    age_sum = 0
    num_retrieved = 0

    retrieve_students_ssn_list = list_fetcher.get_list_of_lines('RetrieveNames.txt')
    for ssn in retrieve_students_ssn_list:
        temp_student = StudentFactory.create_dummy_from_ssn(ssn)
        found = False
        for i in range(len(students_list)):
            if students_list[i] == temp_student:
                age_sum += int(students_list[i].age)
                num_retrieved += 1
                found = True
                break
        if not found:
            print "Could not find {ssn} for retrieve!!".format(**{'ssn': ssn})
    average_age = age_sum / float(num_retrieved)

    print "Average age for {0:,d} students: {1:.4f}".format(len(retrieve_students_ssn_list), average_age)
    print section_timing_template.format(time.time() - time_start)
    # - - - -

    time_duration = time.time() - time_master_start
    print output_header("END Student List Fun", 20)
    print "Total Execution time: {0:.3f} seconds".format(time_duration)
    print output_header("Goodbye", 25)


main()
