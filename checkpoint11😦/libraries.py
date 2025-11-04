# import random
# coin = random.choice(["heads", "tails"])
# print(coin)
# n = random.randint(1, 10)
# print(n)
# cards = ["Jack", "Queen", "King", "Ace"]
# random.shuffle(cards)
# for card in cards:
#     print(card)

# import statistics
# print(statistics.mean([100, 90]))

import sys
import cowsay   # i succesfully install it but it doesn't work????
try:
    cowsay.cow("hello,", sys.argv[1])
except IndexError: 
    # print("too few arguments u.u")
    sys.exit("too few arguments.") #it can be empty to just stop the program.
