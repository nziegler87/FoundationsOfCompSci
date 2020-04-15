'''
    CS5001
    Spring 2020
    Practice problems for final exam

    Test code for Part 3 (other data structures)
    Run this test code to make sure your solutions work as expected.
'''

import unittest
from part3 import *

class PracticeTest(unittest.TestCase):

    def test_dictionarysum(self):
        d = {'one':1, 'two': 2, 'three':3}
        self.assertEqual(dictionary_sum(d), 6)

        d = {-1:-10, -2:-20, -3:-30}
        self.assertEqual(dictionary_sum(d), -60)

        d = {}
        self.assertEqual(dictionary_sum(d), 0)

    def test_reversestack(self):
        s = Stack()
        rev = reverse_stack(s)
        self.assertTrue(rev.is_empty())
        
        s.push(1)
        rev = reverse_stack(s)
        self.assertEqual(rev.top(), 1)

        s.push(1)
        s.push(2)
        rev = reverse_stack(s)
        self.assertEqual(rev.top(), 1)

        s.push(3)
        s.push(2)
        s.push(1)
        rev = reverse_stack(s)
        self.assertEqual(rev.top(), 3)
                 

def main():
    unittest.main(verbosity = 3)

main()
