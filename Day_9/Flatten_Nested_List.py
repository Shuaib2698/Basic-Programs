'''Flatten a Nested List ⭐

Given:

data = [1, [2, 3], [4, [5, 6]], 7]

Expected output:

[1, 2, 3, 4, 5, 6, 7]

Condition: Don't use libraries or a built-in flattening function.

This one is harder because the nesting can be at different depths.

Think about whether a normal for loop is enough, or whether you'll need recursion.'''

data = [1, [2, 3], [4, [5, 6]], 7]

def fallaten(data):
    result = []
    for i in data:
        if isinstance(i, list):
            result.extend(fallaten(i))
        else:
            result.append(i)

    return result

print(fallaten(data))