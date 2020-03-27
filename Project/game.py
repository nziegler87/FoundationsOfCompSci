class Game:
    def __init__(self):
        self.pieces = {}

    def add_piece(self, ident, image, x, y):
        self.pieces[ident] = [image, x, y]

    def return_dict(self):
        return self.pieces
