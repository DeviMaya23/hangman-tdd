"""Module for the main running program"""
from console_hangman import init_game, run_game

# Start Game
print("Welcome to Hangman!")

# Pick difficulty
while True:
    option = input("Pick your difficulty. Easy or hard?\n")
    if option.lower() == "easy":
        print("Easy it is!")
        break
    if option.lower() == "hard":
        print("Hard it is!")
        break
    print("Invalid option!")

game = init_game(option)
run_game(game)
