
class Game_Piece:
    '''
    '''
    def __init__(self, identifier, x_cord, y_cord,
                 image, size = 100, color = "blue",):
        '''
        '''
        self.identifier = identifier
        self.x = x_cord
        self.y = y_cord
        self.image = image
        self.size = size
        self.color = color

    def set_cords(self, x_cord, y_cord):
        self.x = x_cord
        self.y = y_cord
