import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
password_list = []
i = 0
while i < nr_letters:
    element = random.choice(letters)
    print(element)
    password += element
    password_list.append(element)
    i += 1

i = 0
while i < nr_symbols:
    element = random.choice(symbols)
    print(element)
    password += element
    password_list.append(element)

    i += 1

i = 0
while i < nr_numbers:
    element = random.choice(numbers)
    print(element)
    password += element
    password_list.append(element)

    i += 1

print(f"Non shuffled password is: {password}")
random.shuffle(password_list)
print(f"Shuffled password LIST is:{password_list}")

shuffled_password = ""
for character in password_list:
    shuffled_password += character

print(f"Shuffled password STRING is:{shuffled_password}")



