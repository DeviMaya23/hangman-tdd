import pytest
from game import Game


@pytest.mark.parametrize(
    ("word", "answer", "result", "life", "revealed"),
    [
        ("Pity", "y", 1, 5, [3]),
        ("Pity", "a", 0, 4, []),
        ("Small", "l", 1, 5, [3, 4])
    ]
)
def test_check_answer(word, answer, result, life, revealed):
    game = Game(word)
    assert game.check_answer(answer) == result
    assert game.life == life
    assert sorted(game.revealed) == sorted(revealed)
