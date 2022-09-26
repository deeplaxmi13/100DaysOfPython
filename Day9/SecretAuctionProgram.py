from art import logo

print(logo)


# name = input("Enter your name: ")
# bid_price = int(input("Enter your bid price: "))

bids = {}
bidding_finished = False

# def add_person(name, bid_price):
#     bids[name]:bid_price

def findHighestBidder(biddingrecord):
    highestBid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if highestBid < bid_amount:
            highestBid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the highest bid of ${highestBid}")

        
    


while not bidding_finished:
    name = input("Enter your name: ")
    bid_price = int(input("Enter your bid price: "))
    bids[name] = bid_price
    # add_person(name,bid_price)
    ifAnyOtherBidders =  input("Enter 'yes' if there are any other bidders otherwise type 'no': ").lower()
    if ifAnyOtherBidders == "no":
        bidding_finished = True
        findHighestBidder(bids)







