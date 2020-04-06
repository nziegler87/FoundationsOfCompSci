from game_piece import Game_Piece
import copy

# constants for game setup
ROWS = "rows"
COLS = "cols"
DIMENSIONS = ["rows", "columns"]
MIN_DIMENSION = 4
DEFAULT_ROWS = 6
DEFAULT_COLS = 7
X_START = -225
Y_START = 150
PIECE_SIZE = 70
ARROW_OFFSET = 70

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

    def get_dimensions(self):
        ''' Name: get_dimensions
            Parameters:
                self -- the current object
            Returns: nothing
        '''
        dimensions = []
        for dimension in DIMENSIONS:
            value = input("Number of " + dimension + " (min " + str(MIN_DIMENSION) + "): ")
            while not value.isdigit() or int(value) < MIN_DIMENSION:
                value = input("That was not a valid input. Try again: ")
            dimensions.append(int(value))
        self.rows, self.cols = dimensions
        self.total_pieces = self.rows * self.cols

    def setup_board(self):
        '''
        Method: collect settings needed to set up board
        Parameters:
            self -- the current object
        Returns: nothing
        Does: creates nested list of game pieces based on # rows and cols as well as
              list of arrow objects
        '''
        # make nested list of game piece objects and save to self.board
        y = Y_START
        for i in range(self.rows):
            x = X_START
            temp_row = []
            for column, j in enumerate(range(self.cols)):
                piece = Game_Piece(column, x, y)
                temp_row.append(piece)
                x += PIECE_SIZE
            self.board.append(temp_row)
            y -= PIECE_SIZE

        # make list of arrow piece objects and safe to self.arrows
        for j in range(len(self.board[0])):
            # using deep copy to make a copy of each top row game pice to be arrows
            piece = copy.deepcopy(self.board[0][j])
            piece.y += ARROW_OFFSET
            self.arrows.append(piece)


    def __str__(self):
        board = ""
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                piece = self.board[i][j]
                board += "(" + str(piece.x) + ", " + str(piece.y) + \
                         ", " + str(piece.filled) + ")"
            board += "\n"
        return board
