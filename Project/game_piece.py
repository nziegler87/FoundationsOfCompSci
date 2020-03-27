WHITE = "./images/white_piece_90.gif"

class Game_Piece:
    '''
    '''
    def __init__(self, x_cord, y_cord, image = WHITE, size = 100, color = "blue",):
        '''
        '''
        self.x = x_cord
        self.y = y_cord
        self.image = image
        self.size = size
        self.color = color

    def set_cords(self, x_cord, y_cord):
        self.x = x_cord
        self.y = y_cord
