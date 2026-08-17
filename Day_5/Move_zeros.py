# Given an array, move all zeros to the end while maintaining the order of other elements.
# Input: [1, 0, 2, 0, 3, 0, 4]
# Output: [1, 2, 3, 4, 0, 0, 0]

arr = [1, 0, 2, 0, 3, 0, 4]

#method 1: using extra lists
# def move_zeros(arr):
#     zero = []
#     digits = []
#
#     for i in range(len(arr)):
#         if arr[i] != 0:
#             digits.append(arr[i])
#         else:
#             zero.append(arr[i])
#
#     return digits + zero

#Method 2 using list comprehension
# def move_zeros(arr):
#     digits = [x for x in arr if x!=0]
#     zeros = [0] * (len(arr) - len(digits))
#     return digits + zeros


def move_zeros(arr):
    pos = 0

    for x in range(len(arr)):
        if arr[x]!=0:
            arr[x], arr[pos] = arr[pos], arr[x]
            pos = pos + 1

    return arr

print(move_zeros(arr))