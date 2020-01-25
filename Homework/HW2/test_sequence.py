'''
    Nathanial Ziegler
    CS5001
    Homework 2
    January 21, 2020
    Description:
        Test suite to test kth_term and arith_sum functions.
'''

from sequence import *

def test_kterm (initial, diff, k, expected):
    ''' Function: test_kterm
        Inputs: Values to pass to kth_term for ONE test --
                initial, diff, k, and expected output (all ints)
        Returns: Nothing
        Does: Calls kth_term with inputs and
              prints results as well as expected results
    '''
    print("Testing Inputs:\t\t", initial, ", ", diff, ", ", k, "\n",
          "Expected kth Term:\t", expected, sep = "")
    actual = kth_term(initial, diff, k)
    print("Actual:\t\t\t", actual, "\n", sep = "")

def test_arith_sum (initial, diff, n, expected):
    ''' Function: test_arith_sum
        Inpputs: Values to pass to arith_sum for ONE test --
                 initial, diff, n and expected result (al ints)
                 Returns: Nothing
        Does: Calls arith_sum with inputs and prints results
              as well as expected results
    '''
    print("Testing Inputs:\t", initial, ", ", diff, ", ", n,
          "\nExpected Sum:\t", expected, sep = "")
    actual = arith_sum(initial, diff, n)
    print("Actual:\t\t", actual, "\n", sep = "")

def main():
    # Testing of test_kterm
    print("**Testing kth_term Function**\n")

    # Test 1: initial = 3, difference = 7, k = 24. Value should equal 164
    test_kterm(3, 7, 24, 164)

    # Test 2: initial = 0, difference = -2, k = 14. Value should equal -26
    test_kterm(0, -2, 14, -26)

    # Test 3: initial = 35, difference = 21, k = 4. Value should equal 98
    test_kterm(35, 21, 4, 98)

    # Test 4: initial = -120, difference = 17, k = 67. Value should equal 1002
    test_kterm(-120, 17, 67, 1002)

    # Testing of arith_sum
    print("**Testing of arith_sum**\n")

    # Test 1: initial = 1, difference = 5, n = 10. Value should equal 235.0
    test_arith_sum(1, 5, 10, 235.0)

    # Test 2: initial = -12, difference = 3, n = 6. Value should equal -27.0
    test_arith_sum(-12, 3, 6, -27.0)
    
    # Test 3: initial = 1014, difference = 57, n = 67. Value should be 193965.0
    test_arith_sum(1014, 57, 67, 193965.0)
    
    # Test 4: initial = -89, difference = -4, n = 101. Value should be -29189.0
    test_arith_sum(-89, -4, 101, -29189.0)
    
main()

    
