options = ["1.\t Learn Python", "2.\t Learn Java", "3.\t Learn C#", "4.\t Go Swimming", "5.\t Have dinner",
           "6.\t Go to bed", "0.\t Quit"]
still_going = True
wrong_option = False
while still_going:
    if not wrong_option:
        print("Please choose your option from the list below: ")
        for option in options:
            print(option)
    choice = input()
    for option in options:
        if choice in option and choice.isdigit():
            if choice == "0":
                print("You quited")
                still_going = False
                break
            print("Your chose number: {} : {}".format(choice, option))
            print("Choose again:")
            wrong_option = True
            break
    else:
        print("your option: {} was not in the list".format(choice))
        wrong_option = False
