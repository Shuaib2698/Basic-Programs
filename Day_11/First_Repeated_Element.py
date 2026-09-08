'''Find First Repeated Element ⭐⭐

Given:

numbers = [4, 7, 2, 9, 7, 5, 2]

Expected:

7

Return the first element that appears again while scanning from left to right.

Don't use set() for this one.'''

numbers = [4, 7, 2, 9, 7, 5, 2]

def first_rep_ele(numbers):
    seen = {}
    for i in numbers:
        if i in seen:
            return i
        seen[i] = True

    return False

print(first_rep_ele(numbers))
