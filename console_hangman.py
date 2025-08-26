"""Module for console hangman python game"""

from game import Game
from dictionary import Dictionary


INPUT_TIMER_SECOND = 15


def init_game(difficulty):
    """
    Function used to initialise the dictionary.

    Args:
        difficulty (string): difficulty option for the game (easy/hard)
        dictionary (Dictionary): dictionary object
    """
    dictionary = Dictionary()
    if difficulty.lower() == "easy":
        ans = dictionary.get_word()
    else:
        ans = dictionary.get_phrase()
    return Game(ans)


def run_game(game):
    """
    Function used to run the game.

    Args:
        Game: Game object
    """
    while game.is_game_alive():
        print("Your clue is: ", game.current_answer())
        print("Attempts remaining: ", game.life)

        while True:
            guess = input("Enter your guess: ")
            try:
                game.validate_guess(guess)
            except ValueError as err:
                print("Input error: ", err)
            else:
                break
        if game.check_answer(guess):
            print("Correct guess!")
            if game.is_game_finished():
                print("Congratulations! You have won!")
                break
        else:
            print("Incorrect...")
            if not game.is_game_alive():
                print("Game over :(")

    print("The answer is: ", game.answer)
