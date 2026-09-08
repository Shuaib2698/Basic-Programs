'''*args + **kwargs ⭐⭐

Create:

def student(name, *marks, **details):

Given:

student(
    "Shuaib",
    80,
    75,
    90,
    age=28,
    course="Data Science"
)

Calculate the average of the marks and print:

Name: Shuaib
Average: 81.666...
Age: 28
Course: Data Science

For Q3, don't use sum(). Use a loop.'''


def student(name, *marks, **details):

    total = 0
    for i in marks:
        total += i
    average = total/len(marks)

    profile = {
            "Name" : name,
            "Average" : average,
            "Age" : details["age"],
            "course" : details["course"]
        }

    return profile

print(student(
    "Shuaib",
    80,
    75,
    90,
    age=28,
    course="Data Science"
))