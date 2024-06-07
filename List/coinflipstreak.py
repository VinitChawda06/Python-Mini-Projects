# Title: Coin Flip streak
# Author: Vinit Chawda
# Date: 5th June 2024

import random

numberofstreaks = 0
for experimentNumber in range(10000):

# Code that creates a list of 100 'heads' or 'tails' values.
    l = []
    for i in range(100):
        l.append(random.choice(["H","T"]))

# Code that checks if there is a streak of 6 heads or tails in a row.
    hcount = 0
    tcount = 0
    for i in l:
        if i == "H":
            hcount += 1
            tcount = 0
            if hcount == 6:
                numberofstreaks += 1
                hcount = 0
                break

        elif i == "T":
            tcount += 1
            hcount = 0
            if tcount == 6:
                numberofstreaks += 1
                tcount = 0
                break

print('Chance of streak: %s%%' % (numberofstreaks / 100))