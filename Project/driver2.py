from game import *  # SHOULD I SPECIFY WHICH FUNCTIONS LATER?
from graphics import *

# FILE CONSTANTS
SCOREFILE = "scorefile.txt"     # NEED TO CREATE FUNCTION

def main():
    game = Game()
    game.initialize_game()
    game.play_game()
    

main()
