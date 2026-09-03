'''Find Maximum Without max() ⭐

Input:

numbers = [12, 45, 7, 89, 34, 23]

Expected:

89

Don't use max().'''

def largest_num(arr):
    largest = float('-inf')


    for i in arr:
        if i > largest:
            largest = i

    return largest

arr = [12, 45, 7, 89, 34, 23]
print(largest_num(arr))