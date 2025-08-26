"""This module provides a class that represents a hangman game with its
various functions."""


class Game:
    """This class represents a game of hangman."""

    def __init__(self, answer):
        """
        Initialisation function for the class.
        Args :
        answer (string): Word or phrase used in the game.
        """
        self.answer = answer.lower()
        self.life = 5
        self.revealed = set()
        self.correct_characters = set()

    def check_answer(self, guess):
        """
        Function that is run when the player submits an guess.
        Checks whether the guess is correct and updates the game attributes
        accordingly.

        Args:
        guess (string): A character submitted as a guess.
        """
        found = 0
        guess = guess.lower()
        for i, character in enumerate(self.answer):
            if character == guess:
                self.revealed.add(i)
                found = 1
        if not found:
            self.life = self.life - 1
            return 0
        self.correct_characters.add(guess)
        return 1

    def current_answer(self):
        """Function that returns the current state of the answer

        Returns:
            string: The current word/phrase, with _ in the places of characters
                that hasn't been guessed yet
        """
        output = ""
        start_flag = 1
        for i, character in enumerate(self.answer):
            if start_flag:
                start_flag = 0
            else:
                output += " "
            if i in self.revealed:
                output += character
            else:
                output += "_"
        return output

    def is_game_alive(self):
        """Function that returns the current state of the game

        Returns:
            bool: Returns true if the game still has more than 0 life.
        """
        return self.life > 0
