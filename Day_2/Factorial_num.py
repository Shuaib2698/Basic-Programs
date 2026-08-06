'''Write a function to calculate the factorial of a number.

Example:

Input:
5
Output:
120'''

n = int(input("Enter the number : "))

def fact(n):
  if n == 0:
    return 0
  if n == 1:
    return 1

  return n * fact(n-1)

print(fact(n))