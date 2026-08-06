'''Q1 — Fibonacci Series

Write a function that prints the first n Fibonacci numbers.

Example:

Input:
7

Output:
0 1 1 2 3 5 8'''

n = int(input("Enter the n value : "))

def fibonacci(n):
  first = 0
  second = 1
  print(first, second, end= " ")

  for i in range(n):
    next = first + second
    first = second 
    second = next
    print(next, end = " ")

fibonacci(n)
