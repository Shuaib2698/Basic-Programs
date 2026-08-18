'''Replace negative numbers with zero
Input:
[10, -2, 5, -7, 8, -1]


Output:
[10, 0, 5, 0, 8, 0]'''

def replace_neg(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = 0
    return arr

arr = list(map(int, input().split()))
print(replace_neg(arr))