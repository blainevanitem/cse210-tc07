'''The main driver of the program that will manage sequence of play'''
from time import sleep
from game import constants
from game.point import Point
from game.score import Score
from game.word import Word

class Director:
    def __init__(self,input_service,output_service):    
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._word = Word()
        self._score = Score()
        self._point = Point()
        self._first_display = True
        self._update_index = 0

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._word.get_words()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    
    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """
        self.letter = self._input_service.get_letter()
        self.buffer = self._word.build_word(self.letter)
        
        

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        if self._score.get_score(self._word._word,self._word._words) == True:
            
            self._update_index = self._word.is_word_on_screen(self._word._word,self._word._words,self._update_index)
            self._word.clear_word()
            self._word.update_with_new_word(self._update_index)
            
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """

        self._output_service.clear_screen()
        self._output_service.display_words(self._word._words)
        self._output_service.update_buffer(self.buffer)
        self._output_service.update_score(self._score.score)
        self._output_service.flush_buffer()