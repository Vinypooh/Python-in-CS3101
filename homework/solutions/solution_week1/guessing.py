# CS3101-1 Python - Homework 1
# Daniel Bauer (db2711)
# Problem 1

import random

# guess a secret number
secret_number = random.choice(range(1,11)

for i in range(5): #user has 5 attempts
    guess = int(input('Guess a number between 1 and 10:'))
    difference = abs(guess - secret_number)

    if difference == 0:
        print("Congratulations, you won")
        break
    elif difference > 5:
        print("not even close")
    elif difference < 3:
        print("almost there")
    elif difference >= 3 and difference <=5:
        print("close")
    else: 
        print "user entered invalid number"
else:
    print("Sorry you lost")
