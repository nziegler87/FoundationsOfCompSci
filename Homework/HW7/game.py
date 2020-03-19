'''
    CS 5001
    Nathanial Ziegler
    March 2020
    HW 7
    Description:
        Game Class file
'''

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
        '''
        self.scorefile = scorefile
        self.achievefile = achievefile
            
        
