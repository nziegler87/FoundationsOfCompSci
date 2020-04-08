'''
    CS 5001
    Nathanial Ziegler
    April 2020
    Final Project
    Description:
        Test case for game class
'''

import unittest
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
    return board

def fill_row(board, row, string):
    ''' Name: fill_row
        Parameters: Game_Board instance, row (int), and a string
        Returns: nothing
        Does: fills specified row with a string
    '''
    for i in range(len(board.board[row])):
        board.board[row][i].filled = string

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
        # set up a game with a human and computer player then make sure
        # current move is player at position 0 in list
        game = setup_two_players()
        self.assertEqual(game.current_move, 0)

    def test_switch_player(self):
        # set up game with a human and computer player
        game = setup_two_players()

        # confirm that method switches current player from 0 > 1 and then 1 > 0
        game.switch_player()
        self.assertEqual(game.current_move, 1)

        game.switch_player()
        self.assertEqual(game.current_move, 0)

    def test_set_player_img(self):
        # set up two-player game as described in setup_two_players function
        game = setup_two_players()
        RED = "red"
        RED_IMG = "./images/red_piece_60.gif"
        YELLOW_IMG = "./images/yellow_piece_60.gif"

        # test to make sure that no image is loaded in current_img attribute
        # before method is run
        self.assertEqual(game.current_img, "")

        # with this sample setup, player 1 (current player), should have their
        # image loaded into the .current_img attribute        
        game.set_player_img()
        self.assertEqual(game.current_img, RED_IMG)

        # switching players and rerunning set_player method should change
        # image to yellow
        game.switch_player()
        game.set_player_img()
        self.assertEqual(game.current_img, YELLOW_IMG)

    def test_get_column(self):
        # set up a test game and board
        game = setup_two_players()
        board = setup_custom_board(5, 4)
        game.board = board

        # tests where x and y click is on an arrow
        self.assertEqual(game.get_column(-350, 320), 0)
        self.assertEqual(game.get_column(-210, 320), 2)

        # tests where x is on an arrow but y is out of range
        self.assertEqual(game.get_column(-250, 0), None)
        self.assertEqual(game.get_column(-210, 0), None)

        # tests where y is on arrow but x is out of range
        self.assertEqual(game.get_column(-400, 320), None)
        self.assertEqual(game.get_column(400, 320), None)

    def test_drop_piece(self):
        # set up a test game and board
        game = setup_two_players()
        board = setup_custom_board(5, 4)
        game.board = board

        # drop piece three times in same column and once in another
        # make sure return coordinates are correct
        self.assertEqual(game.drop_piece(1, "red"),(-280, -30))
        self.assertEqual(game.drop_piece(1, "yellow"), (-280, 40))
        self.assertEqual(game.drop_piece(1, "red"), (-280, 110))
        self.assertEqual(game.drop_piece(2, "yellow"), (-210, -30))
                         
    def test_check_full(self):
        # set up a test game and board
        game = setup_two_players()
        board = setup_custom_board(5, 4)
        game.board = board

        # fill all pieces with same color
        for i in range(len(game.board.board)):
            for j in range(len(game.board.board[i])):
                game.board.board[i][j].filled = "yes"

        # remove one piece so game is not full
        game.board.board[0][0].filled = ""
        game.check_full()
        self.assertEqual(game.game_over, False)

        # fill piece back in and rerun check_full method
        game.board.board[0][0].filled = "yes"
        game.check_full()
        self.assertEqual(game.game_over, True)

    def test_collect_functions(self):
        # create custom board and fill a row with "red"
        board = setup_custom_board(5, 4)
        fill_row(board, 3, "red")

        # create game object and update board with custom
        game = setup_two_players()
        game.board = board

        # first check that horizontal collection works
        horizontal = [["", "", "", ""],
                      ["", "", "", ""],
                      ["", "", "", ""],
                      ["red", "red", "red", "red"],
                      ["", "", "", ""]]
        self.assertEqual(game.collect_horizontals(), horizontal)

        # check that vertical collection works
        vertical = [["", "", "", "red", ""],
                    ["", "", "", "red", ""],
                    ["", "", "", "red", ""],
                    ["", "", "", "red", ""]]
        self.assertEqual(game.collect_verticals(), vertical)


        # check that antidiagonal collection works
        antidiagonal = [[""],
                        ["", ""],
                        ["", "", ""],
                        ["red", "", "", ""],
                        ["", "red", "", ""],
                        ["", "red", ""],
                        ["", "red"],
                        [""]]

        self.assertEqual(game.collect_antidiagonals(), antidiagonal)

        # check that diagonal collection works
        diagonal = [[""],
                    ["red", ""],
                    ["", "red", ""],
                    ["", "", "red", ""],
                    ["", "", "", "red"],
                    ["", "", ""],
                    ["", ""],
                    [""]]

        self.assertEqual(game.collect_diagonals(), diagonal)

        # check that collect_all_directions works
        all_directions = [[["", "", "", ""],
                            ["", "", "", ""],
                            ["", "", "", ""],
                            ["red", "red", "red", "red"],
                            ["", "", "", ""]],
                          [["", "", "", "red", ""],
                           ["", "", "", "red", ""],
                           ["", "", "", "red", ""],
                           ["", "", "", "red", ""]],
                          [[""],
                           ["red", ""],
                           ["", "red", ""],
                           ["", "", "red", ""],
                           ["", "", "", "red"],
                           ["", "", ""],
                           ["", ""],
                           [""]],
                          [[""],
                           ["", ""],
                           ["", "", ""],
                           ["red", "", "", ""],
                           ["", "red", "", ""],
                           ["", "red", ""],
                           ["", "red"],
                           [""]]]
                         
        self.assertEqual(game.collect_all_directions(), all_directions)
        
def main():
    unittest.main(verbosity = 3)

main()
