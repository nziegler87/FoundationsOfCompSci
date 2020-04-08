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

def main():
    unittest.main(verbosity = 3)

main()
