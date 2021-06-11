''' Pulls 5 random words from the word bank in input_service.'''
import random

class Word:
    def __init__(self):
        self._word = ""
        self._words_list = []
        self._words = ['','','','','']

    def get_words(self):
        self.my_file = open("speed\game\words.txt")
        self._words_list = self.my_file.readlines()
        self.my_file.close()
        for x in range(5):
            self._words[x] = self._words_list[random.randint(0,len(self._words_list)-1)]
        print(self._words)

    def build_word(self,letter):
        letter = letter
        if letter == "*":
            self._word = ""
        else:
            self._word += letter
        return self._word

    def clear_word(self):
        self._word = ""
