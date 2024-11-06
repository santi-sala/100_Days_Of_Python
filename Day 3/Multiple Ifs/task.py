print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

price = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?\n"))
    if age <= 12:
        price = 5
        print(f"Price is: {price}€.")
    elif age <= 18:
        price = 7
        print(f"Price is: {price}€.")
    else:
        price = 12
        print(f"Price is: {price}€.")

    picture = input("Do you want to have a picture? Type y for Yes and n for No:\n")
    if picture == "y":
        price += 3
        print(f"That's an extra 3€ for a total of {price}€ thank you.")
    else:
        print(f"That would be {price}€ thank you.")
else:
    print("Sorry you have to grow taller before you can ride.")
