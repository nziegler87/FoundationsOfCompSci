import unittest
from palindrome import is_pal2

class PalindromeTest(unittest.TestCase):
    def test_is_pal2(self):
        self.assertTrue(is_pal2("tacocat"))
        self.assertTrue(is_pal2("radar"))
        self.assertTrue(is_pal2("borroworrob"))
        self.assertTrue(is_pal2("madamimadam"))
        self.assertTrue(is_pal2("aa"))
        self.assertTrue(is_pal2("a"))
        self.assertTrue(is_pal2(""))

def main():
    unittest.main(verbosity = 3)

main()
