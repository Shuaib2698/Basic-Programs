'''Find the Most Frequent Element

Input:

[1,2,2,3,3,3,4]

Output:

3'''

def frequent_ele(n):
    freq ={}

    for i in n:
        freq[i] = freq.get(i, 0)+1

    return max(freq, key= freq.get)

n = [1,2,2,3,3,3,4]
print(frequent_ele(n))