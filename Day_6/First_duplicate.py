'''Find the first duplicate
Input:
[5, 3, 4, 3, 2, 5]


Output:
3'''

def first_dup(arr):
    seen = set()
    for i in arr:
        if i in seen:
            return i
        seen.add(i)

    return None

arr = [5, 3, 4, 3, 2, 5]
print(first_dup(arr))