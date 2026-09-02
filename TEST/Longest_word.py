'''Find the Longest Word ⭐

Input:

sentence = "Python is powerful and easy"

Expected:

powerful

Write a function.'''

sentence = "Python is powerful and easy"

def longest_word(sentence):
    words = sentence.split()
    longest = ""

    for i in words:
        if len(i) > len(longest):
            longest = i
    return longest

print(longest_word(sentence))