'''Find the Longest Word

Input:

"I am learning Python programming"

Expected output:

"programming"

Don't use any library specifically designed to find the longest word.'''

words = "I am learning Python programming"

def long_word(words):
    word = words.split()
    longest = ""

    for i in word:
        if len(i) > len(longest):
            longest = i

    return longest

print(long_word(words))

