class Game:
    def __init__(self, word):
        self.word = word
        self.life = 5
        self.revealed = []

    def check_answer(self, answer):
        found = 0
        for i, character in enumerate(self.word):
            if character == answer:
                self.revealed.append(i)
                found = 1
        if not found:
            self.life = self.life - 1
            return 0
        return 1
