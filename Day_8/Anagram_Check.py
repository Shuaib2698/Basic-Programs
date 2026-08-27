'''Anagram Check ⭐

Two strings are anagrams if they contain the same characters with the same frequency.

Example 1
"listen"
"silent"

Output:

True
Example 2
"hello"
"world"

Output:

False

Try solving this using a frequency dictionary rather than simply sorting the strings.'''

def anagram_check(s1, s2):
    freq1 = {}
    freq2 = {}

    if len(s1)!= len(s2):
        return False

    for i in s1:
        freq1[i] = freq1.get(i, 0)+1

    for j in s2:
        freq2[j] = freq2.get(j, 0)+1


    for key in freq1:
        if freq1[key] != freq2[key]:
            return False

    return True

print(anagram_check(s1="listen", s2="silent"))