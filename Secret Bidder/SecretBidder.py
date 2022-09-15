import os
from time import sleep

print("""
Welcome to the
                  _   _             
                 | | (_)            
  __ _ _   _  ___| |_ _  ___  _ __  
 / _` | | | |/ __| __| |/ _ \| '_ \ 
| (_| | |_| | (__| |_| | (_) | | | |
 \__,_|\__,_|\___|\__|_|\___/|_| |_|



""")
loop = 'yes'

bid_data = {}

while loop == 'yes':
    name = input("Enter your name.\n")
    bid = int(input("Enter the amount you want to bid.\n$"))
    loop = input("Type 'yes' if there are more bidder, else type 'no'.\n").lower()

    bid_data[name] = bid

    if loop == 'yes':
        print("Screen will clear in one second.")
        sleep(1)
        os.system('cls')

max_bid = 0
max_bid_name = ''
for i in bid_data:
    score = bid_data[i]
    if score > max_bid:
        max_bid = score
        max_bid_name = i 

print(f"{max_bid_name} won the auction for the amount ${max_bid}.")
