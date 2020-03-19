'''
    CS5001
    Spring 2020
    HW7 test code

    Here we inherit from the unittest.TestCase class
    so we have access to its attributes and methods
'''

import unittest
import os
from game import Game
from cookie import Cookie
'''
    Nathanial Ziegler
    CS 5001
    March 2020
    HW 7
    Description: Test suite provided by CS 5001 Instructors
'''

class CookieTest(unittest.TestCase):
    def test_init(self):
        c = Cookie()
        self.assertEqual(c.score, 0)
        self.assertEqual(c.achievements, {})

    def test_score(self):
        c = Cookie()

        # Add one point, go from zero to 1
        c.add_point()
        self.assertEqual(c.score, 1)

        # Initialize score from file with a non-
        # existent file; score goes back to zero
        if os.path.exists('nofile.txt'):
            os.remove('nofile.txt')
        c.initialize_score('nofile.txt')
        self.assertEqual(c.score, 0)

        # Initialize score from file with a score of
        # 10
        with open('testscore.txt', 'w') as outfile:
            outfile.write('10')
        c.initialize_score('testscore.txt')
        self.assertEqual(c.score, 10)
        os.remove('testscore.txt')

class GameTest(unittest.TestCase):
    def test_init(self):
        g = Game('noscore.txt', 'noachieve.txt')
        self.assertEqual(g.scorefile, 'noscore.txt')
        self.assertEqual(g.achievefile, 'noachieve.txt')
    

def main():
    unittest.main(verbosity = 3)

main()
