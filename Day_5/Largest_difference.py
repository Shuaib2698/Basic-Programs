'''Find the largest difference
Input:
[7, 1, 5, 3, 6, 4]


Output:
5'''

n = [7, 1, 5, 3, 6, 4]

#Buy and Sell program. Buy when the price is low and sell when prices is high
def lar_diff(n):
    buy = n[0]
    profit = 0

    for i in range(1, len(n)):
        if n[i] < buy:
            buy = n[i]
        elif n[i] - buy > profit:
            profit = n[i] - buy

    return profit

print(lar_diff(n))