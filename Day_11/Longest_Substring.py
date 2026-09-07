
'''Longest Substring Without Repeating Characters ⭐⭐⭐

Given:

s = "abcabcbb"

Expected:

3

Because the longest substring without repeating characters is:

"abc"

Another example:

s = "pwwkew"

Expected:

3

Don't use a library that directly solves the problem.

Hint: You'll need a dictionary or another structure to keep track of characters you've seen.

This is an important interview problem, so don't worry if this one is difficult.'''


s = "abcabcbb"

def len_longsubstr(s):
    seen = set()
    l = 0
    max_len = 0

    for i in range(len(s)):
        while s[i] in seen:
            seen.remove(s[l])
            l+=1

        seen.add(s[i])
        max_len = max(max_len, i-l +1)
    return max_len

print(len_longsubstr(s))