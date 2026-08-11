n = int(input("Enter the Year to check leap year : "))

def leap_year(n):
    if n % 4 == 0 and n % 100 != 0:
        return True
    elif n % 400 == 0:
        return True
    return False

if leap_year:
    print(n , "is a leap year")
else:
    print(n, "is not a leap year")