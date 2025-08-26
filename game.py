class Game:
    def __init__(self, word):
        self.word = word.lower()
        self.life = 5
        self.revealed = set()
        self.correct_characters = set()

    def check_answer(self, answer):
        found = 0
        answer = answer.lower()
        for i, character in enumerate(self.word):
            if character == answer:
                self.revealed.add(i)
                found = 1
        if not found:
            self.life = self.life - 1
            return 0
        self.correct_characters.add(answer)
        return 1

    def current_word(self):
        output = ""
        start_flag = 1
        for i, character in enumerate(self.word):
            if start_flag:
                start_flag = 0
            else:
                output += " "
            if i in self.revealed:
                output += character
            else:
                output += "_"
        return output
