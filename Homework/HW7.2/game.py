'''
    CS 5001
    Nathanial Ziegler
    March 2020
    HW 7
    Description:
        Game Class file
'''

MESSAGES = {1: "Congrats, you made one cookie. Do you want a trophy?",
            13: "13 Points! A Baker's dozen. Keep up the work...but" + \
            " don't quit your day job.",
            24: "Two dozen points - nice! However, it took you long enough...",
            49: "Almost 50 points! I underestimated you!",
            100: "You are really rocking this!",
            115: "Wow, keep up the good work!", 150: "Look at you go!",
            314: "3.14 points for Pi Day",}

import turtle
from cookie import Cookie
from screen import Screen

class Game:
    ''' class: Game
        Attributes: cookie and screen objects, score and achievement files,
                    message dictionary
        Methods:
            constructor -- creates a new instances of gameplay
            
    '''
    def __init__(self, scorefile, achievefile):
        '''
        Constructor -- creates a new cookie object and initializes attributes
                       scorefile and achievefile to the given strings
        Parameters:
            self -- the current object
            cookie -- a Cookie object
            display -- a Screen object
            scorefile -- filename where score is stored (a string)
            achievefile -- filename where achievements are stored (a string)
            messages -- messages dict formatted as {score(int):message(str)}
        '''
        self.cookie = Cookie()
        self.display = Screen()
        self.scorefile = scorefile
        self.achievefile = achievefile
        self.messages = MESSAGES

    def click_play(self, x, y):
        '''
        Method - calls necessary methods to process gameplay
        Parameters:
            self -- the current object
            x -- x_cord
            y -- y_cord
        Returns: nothing
        '''
        self.cookie.add_point()
        self.add_achievement(self.cookie.achievements)
        self.display.display_text(self.cookie.score)
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
        Returns: nothing
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
