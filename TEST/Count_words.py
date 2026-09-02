'''Count Words ⭐

Input:

sentence = "python java python sql python java"

Expected:

{
    "python": 3,
    "java": 2,
    "sql": 1
}'''

sentence = "python java python sql python java"

def count_word(sentence):
    words = sentence.split()
    result = {}

    for i in words:
        result[i] = result.get(i, 0) + 1

    return result

print(count_word(sentence))