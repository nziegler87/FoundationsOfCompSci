'''
    CS 5001
    Nathanial Ziegler
    April 2020
    Final Project
    Description:
        Class to create and modify game pieces for Connect 4
'''

class Game_Piece:
    ''' class: Game_Piece
        Attributes: identifier, filled, x, y
        Methods: fill_piece
    '''
    def __init__(self, identifier, x, y):
        '''
        Constructor -- creates a game piece instance
        Attributes:
            identifier -- default blank, to be filled with unique identifier,
                          an int in this game
            filled -- default of blank, else with color of fill as string
            x -- center x coordinate of game piece (a float)
            y -- center y coordinate of game piece (a float)
        '''
        self.identifier = identifier
        self.filled = ""
        self.x = x
        self.y = y

    def fill_piece(self, color):
        ''' Method: fill_piece
            Parameters:
                self -- the current object
                color -- a string, representing the object's color
            Returns: nothing
            Does: updates filled attribute with string
        '''
        self.filled = color

