'''
    CS 5001
    Nathanial Ziegler
    March 2020
    HW 7
    Description:
        Game Class file
'''

import turtle
from cookie import Cookie

FONT = "arial"
SIZE = 14
TYPE = "bold"

SCORE_POS = (-50, 150)

def setup_screen(cookie_turtle, screen_turtle, score_turtle,
                 score, cookie_file, bg_color):
    ''' Name: setup_screen
        Parameters: cookie, screen, and score turtle variables, score (int),
                    filename for cookie image and background color (both strs)
        Returns: nothing
        Does: initializes screen
    '''
    # create turtles
    screen_turtle.addshape(cookie_file)
    screen_turtle.bgcolor(bg_color)
    cookie_turtle.shape(cookie_file)

    # set up score turtle
    score_turtle.hideturtle()
    score_turtle.up()
    score_turtle.setpos(SCORE_POS)
    display_score(score_turtle, score)

def display_score(score_turtle, score):
    ''' Name: display_score
        Parameters: score turtle variable, score to display (int)
        Returns: nothing
    '''
    score_turtle.clear()
    score_turtle.write("Your score:\n" + str(score), font = (FONT, SIZE, TYPE))

class Game:
    ''' class: Game
        Attributes:
            cookie -- a Cookie object
            scorefile -- filename where score is stored (a string)
            achievefile -- filename where achievements are stored (a string)
        Methods:
            constructor -- creates a new instances of gameplay
    '''
    def __init__(self, scorefile, achievefile):
        '''
        Constructor -- creates a new cookie object and initializes attributes
                       scorefile and achievefile to the given strings
        Parameters:
            self -- the current object
            scorefile -- filename where score is stored (a string)
            achievefile -- filename where achievements are stored (a string)
 >>>>>      # UPDATEEE
        '''
        self.cookie = Cookie()
        self.scorefile = scorefile
        self.achievefile = achievefile
        self.x_cord = 0
        self.message_key = 0

    def click_play(self, x, y):
        '''
        Method - NOT SURE HOW TO DESCRIBE
        Parameters:
            self -- the current object
            x -- x_cord
            y -- y_cord
        '''
        self.x_cord = x

    def add_achievement(self, achievement_dict):
        '''
        Method: if score is found in achievement key, add value to score
        Parameters:
            self -- the current object
            achievement_dict -- dictionary of milestones and score values
        '''
        if self.cookie.score in achievement_dict.keys():
            points = achievement_dict[self.cookie.score]
            self.cookie.score += achievement_dict[self.cookie.score]
            print("Achievement unlocked! Add " + \
                  str(points) + " points!")

    def display_message(self, message_dict):
        '''
        Method: displays a message in the terminal based on current score
        Parameters:
            self -- the current object
            message_dict -- dictionary with score keys and message values
        '''
        if self.cookie.score in message_dict.keys():
            print(message_dict[self.cookie.score])
        

    def save_score(self, current_score):
        '''
        Method: writes current score to file
        Parameters:
            self -- the current object
            current_score -- current score (int)
        '''
        try:
            with open(self.scorefile, "w") as infile:
                infile.write(str(current_score))
        except OSError:
            print("I'm sorry. Your score cannot be saved. All progress lost.")
        

    
        

 
        

