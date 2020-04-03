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
            size -- size of image dimension (a float)...assumes image is square
        '''
        self.identifier = identifier
        self.filled = ""
        self.x = x
        self.y = y

    def fill_piece(self, color):
        self.filled = color

# probably don't need these and can be deleted
    def __str__(self):
        print_str = str(self.identifier) + " " + str(self.filled)
        return print_str

    def set_cords(self, x_cord, y_cord):
        self.x = x_cord
        self.y = y_cord
