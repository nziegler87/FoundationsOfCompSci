'''
    CS 5001
    Nathanial Ziegler
    March 2020
    HW 7
    Description:
        Cookie Class file
'''

class Cookie:
    ''' class: Cookie
        Attributes: score (int), achievements (dictionary)
        Methods:
            add_point -- increments value in score attribute
            initialize_score -- reads saved score or sets to 0
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

    def initialize_score(self, name):
        return 0
            
