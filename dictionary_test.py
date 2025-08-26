"""Test module for dictionary.py"""
from dictionary import Dictionary, word_list, phrase_list


def test_init_custom_dictionary():
    """
    Test case that checks whether or not the init
    function populates custom word/phrase list properly.
    """
    dictionary = Dictionary(["Pikachu"], ["Kanto Region"])
    assert dictionary.get_word() == "Pikachu"
    assert dictionary.get_phrase() == "Kanto Region"


def test_init_default_dictionary():
    """
    Test case that checks whether or not the init
    function populates the default word/phrase list properly.
    """
    dictionary = Dictionary()
    assert dictionary.word_list == word_list
    assert dictionary.phrase_list == phrase_list


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
