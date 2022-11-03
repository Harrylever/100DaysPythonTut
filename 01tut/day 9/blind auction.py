import sys
print("Blind Auction Logo")
auction_details = {}
message = ''
counter = True
while counter:
    player_name = input("Enter your name?: ")
    player_bid = int(input("What's your bid?: $"))
    auction_details[player_name] = player_bid
    while True:
        cont = input("Are there any other bidders? Type \'Yes\' or \'No\' ").lower()
        if cont == "yes":
            break
        elif cont == "no":
            auction_bid = 0
            for bidders in auction_details:
                if auction_details[bidders] > auction_bid:
                    auction_bid = auction_details[bidders]
                    message = f"The winner is {bidders} with a bid of ${auction_details[bidders]}"
                elif auction_details[bidders] == auction_bid:
                    message += f"\nThe winner is {bidders} with a bid of ${auction_details[bidders]}"
            print(message)
            sys.exit()
        else:
            print("Please enter a valid answer")
