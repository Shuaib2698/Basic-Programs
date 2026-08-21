'''Count Words in a Sentence

Count how many times each word occurs.

Input:

"python is easy and python is powerful"

Expected output:

{
    "python": 2,
    "is": 2,
    "easy": 1,
    "and": 1,
    "powerful": 1
}

Hint:

sentence.split()'''

words = input("Enter the sentence : ").split()

def count_words(words):
    freq = {}
    for ch in words:
        freq[ch] = freq.get(ch, 0) + 1

    return freq

print(count_words(words))