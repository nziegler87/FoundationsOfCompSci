'''
    CS 5001
    Nathanial Ziegler
    March 2020
    HW 7
    Description:
        Screen class file
'''

import turtle

class Screen:
    ''' class: Screen
        Attributes:
            screen_turtle -- turtle for screen setup (add img and background)
            score_turtle -- turtle to display text (ie score)
            cookie_turtle -- turtle to display cookie_image
        Methods:

    '''
    def __init__(self):
        self.screen = turtle.Screen()
        self.score = turtle.Turtle()
        self.cookie = turtle.Turtle()
        self.font = "arial"
        self.size = 14
        self.type = "bold"
        self.bg_color = "light grey"
        self.score_pos = (-50, 125)

    def setup_screen(self, score, cookie_file):
        ''' Method: setup_screen
            Attributes:
                self -- the current object
                score -- score value (int)
                cookie_file -- file name of cookie image (str)
                bg_color -- background color (str)
        '''
        self.screen.setup(400, 800)
        self.screen.addshape(cookie_file)
        self.screen.bgcolor(self.bg_color)
        self.cookie.shape(cookie_file)

        self.score.hideturtle()
        self.score.up()
        self.score.setpos(self.score_pos)

    def display_score(self, score):
        ''' Method: display_score
            Attributes:
                self -- the current object
                score -- score value (int)
        '''
        self.score.clear()
        self.score.write("Your score:\n" + str(score), font = (self.font, self.size,
                                                               self.type))
