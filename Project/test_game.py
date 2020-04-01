import unittest
from game import create_streak, check_four, check_winner

class Game_Board_Test(unittest.TestCase):
    def test_create_streak(self):
        self.assertEqual(create_streak([1, 1, 1, 2, 2, 3]),
                         [(3, 1),(2, 2), (1,3)])
        self.assertEqual(create_streak([]),[])
        self.assertEqual(create_streak([""]), [(1, "")])
        self.assertEqual(create_streak(["", "", ""]), [(3, "")])
        self.assertEqual(create_streak(["a"]),[(1, "a")])
        self.assertEqual(create_streak(["red", "red", "blue", "blue"]),
                         [(2, "red"), (2, "blue")])
        self.assertEqual(create_streak(["r", "r", "r", "r", "r"]), [(5, "r")])
        self.assertEqual(create_streak(["r", "r", "r", "b", "b", "r", "r"]),
                         [(3, "r"), (2, "b"), (2, "r")])
                         
    def test_check_four(self):
        self.assertEqual(check_four([]), None)
        self.assertEqual(check_four([(4, "")]), None)
        self.assertEqual(check_four([(3, "red"), (2, "blue")]), None)
        self.assertEqual(check_four([(4, "yellow")]), (True, "yellow"))
        self.assertEqual(check_four([(4, 4)]), (True, 4))
        self.assertEqual(check_four([(3, "green"), (2, "blue"), (5, "red")]),
                         (True, "red"))
        self.assertEqual(check_four([(2, 3), (12, 20), (0, 30)]), (True, 20))
        self.assertEqual(check_four([(4, "r"), (20, "b"), (3, "c")]),
                         (True, "r"))
    
    def check_winner(self):
        self.assertEqual(check_winner([]), None)
        self.assertEqual(check_winner([""]), None)
        self.assertEqual(check_winner(["a", "a", "a", "b", "b"]), None)
        self.assertEqual(check_winner(["a", "a", "a", "a", "a", "a"]),
                         (True, "a"))
        self.assertEqual(check_winner(["a", "b", "b", "b", "b", "c"]),
                         (True, "b"))

def main():
    unittest.main(verbosity = 3)

main()
