#Sum of Digits

'''Input:
4567
Output:
22'''

n = int(input("Enter the digits : "))

def sum_digit(n):
    # by converting str to int  
#   sum = 0
#   for i in n:
#     sum = sum +int(i)
#   return sum

# Arithmatic way
    sum = 0

    while n > 0:
        digit = n % 10
        sum += digit
        n //= 10
    return sum


print(sum_digit(n))