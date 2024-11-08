import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_number = random.randint(0, len(friends) -1)
print(f"Random number is: {random_number}.")
print(f"Random friend is: {friends[random_number]}.")

print(f"Random friend is: {random.choice(friends)}.")
