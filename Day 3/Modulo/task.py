# Challenge one
print("Calculate the modulo of two numbers")
first_number = int(input("Enter a first number:\n"))
second_number = int(input("Enter a second number:\n"))
modulo_number = first_number % second_number
print(f"The module number of {first_number} % {second_number} is: {modulo_number}")

#Challenge two
print("Check if a given number is Even or Odd")
given_number = int(input("Enter a number to check if it is Even or Odd\n"))
if given_number % 2 == 0:
    print(f"The number {given_number} is an EVEN number")
else:
    print(f"The number {given_number} is an ODD number")
