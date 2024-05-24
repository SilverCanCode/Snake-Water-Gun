# Case 1 - DRAW
# Case 2 - SNAKE > GUN
# Case 3 - GUN > WATER
# Case 4 - WATER > SNAKE

from art import *
import random

print(display)
print("Welcome to game - SNAKE WATER GUN.")
print(rules)
choice = ["s", "w", "g"]


def game():
    comp = random.choice(choice)
    # Case 1
    user = input("Enter your choice - S for Snake, W for water, G for gun: ").lower()
    if user == comp:
        return f"You chose {user} and the computer chose {comp}. Its an draw !"
    # Case 2
    elif user == "s" and comp == "g":
        return f"You chose {user} and the computer chose {comp}. The computer wins !"
    elif user == "g" and comp == "s":
        return f"You chose {user} and the computer chose {comp}. You win !"
    # Case 3
    elif user == "g" and comp == "w":
        return f"You chose {user} and the computer chose {comp}. The computer wins !"
    elif user == "w" and comp == "g":
        return f"You chose {user} and the computer chose {comp}. You win !"
    # Case 4
    elif user == "w" and comp == "s":
        return f"You chose {user} and the computer chose {comp}. The computer wins !"
    elif user == "s" and comp == "w":
        return f"You chose {user} and the computer chose {comp}. You win !"
    else:
        return "Invalid move"


print(game())

answer = True

while answer:
    con = input("Do you want to continue the game ? (Yes/No):  ").lower()
    if con == "yes":
        print(game())
    elif con == "no":
        answer = False
        print("Bye Bye")
    else:
        print("Invalid input")
