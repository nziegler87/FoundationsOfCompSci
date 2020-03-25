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
        Attributes: screen, score, and cookie turtles, font, font size,
                    font type, font alignment, background color,
                    score position, screen x dimension and screen y dimension
        Methods: initialize_graphics -- sets screen, text, and image inital
                                        settings
                 display_text -- displays score on screen

    '''
    def __init__(self, font = "arial", bg_color = "light grey",
                 ft_size = 16, ft_type = "bold"):
        '''
        Constructor -- creates a new instance of a game screen
        Parameters:
            self -- the current object
            screen_turtle -- turtle for screen setup (add img and background)
            score_turtle -- turtle to display text (ie score)
            cookie_turtle -- turtle to display cookie_image
            font (optional) -- font for displaying text on turtle screen
            size (optional) -- font size for displaying text on turtle screen
            type (optional) -- font type (bold, italic, regular) for
                               displaying text
            align -- font alignment for score
            bg_color (optional) -- color of background screen
            score_pos -- position of score on screen
            screen_x -- x dimension of screen
            screen_y -- y dimension of screen
        '''
        self.screen = turtle.Screen()
        self.score = turtle.Turtle()
        self.cookie = turtle.Turtle()

        # font settings
        self.font = font
        self.size = ft_size
        self.type = ft_type
        self.align = "center"
        self.bg_color = bg_color
        self.score_pos = (0, 125)

        # screen size settings
        self.screen_x = 400
        self.screen_y = 600

    def initialize_graphics(self, score, cookie_file):
        ''' Method: initializes screen, cookie graphic, and score text
            Attributes:
                self -- the current object
                score -- score value (int)
                cookie_file -- file name of cookie image (str)
            Returns: nothing
        '''
        # set up screen size and color
        self.screen.setup(self.screen_x, self.screen_y)
        self.screen.bgcolor(self.bg_color)

        # add cookie image
        self.screen.addshape(cookie_file)
        self.cookie.shape(cookie_file)

        # set up score turtle
        self.score.hideturtle()
        self.score.up()
        self.score.setpos(self.score_pos)

    def display_text(self, score):
        ''' Method: displays current text
            Attributes:
                self -- the current object
                score -- score value (int)
            Returns: nothing
        '''
        self.score.clear()
        self.score.write("Your score: " + str(score), align = self.align,
                         font = (self.font, self.size, self.type))
