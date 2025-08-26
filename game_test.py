import pytest
from game import Game


@pytest.mark.parametrize(
    ("word", "answer", "result", "life"),
    [
        ("Pity", "y", 1, 5),
        ("Pity", "a", 0, 4),
    ]
)
def test_check_answer(word, answer, result, life):
    game = Game(word)
    assert game.check_answer(answer) == result
    assert game.life == life
