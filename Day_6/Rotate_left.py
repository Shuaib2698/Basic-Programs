'''Rotate list left by one
Input:
[1, 2, 3, 4, 5]


Output:
[2, 3, 4, 5, 1]'''

def rotate_left(arr, k):
    n = len(arr)
    k = k % n

    def swap(l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l+=1
            r-=1

    swap(0, n-1) #5,4,3,2,1
    swap(0, n-k-1) #2,3,4,5,1  5-1-1 = 3
    swap(n-k, n-1) # 2,3,4,5,1    4, 1-1=0

    return arr

arr = [1,2,3,4,5]
print(rotate_left(arr,k=1))
