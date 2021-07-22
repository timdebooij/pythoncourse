name = input("Enter your name please: ")
age = int(input("Enter your age please: "))

if 18 <= age < 31:
    print("Welcome {}, let's go on the holiday!".format(name))
else:
    print("Excuses, you are not in the right age range")
