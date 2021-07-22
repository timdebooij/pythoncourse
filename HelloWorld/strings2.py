# parrot = "Norwegian Blue"
#
# print(parrot[0:6])  # Norweg
#
# print(parrot[:9])
#
# print(parrot[-4:-2])
# print(parrot[-4:12])
#
# print(parrot[:6:2])

# number = input("Please enter a series of numbers, using any separators: ")
#
# seperators = ""
# for char in number:
#     if not char.isnumeric():
#         seperators = seperators + char
# print(seperators)
#
# # seperators = number[1::4]
# values = "".join(char if char not in seperators else " " for char in number).split()
# print([int(val) for val in values])
# print(sum([int(val) for val in values]))

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
for char in quote:
    if str. isupper(char):
        print(char)
