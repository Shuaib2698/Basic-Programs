def check_prime(n):
    if n <= 1:
        return "Not Prime"

    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"

    return "Prime"

n = int(input("Enter the number to check : "))
print(check_prime(n))

    