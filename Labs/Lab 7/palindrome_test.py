'''
    CS5001
    Spring 2020
    Lab 7 source code - testing the palindrome function
'''

from palindromes import is_pal

def test_is_pal(s, expected):
    ''' Function test_is_pal
        Params: string that may/may not be a palindrome, expected result
        Returns: boolean indicating pass/fail
    '''
    print('Testing input string', s, 'expected output', expected)
    if is_pal(s) == expected:
        print('SUCCESS!\n')
        return True
    print('FAIL :(\n')
    return False


def run_pal_tests():
    ''' Function: run_pal_tests
        Params: none
        Returns: int, number of tests that failed
    '''
    num_fail = 0

    # Test One: Empty string, is a palindrome
    if not test_is_pal('', True):
        num_fail += 1

    # Test Two: String with one letter, is a palindrome
    if not test_is_pal('a', True):
        num_fail += 1

    # Test Three: String with two letters, not a palindrome
    if not test_is_pal('ab', False):
        num_fail += 1

    # Test Four: Longer string, odd # of letters, is a palindrome
    if not test_is_pal('borroworrob', True):
        num_fail += 1

    # Test Five: Longer string, odd # of letters, not a palindrome
    if not test_is_pal('borroorrobw', False):
        num_fail += 1

    # Test Six: Longer string, even # of letters, is a palindrome
    if not test_is_pal('yobanaanaboy', True):
        num_fail += 1

    # Test Seven: Longer string, even # of letters, not a palindrome
    if not test_is_pal('yobanabnaboy', False):
        num_fail += 1


    return num_fail



def main():
       
    num_failed = run_pal_tests()
    if num_failed == 0:
        print('All get palindrome tests passed!\n')
    else:
        print('Something broke in is_pal, fix pls.\n')

  
            
main()
