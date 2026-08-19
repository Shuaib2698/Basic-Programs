'''Squares of Numbers

Input:

[1,2,3,4]

Output:

[1,4,9,16]'''

def sq_nums(n):
    return [x**2 for x in n ]
    # ans = []
    # for i in n:
    #     ans.append(pow(i, 2))
    #
    # return ans
n = [2, 5, 10, 20]
print(sq_nums(n))