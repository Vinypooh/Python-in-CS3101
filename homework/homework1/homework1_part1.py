#Part 1
#######

import random

m1 = 'not even close'
m2 = 'close'
m3 = 'almost there'
m4 = 'correct! you win'
m5 = 'sorry, you have tried 5 times, you lose!'

randomN = random.choice(range(1,11))
n = 5
while n > 0:
    guess = int(input('Guess a number between 1 and 10: '))
    para = abs(randomN - guess)
    if para == 0:
        print(m4)
        break
    elif para > 5:
        print(m1)
    elif 3 <= para <= 5:
        print(m2)
    else:
        print(m3)
    n -= 1
else:
    print ('=' * 20)
    print(m5)


