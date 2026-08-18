'''Extract positive numbers
Input:
[-5, 10, -2, 7, 0, -1, 20]


Output:
[10, 7, 20]'''

def pos_num(arr):
    pos = []
    for i in arr:
        if i > 0:
            pos.append(i)

    return pos

arr = list(map(int, input("Enter the list :").split()))
print(pos_num(arr))