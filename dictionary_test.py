"""Test module for dictionary.py"""
from dictionary import Dictionary


def test_get_word():
    """
    Test case that checks if the function get_word
    returns a single word (all alpha characters)
    """
    dictionary = Dictionary()
    assert dictionary.get_word().isalpha() == 1


def test_get_phrase():
    """
    Test case that checks if the function get_phrase
    returns a phrase (more than one word)
    """
    dictionary = Dictionary()
    assert len(dictionary.get_phrase().split()) > 1
