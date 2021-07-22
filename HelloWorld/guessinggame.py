import random

highest = 1000
answer = random.randint(0, highest)
count = 0

print("Please guess a number between 1 and {}: ".format(highest))
while True:
    guess = int(input())
    count += 1
    if guess == answer:
        print("well done, you got it in {} guesses".format(count))
        break
    elif guess == 0:
        print("You quited")
        break
    elif guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")




