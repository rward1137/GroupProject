##
# This module is part of a school registration system
# and contains methods to add and drop a student from courses as well
# as return the courses in which a student is currently enrolled.
# Proposing wait-list functionality.
# RW - 11/18/21
##

# Add student to course, on three conditions:
# the course exists, student not yet enrolled, and there's a spot
# parameters:
# (str) student ID
# (dict) courses w/ rosters
# (dict) courses w/ # of seats
# !!! Proposal: Add a c_wait_list dict parameter;
# key is course ID, value is list of ID numbers
# of students waiting to enroll if a seat opens up
def add_course(id, c_roster, c_max_size, c_wait_list):
    # user input
    usr_input = input('Enter course you want to add: ')
    # test for match in course dictionary,
    # else display message and return
    if usr_input not in list(c_roster.keys()):
        print('Course not found')
        return
    # test if student is already enrolled,
    # if so display message and return
    elif str(id) in c_roster[usr_input]:
        print('You are already enrolled in that course')
        return
    # test if the course is already full
    elif c_max_size[usr_input] == len(c_roster[usr_input]):
        # wait-list student then display message and return
        if usr_input in c_wait_list.keys():
            # a wait-list exists for course already
# !!!! This if statement needs to be added to Jackie's student.py file:
            # functionality for someone adding a course when they're already wait-listed.
            if id not in c_wait_list[usr_input]:
                c_wait_list[usr_input].append(id)
                print('Course full, added to wait-list')
                return
            else:
                print('You are already wait-listed for that course.')
                return
    # all test conditions passed, add student to c_roster
    else:
        c_roster[usr_input].append(str(id))
        print('Course added')
        return


# Drop student from course, with two conditions:
# the course exists and student is enrolled
# !!! Proposal: If student is on wait-listed,
# drop_course method will remove them from the wait-list.
# !!! Proposal: If a student drops a course, the method
# wait_list_get_next is called
# parameters:
# (str) student ID
# (dict) courses w/ rosters
# (dict) courses w/ lists of student id strings
def drop_course(id, c_roster, c_wait_list):
    # user input
    usr_input = input('Enter course you want to drop:')
    # test for match in course dictionary,
    # else display message and return
    if usr_input not in list(c_roster.keys()):
        print('Course not found')
        return
    # test if student is enrolled,
    # else display message and return
    elif str(id) not in c_roster[usr_input]:
        if usr_input in c_wait_list.keys():
            if str(id) in c_wait_list[usr_input]:
                # !!! Proposal:
                # remove student from the wait-list
                c_wait_list[usr_input].remove(id)
                print('Removed from wait-list')
        else:
            print('You are not enrolled in that course')
        return
    # both test conditions met, then remove student from c_roster
    else:
        c_roster[usr_input].remove(str(id))
        print('Course dropped')
        # !!! Proposal:
        # call method to check for a wait-list since a spot just opened up
        wait_list_get_next(usr_input, c_roster, c_wait_list)
        return


# !!! Proposal:
# This method will be called at the end of the drop_course method
# if a student drops a course. It checks for a wait-list and
# if one exists, it adds the next person in line.
# parameters:
# (str) course id
# (dict) courses w/ rosters
# (dict) courses w/ wait-lists
def wait_list_get_next(course_id, c_roster, c_wait_list):
    # if a non-zero wait-list exists for the course_id passed in:
    if course_id in c_wait_list.keys():
        if len(c_wait_list[course_id]) != 0:
            # remove the first student id on the wait-list, storing the ID
            waiting_student = c_wait_list[course_id].pop(0)
            # add the waiting_student id to the roster
            c_roster[course_id].append(waiting_student)
    return


# Display and count number of courses student is enrolled in.
# !!! Proposal: pass in c_wait_list too, so that wait-list
# info can be displayed
# parameters:
# (str) student id
# (dict) courses w/ rosters
def list_courses(id, c_roster, c_wait_list):
    count = 0
    courses_list = []
    display_str = f'Courses registered:\n'
    # loop iterates through a list of tuples representing each course
    # The first element of the tuples is the course id
    # and the second element is the corresponding roster.
    for c in c_roster.items():
        # if the student's id is in the roster
        if id in c[1]:
            # add the course to their list
            courses_list.append(c[0])
            # update count
            count += 1
            # add to string
            display_str += f'{c[0]}\n'
    # display registered course count and registered course list
    print(display_str + f'Total number: {count}\n')

    # !!! Proposal:
    # re-use variables to list courses that student is wait-listed for
    count = 0
    courses_list.clear()
    display_str = f'Courses wait-listed:\n'
    for c in c_wait_list.items():
        # if the student's id is in the roster
        if id in c[1]:
            # add the course to their list
            courses_list.append(c[0])
            # update count
            count += 1
            # add to string
            display_str += f'{c[0]}\n'
    # display registered course count and registered course list
    print(display_str + f'Total number: {count}')
    # display wait-listed course count and wait-listed courses
    return
