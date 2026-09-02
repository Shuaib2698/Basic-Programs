'''Reverse a String ⭐

Write a function:

reverse_string("hello")

Expected:

"olleh"

Try to solve it without using a built-in reverse function.'''


string = input("Enter the string :")

def reverse_string(string):
    reverse = ""

    for i in string:
        reverse = i + reverse

    return reverse

print(reverse_string(string))