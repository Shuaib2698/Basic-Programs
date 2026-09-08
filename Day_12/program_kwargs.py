'''program using **kwargs -> collects keyword positional arguments

def student_details(**kwargs):

Print every key and value.

Example:

student_details(
    name="Shuaib",
    age=28,
    course="Data Science"
)

Expected:

name : Shuaib
age : 28
course : Data Science'''

def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":" , value)

student_details(
    name="Shuaib",
    age=28,
    course="Data Science"
)

def employee(**kwargs):
    for key, value in kwargs.items():
        print(key, ":" , value)

employee(
    name="Amit",
    department="IT",
    salary=60000,
    experience=2
)