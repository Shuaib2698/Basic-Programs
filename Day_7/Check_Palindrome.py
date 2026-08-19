'''Check Palindrome

Input:

"madam"

Output:

True'''

from Reverse_a_String import rev_string

def chk_palid(s):
    if s == rev_string(s):
        return True
    return False

print(chk_palid(s = 'madam'))