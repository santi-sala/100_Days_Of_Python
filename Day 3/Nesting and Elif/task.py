print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you?\n"))
    if age > 18:
        print("Its 12€, thank you!")
    elif age >= 12:
        print("Its 7€, thank you!")
    else:
        print("It's 5€ thank you!")
else:
    print("Sorry you have to grow taller before you can ride.")
