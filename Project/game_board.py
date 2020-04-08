'''
    CS 5001
    Nathanial Ziegler
    April 2020
    Final Project
    Description:
        Class used to create and modify Connect 4 gameboard
'''

from game_piece import Game_Piece
import copy

# constants for game setup
DIMENSIONS = ["rows", "columns"]
ROWS = "rows"
COLS = "cols"

# board dimension limits
MIN_DIMENSION = 4
MAX_DIMENSION = 10

# default board dimensions
DEFAULT_ROWS = 6
DEFAULT_COLS = 7

# default starting x, y coordinates
X_START = -350
Y_START = 250

# size for spacing game pieces apart
PIECE_SIZE = 70

class Game_Board:
    ''' class: Game_Board
        Attributes: rows, cols, total_pieces, board, arrows
        Methods: get_dimensions, setup_board, __str__
    '''
    def __init__(self):
        '''
        Constructor -- creates an instance of the game board
        Attributes:
            self -- the current object
            rows -- (int) default to constant; can be updated by user
            cols -- (int) default to constant; can be updated by user
            total_pieces -- the number of total pieces on board (int)
            board -- an empty list, to  be filled with a nested list
                     of game piece objects
            arrows -- an empty list, to be filled with list of arrow objects
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
            Does: asks user for their desired board dimensions while
                  enforcing a min ans max
        '''
        dimensions = []
        
        for dimension in DIMENSIONS:
            value = input("Number of {} (min {} / max {}): ".format(dimension,
                                                                MIN_DIMENSION,
                                                                MAX_DIMENSION))

            while (not value.isdigit() or
                   int(value) < MIN_DIMENSION or int(value) > MAX_DIMENSION):
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
        Does: creates nested list of game pieces based on # rows and cols as well
              as list of arrow objects
        '''
        # make nested list of game piece objects and save to self.board
        # use X_START, Y_START, and PIECE_SIZE to assign x, y coordinates
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
            # use deep copy to make copy of each top row game piece to be arrows
            piece = copy.deepcopy(self.board[0][j])
            piece.y += PIECE_SIZE
            self.arrows.append(piece)

    def __str__(self):
        ''' Method: __str__
            Parameters:
                self -- the current object
            Returns: nothing
        '''
        board = ""
        
        # first row = arrow object details
        for i in range(len(self.arrows)):
            arrow = self.arrows[i]
            board += "(" + str(arrow.identifier) + ", " + str(arrow.x) + \
                     ", " + str(arrow.y) + ")"
        board += "\n\n"

        # rest of rows = game piece object details
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                piece = self.board[i][j]
                board += "(" + str(piece.identifier) + ", " + \
                         str(piece.x) + ", " + str(piece.y) + \
                         ", " + str(piece.filled) + ")"
            board += "\n"
            
        return board
