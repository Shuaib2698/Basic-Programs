'''Find the first non-repeating element
Input:
[4, 5, 1, 2, 1, 4, 5]


Output:
2'''

def non_rep(arr):
    freq = {}

    for i in arr:
        freq[i] = freq.get(i, 0) + 1

    for keys, value in freq.items():
        if value == 1:
            return keys

    return None

arr = [4, 5, 1, 2, 1, 4, 5]
print(non_rep(arr))

