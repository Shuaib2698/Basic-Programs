'''Q15 — Anagram Check

Check whether two strings are anagrams.

Example:

listen
silent

Output:

True

Example:

hello
world

Output:

False'''

s1 = input("Enter the 1st string : ")
s2 = input("Enter the 2nd string : ")

# Using Sorted()
# def anagram(s1, s2):
#   if len(s1)!= len(s2):
#     return False

#   if sorted(s1) == sorted(s2):
#     return True
#   else:
#     return False

# print(anagram(s1, s2))

#Without Using Sorted()

def anagram(s1, s2):
    if len(s1)!= len(s2):
        return False

    freq = {}

    for ch in s1:
        freq[ch] = freq.get(ch, 0)+1

    for ch in s2:
        if ch not in freq:
            return False
        freq[ch] -= 1

        if freq[ch] < 0:
            return False

    return True

if anagram(s1, s2):
    print("Anagram")
else:
    print("Not Anagram")