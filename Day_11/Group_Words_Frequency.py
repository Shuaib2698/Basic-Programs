'''Group Words by Frequency ⭐⭐

Given:

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

Expected:

{
    "apple": 3,
    "banana": 2,
    "orange": 1
}

Use a dictionary.'''

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

def word_group(words):
    result = {}

    for i in words:
        result[i] = result.get(i, 0) + 1

    return result

print(word_group(words))