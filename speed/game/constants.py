import os

# Size of the screen and how many words you will have shown on the screen, also brinsg
# in the 3rd party library required for making the game appear.

MAX_X = 60
MAX_Y = 20
FRAME_LENGTH = 1/12
STARTING_WORDS = 5
PATH = os.path.dirname(os.path.abspath(__file__))
LIBRARY = open(PATH + "/words.txt").read().splitlines()
