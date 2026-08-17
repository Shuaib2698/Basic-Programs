'''Find elements present in A but not B
A = [1, 2, 3, 4, 5]
B = [3, 4, 5]


Output:
[1, 2]'''

A = [1, 2, 3, 4, 5]
B = [3, 4, 5]

def unique_ele(A, B):
    unique = []
    for i in A:
        if i not in B:
            unique.append(i)
    return unique

print(unique_ele(A, B))