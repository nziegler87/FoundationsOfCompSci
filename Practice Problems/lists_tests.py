'''
    CS5001
    Spring 2020
    PP#4 - Testing the list functions
'''

from lists import mean
from lists import intersect
from lists import dedupe

EPSILON = 0.0001

def test_mean(lst, expected):
    ''' Function: test_mean
        Parameters: lists for input, float for expected output
        returns: boolean, indicating if the test passed
    '''
    actual = mean(lst)
    print("Testing average of", lst, "\n"
          "\t...Expected:", expected, "\n"
          "\t...Actual:", actual)
    return abs(actual - expected) < EPSILON


def test_all_mean():
    ''' Function: test_all_mean
        Parameters: none
        Returns: an int, number of tests that failed
    '''
    fails = 0
    if not test_mean([], 0):
        fails += 1
    if not test_mean([1, 3], 2.0):
        fails += 1
    if not test_mean([1, 2, 3, 4], 2.5):
        fails += 1
    if not test_mean([4, 4, 4, 4], 4.0):
        fails += 1
    return fails


def test_intersection(a, b, expected):
    ''' Function: test_intersect
        Parameters: two lists for input, one list for expected output
        returns: boolean, indicating if the test passed
    '''
    actual = intersect(a, b)
    print("Testing intesection of", a, "and", b, "\n"
          "\t...Expected:", expected, "\n"
          "\t...Actual:", actual)
    return actual == expected


def test_all_intersection():
    ''' Function: test_all_intersection
        Parameters: none
        Returns: an int, number of tests that failed
    '''
    fails = 0
    if not test_intersection([], [], []):
        fails += 1
    if not test_intersection([1, 2], [2, 1], [1, 2]):
        fails += 1
    if not test_intersection([1, 2, 3, 4], [2, 1], [1, 2]):
        fails += 1
    if not test_intersection([1, 2], [2, 1, 3, 4], [1, 2]):
        fails += 1
    return fails


def test_dedupe(lst, expected):
    ''' Function: test_dedupce
        Parameters: lists for input, one list for expected output
        returns: boolean, indicating if the test passed
    '''
    actual = dedupe(lst)
    print("Testing deduping of", lst, "\n"
          "\t...Expected:", expected, "\n"
          "\t...Actual:", actual)
    return actual == expected


def test_all_dedupe():
    ''' Function: test_all_dedupe
        Parameters: none
        Returns: an int, number of tests that failed
    '''
    fails = 0
    if not test_dedupe([], []):
        fails += 1
    if not test_dedupe([1, 2, 2], [1, 2]):
        fails += 1
    if not test_dedupe([1, 2, 3, 4], [1, 2, 3, 4]):
        fails += 1
    if not test_dedupe([4, 4, 4, 4], [4]):
        fails += 1
    return fails

def main():
    
    num_fails = test_all_mean()
    if num_fails == 0:
        print("All mean tests passed congrats!!\n\n")
    else:
        print(num_fails, "mean tests failed, sorry fix pls :(\n\n")

    num_fails = test_all_intersection()
    if num_fails == 0:
        print("All intersection tests passed congrats!!\n\n")
    else:
        print(num_fails, "intersection tests failed, sorry fix pls :(\n\n")

    num_fails = test_all_dedupe()
    if num_fails == 0:
        print("All dedupe tests passed congrats!!\n\n")
    else:
        print(num_fails, "dedupe tests failed, sorry fix pls :(\n\n")

main()
