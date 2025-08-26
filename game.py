class Game:
    def __init__(self, word):
        self.word = word

    def check_answer(self, answer):
        return answer in self.word
