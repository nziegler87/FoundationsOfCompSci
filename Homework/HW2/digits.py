'''
    Nathanial Ziegler
    CS5001
    Homework 2
    January 21, 2020
    Description:
        For this program, the user inputs an integer and then
        the 10^n place value the wish to isoalte in that number.
    Consulted:
        https://www.geeksforgeeks.org/abs-in-python/
'''

def get_digit(num, power):
    ''' Function: get_digits
        Inputs: Number and 10^n digit to isolate from number (both ints)
        Returns: Isolated number as int
        Does: Isolates 10^n digit from inputed integer and n values
    '''
    # Return absolute value of entered number
    abs_num = abs(num)

    # Move digit to isolate to the ones place
    isolated_num = abs_num // 10**power

    # Isolate digit in ones place
    isolated_num = isolated_num % 10
    
    return isolated_num
