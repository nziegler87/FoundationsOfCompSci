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
from screen import Screen

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
        self.display = Screen()
        self.scorefile = scorefile
        self.achievefile = achievefile
        self.messages = {1: "Congrats, you made one cookie. " + \
                         "Do you want a trophy?",
                         13: "You made a baker's dozen. " + \
                         "Still, don't quit your day job!",
                         24: "Two dozen cookies - nice! " + \
                         "However, it took you long enough...",
                         49: "Almost 50 cookies! I underestimated you!",
                         100: "You are really rocking this!",
                         115: "Wow, keep up the good work!",
                         150: "Look at you go!",
                         314: "3.14 cookies for Pi Day",}

    def click_play(self, x, y):
        '''
        Method - NOT SURE HOW TO DESCRIBE
        Parameters:
            self -- the current object
            x -- x_cord
            y -- y_cord
        '''
        self.cookie.add_point()
        self.add_achievement(self.cookie.achievements)
        self.display.display_score(self.cookie.score)
        self.display_message(self.cookie.score)

    def exit(self, x, y):
        if x < -100:
            self.save_score(self.cookie.score)
            self.display.screen.bye()

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

    def display_message(self, current_score):
        '''
        Method: displays a message in the terminal based on current score
        Parameters:
            self -- the current object
            score -- score value (int)
            message_dict -- dictionary with score keys and message values
        '''
        if current_score in self.messages.keys():
            print(self.messages[current_score])

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
        

    
        

 
        

