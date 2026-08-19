'''Count Vowels

Input:

"programming"

Output:

3'''

def count_vowels(str1):
    vowels = 'AEIOUaeiou'
    count = 0

    for i in str1:
        if i in vowels:
            count+=1

    return count

print(count_vowels(str1 = "programming"))