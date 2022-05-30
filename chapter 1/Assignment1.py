# The below program is to Roll the Dice
import random
def roll_dice(max_dice_number):
    number_rolled=random.randint(1, max_dice_number)
    return number_rolled


def main():
    max_dice_number=6
    roll_again=True
    while roll_again:
        roll_dice=input("Ready to roll? Enter Q to Quit")
        if roll_dice.lower() !="q":
            number_rolled=roll_dice(max_dice_number)
            print("You have rolled a",number_rolled)
        else:
            roll_again=False

main()