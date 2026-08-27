'''Find Two Numbers Whose Sum Equals Target

Given:

numbers = [2, 7, 11, 15]
target = 9

Find the two numbers whose sum is equal to target.

Expected output:

[2, 7]

For now, don't worry about optimizing it with a dictionary. Try the straightforward nested-loop approach first.'''
num = [2,7,11,15]
target = 9
def two_sum(num, target):
    for i in range(len(num)):
        for j in range(1, len(num)):
            if num[i] + num[j] == target:
                return [num[i], num[j]]
    return None

print(two_sum(num , target))