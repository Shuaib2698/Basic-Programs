'''Count Characters

Input:

"hello"

Output:

{'h':1, 'e':1, 'l':2, 'o':1}'''

def count_char(c):
    freq = {}
    for i in c:
        if i in freq:
            freq[i] +=1
        else:
            freq[i] = 1

    return freq

c = "hello"
print(count_char(c))