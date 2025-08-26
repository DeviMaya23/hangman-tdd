import pytest
from game import Game


@pytest.mark.parametrize(
    ("word", "answer", "result"),
    [
        ("Pity", "y", 1),
        ("Pity", "a", 0),
    ]
)
def test_check_answer(word, answer, result):
    logic = Game(word)
    assert logic.check_answer(answer) == result
