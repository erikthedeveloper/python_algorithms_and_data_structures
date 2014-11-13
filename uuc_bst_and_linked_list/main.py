from student import Student, StudentFactory, StudentListFetcher
from uuc import UnorderedUniqueContainer
from linked_list import LinkedList
from bst import Bst
import time

USE_MEDIUM = True


def section_header(contents, pad_deep = 15):
    header_format = "\n" + "=" * pad_deep + " {0}\n"
    return header_format.format(contents)


def section_timing_footer(time_elapsed):
    section_timing_template = "Execution time for section: {0:.3f} seconds"
    return section_timing_template.format(time_elapsed)


def do_insert(uuc):
    """
    Insert - Detect any duplicate objects. That is, if a student has the same SSN as a previous student, do not add that student. Instead, print an error message.
    """
    list_fetcher = StudentListFetcher()
    file_name = 'InsertNamesMedium.txt' if USE_MEDIUM else 'InsertNames.txt'
    lines_list = list_fetcher.get_list_of_lines(file_name)
    print section_header("Insert")
    time_start = time.time()
    failed = 0
    for line in lines_list:
        new_student = StudentFactory.create_from_insert_row_string(line)
        if not uuc.insert(new_student):
            if not USE_MEDIUM:
                print "Duplicate SSN ({1}) for {0}".format(new_student, new_student.ssn)
            failed += 1
            continue
    print "Num failed: ", failed
    print "Read Length: {0:,d} | Results Length: {1:,d}".format(len(lines_list), uuc.size())
    print section_timing_footer(time.time() - time_start)
    return list_fetcher


def do_traverse(uuc):
    """
    Traverse all students in the pythonList, and print their average age (as a Float, not an Int). Print how many seconds that took.
    """
    print section_header("Traverse")
    time_start = time.time()
    ages = {'sum': 0}

    def add_to_sum(student):
        ages['sum'] += int(student.age)

    uuc.traverse(add_to_sum)
    average_age = ages['sum'] / float(uuc.size())
    print "Average age for {0:,d} students: {1:.10f}".format(uuc.size(), average_age)
    print section_timing_footer(time.time() - time_start)


def do_delete(uuc):
    """
    Delete all students in DeleteNames.txt, and print how long that took.
    """
    print section_header("Delete")
    list_fetcher = StudentListFetcher()
    time_start = time.time()
    file_name = 'DeleteNamesMedium.txt' if USE_MEDIUM else 'DeleteNames.txt'
    delete_names_ssn_list = list_fetcher.get_list_of_lines(file_name)
    failed = 0
    for delete_ssn in delete_names_ssn_list:
        temp_student = StudentFactory.create_dummy_from_ssn(delete_ssn)
        if not uuc.delete(temp_student):
            if not USE_MEDIUM:
                print "Could not find {ssn} for delete!!".format(**{'ssn': delete_ssn})
            failed += 1
    print "Num failed: ", failed
    print section_timing_footer(time.time() - time_start)


def do_retrieve(uuc):
    """
    Retrieve all students in RetrieveNames.txt, print their average age (again, with decimal accuracy), and how long that took.
    """
    print section_header("Retrieve")
    list_fetcher = StudentListFetcher()
    file_name = 'RetrieveNamesMedium.txt' if USE_MEDIUM else 'RetrieveNames.txt'
    retrieve_students_ssn_list = list_fetcher.get_list_of_lines(file_name)
    time_start = time.time()
    age_sum = 0
    num_retrieved = 0
    failed = 0
    for ssn in retrieve_students_ssn_list:
        temp_student = StudentFactory.create_dummy_from_ssn(ssn)
        found_student = uuc.retrieve(temp_student)
        if found_student:
            age_sum += int(found_student.age)
            num_retrieved += 1
        else:
            if not USE_MEDIUM:
                print "Could not find {ssn} for retrieve!!".format(**{'ssn': ssn})
            failed += 1
    print "Num failed: ", failed
    average_age = age_sum / float(num_retrieved)
    print "Average age for {0:,d} students: {1:.10f}".format(len(retrieve_students_ssn_list), average_age)
    print section_timing_footer(time.time() - time_start)


def main():
    uuc = Bst()
    print section_header("Student List Fun BST (Assignment Part 02)", 20)
    time_master_start = time.time()

    do_insert(uuc)
    do_traverse(uuc)
    do_delete(uuc)
    do_retrieve(uuc)

    print section_header("END Student List Fun", 20)
    print "Total Execution time: {0:.3f} seconds".format(time.time() - time_master_start)

    # uuc = LinkedList()
    #
    # print section_header("Student List Fun LinkedList (Assignment Part 02)", 20)
    # time_master_start = time.time()
    #
    # do_insert(uuc)
    # do_traverse(uuc)
    # do_delete(uuc)
    # do_retrieve(uuc)
    #
    # print section_header("END Student List Fun", 20)
    # print "Total Execution time: {0:.3f} seconds".format(time.time() - time_master_start)

    print section_header("Goodbye", 25)


main()
