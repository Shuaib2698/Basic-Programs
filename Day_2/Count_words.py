'''Q14 — Count Words

Input:

Python is easy to learn

Output:

5'''

s = list(map(str, input("Enter the string : ").split()))
# s = list(str1)
# print(s)

def count_word(s):
  count = 0
  for i in s:
    count+=1

  return count

print(count_word(s))