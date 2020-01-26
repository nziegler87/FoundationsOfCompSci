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
    print("\tActual result: ", actual, "\n", sep = "")
    return actual == expected

def test_all_flip():
    ''' Inputs: none
        Returns: Number of tests failed
    '''
    num_fail = 0
    
    # Test 1 - Test Number: 2; Expected Result: H
    if not test_flip(2, "H"):
        num_fail += 1
    # Test 2 - Test Number: 103; Expected Result: T
    if not test_flip(103, "T"):
        num_fail += 1
    # Test 3 - Test Number: 10; Expected Result: H
    if not test_flip(10, "H"):
        num_fail += 1
    # Test 4 - Test Number: 987; Expected Result: T
    if not test_flip(987, "T"):
        num_fail += 1
    # Test 5 - Test Number: 244; Expected Result: H
    if not test_flip(244, "H"):
        num_fail += 1

    return num_fail

def test_is_over(number, expected):
    ''' Inputs: number of remaining beans (int), expected (Boolean)
        Returns: True or False
        Does: Calls is_over function and passes number. Compares against
              expected value and returns True if equal, else False
    '''
    print("Test number: ", number, "   Expected: ", expected, sep = "")
    actual = is_over(number)
    print("Actual:", actual, "\n")
    return actual == expected

def test_all_is_over():
    ''' Inputs: none
        Returns: Number of tests failed
    '''

    num_fail = 0
    # Test 1 - Test Number: 20; Expected Result: False
    if not test_is_over(20, False):
        num_fail += 1
    # Test 2 - Test Number: 0; Expected Result: True
    if not test_is_over(0, True):
        num_fail += 1
    # Test 3 - Test Number: -1; Expected Result: False
    if not test_is_over(-1, False):
        num_fail += 1
    # Test 4 - Test Number: 4; Expected Result: False
    if not test_is_over(4, False):
        num_fail += 1

def test_coin_toss_result(user_choice, toss_result, player_name, expected):
    ''' Inputs: For one test -- user_choice (H or T), random
                result (H or T), player_name, and expected (str)
        Returns: True or False
        Does: Calls coin_toss_results and passes inputs. Compares against
              expected value and returns True if equal, else False
    '''
    print("Test inputs:\n   User Name: ", player_name, "\n   User Choice: ",
          user_choice, "\n   Toss Result: ", toss_result, "\nExpected "
          "Result: ", expected, sep = "")
    actual = coin_toss_result(user_choice, toss_result, player_name)
    print("Actual:", actual, "\n")
    return actual == expected

def test_all_coin_toss_result():
    ''' Inputs: none
        Returns: Number of test failed
    '''

    num_fail = 0
    # Test 1 - Player Name: "Jonas"; User Choice: "H";
    #          Toss Result: "T"; Expected: "computer"
    if not test_coin_toss_result("H", "T", "Jonas", "computer"):
        num_fail += 1

    # Test 2 - Player Name: "Nate"; User Choice: "H";
    #          Toss Result: "H"; Expected: "Nate"
    if not test_coin_toss_result("H", "H", "Nate", "Nate"):
        num_fail += 1

    # Test 3 - Player Name: "Sally"; User Choice: "T";
    #          Toss Result: "T"; Expected: "Sally"
    if not test_coin_toss_result("T", "T", "Sally", "computer"):
        num_fail += 1
    # Test 4 - Player Name: "Lanie"; User Choice: "T";
    #          Toss Result: "H"; Expected: "computer"
    if not test_coin_toss_result("T", "H", "Lanie", "computer"):
        num_fail += 1

def main():

    # Testing of test_flip
    print("--Testing test_flip--\n")
    
    failed_tests = test_all_flip()
    if failed_tests == 0:
        print("All tests passed.\n")
    else:
        print(failed_tests, "tests failed.\n")

    # Testing of is_over
    print("--Testing is_over--\n")
    
    fail_tests = test_all_is_over()
    if failed_tests  == 0:
        print("All tests passed.\n")
    else:
        print(failed_tests, "test failed.\n")

    # Testing of coin_toss_result
    print("--Testing coin_toss_result--\n")
    
    failed_test = test_all_coin_toss_result()
    if failed_tests == 0:
        print("All tests passed.\n")
    else:
        print(failed_tests, "tests failed.\n")
        
main()
