"""Test module for the module game"""

import pytest
from game import Game


@pytest.mark.parametrize(
    ("word", "answer", "result"),
    [
        ("pity", "y", 1),
        ("pity", "a", 0),
        ("pity", "P", 1)
    ]
)
def test_check_answer_result(
        word, answer, result):
    game = Game(word)
    assert game.check_answer(answer) == result


@pytest.mark.parametrize(
    ("word", "answer", "life", "revealed", "correct_characters"),
    [
        ("pity", "y", 5, {3}, {"y"}),
        ("pity", "a", 4, {}, {}),
        ("pity", "P", 5, {0}, {"p"}),
        ("small", "l", 5, {3, 4}, {"l"})
    ]
)
def test_check_answer_state(
        word, answer, life, revealed, correct_characters):
    game = Game(word)
    game.check_answer(answer)
    assert game.life == life
    assert sorted(game.revealed) == sorted(revealed)
    assert sorted(game.correct_characters) == sorted(correct_characters)


def _check_answer_game_in_progress_game():
    game = Game("small")
    game.check_answer("s")
    return game


@pytest.mark.parametrize(
    ("game", "answer", "life", "revealed", "correct_characters"),
    [
        (_check_answer_game_in_progress_game(), "l", 5, {0, 3, 4}, {"s", "l"}),
        (_check_answer_game_in_progress_game(), "k", 4, {0}, {"s"})
    ]
)
def test_check_answer_game_in_progress(
        game, answer, life, revealed, correct_characters):
    game.check_answer(answer)
    assert game.life == life
    assert sorted(game.revealed) == sorted(revealed)
    assert sorted(game.correct_characters) == sorted(correct_characters)


@pytest.mark.parametrize(
    ("word", "revealed", "expected"),
    [
        ("Pity", {3}, "_ _ _ y"),
        ("Pity", {}, "_ _ _ _"),
        ("Small", {0, 3, 4}, "s _ _ l l")
    ]
)
def test_current_answer(word, revealed, expected):
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
    game = Game("test")
    game.life = life
    assert game.is_game_alive() == expected
