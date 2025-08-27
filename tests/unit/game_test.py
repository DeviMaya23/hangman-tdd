"""Test module for the module game"""

import pytest
import errors
from game import Game


@pytest.mark.parametrize(
    ("word", "answer", "result"),
    [
        ("pity", "y", 1),
        ("pity", "a", 0),
        ("pity", "P", 1),
        ("small favours", "s", 1)
    ]
)
def test_check_answer_result(word, answer, result):
    """
    Test case for checking if the function check_answer returns the correct
    value or not.
    """
    game = Game(word)
    assert game.check_answer(answer) == result


@pytest.mark.parametrize(
    ("word", "answer", "life", "revealed", "correct_characters"),
    [
        ("pity", "y", 5, {3}, {"y"}),
        ("pity", "a", 4, {}, {}),
        ("pity", "P", 5, {0}, {"p"}),
        ("small", "l", 5, {3, 4}, {"l"}),
        ("small favours", "s", 5, {0, 12}, {"s"})
    ]
)
def test_check_answer_state(
        word, answer, life, revealed, correct_characters):
    """
    Test case for checking if the function check_answer updates the
    game attributes correctly or not.
    """
    game = Game(word)
    game.check_answer(answer)
    assert game.life == life
    assert sorted(game.revealed) == sorted(revealed)
    assert sorted(game.correct_characters) == sorted(correct_characters)


def _example_in_progress_game():
    """
    Helper function that returns an ongoing game to be used in testing.
    """
    game = Game("small")
    game.check_answer("s")
    return game


@pytest.mark.parametrize(
    ("game", "answer", "life", "revealed", "correct_characters"),
    [
        (_example_in_progress_game(), "l", 5, {0, 3, 4}, {"s", "l"}),
        (_example_in_progress_game(), "k", 4, {0}, {"s"})
    ]
)
def test_check_answer_game_in_progress(
        game, answer, life, revealed, correct_characters):
    """
    Test case for checking if the function check_answer updates the
    game attributes of an ongoing game correctly or not.
    """
    game.check_answer(answer)
    assert game.life == life
    assert sorted(game.revealed) == sorted(revealed)
    assert sorted(game.correct_characters) == sorted(correct_characters)


@pytest.mark.parametrize(
    ("word", "revealed", "expected"),
    [
        ("Pity", {3}, "_ _ _ y"),
        ("Pity", {}, "_ _ _ _"),
        ("Small", {0, 3, 4}, "s _ _ l l"),
        ("Small favours", {0, 3, 4, 12}, "s _ _ l l   _ _ _ _ _ _ s")
    ]
)
def test_current_answer(word, revealed, expected):
    """
    Test case for checking if the function current_answer
    prints out the current answer correctly or not.
    """
    game = Game(word)
    game.revealed = revealed
    assert game.current_answer() == expected


@pytest.mark.parametrize(
    ("life", "expected"),
    [
        (2, 1),
        (0, 0)
    ]
)
def test_is_game_alive(life, expected):
    """
    Test case for checking if the function is_game_alive
    returns correct value.
    """
    game = Game("test")
    game.life = life
    assert game.is_game_alive() == expected


@pytest.mark.parametrize(
    ("current_game", "guess"),
    [
        (_example_in_progress_game(), "l"),
        (_example_in_progress_game(), "L")
    ]
)
def test_validate_guess_correct(current_game, guess):
    """
    Test case for checking if the function validate_guess
    runs correctly.
    """
    assert current_game.validate_guess(guess) is None


@pytest.mark.parametrize(
    ("current_game", "guess", "exception", "error_message"),
    [
        (_example_in_progress_game(), "s", ValueError,
            errors.ERROR_INPUT_USED),
        (_example_in_progress_game(), "@", ValueError,
            errors.ERROR_INPUT_INVALID),
        (_example_in_progress_game(), "sa", ValueError,
            errors.ERROR_INPUT_INVALID)
    ]
)
def test_validate_guess_incorrect(
        current_game, guess, exception, error_message):
    """
    Test case for checking if the function validate_guess
    returns correct error message for a failed input validation.
    """
    with pytest.raises(exception, match=error_message):
        current_game.validate_guess(guess)


@pytest.mark.parametrize(
    ("answer", "revealed", "expected"),
    [
        ("Me", {0, 1}, 1),
        ("Me Want", {0, 1, 3, 4, 5, 6}, 1)
    ]
)
def test_is_game_finished(answer, revealed, expected):
    """
    Test case for checking if the function is_game_finished
    returns correct value.
    """
    game = Game(answer)
    game.revealed = revealed
    assert game.is_game_finished() == expected


def test_deduct_life():
    """
    Test case for checking if the function deduct_life
    correctly deducts one life in the game state.
    """
    game = Game("Test")
    game.deduct_life()
    assert game.life == 4
