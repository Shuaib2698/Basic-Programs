'''Count Uppercase, Lowercase and Digits
Input
"Python123DATA456"
Expected output
Uppercase: 8
Lowercase: 6
Digits: 6

Hint: Python provides methods such as:

isupper()
islower()
isdigit()'''

n = "Python123DATA456"

def find_uld(n):
    uppercase = 0
    lowercase = 0
    digits = 0

    for i in n:
        if i.isupper():
            uppercase+=1
        elif i.islower():
            lowercase+=1
        elif i.isdigit():
            digits+=1

    return uppercase, lowercase, digits

print(find_uld(n))

