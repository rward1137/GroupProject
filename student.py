##
# The Student class works as part of a school registration system.
# Student object has methods to add and drop itself from courses as well
# as return the courses in which student is currently enrolled.
# Proposing wait-list functionality.
# RW - 11/18/21
##
class Student:
    # Add student to course, on three conditions:
    # the course exists, student not yet enrolled, and there's a spot
    # parameters:
    # (str) student ID
    # (dict) courses w/ rosters
    # (dict) courses w/ # of seats
    # !!! Proposal: Add a c_wait_list dict parameter;
    # key is course ID, value is list of ID numbers
    # of students waiting to enroll if a seat opens up
    def add_course(self, id, c_roster, c_max_size, c_wait_list):
        # user input
        usr_input = input('Enter course you want to add:')
        # test for match in course dictionary,
        # else display message and return
        if usr_input not in list(c_roster.keys()):
            print('course not found')
            return
        # test if student is already enrolled,
        # if so display message and return
        elif str(id) in c_roster[usr_input]:
            print('already enrolled')
            return
        # test if the course is already full
        elif c_max_size[usr_input] == len(c_roster[usr_input]):
            # wait-list student then display message and return
            if usr_input in c_wait_list:
                # a wait-list exists for course already
                c_wait_list[usr_input].append(str(id))
                print('course full, added to wait-list')
                print(c_wait_list[usr_input])
                return
            else:
                # create wait-list for course
                c_wait_list[usr_input] = str(id)
                print('course full, added to wait-list')
                return
        # all test conditions passed, add student to c_roster
        else:
            c_roster[usr_input].append(str(id))
            print('course added')
            return

    # Drop student from course, with two conditions:
    # the course exists and student is enrolled
    # parameters:
    # (str) student ID
    # (dict) courses w/ rosters
    def drop_course(self, id, c_roster):
        # user input
        usr_input = input('Enter course you want to drop:')
        # test for match in course dictionary,
        # else display message and return
        if usr_input not in list(c_roster.keys()):
            print('course not found')
            return
        # test if student is enrolled,
        # else display message and return
        elif str(id) not in c_roster[usr_input]:
            print('not enrolled')
            return
        # both test conditions met, then remove student from c_roster
        else:
            c_roster[usr_input].remove(str(id))
            print('course dropped')
            # !!! Proposal:
            # call method to check for a wait-list and add the next person in line
            return

# Still working on everything below here! :) 


    # !!! Proposal:
    # Add student to roster of course for which they are next on wait-list.
    # (I'm thinking main will determine if there's a wait-list and who's next on it)
    # parameters:
    # (str) student id, (str) course id, (dict) courses w/ rosters, (dict) courses w/ wait-lists
    def wait_list_add(self, id, course_id, c_roster, c_wait_list):
        # remove student from wait-list
        # add student to course roster
        # (no message to display for current user, correct? This method is called by main after
        # a current user removes themselves from a course.)
        # return

    # Display and count number of courses student is enrolled in.
    # parameters: (str) student id, (dict) courses w/ rosters
    # !!! Proposal: pass in c_wait_list too, so that wait-list info can be displayed
    def list_courses(self, id, c_roster):
        # count variable = 0
        # list of courses variable = []
        # for each course in c_roster
            # if student is present on roster
                # add course to list
                # update count
        # display registered course count and registered course list
        # !!! Proposal:
        # re-use variables; count = 0,  list = []
        # for each course in c_wait_list:
            # if student is present on wait-list
                # add course to list
                # update count
        # display wait-listed course count and wait-listed courses
        # return
