
# This keeps track of the points

class Score:

    # This is the starting point value

    def __init__(self):
        self.score = 0

    # This allows the game to know how many points the person gets when they type it in correctly.

    def get_score(self,word,words):
        for x in range(5):
            if word == words[x].rstrip('\n'):
                self.score += 5
                return True