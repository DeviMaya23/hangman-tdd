"""Module for dictionary used by hangman game."""
import random

word_list = [
    "apple", "banana", "grapes", "cherry", "mango",
    "peach", "lemon", "orange", "melon", "papaya",
    "tiger", "eagle", "shark", "rabbit", "falcon",
    "lion", "zebra", "otter", "koala", "penguin",
    "guitar", "pencil", "bucket", "ladder", "hammer",
    "window", "mirror", "button", "socket", "wallet",
    "planet", "galaxy", "comet", "asteroid", "meteor",
    "sunrise", "horizon", "volcano", "ocean", "desert",
    "castle", "statue", "forest", "temple", "island",
    "bridge", "tunnel", "station", "market", "museum",
]


phrase_list = [
    "break the ice",
    "once in a lifetime",
    "easy come easy go",
    "a piece of cake",
    "miss the boat",
    "under the weather",
    "hit the sack",
    "a dime a dozen",
    "spill the beans",
    "bite the bullet",
    "costs an arm and a leg",
    "go the extra mile",
    "jump the gun",
    "cut to the chase",
    "kill two birds with one stone",
    "burn the midnight oil",
    "caught red handed",
    "cry over spilled milk",
    "raining cats and dogs",
    "back to square one",
    "the ball is in your court",
    "every cloud has a silver lining",
    "let the cat out of the bag",
    "call it a day",
    "no pain no gain",
    "not a big deal",
    "practice makes perfect",
    "time flies",
    "read between the lines",
    "hit the nail on the head",
    "throw in the towel",
    "face the music",
    "beat around the bush",
    "burn bridges",
    "on thin ice",
    "speak of the devil",
    "take it with a grain of salt",
    "jump on the bandwagon",
    "break a leg",
    "roll with the punches",
    "kick the bucket",
    "hit the books",
    "take the high road",
    "bend over backwards",
    "come rain or shine",
    "by the book",
    "pulling your leg",
    "mind over matter",
    "food for thought",
    "over the moon",
]


class Dictionary:
    """Class that contains the dictionary used for hangman game"""
    def __init__(self):
        """Intial function to create dictionary class"""
        self.word_list = word_list
        self.phrase_list = phrase_list

    def get_word(self):
        """A function that retrieves a single word from the dictionary"""
        return random.choice(self.word_list)

    def get_phrase(self):
        """A function that retrieves a single phrase from the dictionary"""
        return random.choice(self.phrase_list)
