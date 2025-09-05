"""Module for console hangman python game"""
import time
import threading
from inputimeout import inputimeout, TimeoutOccurred
from game import Game
from dictionary import Dictionary


# Timer constant
INPUT_TIMER_SECOND = 15
# Thread event for countdown
is_countdown_finished = threading.Event()


def countdown_timer():
    """
    Function used to print out a timer counting down.
    It will stop the countdown prematurely if
    is_countdown_finished is already set.
    """
    for x in range(INPUT_TIMER_SECOND, 0, -1):
        if is_countdown_finished.is_set():
            break
        print("Time:", x)
        print("Enter your guess :")
        time.sleep(1)


def get_guess_timed():
    """
    Function used to get user's guess
    with a timer counting down.
    """
    # Clears event flag & starts countdown in a new thread
    is_countdown_finished.clear()
    thread = threading.Thread(target=countdown_timer)
    thread.daemon = True
    thread.start()

    # Gets user input with a timeout
    # Flags the event flag if input received/timer ran out
    guess = None
    try:
        guess = inputimeout(
            prompt="", timeout=INPUT_TIMER_SECOND
        )
        is_countdown_finished.set()
        thread.join()
    except TimeoutOccurred:
        is_countdown_finished.set()
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
            print("Ran out of time :( lost 1 attempt.")
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
