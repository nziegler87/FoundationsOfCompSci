import unittest
from binary_to_decimal import convert_to_decimal

class TestConversion(unittest.TestCase):
    def test_convert_to_decimal(self):
        self.assertEqual(convert_to_decimal('0'), 0)
        self.assertEqual(convert_to_decimal('1'), 1)
        self.assertEqual(convert_to_decimal('10'), 2)
        self.assertEqual(convert_to_decimal('10100'), 20)
        self.assertEqual(convert_to_decimal('111100011111111'), 30975)
        self.assertEqual(convert_to_decimal('111111111111'), 4095)

def main():
    unittest.main(verbosity = 3)

main()
