'''Find duplicate elements
Input:
[1, 2, 3, 2, 4, 5, 3]

Output:
[2, 3]

Don't print the same duplicate more than once.'''

n = [1, 2, 3, 2, 4, 5, 3]

def duplicate_num(n):
    dup = []
    seen = []
    for i in n:
        if i in seen:
            if i not in dup:
                dup.append(i)
        else:
            seen.append(i)
    return dup

print(duplicate_num(n))