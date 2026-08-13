'''Find the Frequency of the elements list'''
n = [1, 2, 2, 3, 1, 2, 4]

def freq_nums(n):
    freq = {}

    # Second way
    # for i in n:
    #     if i in freq:
    #         freq[i]+=1
    #     else:
    #         freq[i] = 1
    # return freq

    for i in n:
        freq[i] = freq.get(i, 0)+1
    return freq

print(freq_nums(n))