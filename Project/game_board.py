from game_piece import Game_Piece

# constants for game setup
ROWS = "rows"
COLS = "cols"
MIN_DIMENSION = 4
X_START = -250
Y_START = 250
PIECE_SIZE = 100

def get_dimensions(string):
    ''' Name: get_dimensions
        Parameters: a string
        Returns: an int
    '''
    value = input("Number of " + string + " (min " + str(MIN_DIMENSION) + "): ")
    while not value.isdigit() or int(value) < MIN_DIMENSION:
        value = input("That was not a valid input. Try again: ")
    return int(value)

class Game_Board:
    def __init__(self):
        '''
        Constructor -- creates an instance of the game board
        Attributes:
            self -- the current object
            rows -- 4, to be replaced with an int specified by user
            cols -- 4, to be replaced with an int specified by user
            total_pieces -- the number of total pieces on board
            board -- an empty list, to eventually be filled with a nested list
                     of game piece objects
        '''
        self.rows = MIN_DIMENSION
        self.cols = MIN_DIMENSION
        self.total_pieces = self.rows * self.cols
        self.board = []
        self.arrows = []

    def setup_board(self):
        '''
        Method: collect settings needed to set up board
        Parameters:
            self -- the current object
        '''
        print("Specify game board dimensions.")
        self.rows = get_dimensions(ROWS)
        self.cols = get_dimensions(COLS)
        self.total_pieces = self.rows * self.cols
        y = Y_START
        for i in range(self.rows):
            x = X_START
            temp_row = []
            column = 1             # THIS IS AN IDENTIFIER THAT CAN BE REMOVED
            for j in range(self.cols):
                piece = Game_Piece(column, x, y)
                temp_row.append(piece)
                x += PIECE_SIZE
                column += 1       # REMOVE AT SOME POINT
            self.board.append(temp_row)
            y -= PIECE_SIZE

        for j in range(len(self.board[0])):
            piece = self.board[0][j]
            self.arrows.append([piece.identifier, piece.x, piece.y])

        print(self.arrows)

    def __str__(self):
        board = ""
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                piece = self.board[i][j]
                board += "(" + str(piece.x) + ", " + str(piece.y) + ")"
            board += "\n"
        return board
