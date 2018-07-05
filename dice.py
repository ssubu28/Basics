# Dice rolling simulator
"""
Random selection of number + print
Ask if dice should be rolled again
Values range: min = 1 and max = 6
"""

import random


def randomNumberGenerate():
    randomNumber = random.randint(1,7)
    return randomNumber


while raw_input("Do you want to roll the dice again ? If yes, Please press 'y' followed by enter else please press enter: "):

    rn = randomNumberGenerate()

    print "Number on dice: ", rn
