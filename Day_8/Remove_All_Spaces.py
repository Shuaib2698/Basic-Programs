'''Remove All Spaces

Write a function that removes spaces from a string.

Input
"I love Python programming"
Expected output
"IlovePythonprogramming"

Try doing it without using:

replace()'''

i = "I love Python programming"

def remove_space(i):
    new = ""
    for ch in i:
        if ch != " ":
            new+=ch

    return new

print(remove_space(i))