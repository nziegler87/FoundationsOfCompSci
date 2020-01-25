''' CS5001
    Spring 2020
    HW2 Starter Code

    Test suite for digits functions
'''

from digits import get_digit

def report_results(number, power, expected, actual):
    ''' Function report_results
        Parameters: 4 integers -- number we're taking apart,
                    n to give the place 10^n, expected result,
                    actual result
        Returns: Nothing; calls the get_digit function and prints
                 actual vs expected result
    '''
    print("For inputs number =", number, "power =", power,  "...\n"
          "\tExpected:", expected, "\n"
          "\tActual:", actual)


def test_get_digit(num, power, expected):
    ''' Function: test_get_digit
        Parameters: 3 integers -- a number whose digits we want to
                    isolate, n to get 10^n place, and the expected
                    result from calling get_digit
        Returns: nothing, calls the report function to see what happened
    '''
    actual = get_digit(num, power)
    report_results(num, power, expected, actual)

    
def main():
    test_value = 8124
    test_get_digit(test_value, 0, 4)
    test_get_digit(test_value, 1, 2)
    test_get_digit(test_value, 2, 1)
    test_get_digit(test_value, 3, 8)
    test_get_digit(test_value, 4, 0)
    test_get_digit(test_value, 5, 0)

main()
