##
# Rachel Ward, Jacqueline Chambliss, Edward Jenkins - 12/4/21
# This module is a part of a school registration system
# containing methods to add and drop a student from courses as well
# as return the courses in which a student is currently enrolled.
# Wait-list functionality included.
##

# Add student to course, on three conditions:
# the course exists, student not yet enrolled, and there's a seat.
# If the course is full, student will be placed on the wait-list.
# parameters:
# str id: student ID
# dict c_roster: course ID as key, list of ID strings as value
# dict c_max_size: course ID as key, int number of seats as value
# dict c_wait_list: course ID as key, list of ID strings as value
def add_course(id, c_roster, c_max_size, c_wait_list):
    # user input
    usr_input = input('Enter course you want to add: ')
    # test for course ID match in course dictionary,
    # else display message and return
    if usr_input not in list(c_roster.keys()):
        print('Course not found')
        return
    # test if student is already enrolled,
    # if so display message and return
    elif id in c_roster[usr_input]:
        print('You are already enrolled in that course')
        return
    # test if the course is already full
    # if so, wait-list student
    elif c_max_size[usr_input] == len(c_roster[usr_input]):
        # test if wait-list already exists for the course
        if usr_input in c_wait_list.keys():
            # test if student is already on the wait-list,
            # if not, add student to wait-list
            if id not in c_wait_list[usr_input]:
                c_wait_list[usr_input].append(id)
                print('Course full, added to wait-list')
                return
            else:
                print('You are already wait-listed for that course.')
                return
        # if no wait-list exists, create one and add student
        else:
            # create wait-list for course
            c_wait_list[usr_input] = [id]
            print('Course full, added to wait-list')
            return
    # all test conditions passed, add student to c_roster
    else:
        c_roster[usr_input].append(id)
        print('Course added')
        return


# Drop student from course, with two conditions:
# the course exists and student is enrolled. If drop occurs,
# drop_course calls wait_list_get_next method to check for a wait_list.
# If student requests to drop a course for which they are wait-listed,
# drop_course will remove them from the wait-list.
# parameters:
# str id: student ID
# dict c_roster: course ID as key, list of ID strings as value
# dict c_wait_list: course ID as key, list of ID strings as value
def drop_course(id, c_roster, c_wait_list):
    # user input
    usr_input = input('Enter course you want to drop: ')
    # test for user input match in course dictionary,
    # else display message and return
    if usr_input not in list(c_roster.keys()):
        print('Course not found')
        return
    # test if student is not enrolled
    elif id not in c_roster[usr_input]:
        # test if a wait-list exists for the course
        if usr_input in c_wait_list.keys():
            # test if student is on the wait-list for the course
            if id in c_wait_list[usr_input]:
                # remove student from the wait-list of the course
                c_wait_list[usr_input].remove(id)
                print('Removed from wait-list')
        # student not enrolled or wait-listed for course.
        else:
            print('You are not enrolled in that course')
        return
    # remove student from course roster
    else:
        c_roster[usr_input].remove(id)
        print('Course dropped')
        # call wait_list_get_next method to check for a
        # wait-list since a seat in a course just opened up.
        wait_list_get_next(usr_input, c_roster, c_wait_list)
        return


# This method checks for a wait-list and if one exists for
# the course, it adds the next person in line to the roster
# parameters:
# str id: student ID
# dict c_roster: course ID as key, list of ID strings as value
# dict c_wait_list: course ID as key, list of ID strings as value
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
# Display and count number of courses student is wait-listed for.
# Return both sets of info as strings.
# parameters:
# str id: student ID
# dict c_roster: course ID as key, list of ID strings as value
# dict c_wait_list: course ID as key, list of ID strings as value
def list_courses(id, c_roster, c_wait_list):
    count = 0
    courses_list = []
    display_str = f'Courses registered:\n'
    # for loops iterate through a list of tuples representing each course.
    # The first element of each tuple is the course id
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
    registered_string = display_str + f'Total number: {count}\n'
    print(registered_string)

    # re-use variables to list courses that student is wait-listed for
    count = 0
    courses_list.clear()
    display_str = f'Courses wait-listed:\n'
    for c in c_wait_list.items():
        # if the student's id is in the wait-list
        if id in c[1]:
            # add the course to their list
            courses_list.append(c[0])
            # update count
            count += 1
            # add to string
            display_str += f'{c[0]}\n'
    # display registered course count and registered course list
    wait_string = display_str + f'Total number: {count}\n'
    print(wait_string)
    # return student's course registration info
    return registered_string, wait_string
