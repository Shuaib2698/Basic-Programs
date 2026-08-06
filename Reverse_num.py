
'''Reverse a Number

Example:

12345

Output

54321'''

a = int(input("Enter the number : "))

# a = str(a)
# b = int(a[::-1])

# print(b)

rev = 0

while a > 0:
    digit = a % 10
    rev = rev * 10 + digit
    a//=10

print(rev)