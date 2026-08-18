'''. Find pairs with a given sum

Given:

arr = [2, 7, 11, 15]
target = 9

Output:

[2, 7]

Because:

2 + 7 = 9

Start with a brute-force solution using nested loops.'''

def two_sum(arr, t):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == t:
                return [arr[i], arr[j]]

    return None

arr = [2, 7, 11, 15]
print(two_sum(arr, t=9))