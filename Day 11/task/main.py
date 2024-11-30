import random, art

cards = {0: ["2", 2],
         1: ["3", 3],
         2: ["4", 4],
         3: ["5", 5],
         4: ["6", 6],
         5: ["7", 7],
         6: ["8", 8],
         7: ["9", 9],
         8: ["10", 10],
         9: ["J", 10],
         10: ["Q", 10],
         11: ["K", 10],
         12: ["A", 11, 1]
         }

card_keys = list(cards.keys())
dealers_dictionary = {"key": [],
                      "cards": [],
                      "points": 0,
                      "player": "Dealer"}
players_dictionary = {"key": [],
                      "cards": [],
                      "points": 0,
                      "player": "Player"}
first_greeting = "Would you want to play a game of Blackjack? Types 'y' or 'n':\n"
second_greeting = "Type 'y' to get another card or 'n' to pass:\n"
#Greating the player
def does_player_want_to_play(message):
    start_game = input(message)
    if start_game.lower() == "y":
        return True
    elif start_game.lower() == "n":
        print("Thank you for playing!")
        return False
    else:
        print("Please enter either 'y' or 'n'.")
        return does_player_want_to_play(message)

#Get a players hand values
def get_hands_value(hand):
    hand_value = 0
    sorted_hand = sorted(hand["key"])
    for card_value in sorted_hand:
        if cards[card_value][0] == "A" and  hand_value + cards[card_value][1] > 21:
            hand_value += cards[card_value][2]
        else:
            hand_value += cards[card_value][1]
    return hand_value

#Get a card
def get_card(current_player_dictionary):
    random_card = random.choice(card_keys)
    current_player_dictionary["key"].append(random_card)
    current_player_dictionary["cards"].append(cards[random_card][0])
    current_player_dictionary["points"] = get_hands_value(current_player_dictionary)

#Complete dealers hand
def complete_dealers_hand():
    while dealers_dictionary["points"] < 17:
        get_card(dealers_dictionary)

def display_cards():
    print(f"    Your cards are: {players_dictionary['cards']}. Your current score is: {players_dictionary['points']}")
    if len(dealers_dictionary["cards"]) < 2:
        print(f"    Dealer's first card: {dealers_dictionary['cards']}. Dealers score is: {dealers_dictionary['points']}\n")
    else:
        print(f"    Dealer's final cards are: {dealers_dictionary['cards']}. Dealers score is: {dealers_dictionary['points']}\n")


def check_bust_cards(player):
   if player["points"] == 21:
       print("Black jack baby!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
       complete_dealers_hand()
       display_cards()
       return True
   if player["points"] > 21:
       return True
   else:
       return False

#Check winner
def check_winner():
    if players_dictionary["points"] > 21:
        print("Dealer wins! Player Bust\n")
        return
    elif dealers_dictionary["points"] > 21:
        print("Player wins! Dealer Bust\n")
        return
    elif players_dictionary["points"] == 21 and dealers_dictionary["points"] == 21:
        print("It a tie! Even though theres two blackjacks!!!\n")
        return
    elif players_dictionary["points"] == dealers_dictionary["points"]:
        print("it's a tie...!!\n")
        return
    elif dealers_dictionary["points"] == 21:
        print("Dealer wins!! Black Jack Baby!!\n")
        return
    elif players_dictionary["points"] == 21:
        print("PLAYER wins!! Black Jack!!\n")
        return
    elif dealers_dictionary["points"] > players_dictionary["points"]:
        print("Dealer wins!!\n")
    else:
        print("PLAYER wins!!\n")

#Player wants another card or pass
def another_card_or_pass(message):
    player_bust_or_not = check_bust_cards(players_dictionary)
    if player_bust_or_not:
        check_winner()
        return

    player_choice = input(message)
    if player_choice.lower() == "y":
        get_card(players_dictionary)
        display_cards()
        return another_card_or_pass(message)
    elif player_choice.lower() == "n":
        # Complete dealers cards
        complete_dealers_hand()
        display_cards()
        check_winner()
        return
    else:
        print("Please enter either 'y' or 'n'.")
        return another_card_or_pass(message)

#Set each hand empty
def empty_hands(hand):
    for key in hand:
        if key == "key":
            hand[key] = []
        elif key == "cards":
            hand[key] = []
        elif key == "points":
            hand[key] = 0
        else:
            print(f"Shuffling back {hand[key]}'s hand.")

keep_playing = does_player_want_to_play(first_greeting)

while keep_playing:
    empty_hands(dealers_dictionary)
    empty_hands(players_dictionary)
    print(art.logo)
    # Dealers first card
    get_card(dealers_dictionary)
    # Players first 2 cards
    get_card(players_dictionary)
    get_card(players_dictionary)
    #Display cards
    display_cards()
    #Ask player for more cards
    another_card_or_pass(second_greeting)

    keep_playing = does_player_want_to_play(first_greeting)


