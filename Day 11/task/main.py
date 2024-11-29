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
                      "points": 0
                      }
players_dictionary = {"key": [],
                      "cards": [],
                      "points": 0
                      }
#Starting the game
def does_player_want_to_play():
    start_game = input("Would you want to play a game of Blackjack? Types 'y' or 'n':\n")
    if start_game.lower() == "y":
        return True
    elif start_game.lower() == "n":
        print("Thank you for playing!")
        return False
    else:
        print("Please enter either 'y' or 'n'.")
        does_player_want_to_play()

keep_playing = does_player_want_to_play()

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

#Dealers first card
get_card(dealers_dictionary)
#Players first 2 cards
get_card(players_dictionary)
get_card(players_dictionary)
#make sure the dealers hand is more than 17
complete_dealers_hand()
#while keep_playing:

#Missing to write down the loop for playing!!!

print(f"Dealers cards: {dealers_dictionary["cards"]}, Dealers points: {dealers_dictionary['points']}")
print(f"Players cards: {players_dictionary["cards"]}, Players points: {players_dictionary['points']}")



