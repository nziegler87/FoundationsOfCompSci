'''
    CS 5001
    Nathanial Ziegler
    April 2020
    Optional Lab
    Description:
        Part 1 responses
'''

def double_square(integer):
    ''' Name: double_square
        Parameters: one integer
        Returns: the value of the given integer, doubled and then squared
    '''
    integer = integer * 2
    return integer ** 2

def count_list(string_lst, string):
    ''' Name: count_list
        Parameters: a list o strings, and a string
        Returns: an int indicating the number of times the given string appears
                 in the given list
    '''
    count = 0
    for item in string_lst:
        if item == string:
            count += 1
    return count

def count_list_recur(string_lst, string):
    ''' Name: count_list_recur
        Parameters: a list o strings, and a string
        Returns: an int indicating the number of times the given string appears
                 in the given list
    '''
    if not string_lst:
        return 0
    else:
        if string_lst[0] == string:
            return 1 + count_list_recur(string_lst[1:], string)
        else:
            return count_list_recur(string_lst[1:], string)
