'''First Non-Repeating Character ⭐

Find the first character that appears only once.

Input:

"swiss"

Expected output:

"w"

Think about using a frequency dictionary.'''

def non_rep_char(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0)+ 1

    for i in freq:
        if freq[i] == 1:
            return i
    return None

print(non_rep_char(s = 'swiss'))