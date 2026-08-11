'''Check if input is a single-digit, double-digits or more'''

n = input("Enter digits : ")
digit = len(str(abs(n)))


if digit == 1:
    print(n ,"is single-digits number")
elif digit > 2:
    print(n ,"is more than 2 digits")
else:
    print(n ,"is a double-digit number")
