from student import Student, StudentFactory
from uuc import UnorderedUniqueContainer
from linked_list import LinkedList
from bst import Bst
from hash import HashTable
import time


def section_header(contents, pad_deep = 15):
    header_format = "\n" + "=" * pad_deep + " {0}\n"
    return header_format.format(contents)


def section_timing_footer(time_elapsed):
    section_timing_template = "Execution time for section: {0:.3f} seconds"
    return section_timing_template.format(time_elapsed)


def data_file_path(file_name_title):
    file_name = file_name_title + "Names"
    if USE_MEDIUM:
        file_name += "Medium"
    file_name = "./data_students_txt/" + file_name + ".txt"
    return file_name


def do_insert(uuc):
    """
    Insert - Detect any duplicate objects. That is, if a student has the same SSN as a previous student, do not add that student. Instead, print an error message.
    """
    file_path = data_file_path("Insert")
    f = open(file_path, "r+")
    print section_header("Insert")
    time_start = time.time()
    failed = 0
    for line in f:
        try:
            new_student = StudentFactory.create_from_insert_row_string(line)
        except ValueError:
            continue
        if not uuc.insert(new_student):
            if not USE_MEDIUM:
                print "Duplicate SSN ({1}) for {0}".format(new_student, new_student.ssn)
            failed += 1
            continue
    f.close()
    print "Num failed: ", failed
    print "Total Number Students: {0:,d}".format(uuc.size())
    print section_timing_footer(time.time() - time_start)


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
    time_start = time.time()
    file_path = data_file_path("Delete")
    f = open(file_path, "r+")
    failed = 0
    for delete_ssn in f:
        delete_ssn = delete_ssn.replace("\r", "").replace("\n", "")
        temp_student = StudentFactory.create_dummy_from_ssn(delete_ssn)
        if not uuc.delete(temp_student):
            if not USE_MEDIUM:
                print "Could not find {ssn} for delete!!".format(**{'ssn': delete_ssn})
                # exit()
            failed += 1
    f.close()
    print "Num failed: ", failed
    print section_timing_footer(time.time() - time_start)


def do_retrieve(uuc):
    """
    Retrieve all students in RetrieveNames.txt, print their average age (again, with decimal accuracy), and how long that took.
    """
    file_path = data_file_path("Retrieve")
    f = open(file_path, "r+")
    time_start = time.time()
    age_sum = 0
    num_retrieved = 0
    failed = 0
    for ssn in f:
        ssn = ssn.replace("\r", "").replace("\n", "")
        temp_student = StudentFactory.create_dummy_from_ssn(ssn)
        found_student = uuc.retrieve(temp_student)
        if found_student:
            age_sum += int(found_student.age)
            num_retrieved += 1
        else:
            if not USE_MEDIUM:
                print "Could not find {ssn} for retrieve!!".format(**{'ssn': ssn})
            failed += 1
    f.close()
    print "Num failed: ", failed
    average_age = age_sum / float(num_retrieved)
    print "Average age for {0:,d} students: {1:.10f}".format(num_retrieved, average_age)
    print section_timing_footer(time.time() - time_start)


def run_the_gamut(uuc):
    print ("=" * 60) + section_header("Running Student List Gamut ({0})".format(uuc.__class__.__name__), 20) + "=" * 60
    time_master_start = time.time()

    do_insert(uuc)
    do_traverse(uuc)
    do_delete(uuc)
    do_retrieve(uuc)

    print section_header("END Running Student List Gamut ({0})".format(uuc.__class__.__name__), 20)
    print "Total Execution time: {0:.3f} seconds".format(time.time() - time_master_start) + "\n\n"


def main():
    global USE_MEDIUM
    USE_MEDIUM = True

    # - - - Linked List
    # run_the_gamut(LinkedList())

    # - - - Binary Search Tree
    run_the_gamut(Bst())

    # - - - Hash Table
    hash_table_item_count = 300000 if USE_MEDIUM else 30000
    run_the_gamut(HashTable(hash_table_item_count))


main()
