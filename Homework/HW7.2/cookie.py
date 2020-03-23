'''
    CS 5001
    Nathanial Ziegler
    March 2020
    HW 7
    Description:
        Cookie Class file
'''
import turtle

class Cookie:
    ''' class: Cookie
        Attributes:
            score (int)
            achievements (dictionary)
        Methods:
            add_point -- increments value in score attribute
            initialize_score -- reads saved score or sets to 0
            display_cookie -- displays cookie image on screen
    '''
    def __init__(self):
        '''
        Constructor -- creates a new instance of cookie gameplay
        Parameters:
            self -- the current object
            score -- default to 0
            achievements -- blank dictionary
        '''
        self.score = 0
        self.achievements = {}

    def add_point(self):
        '''
        Method -- increments value of score attribute by one
        Parameters:
            self -- the current object
        Returns: nothing
        '''
        self.score += 1

    def initialize_score(self, filename):
        '''
        Method -- sets score attribute to integer in score file; else 0
        Parameters:
            self -- the current object
            filename -- name of file containing current score (string)
        Returns: nothing
        '''
        try:
            with open(filename, "r") as infile:
                score = infile.read()
        except OSError:
            score = 0

        # if file exists but unreadable
        try:
            self.score = int(score)
        except ValueError:
            self.score = 0

    def initialize_achievements(self, filename):
        '''
        Method -- initializes achievements dictionary with information in
                  achievements file
        Parameters:
            self -- the current object
            filename -- name of file containing achievements (string)
        Returns: nothing
        '''
        try:
            with open(filename, "r") as infile:
                # add milestone and point values as key:value to dictionary
                for line in infile.readlines():
                    line = line.split()
                    self.achievements[int(line[1])] = int(line[2])     
        except OSError:
            pass
