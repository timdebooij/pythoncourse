# available_exits = ["north", "south", "east", "west"]
#
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = str.casefold(input("Please choose a direction: "))
#     if chosen_exit == "quit":
#         print("Game over")
#         break
# print("glad you got out of that")

for i in range(0,21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)