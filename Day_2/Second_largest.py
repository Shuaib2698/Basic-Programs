'''Second Largest Number

Given a list:

[10, 50, 20, 70, 40]

Output:

50'''

n = list(map(int, input("Enter the list").split()))

def sec_largest(n):
  large = float('-inf')
  second = float('-inf')
  for i in n:
    if large < i:
      second = large
      large = i

    elif i > second and second < large:
      second = i

  return second

print(sec_largest(n))
