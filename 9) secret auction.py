print("Welcome to secret auction!!!")
dictionary = {}
people = True
while people:
    name = input("enter your name: ")
    price = int(input("enter your bid: $"))
    dictionary[name] = price
    decision = input("Is there anyone else (type 'yes' or 'no'): ").lower()
    if decision == "no":
        people = False
highest_bid = 0
for names in dictionary:
    bid = dictionary[names]
    if bid > highest_bid:
        highest_bid = bid
        winner = names
print(f"The winner is {winner} and their bid is ${highest_bid}")
