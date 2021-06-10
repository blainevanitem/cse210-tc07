''' Pulls 5 random words from the word bank in input_service.'''
from random import random

class Word:
    def __init__(self):
        self._word = ""
        self._words = []

    def get_words(self):
        self.my_file = open("speed\game\words.txt")
        self._words = self.my_file.readlines()
        self.my_file.close()
        print(self._words)

    def build_word(self,letter):
        letter = letter
        if letter == "*":
            self._word = ""
        else:
            self._word += letter
        return self._word
