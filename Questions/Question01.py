"""
#
# @File         : Question01.py
# @Created      : 2021-10-11 11:01
# @Author       : Bubashankushan B
# @Version      : v1.0.0
# @Licensing    : 
#
# @Description  : Week 04 Question 01 : Write a python script to determine the following system information.
#                 Import the platform module.Find out the machine(), node, operating system,
#                 current value of the ‘PATH’ and other relevant configuration variables.
#                 Display the information in a tidy manner.
#
"""

import platform
import os

def os_details():
    # Displays the name of the machine.
    print("Machine Name \t\t : {}".format(platform.machine()))
    # Displays the Node of the machine.
    print("Node Name \t\t\t : {}".format(platform.node()))
    # Displays the name of the owner of the machine.
    print("Operating System \t : {}".format(platform.system()))
    # Displays the Current Path of the os
    print("Current Path \t\t : {}".format(os.path))
    # Displays the python version
    print("Python version \t\t : {}".format(platform.python_version()))


if __name__ == "__main__":
    '''
       Main method of application :
       
       Parameters:
        none
       Returns:
        none
    '''
    # Use the function to display details
    os_details()

