'''
    CS5001
    Spring 2020
    Source code from lecture - tests for stack applications

   This is all test code that goes with the worksheet and video #4 -
   writing code for which a stack is a good solution.

   In video #4 from this week, we write the code for rev_string, so 
   that test passes OK.

   In the worksheet from this week, we describe these tests,
   but it's your job to write functions that pass the tests.
   (We'll post the solutions eventually, but take a crack at them first!)
'''

import unittest
from stack_functions import *

##class TestReverse(unittest.TestCase):
##    def test_rev_string(self):
##        self.assertEqual(rev_string("pie"), "eip")
##        self.assertEqual(rev_string("pumpkin pie"), "eip nikpmup")
##        self.assertEqual(rev_string("p"), "p")
##        self.assertEqual(rev_string("pie!! "), " !!eip")
##        self.assertEqual(rev_string("123456789"), "987654321")
##        self.assertEqual(rev_string("5.67 1.33"), "33.1 76.5")
##        self.assertEqual(rev_string("\nhello\n"), "\nolleh\n")
##        self.assertEqual(rev_string(""), "")
##
class TestMyBalance(unittest.TestCase):
    def test_is_balanced(self):
        self.assertTrue(is_balanced("()"))
        self.assertTrue(is_balanced(""))
        self.assertTrue(is_balanced("string of words!"))
        self.assertTrue(is_balanced("(())"))
        self.assertTrue(is_balanced("(s)"))
        self.assertTrue(is_balanced("()s"))
        self.assertTrue(is_balanced("()()"))
        self.assertTrue(is_balanced("(())(hello)(goodbye)"))
        self.assertTrue(is_balanced("a(b(cdef)g)"))
        self.assertTrue(is_balanced("()()()()()((((()))))"))

        self.assertFalse(is_balanced("("))
        self.assertFalse(is_balanced(")"))
        self.assertFalse(is_balanced(")("))
        self.assertFalse(is_balanced("(s)("))
        self.assertFalse(is_balanced("(hello!)()()())"))
        self.assertFalse(is_balanced("(())((()))("))
        
class TestConversion(unittest.TestCase):
    def test_convert_to_binary(self):
        self.assertEqual(convert_to_binary(0), "0")
        self.assertEqual(convert_to_binary(1), "1")
        self.assertEqual(convert_to_binary(2), "10")
        self.assertEqual(convert_to_binary(3), "11")
        self.assertEqual(convert_to_binary(4), "100")
        self.assertEqual(convert_to_binary(-1), "")
        self.assertEqual(convert_to_binary(-10), "")
        self.assertEqual(convert_to_binary(20), "10100")
        self.assertEqual(convert_to_binary(25), "11001")
        self.assertEqual(convert_to_binary(31), "11111")
        self.assertEqual(convert_to_binary(250), "11111010")
        self.assertEqual(convert_to_binary(256), "100000000")


def main():
    unittest.main(verbosity = 3)

main()
