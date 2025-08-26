"""Testing module"""
from console_hangman import run_game
from game import Game


def test_run_game_win(monkeypatch):
    """
    Test function to check the game state
    when provided a winning input
    """

    # Monkeypatch all console input()
    inputs = iter(["easy", "a", "s", "h", "e", "n"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # The answer is fixed so the test can guess correctly
    game = Game("ashen")
    run_game(game)

    assert game.is_game_finished() == 1


def test_run_game_losing(monkeypatch):
    """
    Test function to check the game state
    when provided a winning input
    """

    # Monkeypatch all console input()
    inputs = iter(["easy", "a", "s", "h", "e", "n"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    game = Game("bully")
    run_game(game)

    assert game.is_game_finished() == 0
    assert game.is_game_alive() == 0
