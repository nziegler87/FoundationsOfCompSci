'''
    CS5001
    Spring 2020
    Practice problems for final exam

    Test code for Part I (shorter problems)
    Run this test code to make sure your solutions work as expected.
'''

import unittest
from part1 import *

class PracticeTest(unittest.TestCase):
    def test_doublesquare(self):
        self.assertEqual(double_square(1), 4)
        self.assertEqual(double_square(-1), 4)
        self.assertEqual(double_square(0), 0)
        self.assertEqual(double_square(5), 100)
        self.assertEqual(double_square(-5), 100)

    def test_countlist(self):
        self.assertEqual(count_list([], ''), 0)
        self.assertEqual(count_list(['a'], 'a'), 1)
        self.assertEqual(count_list(['a'], 'b'), 0)
        self.assertEqual(count_list(['a', 'a'], 'a'), 2)
        self.assertEqual(count_list(['a', 'b', 'b', 'a'], 'b'), 2)

    def test_countlist_recursive(self):
        self.assertEqual(count_list_recur([], ''), 0)
        self.assertEqual(count_list_recur(['a'], 'a'), 1)
        self.assertEqual(count_list_recur(['a'], 'b'), 0)
        self.assertEqual(count_list_recur(['a', 'a'], 'a'), 2)
        self.assertEqual(count_list_recur(['a', 'b', 'b', 'a'], 'b'), 2)
                         

                         

def main():
    unittest.main(verbosity = 3)

main()
