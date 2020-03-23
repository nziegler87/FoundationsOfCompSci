'''
    CS 5001
    Nathanial Ziegler
    March 2020
    HW 7
    Description:
        NEED TO UPDATE
'''

COOKIE = "cc_cookie.gif"
BG_COLOR = "light grey"
ACHIEVEMENT_FILE = "achievements.txt"
SCORE_FILE = "scores.txt"
MESSAGES = {1: "Congrats, you made on cookie. Do you want a trophy?",
            13: "You made a baker's dozen. Still, don't quit your day job!",
            24: "Two dozen cookies - nice! However, it took you long enough...",
            49: "Almost 50 cookies! I underestimated you!",
            100: "You are really rocking this!",
            115: "Wow, keep up the good work!",
            314: "3.14 cookies for Pi Day",}

import turtle
from game import *
import time


def main():
    # create game and cookie objects
    game = Game(SCORE_FILE, ACHIEVEMENT_FILE)
    game.cookie.initialize_score(game.scorefile)
    game.cookie.initialize_achievements(game.achievefile)

    # set up screen for gameplay
    screen_turtle = turtle.Screen()
    cookie_turtle = turtle.Turtle()
    score_turtle = turtle.Turtle()
    setup_screen(cookie_turtle, screen_turtle, score_turtle, game.cookie.score,
                 COOKIE, BG_COLOR)

##    cookie_turtle.onclick(game.click_play())

    # simulated gameplay
    time.sleep(1)
    n = 0
    while n < 20:
        game.cookie.add_point()
        game.add_achievement(game.cookie.achievements)
        display_score(score_turtle, game.cookie.score)
        game.display_message(MESSAGES)
        time.sleep(.5)
        n += 1
    game.save_score(game.cookie.score)
        
    
main()
