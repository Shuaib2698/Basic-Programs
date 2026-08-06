'''Q5 — Palindrome Number

Example

121

Output

True
123

Output

False'''

n = int(input("Enter the number : "))

def palidrome_num(n):
    # if n == n[::-1]:
    #     print('True')
    # else:
    #     print("False")
    num = n
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10

    if rev == num:
        return True
    else:
        return "Not a Palidrome number"
    
print(palidrome_num(n))

