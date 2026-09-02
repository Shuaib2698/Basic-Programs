'''Q3 — Count Characters ⭐

Input:

"programming"

Expected:

{
    "p": 1,
    "r": 2,
    "o": 1,
    "g": 2,
    "a": 1,
    "m": 2,
    "i": 1,
    "n": 1
}

Use a dictionary.'''

n = input("Enter the string :")

def count_char(n):
    count = {}

    for i in n:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    return count
print(count_char(n))