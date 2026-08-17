arr = [10, 20, 10, 30, 10, 40]
k = int(input("Enter the element : "))

def index_occ(arr):
    index = []

    for i in range(len(arr)):
        if arr[i] == k:
            index.append(i)

    return index
print(index_occ(arr))