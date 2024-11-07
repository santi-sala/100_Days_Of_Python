print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

player_choice = input('You arrive into an intersection. Type "right" to go on the Right or anything else to go on the left.\n')
if player_choice == 'right' or player_choice == 'Right':
    print("You fall into a hole. Game Over!!")
    exit()
player_choice = input('You arrived into a lake. Type "swim" to swim or anything else to wait for a boat.\n')
if player_choice == 'swim' or player_choice == 'Swim':
    print("You've been attacked by a trout. Game Over!! ")
    exit()
player_choice = input('You have three doors in front of you. Choose between "red", "blue" or "yellow"\n')
if player_choice == 'red' or player_choice == 'Red':
    print("You've been burned by fire. Game Over!! ")
    exit()
elif player_choice == 'blue' or player_choice == 'Blue':
    print("You've been eaten by beasts. Game Over!! ")
    exit()
elif player_choice == 'yellow' or player_choice == 'Yellow':
    print("Congratulation you found the treasure. You win!! ")
    exit()
else:
    print("I could not understand you. You died by waiting  too long. Game Over!!")
    exit()