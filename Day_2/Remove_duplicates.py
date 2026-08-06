'''Q13 — Remove Duplicates

Input:

[1,2,2,3,4,4,5]

Output:

[1,2,3,4,5]'''


n = [1,2,2,3,4,4,5]

# def remove_dup(n):
#   seen = []

#   for i in n:
#     if i not in seen:
#       seen.append(i)

#   return seen

def remove_dup(n):
  ans = set(n)
  return ans

print(remove_dup(n))


