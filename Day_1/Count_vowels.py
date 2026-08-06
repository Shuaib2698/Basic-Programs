'''Q6 — Count Vowels

Input

"Data Science"

Output

5'''

n = input("Enter the string : ")

def count_vowels(n):
    vowels = 'aeiouAEIOU'
    count = 0

    for i in n:
        if i in vowels:
            count+=1

    print(count)

count_vowels(n)