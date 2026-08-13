'''Write a program that repeatedly asks the user to input a number. The program should print the square of the number.
The loop should continue until the user inputs 0. If the user inputs a non-numeric value, print an error message
and ask for the input again.'''


while True:
  try :
    n = float(input("Enter the number : "))
    if n == 0:
      print("Exited")
      break
    print(n**2)

  except ValueError:
    print("invalid Input")
