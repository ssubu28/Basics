# Guess the number

"""
Generate random Number
Input number through user
Compare both numbers
"""

from random import randint

Val = True

def CompareNumbers(genNum, usrNum):
    if genNum == usrNum:
        return "Correct Guess! Do you want to try again ? If yes, please press 'y'. "
    else:
        if usrNum > genNum:
            return "Incorrect Guess: Number too large. Press 'y' to try again!"
        else:
            return "Incorrect Guess: Number too small. Press 'y' to try again!"



while Val:
    usrNum = int(raw_input("Enter a number between 0 and 500."))
#    if usrNum != int(usrNum):
#        print "Please enter a valid integer."

    genNum = randint(0,5)
    print 'GenNum = ', genNum

    print CompareNumbers(genNum, usrNum)

    tryAgain = raw_input()
    if tryAgain == 'y' or tryAgain == 'Y':
        Val = True
    else:
        Val = False
