# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art

print(art.logo)
print("Welcome to the Bidding Auction!\n")

bidding = True

bid_info = {}

while bidding:

    user_name = input("Enter your name: ")
    user_price = int(input("Enter your price: $"))
    bid_info[user_name] = user_price

    new_bidder = input("Are there any other bidders? (y/n)\n").lower()

    if new_bidder == "y":
        print("\n" * 20)
    else:
        bidding = False


print("\n" * 20)

winner = max(bid_info, key=bid_info.get)
max_price = bid_info[winner]

print(f"The winner is {winner} with bidding ${max_price}.")
