import pytest
from game import Game


@pytest.mark.parametrize(
    ("word", "answer", "result", "life", "revealed", "correct_characters"),
    [
        ("pity", "y", 1, 5, {3}, {"y"}),
        ("pity", "a", 0, 4, {}, {}),
        ("pity", "P", 1, 5, {0}, {"p"}),
        ("small", "l", 1, 5, {3, 4}, {"l"})
    ]
)
def test_check_answer(
        word, answer, result, life, revealed, correct_characters):
    game = Game(word)
    assert game.check_answer(answer) == result
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
def test_current_word(word, revealed, expected):
    game = Game(word)
    game.revealed = revealed
    assert game.current_word() == expected
