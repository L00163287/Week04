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

if __name__ == "__main__":
    '''
       Main method of application :
       
       Parameters:
        none
       Returns:
        none
    '''

    print("Machine Name \t\t : {}".format(platform.machine()))
    print("Node Name \t\t\t : {}".format(platform.node()))
    print("Operating System \t : {}".format(platform.system()))
    print("Current Path \t\t : {}".format(os.path))
    print("Python version \t\t : {}".format(platform.python_version()))
