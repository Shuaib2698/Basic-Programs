'''Separate even and odd
Input:
[1, 2, 3, 4, 5, 6]


Output:
Even: [2, 4, 6]
Odd: [1, 3, 5]'''

def sep_eve_odd(arr):
    even = []
    odd = []
    for i in arr:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd

arr = [1,2,3,4,5,6]
print(sep_eve_odd(arr))