'''Count Digits

Example

987654

Output

6'''

n = input("ENter the digits : ")

def count_dig(n):
    count = 0
    for i in n:
        count +=1

    print(count)

count_dig(n)