import random

choice = ["rock", "paper", "scisors"]

computer = random.choice(choice)

player = input("rock, paper or scissors?: ")


print(f"computer: {computer}")
print(f"player: {player}")