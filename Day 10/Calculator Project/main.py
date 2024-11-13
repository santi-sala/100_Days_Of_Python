import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
print(art.logo)


keep_calculating = True
first_time = True
first_number = 0

while keep_calculating:
    if first_time:
        first_number = float(input("What is your first number? "))
    for symbol in operations:
        print(symbol)
    current_operation = input("Pick an operation? ")
    second_number = float(input("What's the next number? "))
    print(f"{first_number} {current_operation} {second_number} = {operations[current_operation](first_number, second_number)}")
    first_number = operations[current_operation](first_number, second_number)

    continue_calculating = input(f"Type 'y' to continue calculating with {first_number}, or type 'n' to start a new calculation: ")
    if continue_calculating.lower() == "y":
        keep_calculating = True
        first_time = False
    elif continue_calculating.lower() == "n":
        keep_calculating = True
        first_time = True
        first_number = 0
    else:
        keep_calculating = False
        print("Thank you for using Pipo Calculator")




