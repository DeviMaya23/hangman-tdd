class Game:
    def __init__(self, word):
        self.word = word.lower()
        self.life = 5
        self.revealed = []
        self.correct_characters = []

    def check_answer(self, answer):
        found = 0
        answer = answer.lower()
        for i, character in enumerate(self.word):
            if character == answer:
                self.revealed.append(i)
                found = 1
        if not found:
            self.life = self.life - 1
            return 0
        self.correct_characters.append(answer)
        return 1
