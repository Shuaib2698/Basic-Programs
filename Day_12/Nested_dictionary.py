'''Nested Dictionary

Given:

students = {
    "Amit": {
        "age": 22,
        "marks": 85
    },
    "Sara": {
        "age": 21,
        "marks": 92
    },
    "John": {
        "age": 23,
        "marks": 78
    }
}

Write a function:

def highest_scorer(students):
    # your code

Expected output:

Sara
Your task

Return the name of the student who has the highest marks.

Don't use max() yet.

Try solving it yourself using:

for loop
dictionary access
comparison
a variable to track the highest marks'''

def highest_scorer(students):
    highest_marks = 0
    student = ""

    for keys, values in students.items():
        if values["marks"] > highest_marks:
            highest_marks = values["marks"]
            student = keys

    return student


students = {
    "Amit": {
        "age": 22,
        "marks": 85
    },
    "Sara": {
        "age": 21,
        "marks": 92
    },
    "John": {
        "age": 23,
        "marks": 78
    }
}
print(highest_scorer(students))
