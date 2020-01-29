'''
    Nathanial Ziegler
    CS 5001
    January 29, 2020
    HW 3
    Description:
        Functions for nim:
            coin_flip, is_over, validate_input, user_coin_selection
            coin_toss_result, validate_deduct, computer_deduct
'''

import random

def coin_flip(number):
    ''' Name: coin_flip
        Input: even or odd number (int)
        Returns: sting
        Does: Returns string "H" if number is even and "T" if number is odd.
    '''
    if (number % 2) == 0:
        return "H"
    else:
        return "T"

def is_over(number):
    ''' Name: is_over
        Input: number (int)
        Return: True or False
        Does: Input number of remaining beans and return False if
              all beans are used, else True.
    '''
    if number == 0:
        return True
    else:
        return False

def validate_input(user_input, option_a, option_b):
    ''' Name: validate_input
        Inputs: user_input, option_a, option_b (all ints)
        Returns: Boolean (True or False)
        Does: Compares user_input to two options and returns True
              if user_input matches one of the responses.
    '''
    if user_input != option_a and user_input != option_b:
        return False
    else:
        return True

def user_coin_selection(player_name):
    ''' Name: user_coin_selection
        Input: player_name (string)
        Returns: User selection, either H or T (strings) for coing toss
        Does: Returns user choice, H or T, as capitals
    '''
    user_choice = input("\n" + player_name + ", enter H for Heads "
                        "or T for tales: ").upper()
    return user_choice

def coin_toss_result(user_choice, toss_result, player_name, computer_name):
    ''' Name: coin_toss_result
        Input: user_choice (H or T), toss_result (H or T),
               player name, and computer_name...all strings
        Returns: Name of starting player, either computer or
                 player_name, as strings
        Does: Compares user coin side choice to coin toss result and
              announces winner
    '''
    if user_choice == toss_result:
        return player_name
    else:
        return computer_name

def validate_deduct(total, deduct):
    ''' Name: validate_deduct
        Input: total and deduct (ints)
        Returns: True or False
        Does: Ensures user deduction for min game is valid
    '''
    if deduct > total:
        return False
    else:
        if deduct <= 3 and deduct > 0:
            return True
        else:
            return False

def computer_deduct(bean_pile):
    ''' Name: computer_deduct
        Input: Number of beans remaining, int greater than 0
        Returns: Number of beans computer wishes to deduct (int)
        Does: Return computer deduction based on number of remaining beans
    '''
    if bean_pile > 4:
        deduct = random.randint(1, 3)
    elif bean_pile == 4:
        deduct = 3
    elif bean_pile == 3:
        deduct = 2
    else:
        deduct = 1
    return deduct
