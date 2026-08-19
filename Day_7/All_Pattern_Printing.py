'''Pattern Printing
Q9.

Output:

*
**
***
****
*****'''

n = 5
print("=====Right Angle Triange(*)===== \n")
for i in range(1, n+1):
    print("*"*i)

print("=====Inverted Right Angle Triange(*)===== \n")
for i in range(n, 0, -1):
    print("*"*i)

print("=====Right Angle Triange(numbers)===== \n")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()

print("=====inverted Right Angle Triange(numbers)=====\n ")
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end="")
    print()

print("=====Right Angle Triange(numbers)===== \n")
for i in range(1, n+1):
    for j in range(i):
        print(i, end ="")
    print()

print("=====inverted Right Angle Triange(numbers)===== \n")

for i in range(n, 0, -1):
    for j in range(i):
        print(i, end="")
    print()

print("=====Rectangle(*)===== \n")

for i in range(1, n+1):
  for j in range(1, n+1):
    if i == 1 or i == n or j == 1 or j == n:
      print("*", end = "")
    else:
      print(" ", end = "")
  print()

print("=====pyramid(*)===== \n")

for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()


print("=====inverted pyramid(*)===== \n")

for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()

