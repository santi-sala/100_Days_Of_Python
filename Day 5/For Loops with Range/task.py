for number in range(1, 10):
    print(number)

print("\n")
for number in range(1,10, 2):
    print(number)

total_number = 0
current_number = 0
for number in range(1, 101):
    total_number += number
    current_number += 1
    print(f"Current number is: {current_number} and total is: {total_number}")

print(f"The sum of all numbers from 1 to 100 is: {total_number}")