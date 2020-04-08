'''
    CS 5001
    Nathanial Ziegler
    April 2020
    Final Project
    Description:
        Driver to run Connect 4 game
'''

from game import *

def main():
    game = Game()

    game.initialize_game()

    game.play_game()
    
main()
