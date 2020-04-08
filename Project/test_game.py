import unittest
from unittest.mock import patch
from game import *


def setup_two_players():
    ''' Name: setup_two_players
        Parameters: nothing
        Returns: game object with two players
        Does: sets up game with two players, one of which is computer,
              so player 1 goes first
    '''
    game = Game()
    user = Player("user")
    user.name = "nate"
    user.color = "red"
    game.players.append(user)

    computer = Player("computer")
    computer.name = "Computer"
    computer.color = "yellow"
    game.players.append(computer)
    
    game.play_computer = True
    game.pick_starting_player()

    return game

def setup_custom_board(row, col):
    ''' Name: setup_custom_board
        Parameters: nothing
        Returns: game board object with 4x4 pieces
        Does: sets up board using constants in game_board file
    '''
    # update number of rows and columns
    board = Game_Board()
    board.rows = row
    board.cols = col
    board.total_pieces = board.rows * board.cols
    board.setup_board()
    print(board)
    return board

def fill_row(board, row, string):
    ''' Name: fill_row
        Parameters: Game_Board instance, row (int), and a string
        Returns: nothing
        Does: fills specified row with a string
    '''
    for i in range(len(board.board[row])):
        board.board[row][i].filled = string
    print(board)

def fill_col(board, col, string):
    ''' Name: fill_col
        Parameters: Game_Board instance, col (int), and a string
        Returns: nothing
        Does: fills specified col with a string
    '''
    for i in range(len(board.board)):
        board.board[col][i].filled = string
    print(board)

class Game_Test(unittest.TestCase):

    def test_init(self):
        game = Game()
        self.assertEqual(game.play_computer, "")
        self.assertEqual(game.default_board, "")
        self.assertEqual(game.game_over, False)
        self.assertIsInstance(game.board, object)
        self.assertEqual(game.current_move, "")
        self.assertEqual(game.current_img, "")
        self.assertEqual(game.players, [])
    
    def test_pick_starting_player(self):
        game = setup_two_players()
        self.assertEqual(game.current_move, 0)

    def test_switch_player(self):
        game = setup_two_players()

        # confirm that method switches current player from 0 > 1 and then 1 > 0
        game.switch_player()
        self.assertEqual(game.current_move, 1)

        game.switch_player()
        self.assertEqual(game.current_move, 0)

    def test_collect_rows(self):
        # create custom board and fill a row with "red"
        board = setup_custom_board(5, 4)
        fill_row(board, 3, "red")

        # create game object and update board with custom
        game = Game()
        game.board = board
        
        expected = [["", "", "", ""],
                    ["", "", "", ""],
                    ["", "", "", ""],
                    ["red", "red", "red", "red"],
                    ["", "", "", ""]]

        # first check that horizontal collection works
        self.assertEqual(game.collect_horizontals(),expected)

        # second check that check_win works
        game.check_win()
        self.assertEqual(game.game_over, True)

        

def main():
    unittest.main(verbosity = 3)

main()
