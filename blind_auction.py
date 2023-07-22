import os
from blind_auction_art import logo
print(logo)

# The program is to take in bids for items and then compare and award the bid to the individual with the highest bid

bids = {}

# The program will run on a while loop to ensure that as many users as is present can input their bids
still_bidding = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # The program will take in the record of the users by recording their individual names and how much each is bidding. It will then only compare the amounts to determine the winner
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_bid}")

while still_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == "no":
        still_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system("cls")
