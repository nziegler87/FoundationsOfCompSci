from game import *  # SHOULD I SPECIFY WHICH FUNCTIONS LATER?
from graphics import *

# FILE CONSTANTS
SCOREFILE = "scorefile.txt"     # NEED TO CREATE FUNCTION

def main():
    game = Game()
    board = Game_Board()
    game.collect_settings()
    board.setup_board()
    graphics = Graphics(board.board)
    graphics.draw_blank_board()
    

main()
