'''Remove Duplicate Characters

Write a function to remove repeated characters while preserving the original order.

Input:

"programming"

Expected output:

"progamin"

Hint:
programming → p r o g r a m m i n g

Keep only the first occurrence of each character.'''

def remove_rep_char(s):
    new_s = ""
    for i in s:
        if i not in new_s:
            new_s+=i
    return new_s

s = "programming"
print(remove_rep_char(s))