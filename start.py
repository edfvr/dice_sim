import random

player_input = "y"
while player_input == "y":
    number = random.randint(1,6)

    if number == 1:
        print("\n|       |\n|   o   |\n|       |\n")
    if number == 2:
        print("\n| o     |\n|       |\n|     o |\n")
    if number == 3:
        print("\n|     o |\n|   o   |\n| o     |\n")
    if number == 4:
        print("\n| o   o |\n|       |\n| o   o |\n")
    if number == 5:
        print("\n| o   o |\n|   o   |\n| o   o |\n")
    if number == 6:
        print("\n| o   o |\n| o   o |\n| o   o |\n")

    player_input = input("Again? [y/n]:\n")