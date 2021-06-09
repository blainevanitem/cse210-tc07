'''Will display the screen and the words across the screen'''
import sys
from game import constants
from asciimatics.widgets import Frame

class OutputService:
    def __init__(self, screen):
        """The class constructor.
        
        Args:
            self (OutputService): An instance of OutputService.
            screen (Screen): An Asciimatics Screen.
        """
        self._screen = screen


    def clear_screen(self):
        """Clears the Asciimatics buffer in preparation for the next rendering.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        self._screen.clear_buffer(7, 0, 0)
        self._screen.print_at("-" * constants.MAX_X, 0, 0, 7)
        self._screen.print_at("-" * constants.MAX_X, 0, constants.MAX_Y, 7)

    def update_buffer(self,buffer):
        self._screen.print_at("-Buffer: " + buffer,0,7)
    
    def flush_buffer(self):
        """Renders the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        self._screen.refresh() 