'''
    Nathanial Ziegler
    CS 5001
    January 29, 2020
    HW 3
    Description:
        Tests for coin_flip and is_over fuctnions
'''

from nim_functions import *

def test_flip(number, expected):
    ''' Inputs: even or odd number (int) for one test of coin_flip and
                expected result, "H" or "T" (strings)
        Returns: True or False
        Does: Calls entered number, compares against expected, and returns True
              or Flase
    '''
    print("Test number: ", number, "  Expected number: ", expected, sep = "")
    actual = coin_flip(number)
    print("\tActual result: ", actual, sep = "")
    return actual == expected

def test_all_flip():
    ''' Inputs: none
        Returns: Number of tests failed
    '''
    num_fail = 0
    
    # Test 1 - Test Number: 2; Expected Result H
    if not test_flip(2, "H"):
        num_fail += 1
    # Test 2 - Test Number: 103; Expected Result T
    if not test_flip(103, "T"):
        num_fail += 1
    # Test 3 - Test Number: 10; Expected Result H
    if not test_flip(10, "H"):
        num_fail += 1
    # Test 4 - Test Number: 987; Expected Result T
    if not test_flip(987, "T"):
        num_fail += 1
    # Test 5 - Test Number: 244; Expected Result H
    if not test_flip(244, "H"):
        num_fail += 1

    return num_fail
        
def main():
    failed_tests = test_all_flip()
    if failed_tests == 0:
        print("All tests passed.")
    else:
        print(failed_tests, "tests failed.")
        
main()

    
