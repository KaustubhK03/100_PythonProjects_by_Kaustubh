from logo import logo
import replit
print(logo)
Auction_dict = {}
highest_bid = []
bidder = "yes"
while bidder == 'yes':
    replit.clear()
    name = input("What is your name? ")
    bid = int(input("What's your bid amount? "))
    Auction_dict[name] = bid
    highest_bid.append(bid)
    bidder = input("Are there any other bidders? 'yes' or 'no'")

winning_amount = 0
for key in Auction_dict:
    amount = Auction_dict[key]
    if amount > winning_amount:
        winning_amount = amount
        winner = key
    else:
        continue
print(f"The winner is {winner} with a bid of {winning_amount}.")