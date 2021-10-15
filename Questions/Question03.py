"""
#
# @File         : Question03.py
# @Created      : 2021-10-15 10:10
# @Author       : Bubashankushan B
# @Version      : v1.0.0
# @Licensing    : 
#
# @Description  :
#
"""

import pprint

# Initialize empty course list
courses = {}


def add_course():
    # function to add new course name and course code
    course_name = input("Course name :")
    course_code = input("Course code :")
    courses[course_code] = course_name


def edit_course():
    # function to edit course name
    code = input("Enter course code: {}".format(courses))
    if code in courses:
        # Get old course name
        course = courses[code]
        # Get updated course name from the user
        updated = input("Enter the course name :")
        # Update value in list
        courses[code] = updated
        print("Course name changed successfully {} as {}".format(course, updated))
    else:
        print("Invalid Course code")


def view_courses():
    # use pprint library to Display course list
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(courses)


if __name__ == '__main__':
    # main function to read user option

    while 1:
        user_option = int(input("1. Add Course\n2. Edit Course\n3. Display Courses\n4. Quit\n"))
        if user_option == 1:
            add_course()
        elif user_option == 2:
            edit_course()
        elif user_option == 3:
            view_courses()
        elif user_option == 4:
            break
        else:
            print("Please enter a valid option")
