from game_piece import Game_Piece
from game import check_winner, check_four, create_streak



class Game_Board:
    def __init__(self):
        self.pieces = {}
        self.board = []

        self.total_pieces = self.rows * self.columns

    def add_piece(self, ident, image, x, y):
        self.pieces[ident] = [image, x, y]

    def return_dict(self):
        return self.pieces

    def drop_piece(self, column, color, turn):
        for i in range(len(self.board) - 1, -1, -1):
            if not self.board[i][column].filled:
                self.board[i][column].fill_piece(color, turn)
                return self.board[i][column]

    def check_full(self):
        total_filled = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].filled != "":
                    total_filled += 1
        if self.total_pieces == total_filled:
            print("Board is Full")      # SHOULD RETURN BOOL

    def check_horizontal_streak(self):
        for i in range(len(self.board)):
            row_streak = []
            for j in range(len(self.board[i])):
                row_streak.append(self.board[i][j].filled)
            check_winner(row_streak)

    def check_vertical_streak(self):
        for i in range(len(self.board)):
            col_streak = []
            for j in range(len(self.board[i])):
                col_streak.append(self.board[j][i].filled)
            check_winner(col_streak)
