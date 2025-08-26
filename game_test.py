import pytest
from game import Game


@pytest.mark.parametrize(
    ("word", "answer", "result", "life", "revealed", "correct_characters"),
    [
        ("Pity", "y", 1, 5, [3], ["y"]),
        ("Pity", "a", 0, 4, [], []),
        ("Small", "l", 1, 5, [3, 4], ["l"])
    ]
)
def test_check_answer(
        word, answer, result, life, revealed, correct_characters):
    game = Game(word)
    assert game.check_answer(answer) == result
    assert game.life == life
    assert sorted(game.revealed) == sorted(revealed)
    assert sorted(game.correct_characters) == sorted(correct_characters)
