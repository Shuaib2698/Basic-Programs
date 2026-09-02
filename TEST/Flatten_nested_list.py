'''Flatten a Nested List ⭐⭐

Input:

data = [1, [2, 3, [4, 5], 6], 7]

Expected:

[1, 2, 3, 4, 5, 6, 7]

The nesting depth can be arbitrary.

Use isinstance() and recursion.'''


arr =[1, [2, 3, [4, 5], 6], 7]

def flatten(arr):
    result = []

    for i in arr:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)

    return result

print(flatten(arr))