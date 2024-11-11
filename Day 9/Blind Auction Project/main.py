# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)
bids = {}
add_user = True

def add_to_bids(user, user_bid):
    bids[user] = user_bid
def compare_bids():
    winner = list(bids.keys())[0]
    print(f"First in dictionary is: {winner}")
    for bidder in bids:
        if bids[bidder] >= bids[winner]:
            winner = bidder

    globals() ["add_user"] = False
    print(f"Winner is: {winner} with a bid of {bids[winner]}.")
while add_user:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    add_to_bids(name, bid)
    add_more_user = input("Would you like to add more bidder? press 'y' for Yes and 'n' for No: ")
    if add_more_user == "y":
        print("\n" * 100)
        add_user = True
    else:
        compare_bids()

