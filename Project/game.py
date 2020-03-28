from game_piece import Game_Piece
from stack import Stack

def check_winner(lst):
    tuples = create_streak(lst)
    print(tuples)
    check_four(tuples)
    
def check_four(lst_of_tuples):
    for i in range(len(lst_of_tuples)):
        if lst_of_tuples[i][0] >= 4 and lst_of_tuples[i][1] != "":
                winner = lst_of_tuples[i][1]
                print("The winner is", winner)

def create_streak(lst):
    stack = Stack()
    streak = []
    count = 1

    for i in range(len(lst) - 1, -1, -1):
        stack.push(lst[i])

    # get first item and remove it from stack
    while not stack.is_empty():
        item = stack.top()
        stack.pop()

        if stack.top() == item:
            count += 1
        else:
            streak.append((count,item))
            count = 1

    return streak

class Game:
    def __init__(self):
        self.pieces = {}
        self.board = []
        self.rows = 2 ## NEED TO WORK ON...should be when initialized
        self.columns = 2 ## NEED TO WORK ON
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
            print(True)
        else:
            print(False)

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
