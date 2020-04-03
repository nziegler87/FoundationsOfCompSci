import unittest
from game_board import *

class Test_Game_Board(unittest.TestCase):
    def test_init(self):
        gb = Game_Board()
        self.assertEqual(gb.rows, 4)
        self.assertEqual(gb.cols, 4)
        self.assertEqual(gb.total_pieces, 16)
        self.assertEqual(gb.board, [])

def main():
    unittest.main(verbosity = 3)

main()
