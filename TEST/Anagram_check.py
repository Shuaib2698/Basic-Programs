'''Anagram Check ⭐

Write:

is_anagram("listen", "silent")

Expected:

True

And:

is_anagram("hello", "world")

Expected:

False

Try using a frequency dictionary rather than simply sorting the strings.'''

def is_anagram(s1, s2):
    a1 = {}
    a2 = {}
    if len(s1) != len(s2):
        return False

    for i in s1:
        a1[i] = a1.get(i, 0) + 1

    for j in s2:
        a2[j] = a2.get(j, 0) + 1


    for key in a1:
        if a1[key] != a2[key]:
            return False

    return True

print(is_anagram(s1 = "hello", s2 = "word"))
