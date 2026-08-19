'''Find Maximum Value

Input:

marks = {
    "Math": 85,
    "Science": 90,
    "English": 78
}

Output:

Science'''

def max_val():
    marks = {
        "Math": 85,
        "Science": 90,
        "English": 78
    }
    #
    # return max(marks, key = marks.get)

    max_marks = 0
    subject = ""

    for keys, values in marks.items():
        if values > max_marks:
            max_marks = values
            subject = keys

    return subject

print(max_val())