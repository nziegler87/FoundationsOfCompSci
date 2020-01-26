''' CS5001
    Spring 2020
    HW3: Test suite for typing functions
'''

EPSILON = 0.0001
from typing_functions import calculate_wpm
from typing_functions import calculate_adjusted

def test_calculate_wpm(num_words, time, expected):
    ''' Function: test_calculate_wpm
        Parameters: number of words and seconds (int, float), which
                    are arguments to the function we're testing, and
                    the expected result (float)
        returns: Boolean indicating if the test passed
    '''
    actual = calculate_wpm(num_words, time)
    print("Testing calculate_wpm with", num_words, "and", time, "\n"
          "\t...Expected:", expected, "\n"
          "\t...Actual:", actual)
    return (expected - actual) < EPSILON



def test_all_calculate_wpm():
    ''' Function: test_calculate_wpm
        Parameters: none
        Returns: an int, number of tests that failed
    '''
    num_fails = 0
    if not test_calculate_wpm(10, 60, 10.0):
        num_fails += 1
    if not test_calculate_wpm(0, 60, 0.0):
        num_fails += 1
    if not test_calculate_wpm(60, 30, 120.0):
        num_fails += 1
    if not test_calculate_wpm(60, 120, 30.0):
        num_fails += 1
    return num_fails

def test_calculate_adjusted(num_words, num_mistakes, time, expected):
    ''' Function: test_calculate_adjusted
        Parameters: number of words, mistakes, and seconds (int, int float),
                    which are arguments to the function we're testing, and
                    the expected result (float)
        returns: Boolean indicating if the test passed
    '''
    actual = calculate_adjusted(num_words, num_mistakes, time)
    print("Testing calculate_adjusted with", num_words, "and",
          num_mistakes, "and", time, "\n"
          "\t...Expected:", expected, "\n"
          "\t...Actual:", actual)
    return (expected - actual) < EPSILON

def test_all_calculate_adjusted():
    ''' Function: test_calculate_adjusted
        Parameters: none
        Returns: an int, number of tests that failed
    '''
    num_fails = 0
    if not test_calculate_adjusted(10, 60, 10, 0.0):
        num_fails += 1
    if not test_calculate_adjusted(1, 10, 60, 0.0):
        num_fails += 1
    if not test_calculate_adjusted(60, 5, 30, 110.0):
        num_fails += 1
    if not test_calculate_adjusted(60, 20, 120, 20.0):
        num_fails += 1
    return num_fails
        

def main():
    fails = test_all_calculate_wpm()
    if fails == 0:
        print("All your wpm calculations passed great job!\n\n")
    else:
        print(fails, "tests failed go back and fix pls.\n\n")

    fails = test_all_calculate_adjusted()
    if fails == 0:
        print("All your adjusted calculations passed great job!\n\n")
    else:
        print(fails, "tests failed go back and fix pls.\n\n")

main()
