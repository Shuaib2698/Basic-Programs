'''Frequency of Elements

Input:

[1, 2, 2, 3, 1, 2]

Output:

{1:2, 2:3, 3:1}'''

def freq_ele():
    freq = {}

    # for i in n:
    #     freq[i] = freq.get(i, 0) + 1

    for i in n:
        if i in freq:
            freq[i]+=1
        else:
            freq[i] =1

    return freq

n = [1,2,2,3,1,2]
print(freq_ele())