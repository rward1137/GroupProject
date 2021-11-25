# ----------------------------------------------------------------
# Author:
# Date:
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are registered for.
# (in the student module)
#
# It also allows students to review the tuition costs for their course roster.
# (in the billing module)
# -----------------------------------------------------------------
import student
import billing


def main():
    # ------------------------------------------------------------
    # This function manages the whole registration system.  It has
    # no parameter.  It uses a loop to serve multiple students.
    # Inside the loop, ask student to enter
    # ID, and call the login function to verify student's identity.
    # Then let student choose to add course, drop course or list
    # courses. This function has no return value.
    # -------------------------------------------------------------

    # The Student List -- is a list of tuples??
    student_list = [('1001', '111'), ('1002', '222'),
                    ('1003', '333'), ('1004', '444')]

    # The In-State List -- is a dictionary?
    student_in_state = {'1001': True,
                        '1002': False,
                        '1003': True,
                        '1004': False}

    # Course Roster
    course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002'],
                     'CSC104': []}

    # Hours / Course
    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}

    # Max Size / Class
    course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}

    # Course Wait List
    # RW - I changed this to a dictionary with a list as the value,
    # instead of an integer. This could be why we got errors on the first run.
    course_wait_list = {'CSC101': []}

    while True:
        # begin loop by asking for user ID
        id = input('Enter ID to log in, or 0 to quit: ')
        # if user enters zero, program should quit
        if id == '0':
            break

        # call login method in a loop that repeats until correct
        # ID/PIN combo is entered
        while True:
            if login(id, student_list):
                break
            else:
                continue
        response = -1
        while response != 0:
            # Ask the user for the item type they are adding.
            response = input('Enter 1 to add course, 2 to drop course, '
                             '3 to list courses, 4 to show bill, 0 to exit:')
            # if entry is invalid ask again
            while response not in ['0', '1', '2', '3', '4']:
                response = input('Enter 1 to add course, 2 to drop course, '
                                 '3 to list courses, 4 to show bill, 0 to exit:')
            # Call appropriate method
            if response == '1':
                student.add_course(id, course_roster, course_max_size, course_wait_list)
            elif response == '2':
                student.drop_course(id, course_roster, course_wait_list)
            elif response == '3':
                student.list_courses(id, course_roster, course_wait_list)
            elif response == '4':
                billing.calculate_hours_and_bill(id, student_in_state, course_roster, course_hours)
            else:
                break


def login(id, s_list):
    # ------------------------------------------------------------
    # This function allows a student to log in.
    # It has two parameters: id and s_list, which is the student
    # list. This function asks user to enter PIN. If the ID and PIN
    # combination is in s_list, display message of verification and
    # return True. Otherwise, display error message and return False.
    # -------------------------------------------------------------
    pin = input('Enter your pin: ')
    entry = (id, pin)
    if entry in s_list:
        print('ID verified.')
        return True
    else:
        print('Invalid entry. Please try again.')
        return False


main()
