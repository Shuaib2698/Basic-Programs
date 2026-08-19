'''Reverse a String

Input:

"python"

Output:

"nohtyp"'''

# def rev_string(str1):
#     return str1[::-1]

str1 = input("enter the str :")
def rev_string(str1):
    rev = ""
    for i in str1:
        rev = i + rev

    return rev

print(rev_string(str1))