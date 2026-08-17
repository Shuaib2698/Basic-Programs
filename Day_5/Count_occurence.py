arr = [1, 2, 2, 3, 2, 4, 2]
n = int(input("Enter the element to find no.of occurnce : "))

def count_occerence(arr):
    count = 0

    for i in arr:
        if i == n:
            count+=1
    return count

print(count_occerence(arr))