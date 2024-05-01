import os
def clear():
  os.system('clear')

from art import logo
print(logo)
print("Welcome to the secret auction program.")
bidders_name = input("What is your name? :")
bidders_price = int(input("What's your bid: $"))
bidders_dictionary = {}
bidders_dictionary["Bidder's Name"] = bidders_name
bidders_dictionary["Bidder's Price"] = bidders_price
bidders = []
bidders.append(bidders_dictionary)
while True:
  choice = input("Are there are any other bidder's? Type 'yes' or 'no'. \n")
  if choice == 'yes':
    clear()
    bidders_name = input("What is your name? :")
    bidders_price = int(input("What's your bid: $"))
    bidders_dictionary = {}
    bidders_dictionary["Bidder's Name"] = bidders_name
    bidders_dictionary["Bidder's Price"] = bidders_price
    bidders = []
    bidders.append(bidders_dictionary)
  elif choice == 'no':
    break


clear()
highest_bid = 0
for bid in bidders:
  if bid["Bidder's Price"] > highest_bid:
    bidders_price = bidders_dictionary["Bidder's Price"]
    bidders_name = bidders_dictionary["Bidder's Name"]
print(f"The winner is {bidders_name} with a bid of ${bidders_price}")

