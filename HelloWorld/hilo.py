low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("press ENTER to start")

guesses = 1

while True:
    guess = low + (high - low) // 2
    print("My guess is {}".format(guess))
    char = input("Is it higher, lower or correct(Type H, L or C): ").casefold()
    while char != "h" and char != "l" and char != "c":
        char = input("Please put only a H, L or C: ")
    if char == "h":
        low = guess + 1
    elif char == "l":
        high = guess - 1
    elif char == "c":
        if guesses == 1:
            print("I won in 1 move!")
        else:
            print("I won in {} moves!".format(guesses))
        break
    guesses += 1
