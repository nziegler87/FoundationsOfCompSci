'''
    CS5001
    Spring 2020
    Practice problems for final exam

    Test code for Part 2 (classes and lists)
    Run this test code to make sure your solutions work as expected.
'''
import unittest
from part2 import *

class PracticeTest(unittest.TestCase):
    def test_movie(self):
        m = Movie('a', 10, 'b')
        self.assertEqual(m.title, 'a')
        self.assertEqual(m.runtime, 10)
        self.assertEqual(m.rating, 'b')

    def test_longer(self):
        m1 = Movie('a', 10, 'b')
        m2 = Movie('a', 9, 'b')
        self.assertTrue(m1.longer(m2))
        self.assertFalse(m2.longer(m1))

        m3 = Movie('a', 10, 'b')
        m4 = Movie('a', 10, 'b')
        self.assertFalse(m3.longer(m4))
        self.assertFalse(m4.longer(m3))

    def test_add_longer(self):
        m1 = Movie('a', 10, 'b')
        m2 = Movie('a', 9, 'b')
        m3 = Movie('a', 11, 'b')
        m4 = Movie('a', 12, 'b')
        
        self.assertEqual(add_longer([], m1), [m1])
        self.assertEqual(add_longer([m1], m2), [m1])
        self.assertEqual(add_longer([m1], m3), [m1, m3])
        self.assertEqual(add_longer([m1, m3], m4), [m1, m3, m4])
        

                         

def main():
    unittest.main(verbosity = 3)

main()
