'''Q2 — Find Missing Number

Given a list containing numbers from 1 to n, with one number missing, find the missing number.

Example:

arr = [1,2,4,5,6]

Output:

3

Rules:

Don't use sort().
Don't use another list.'''

n = int(input("Enter the n numbers :"))

arr = list(map(int, input("Enter the elements :").split()))

def missing_nums(n):
  expected  = n*(n+1)//2
  actual = sum(arr)
  missing = expected - actual
  return missing

print("The missing number from the array is ",missing_nums(n))



