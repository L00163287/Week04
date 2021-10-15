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

