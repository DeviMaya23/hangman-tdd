"""Test module for console_hangman.py"""
from console_hangman import init_game


def test_init_game_easy_option():
    """
    Test function of init_game() that checks
    if the answer of the game is one word.

    The check is done by calling isalpha() to ensure
    all chracters in the string are alpha.
    """
    game = init_game("easy")
    assert game.answer.isalpha() == 1


def test_init_game_hard_option():
    """
    Test function of init_game() that checks
    if the answer of the game is a phrase.

    The check is done by calling split() and len()
    """
    game = init_game("hard")
    assert len(game.answer.split()) > 1
