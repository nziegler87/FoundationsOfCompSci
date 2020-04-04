class Game_Piece:
    '''
    '''
    def __init__(self, identifier, x, y):
        '''
        Constructor -- creates a game piece instance
        Attributes:
            filled -- default of blank, else with color of fill as string
            x -- center x coordinate of game piece (a float)
            y -- center y coordinate of game piece (a float)
        '''
        self.identifier = identifier
        self.filled = ""
        self.x = x
        self.y = y

    def fill_piece(self, color):
        self.filled = color

# this is a debug method, which can be deleted later
    def __str__(self):
        print_str = str(self.identifier) + " " + str(self.filled)
        return print_str

