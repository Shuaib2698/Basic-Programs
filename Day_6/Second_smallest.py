'''Second Smallest — Unique
Input:
[10, 50, 20, 70, 40]


Output:
20

Also handle:

[10, 10, 20, 30]

Expected:

20'''

def second_smallest(arr):
    first = float('inf')
    second = float('inf')

    for i in arr:
        if i < first:
            second = first
            first = i

        elif i < second and i != first:
            second = i

    return second

arr = [10, 10, 20, 30]
print(second_smallest(arr))