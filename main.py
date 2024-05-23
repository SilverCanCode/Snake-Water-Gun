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
comp = random.choice(choice)
def Game():
# Case 1
    user = input("Enter your choice - S for Snake, W for water, G for gun: ").lower()
    if user == comp:
        return(f"You choosed {user} and the computer choosed {comp}. Its an draw !")
    # Case 2
    elif user == "s" and comp == "g":
        return(f"You choosed {user} and the computer choosed {comp}. The computer wins !")
    elif user == "g" and comp == "s":
        return(f"You choosed {user} and the computer choosed {comp}. You win !")
    # Case 3
    elif user == "g" and comp == "w":
        return(f"You choosed {user} and the computer choosed {comp}. The computer wins !")
    elif user == "w" and comp == "g":
        return(f"You choosed {user} and the computer choosed {comp}. You win !")
    # Case 4
    elif user == "w" and comp == "s":
        return(f"You choosed {user} and the computer choosed {comp}. The computer wins !")
    elif user == "s" and comp == "w":
        return(f"You choosed {user} and the computer choosed {comp}. You win !")
    else:
        return("Invalid move")
print(Game())

con = input("Do you want to continue the game ? (Yes/No):  ").lower()

if con == "yes":
    print(Game())
elif con == "no":
    print("The game has exited successfully.")
else:
    print("Invalid input")