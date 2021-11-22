##
# The Student class works as part of a school registration system.
# Student object has methods to add and drop itself from courses as well
# as return the courses in which student is currently enrolled.
# !!! Proposal: Student object has a method to move itself
#               from wait-list to roster
# RW - 11/18/21
##

class Student:
    # initialize student object with necessary variables
    def __init__(self, name='', id='', finaid=0.0):
        self.id = id
        self.name = name
        self.finaid = finaid

    # Add student to course, with three conditions:
    # the course exists, student not yet enrolled, and there's a seat
    # parameters:
    # (string) student ID, (dictionary) courses w/ rosters, (dictionary) class size.
    # !!! Proposal: Add a c_wait_list dictionary of the each course w/ an ordered
    # list of students waiting to enroll if a seat opens up
    def add_course(self, id, c_roster, c_max_size, c_wait_list):
        # user input
        usr_input = ''
        usr_input = input('Enter course you want to add:').capitalize()
        # test for match in course dictionary, else display message and return
        if usr_input not in c_roster:
            print('course not found')
            return
        # test if student is already enrolled, if so display message and return
        elif self.id in c_roster.getelement(usr_input):
            print('already enrolled')
            return
        # test if there is a seat for student,
        elif c_max_size.getelement(usr_input) == len(c_roster.getelement(usr_input)):
        # else wait-list student then display message and return
            if usr_input in c_wait_list:
                # a wait-list exists for course
                c_wait_list.getelement(usr_input).append(self)
                print('course full, added to wait-list')
                return
            else:
                # create wait-list for course
                c_wait_list[usr_input] = self
                print('course full, added to wait-list')
                return
        # all test conditions met, then add student to c_roster
        else:
            c_roster.getelement(usr_input).append(self)
        # display a message
        # return


    # Drop student from course, with two conditions:
    # the course exists and student is enrolled
    # parameters:
    # (string) student ID, (dict) courses w/ rosters, (dict) courses w/ # seats
    def drop_course(self, id, c_roster, c_wait_list):
        # user input
        # test that course is in the dictionary, else display message and return
        # test that student is enrolled, else display message and return
        # both test conditions met, then remove student from c_roster
        # display a message
        # !!! Proposal: this method returns a boolean (and a course id string?) to the
        # main, indicating if student did or did not successfully drop course.
        # If returns true, main must use wait-list dictionary to call
        # wait_list_add for the student who is next in line.


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
