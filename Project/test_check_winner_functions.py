from check_winner_functions import *
import unittest

class Test_Winner_Functions(unittest.TestCase):

    def test_create_streak(self):
        # string of input and outputs to run through a for loop
        tests = [[[""], [(1, "")]],
                   [["a", "b", "b", "c", "a", "a"], [(1, "a"), (2, "b"),
                                                     (1, "c"), (2, "a")]],
                   [["r", "r", "d", "d"], [(2, "r"), (2, "d")]],
                   [["z", "z", "z", "z", "z"], [(5, "z")]]]

        for test in tests:
            self.assertEqual(create_streak(test[0]), test[1])


    def test_check_four(self):
        self.assertEqual(check_four([(3, "z")]), None)
        self.assertEqual(check_four([(4, "z")]), "z")
        self.assertEqual(check_four([(4, "")]), None)
        self.assertEqual(check_four([(2, "a"), (6, "b"), (5, "c")]), "b")
        self.assertEqual(check_four([(8, 1)]), 1)

    def test_check_winner(self):
        tests = [[["a", "a", "a", "b", "b", "b", "b", "b"],"b"],
                 [["red", "red", "red", "red"],"red"],
                 [["", "", "", "", "", "c", "c", "c", "c"],"c"],
                 [[1, 2, 3, 4, 5, 5, 5, 5, 5], 5]]
        for test in tests:
            self.assertEqual(check_winner(test[0]), test[1])

def main():
    unittest.main(verbosity = 3)

main()
        
