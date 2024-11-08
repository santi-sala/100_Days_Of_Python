import random, pipo_module

# print(str(random.randint(0, 10)))
# print(f"Pipo's number is {pipo_module.my_number}.")

random_number = random.random()
print(f"Random number is: {random_number}")
if random_number > 0.5:
    print("Tails")
else:
    print("Heads")