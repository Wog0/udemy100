import os
clear = lambda: os.system('cls')




def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bids in bidding_record:
        actual_bids = bidding_record[bids]
        if actual_bids > highest_bid:
            actual_bids = highest_bid
            winner = bids
    print(f"The winner is {winner} and the highest bid is {highest_bid}")





bidding = True
new_dict = {}
while bidding:
    name = input ("What is your name: \n")
    bid = int(input("What is your bid:\n "))
    new_dict[name] = bid
    amount = input("Are there any other bidders? Type 'yes' or 'no' ")
    bidding  
    if amount == "no":
        bidding = False
        find_highest_bidder(new_dict)
    elif amount =="yes":
        clear()



    














