
class Game_Piece:
    '''
    '''
    def __init__(self, identifier, x_cord, y_cord,
                 image, size, color,):
        '''
        '''
        self.identifier = identifier
        self.filled = ""
        self.x = x_cord
        self.y = y_cord
        self.image = image
        self.size = size
        self.color = color          # SHOULD PROBABLY COMBINE COLOR & FILLED

    def set_cords(self, x_cord, y_cord):
        self.x = x_cord
        self.y = y_cord

    def fill_piece(self, color, turn):
        self.filled = turn
        self.color = color         # IF COMBINE COLOR & FILLED, ALL SETT

    def __str__(self):
        print_str = str(self.identifier) + " " + str(self.filled)
        return print_str
