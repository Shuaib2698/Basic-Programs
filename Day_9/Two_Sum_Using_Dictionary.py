'''Two Sum Using a Dictionary ⭐

This is a very common interview problem.

Given a list of numbers and a target, find two numbers whose sum equals the target.

Input
numbers = [2, 7, 11, 15]
target = 9
Expected output
[2, 7]
Another example
numbers = [3, 2, 4]
target = 6

Expected:

[2, 4]
Important condition

Use a dictionary to solve it.

Don't use nested loops for this version.'''


num = [3,2,4]
target = 6

def two_sum_dic(num, target):
    freq = {}

    for i in num:
        freq[i] = freq.get(i, 0) + 1

    for i in freq:
        needed = target - i

        if needed  in freq :
            if needed != i or freq[i] >=2:
                return [i, needed]
    return False
print(two_sum_dic(num, target))