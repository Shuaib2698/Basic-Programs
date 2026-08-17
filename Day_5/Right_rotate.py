'''Rotate a list one position to the right
Input:
[1, 2, 3, 4, 5]


Output:
[5, 1, 2, 3, 4'''

n = [1,2,3,4,5]
a = len(n)
k = 1

def right_rotate(n, k):
    k = k % a

    def swap(l, r):
        while l < r:
            n[l], n[r] = n[r], n[l]
            l+=1
            r-=1

    swap(0, a-1)
    swap(0, k-1)
    swap(k, a-1)

    return n

print(right_rotate(n, k))


