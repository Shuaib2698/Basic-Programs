'''Palindrome ⭐

Write a function that checks whether a string is a palindrome.

is_palindrome("madam")

Expected:

True

And:

is_palindrome("hello")

Expected:

False

Bonus: Reuse the reverse-string function you created in Q1 by importing it from another Python file.'''
from Reverse_string import reverse_string

def is_palindrome(string):
    if string != reverse_string(string):
        return False
    return True

print(is_palindrome("madam"))