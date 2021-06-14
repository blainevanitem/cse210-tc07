'''Will display the screen and the words across the screen'''
import sys
from game import constants
from game.actor import Actor
from asciimatics.widgets import Frame
import random

class OutputService(Actor):
    def __init__(self, screen):
        """The class constructor.
        
        Args:
            self (OutputService): An instance of OutputService.
            screen (Screen): An Asciimatics Screen.
        """
        super().__init__()
        self._screen = screen


    def clear_screen(self):
        """Clears the Asciimatics buffer in preparation for the next rendering.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        self._screen.clear_buffer(7, 0, 0)
        self._screen.print_at("-" * constants.MAX_X, 0, 0, 7)
        self._screen.print_at("-" * constants.MAX_X, 0, constants.MAX_Y, 7)

    # This updates the buffer and helps to clear it and allow for the player to enter words.

    def update_buffer(self,buffer):
        self._screen.print_at("-Buffer: " + buffer,0,constants.MAX_Y)

    # This keeps track of the score of the player after entering words in the buffer.

    def update_score(self,score):
        self._screen.print_at("-Score: " + str(score),0,0)
    
    def flush_buffer(self):
        """Renders the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        self._screen.refresh() 

    # This defines the word and displays the word and the starting position of said word when it appears on the screen.

    def display_words(self,words):
        self._screen.print_at(words[0],self.position1,self.position1y)
        self._screen.print_at(words[1],self.position2,self.position2y)
        self._screen.print_at(words[2],self.position3,self.position3y)
        self._screen.print_at(words[3],self.position4,self.position4y)
        self._screen.print_at(words[4],self.position5,self.position5y)
        self.move_letters()
        