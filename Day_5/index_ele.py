'''Find the index of an element

Given:

arr = [10, 20, 30, 40, 50]

Input:

30

Output:

Index: 2

If it doesn't exist:

Element not found

Restriction: Don't use .index().'''

arr = [10, 20, 30, 40, 50]
k = int(input("Enter the element: "))

def no_index(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return f"index: {i}"

    return "Element not found"


print(no_index(arr, k))

