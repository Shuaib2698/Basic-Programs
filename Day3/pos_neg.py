'''Write a Python program that continuously takes user input until the user enters 0. The program should keep a running sum of positive numbers and negative numbers separately. Use a while loop for continuous input, and if-else to classify numbers as positive or negative.                                                                             Enter a number: 5
Enter a number: -3
Enter a number: 8
Enter a number: -2
Enter a number: 0
O/p Sum of positive numbers: 13
Sum of negative numbers: -5 '''

pos = 0
neg = 0

while True:
  try:
    n = int(input("Enter the number : "))
    if n == 0:
      print("Exited")
      print("Sum of positive numbers : ",pos)
      print("Sum of negative numbers : ",neg)
      break
    elif n > 0:
      pos += n  
    elif n < 0:
      neg += n
  except ValueError:
    print("Please Enter valid number")

    
    