import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

available_choices = [rock, paper, scissors]
def player_choice():
    try:
        return int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
    except ValueError:
        print("Your choice is not a number. You lose!")
        exit()
player_choice = player_choice()

if player_choice >= 3 or player_choice < 0:
    print("Choice is less than 0 or greater than 2. You lose!")
    exit()

computer_choice = random.randint(0, 2)

print(f"You chose: {available_choices[player_choice]}\n")
print(f"Computer chose: {available_choices[computer_choice]}\n")


if player_choice == 0:
    if computer_choice == 0:
        print("It's a tie!")
    elif computer_choice == 1:
        print("You lose!")
    else:
        print("You win!")
elif player_choice == 1:
    if computer_choice == 0:
        print("You win!")
    elif computer_choice == 1:
        print("It's a tie!")
    else:
        print("You lose!")
else:
    if computer_choice == 0:
        print("You lose!")
    elif computer_choice == 1:
        print("You win!")
    else:
        print("It's a tie!")



