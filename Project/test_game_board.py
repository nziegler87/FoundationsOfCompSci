import unittest
from game_board import *

class Test_Game_Board(unittest.TestCase):
    def test_init(self):
        # setup board using default constants
        gb = Game_Board()
        self.assertEqual(gb.rows, 6)
        self.assertEqual(gb.cols, 7)
        self.assertEqual(gb.total_pieces, 42)
        self.assertEqual(gb.board, [])
        self.assertEqual(gb.arrows, [])

    def test_setup_board(self):
        # setup board using default constants
        gb = Game_Board()
        gb.setup_board()

        # check to make sure length is correct
        self.assertEqual(len(gb.board), 6)
        self.assertEqual(len(gb.board[0]) ,7)
        self.assertEqual(len(gb.arrows), 7)

        # spot check some game piece attributes
        self.assertEqual(gb.board[0][0].x, -350)
        self.assertEqual(gb.board[1][0].y, 180)
        self.assertEqual(gb.board[5][6].x, 70)
        self.assertEqual(gb.board[5][6].y, -100)
        self.assertEqual(gb.arrows[0].identifier, 0)
        self.assertEqual(gb.arrows[3].identifier, 3)

def main():
    unittest.main(verbosity = 3)

main()
