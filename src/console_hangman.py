"""Module for console hangman python game"""

from game import Game
from dictionary import Dictionary
import time
import threading
from inputimeout import inputimeout, TimeoutOccurred


# Timer constant
INPUT_TIMER_SECOND = 5


# Global variable for threading purposes
user_input = None
is_countdown_finished = 0


def countdown_timer():
    """
    Function used to print out a timer counting down.
    """
    global is_countdown_finished
    for x in range(INPUT_TIMER_SECOND, 0, -1):
        if is_countdown_finished:
            break
        print("Time:", x)
        print("Enter your guess :")
        time.sleep(1)


def get_guess_timed():
    """
    Function used to get user's guess
    with a timer counting down.
    """
    global is_countdown_finished
    is_countdown_finished = 0

    thread = threading.Thread(target=countdown_timer)
    thread.daemon = True
    thread.start()

    guess = None
    try:
        guess = inputimeout(
            prompt="", timeout=INPUT_TIMER_SECOND
        )
        is_countdown_finished = 1
        thread.join()
    except TimeoutOccurred:
        is_countdown_finished = 1
        thread.join()
        guess = None

    return guess


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
        print("===================================")
        print("Your clue is: ", game.current_answer())
        print("Attempts remaining: ", game.life)
        print("===================================")

        while True:
            guess = get_guess_timed()
            if guess is None:
                game.deduct_life()
                break
            try:
                game.validate_guess(guess)
            except ValueError as err:
                print("Input error: ", err)
            else:
                break
        if guess is None:
            continue
        if game.check_answer(guess):
            print("\nCorrect guess!")
            if game.is_game_finished():
                print("\n\nCongratulations! You have won!")
                break
        else:
            print("\nIncorrect...")
            if not game.is_game_alive():
                print("\n\nGame over :(")

    print("The answer is: ", game.answer)
