"""Testing module"""
from inputimeout import TimeoutOccurred
from console_hangman import run_game
from game import Game


def test_run_game_win(monkeypatch):
    """
    Test function to check the game state
    when provided a winning input
    """

    # Monkeypatch all console input
    inputs = iter(["easy", "w", "h", "y"])
    monkeypatch.setattr(
        "console_hangman.inputimeout", lambda prompt, timeout: next(inputs))
    monkeypatch.setattr("console_hangman.INPUT_TIMER_SECOND", 1)

    # The answer is fixed so the test can guess correctly
    game = Game("why")
    run_game(game)

    assert game.is_game_finished() == 1  # checks if the game is won


def test_run_game_losing(monkeypatch):
    """
    Test function to check the game state
    when provided a winning input
    """

    # Monkeypatch all console input
    inputs = iter(["easy", "w", "h", "y", "s", "u"])
    monkeypatch.setattr(
        "console_hangman.inputimeout", lambda prompt, timeout: next(inputs))
    monkeypatch.setattr("console_hangman.INPUT_TIMER_SECOND", 1)

    game = Game("are")
    run_game(game)

    # assert that game is lost
    assert game.is_game_finished() == 0  # checks if the game is won
    assert game.is_game_alive() == 0  # checks if the game has 0 attempts


def test_run_game_timeout(monkeypatch, capsys):
    """
    Test function to check the game state
    when the timer to guess ran out
    """

    # Monkeypatch all console input()
    def timeout(prompt, timeout):
        raise TimeoutOccurred()

    monkeypatch.setattr("console_hangman.INPUT_TIMER_SECOND", 2)
    monkeypatch.setattr(
        "console_hangman.inputimeout", timeout)

    game = Game("bully")
    run_game(game)

    captured = capsys.readouterr()

    # assert that the losing attempts are printed out
    assert "Attempts remaining:  4" in captured.out
    assert "Attempts remaining:  3" in captured.out
    assert "Attempts remaining:  2" in captured.out
    assert "Attempts remaining:  1" in captured.out

    # assert that the game is lost
    assert game.is_game_finished() == 0
    assert game.is_game_alive() == 0
