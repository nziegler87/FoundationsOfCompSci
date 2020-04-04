from game_piece import Game_Piece
import copy

# constants for game setup
ROWS = "rows"
COLS = "cols"
MIN_DIMENSION = 4
DEFAULT_ROWS = 6
DEFAULT_COLS = 7
X_START = -250
Y_START = 250
PIECE_SIZE = 100
ARROW_OFFSET = 100

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
            arrows -- an empty list, to eventually be filled with a list of arrow objects
        '''
        self.rows = DEFAULT_ROWS
        self.cols = DEFAULT_COLS
        self.total_pieces = self.rows * self.cols
        self.board = []
        self.arrows = []

    def setup_board(self):
        '''
        Method: collect settings needed to set up board
        Parameters:
            self -- the current object
        Returns: nothing
        Does: creates nested list of game pieces based on # rows and cols as well as
              list of arrow objects
        '''
        # collect game board information
        print("Specify game board dimensions.")
        self.rows = get_dimensions(ROWS)
        self.cols = get_dimensions(COLS)
        self.total_pieces = self.rows * self.cols

        # make nested list of game piece objects and save to self.board
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

        # make list of arrow piece objects and safe to self.arrows
        col = 1
        for j in range(len(self.board[0])):
            # using deep copy to make a copy of each top row game pice to be arrows
            piece = copy.deepcopy(self.board[0][j])
            piece.y += ARROW_OFFSET
            piece.identifier = col
            self.arrows.append(piece)
            col += 1

    def __str__(self):
        board = ""
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                piece = self.board[i][j]
                board += "(" + str(piece.x) + ", " + str(piece.y) + \
                         ", " + str(piece.filled) + ")"
            board += "\n"
        return board
