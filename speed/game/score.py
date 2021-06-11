

class Score:
    def __init__(self):
        self.score = 0

    def get_score(self,word,words):
        for x in range(5):
            if word == words[x].rstrip('\n'):
                self.score += 5
                return True