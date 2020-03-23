'''
    CS 5001
    Nathanial Ziegler
    March 2020
    HW 7
    Description:
        NEED TO UPDATE
'''

COOKIE = "cc_cookie.gif"

ACHIEVEMENT_FILE = "achievements.txt"
SCORE_FILE = "scores.txt"

import turtle
from game import *
from screen import *
import time


def main():
    # create game and cookie objects
    game = Game(SCORE_FILE, ACHIEVEMENT_FILE)
    game.cookie.initialize_score(game.scorefile)
    game.cookie.initialize_achievements(game.achievefile)

    # set up screen for gameplay
    game.display = Screen()
    game.display.setup_screen(game.cookie.score, COOKIE)
    game.display.display_score(game.cookie.score)

    # gameplay
    game.display.cookie.onclick(game.click_play)
    game.display.screen.onclick(game.exit)
      
    
main()
