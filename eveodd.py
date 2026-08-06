'''Write a function that returns whether a number is even or odd.
Input: 25
Output: Odd'''

n = int(input("Enter the number : "))

def even_odd(n):
    if n % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

even_odd(n)
