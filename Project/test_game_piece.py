from game_piece import Game_Piece
import unittest

COLORS = ["blue", "green", "yellow", "red"]

class Test_Game_Piece(unittest.TestCase):
    def test_init(self):
        piece = Game_Piece("1", -202, 301, "yellow.gif", 100)
        self.assertEqual(piece.identifier, "1")
        self.assertEqual(piece.filled, "")
        self.assertEqual(piece.x, -202)
        self.assertEqual(piece.y, 301)
        self.assertEqual(piece.image, "yellow.gif")
        self.assertEqual(piece.size, 100)

    def test_fill_piece(self):
        piece = Game_Piece("0", 0, 0, "test.gif", 0)
        for color in COLORS:
            piece.fill_piece(color)
            self.assertEqual(piece.filled, color)
        
def main():
    unittest.main(verbosity = 3)

main()
