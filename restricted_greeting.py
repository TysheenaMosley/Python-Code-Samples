# Name: Tysheena Mosley
# Date: February 2026
# Program Description:
# This program greets only the student and the instructor.

name = input("Please enter your name: ")

if name.lower() == "tysheena" or name.lower() == "instructor":
    print("Hello, " + name + "! Nice to see you.")
else:
    print("Sorry, you are not authorized to receive a greeting.")
