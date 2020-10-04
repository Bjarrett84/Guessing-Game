import random

highest = 20
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = 0 # initialise to any number that doesn't equal the answer

while guess != answer:
    guess = int(input())

    if guess == answer:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else: # guess must be greater than answer
            print("Please guess lower")









