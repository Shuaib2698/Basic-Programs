'''Q7 — Frequency of Characters (Interview Favorite)

Input

programming

Output

p : 1
r : 2
o : 1
g : 2
...'''


n = input("Enter the string : ")

def freq_char(n):
    freq = {}

    for i in n:
        if n[i] == 0:
            n[i] +=1
        else:
            n[i] = 1

    print(freq)

freq_char(n)