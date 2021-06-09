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

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            #self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    
    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """
        letter = self._input_service.get_letter()
        self.buffer = self._word.build_word(letter)
        

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        pass
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.update_buffer(self.buffer)
        self._output_service.flush_buffer()