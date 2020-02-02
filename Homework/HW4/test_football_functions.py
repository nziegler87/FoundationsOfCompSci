'''
    CS5001
    Spring 2020
    HW4 - testing the football functions
'''

from football_functions import count_result, count_one_wins, \
     compile_streaks, sum_points

def test_count_result(results, outcome, expected):
    ''' Function: test_count_result
        Parameters: results (a list), outcome (W/L/D),
                    expected (an int)
        Returns: Boolean indicating if test passed
    '''
    actual = count_result(results, outcome)
    print("Testing the number of", outcome, "in test list.\n"
          "\t...Expected:", expected, "\n"
          "\t...Actual:", actual)
    return expected == actual

def all_test_count():
    ''' Function: all_test_count
        Parameters: none
        Returns: number of tests that failed
    '''
    num_fails = 0
    if not test_count_result([], 'W', 0):
        num_fails += 1
    if not test_count_result(['W'], 'W', 1):
        num_fails += 1
    if not test_count_result(['L', 'W', 'L'], 'L', 2):
        num_fails += 1
    if not test_count_result(['D', 'D', 'D', 'D'], 'D', 4):
        num_fails += 1
    return num_fails


def test_one_wins(results, goals, expected):
    ''' Function: test_one_wins
        Parameters: results (a list of strings),
                    goals (a list of ints), expected result (an int)
        Returns: Boolean indicating if test passed
    '''
    actual = count_one_wins(results, goals)
    print("Counting one-goal wins in the test list.\n"
          "\t...Expected:", expected, "\n"
          "\t...Actual:", actual)
    return expected == actual

def all_test_one_wins():
    ''' Function: all_test_one_wins
        Parameters: none
        Returns: number of tests that failed
    '''
    num_fails = 0
    if not test_one_wins([], [], 0):
        num_fails += 1
    if not test_one_wins(['W'], [1], 1):
        num_fails += 1
    if not test_one_wins(['L', 'W', 'L'], [0, 0, 0], 0):
        num_fails += 1
    if not test_one_wins(['W', 'W', 'D', 'D'], [1, 1, 1, 1], 2):
        num_fails += 1
    return num_fails


def test_streak(results, expected):
    ''' Function: test_streak
        Parameters: results (a list of strings),
                     expected result (an int)
        Returns: Boolean indicating if test passed
    '''
    actual = compile_streaks(results)
    print("Compiling the streaks in", results, "\n"
          "\t...Expected:", expected, "\n"
          "\t...Actual:", actual)
    return expected.replace(' ', '') == actual.replace(' ', '')

def all_test_streak():
    ''' Function: all_test_streak
        Parameters: none
        Returns: number of tests that failed
    '''
    num_fails = 0
    if not test_streak([], ''):
        num_fails += 1
    if not test_streak(['W'], '1W'):
        num_fails += 1
    if not test_streak(['L', 'W', 'L'], '1L 1W 1L'):
        num_fails += 1
    if not test_streak(['W', 'W', 'D', 'D'], '2W 2D'):
        num_fails += 1
    if not test_streak(['W', 'W', 'D', 'D', 'D'], '2W 3D'):
        num_fails += 1
    if not test_streak(['W', 'W', 'D', 'D', 'W', 'W', 'W'], '2W 2D 3W'):
         num_fails += 1
    if not test_streak(['D', 'D', 'L'], '2D 1L'):
        num_fails += 1
    if not test_streak(['W', 'W', 'D', 'W', 'W', 'W', 'D', 'W', 'W'],
                       '2W 1D 3W 1D 2W'):
        num_fails += 1
    return num_fails


def test_points(results, season, game, expected):
    ''' Function: test_streak
        Parameters: results (a list of strings),
                    outcome (W/L/D), expected result (an int)
        Returns: Boolean indicating if test passed
    '''
    actual = sum_points(results, season, game)
    print("Counting number of points in season", season, "game", game, "\n"
          "\t...Expected:", expected, "\n"
          "\t...Actual:", actual)
    return expected == actual

def all_points_test():
    ''' Function: all_test_streak
        Parameters: none
        Returns: number of tests that failed
    '''
    num_fails = 0
    if not test_points([], 0, 0, 0):
        num_fails += 1
    if not test_points(['L', 'W', 'L'], 1, 1, 0):
        num_fails += 1
    if not test_points(['L', 'W', 'L'], 1, 2, 3):
        num_fails += 1
    if not test_points(['W', 'W', 'D', 'D'], 1, 4, 8):
        num_fails += 1
    return num_fails

def main():
    # Test the first function: Number of win/loss/draw
    fails = all_test_count()
    if fails == 0:
        print("All count-result tests passed, great job!\n\n")
    else:
        print(fails, "tests failed, is brokn pls fix.\n\n")

    # Test the second function: Number of one-goal wins
    fails = all_test_one_wins()
    if fails == 0:
        print("All one-goal win tests passed, great job!\n\n")
    else:
        print(fails, "tests failed, is brokn pls fix.\n\n")

    # Test the third function: Summary of all the streaks
    fails = all_test_streak()
    if fails == 0:
        print("All streak tests passed, great job!\n\n")
    else:
        print(fails, "streak tests failed, is brokn pls fix.\n\n")


    # Test the fourth function: Number of points
    fails = all_points_test()
    if fails == 0:
        print("All points tests passed, great job!\n\n")
    else:
        print(fails, "points tests failed, is brokn pls fix.\n\n")



main()
    
    
        
    
