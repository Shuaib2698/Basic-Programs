'''Flatten Nested List ⭐⭐

You've already solved the basic version, so this time:

data = [1, [2, [3, 4]], 5, [6, [7, [8, 9]]]]

Expected:

[1, 2, 3, 4, 5, 6, 7, 8, 9]

Use recursion.'''

data = [1, [2, [3, 4]], 5, [6, [7, [8, 9]]]]

def flatten(data):
    result = []

    for i in data:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)

    return result

print(flatten(data))