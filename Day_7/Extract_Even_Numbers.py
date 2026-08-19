'''Extract Even Numbers

Input:

[1,2,3,4,5,6,7,8]

Output:

[2,4,6,8]'''

# Using List Comprehensions

def extract_eve(n):
    return [x for x in n if x%2==0]

n = [1,2,3,4,5,6,7,8]
print(extract_eve(n))