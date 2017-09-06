import sys
import re
"""
This file parses a yml file and prints out the contact information of the
desired user or returns a does not exist message

Usage
$python parse.py <filename>
filename is the name of the file to parse

Precondition:
The format for the string to parse must be in this format
"username" #First Name name@scotiabank.com

Programmer: Richard Zeng The INTERN 2017
"""

"""
This function takes in the yml file name and the user name and prints out the
contact information of the user.
"""
def parse_file(file_name, username):
    try:
        file = open(file_name, "r")
    # file cannot be found
    except FileNotFoundError:
        print("Shit. File not found.")

    for line in file:
        if username in line:
            #gathering the contact information
            contact_info = re.match ( r'(.*)\s*#(.*)\s*(.*)\s+(.+@scotiabank.com)*',
             line, re.M|re.I)
            return contact_info.group(2)+ " " + contact_info.group(3)
            + " " + contact_info.group(4)

    return "Username does not exist"

if __name__ == "__main__":
    print(parse_file(sys.argv[1], sys.argv[2]))
