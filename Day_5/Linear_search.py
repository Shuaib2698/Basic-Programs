'''Linear Search

Given:

arr = [10, 25, 30, 45, 50]

Take a number from the user and determine whether it exists.'''

n = int(input("Enter the number to search : "))

arr = list(map(int, input().split()))

def linear_search(arr):
    for i in arr:
        if i == n:
            return "Found"
    return "Not found"

print(linear_search(arr))