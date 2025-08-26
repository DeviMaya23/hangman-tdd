class Game:
    def __init__(self, word):
        self.word = word
        self.life = 5

    def check_answer(self, answer):
        result = answer in self.word
        if not result:
            self.life = self.life - 1
        return result
