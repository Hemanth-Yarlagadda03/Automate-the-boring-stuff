import random
guess = ''
while guess not in ('heads', 'tails'):
 guess = input()
tossvalue = random.randint(0, 1) # 0 is tails, 1 is heads
toss = ''

if tossvalue == 0:
    toss = 'tails'
else:
    toss = 'heads'

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')