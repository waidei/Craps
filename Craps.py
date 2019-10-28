# Isaac Waide
# October 23, 2019
# Craps Due Friday Oct 25,2019
import random

bank = account
roll = roll_dice
bet = bank


def account():
    print("Welcome to Hartwick College roll of chance.")


print("How much money will you be betting today?")
bet = int(input)

while bet <= 0:
    print("Sorry boss, you cannot bet nothing, please try again.")
    bet = int(input)

while bank > 0 and bet > 0:
    def roll_dice():
        return random.randint(2, 12)
print(f"No more bets, time to roll the two dice, you rolled a {roll}.")
if roll == 7 or roll == 11:
    print("Congrats Champ! You won!")

choice = input()
