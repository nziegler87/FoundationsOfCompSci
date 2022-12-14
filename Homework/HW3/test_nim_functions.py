'''
    Nathanial Ziegler
    CS 5001
    January 29, 2020
    HW 3
    Description:
        Tests for the following nim_functions:
            coin_flip       coin_toss_result          
            is_over         validate_deduct
            validate_input
'''

from nim_functions import *

def test_flip(number, expected):
    ''' Inputs: even or odd number (int) for one test of coin_flip and
                expected result, "H" or "T" (strings)
        Returns: True or False
        Does: Calls entered number, and passes to coin_flip function.
              Compares result against expected and returns True if they match
              else Flase
    '''
    print("Test number: ", number, "  Expected number: ", expected, sep = "")
    actual = coin_flip(number)
    print("\tActual result: ", actual, "\n", sep = "")
    return actual == expected

def test_all_flip():
    ''' Name: test_all_flip
        Inputs: none
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
    # Test 4 - Test Number: -987; Expected Result: T
    if not test_flip(-987, "T"):
        num_fail += 1
    # Test 5 - Test Number: -244; Expected Result: H
    if not test_flip(-244, "H"):
        num_fail += 1

    return num_fail

def test_is_over(number, expected):
    ''' Inputs: number of remaining beans (int), expected (Boolean)
        Returns: True or False
        Does: Calls is_over function and passes number. Compares actual against
              expected value and returns True if equal, else False
    '''
    print("Test number: ", number, "   Expected: ", expected, sep = "")
    actual = is_over(number)
    print("Actual:", actual, "\n")
    return actual == expected

def test_all_is_over():
    ''' Name: test_all_is_over
        Inputs: none
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

    return num_fail

def test_validate_input(user_input, option_a, option_b, expected):
    ''' Name: test_validate_input
        Input: user_input, option_a, option_b, expected (strings)
        Returns: True or False
        Does: Calls validate_input and passes user_input. Compares it to
              option_a and option_b then returns True if at least one matches
              else returns False. Then compares actual output vs expected.
    '''
    print("Test inputs:\n User Input: ", user_input, "\n Option A: ",
          option_a, "     Option B: ", option_b, "\nExpected Result: ",
          expected, sep = "")
    actual = validate_input(user_input, option_a, option_b)
    print(" Actual:", actual, "\n")
    return actual == expected

def test_all_validate_input():
    ''' Name: test_all_validate_input
        Inputs: none
        Returns: number of failed tests
    '''
    num_fail = 0
    
    # Test 1 - User Input: "H" ; Option A: "H"; Option B: "T"; Expected: True
    if not test_validate_input("H", "H", "T", True):
        num_fail += 1
        
    # Test 2 - User Input: "h"; Option A: "H"; Option B: "T"; Expected: False
    if not test_validate_input("h", "H", "T", False):
        num_fail += 1
    
    # Test 3 - User Input: "g"; Option A: "H"; Option B: "T"; Expected: False
    if not test_validate_input("g", "H", "T", False):
        num_fail += 1
    
    # Test 4 - User Input: "Blue"; Option A: "Red"; Option B: "Green";
    #          Expected: False
    if not test_validate_input("Blue", "Red", "Green", False):
        num_fail += 1
    
    # Test 5 - User Input: "Blue"; Option A: "Red"; Option B: "Blue";
    #          Expected: True
    if not test_validate_input("Blue", "Red", "Blue", True):
        num_fail += 1

    return num_fail

def test_coin_toss_result(user_choice, toss_result, player_name,
                          computer_name, expected):
    ''' Inputs: For one test -- user_choice , toss_result, player_name,
                computer name, and expected (all strings)
        Returns: True or False
        Does: Calls coin_toss_results and passes inputs. Compares actual
              against expected value and returns True if equal, else False
    '''
    print("Test inputs:\n   User Name: ", player_name, "\n   Computer Name:",
          computer_name, "\n   User Choice: ", user_choice,
          "\n   Toss Result: ", toss_result, "\nExpected "
          "Result: ", expected, sep = "")
    actual = coin_toss_result(user_choice, toss_result, player_name,
                              computer_name)
    print("Actual:", actual, "\n")

    return actual == expected

def test_all_coin_toss_result():
    ''' Name: test_all_coin_toss_result
        Inputs: none
        Returns: Number of test failed
    '''
    num_fail = 0
    
    # Test 1 - Player Name: "Jonas"; Computer Name: "Alvin", User Choice: "H";
    #          Toss Result: "T"; Expected: "computer"
    if not test_coin_toss_result("H", "T", "Jonas", "Alvin", "Alvin"):
        num_fail += 1

    # Test 2 - Player Name: "Nate"; Computer Name: Jane; User Choice: "H";
    #          Toss Result: "H"; Expected: "Nate"
    if not test_coin_toss_result("H", "H", "Nate", "Jane", "Nate"):
        num_fail += 1

    # Test 3 - Player Name: "Sally"; Computer Name: Bob; User Choice: "T";
    #          Toss Result: "T"; Expected: "Sally"
    if not test_coin_toss_result("T", "T", "Sally", "Bob", "Sally"):
        num_fail += 1

    # Test 4 - Player Name: "Lanie"; Computer Name: computer; User Choice: "T";
    #          Toss Result: "H"; Expected: "computer"
    if not test_coin_toss_result("T", "H", "Lanie", "computer", "computer"):
        num_fail += 1

    return num_fail

def test_validate_deduct(total, deduct, expected):
    ''' Name: test_validate_deduct
        Inputs: For one test - total and deduct  plus expected...all ints
        Returns: True or False
        Does: Calls validate_deduct and passes input. Compares expected value
              against expected value and returns True if dequal, else False
    '''
    print("Inputs:\n Total:", total, "\tDeduction:", deduct, "\tExpected:",
          expected)
    actual = validate_deduct(total, deduct)
    print("Actual:", actual, "\n")
    return actual == expected

def test_all_validate_deduct():
    ''' Name: test_all_validate_deduct
        Inputs: Nothing
        Returns: Number of failed tests
    '''

    num_fail = 0
    
    # Test 1 - Total: 10; Deduct: 3; Expected: True
    if not test_validate_deduct(10, 2, True):
        num_fail += 1

    # Test 2 - Total: 20; Deduct: -2; Expected: False
    if not test_validate_deduct(20, -2, False):
        num_fail += 1

    # Test 3 - Total: 2; Deduct: 3; Expected: False
    if not test_validate_deduct(2, 3, False):
        num_fail += 1

    # Test 4 - Total: 1; Deduct: 0; Expected: Flase
    if not test_validate_deduct(1, 0, False):
        num_fail += 1

    return num_fail

def main():

    # Testing of coin_flip
    print("--Testing coin_flip--\n")
    failed_tests = test_all_flip()
    if failed_tests == 0:
        print("All tests passed.\n")
    else:
        print(failed_tests, "tests failed.\n")

    # Testing of is_over
    print("--Testing is_over--\n")
    failed_tests = test_all_is_over()
    if failed_tests == 0:
        print("All tests passed.\n")
    else:
        print(failed_tests, "test failed.\n")

    # Testing of validate_input
    print("--Testing validate_input--\n")
    failed_tests = test_all_validate_input()
    if failed_tests == 0:
        print("All tests passed.\n")
    else:
        print(failed_tests, "tests failed.\n")

    # Testing of coin_toss_result
    print("--Testing coin_toss_result--\n")
    failed_tests = test_all_coin_toss_result()
    if failed_tests == 0:
        print("All tests passed.\n")
    else:
        print(failed_tests, "tests failed.\n")

    # Testing of validate_deduct
    print("--Testing validate_deduct--\n")
    failed_tests = test_all_validate_deduct()
    if failed_tests == 0:
        print("All tests passed.\n")
    else:
        print(failed_tests, "tests failed.\n")
  
main()
