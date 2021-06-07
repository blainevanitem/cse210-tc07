''' Pulls 5 random words from the word bank in input_service.'''

class Word:
    def __init__(self):
        self._word = ""

    def build_word(self,letter):
        letter = letter
        self._word = self._word + letter