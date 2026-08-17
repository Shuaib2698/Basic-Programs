'''Input:
[1, 2, 3, 4, 5, 6, 7, 8]

Output:
[2, 4, 6, 8]

using list cpmprehension'''

n = [1, 2, 3, 4, 5, 6, 7, 8]

def extract_even(n):
    nums = [x for x in n if x%2==0]
    return nums

print(extract_even(n))