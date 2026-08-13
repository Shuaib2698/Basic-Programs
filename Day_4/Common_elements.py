'''Find common elements
A = [1, 2, 3, 4, 5]
B = [3, 4, 5, 6, 7]

Output:
[3, 4, 5]'''

A = [1, 2, 3, 4, 5]
B = [3, 4, 5, 6, 7]

def common_ele(A, B):
    com = []

    # TC = O(n*m) /O(n^2) if size same (simple code)
    for i in A:
        if i in B:
            com.append(i)
    return com

    # TC = O(n*m) /O(n^2) if size same (more code)
    # for i in A:
    #     for j in B:
    #         if i == j:
    #             com.append(i)
    # return com
print(common_ele(A, B))

