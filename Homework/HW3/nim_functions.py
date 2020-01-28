'''
    Nathanial Ziegler
    CS 5001
    January 29, 2020
    HW 3
    Description:
        Functions for nim
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
        Input: number of remaining beans (int)
        Return: True or False
        Does: Input number of remaining beans and return False if
              all beans are used, else True.
    '''
    if number == 0:
        return True
    else:
        return False

# NEED TO WRITE TEST
def validate_input(user_input, option_a, option_b):
    ''' Name: validate_input
        Inputs: user_input, option_a, option_b (all ints)
        Returns: Boolean (True or False)
        Does: Compares user_input to two options and returns True
              if user_input matches one of the responses.
    '''
    if user_input != option_a and user_input != option_b:
        print("I'm sorry, that is not a valid input. You must enter "
              "either ", option_a, " or ", option_b,".\n", sep = "")
        return False
    else:
        return True
        
# STILL NEED TO WRITE TEST SUITE...HOW TO ACCOUNT FOR INV
def user_coin_selection(player_name):
    ''' Name: user_coin_selection
        Input: player_name, string
        Returns: User selection, either H or T (strings) for coing toss
    '''
    user_choice = input(player_name + ", enter H for Heads "
                        "or T for tales: ").upper()
    return user_choice

def coin_toss_result(user_choice, toss_result, player_name):
    ''' Name: coin_toss_result
        Input: user_choice (H or T), toss_result (H or T),
               and player name...all strings
        Returns: Name of starting player, either computer or
                 player_name, as strings
    '''
    if user_choice == toss_result:
        return player_name
    else:
        return "computer"

# STILL NEED TO WRITE TEST SUITE...HOW TO ACCOUNT FOR INVALID MOVE
def user_deduct(bean_pile):
    ''' Name: user_deduct
        Input: Number of beans remaining (int)
        Returns: Number of beans user wishes to deduct (int)
    '''
    while True:
        deduct = int(input("\nThere are " + str(bean_pile) + " beans "
                           "remaining.\nYou must take at least one bean "
                           "but no more than three.\nHow many do you want "
                           "to take? "))
        if deduct > bean_pile:
            print("Invalid move. You can not take more beans "
                  "than what is left in the pot.\nTry again.")
        else:
            if deduct <= 3 and deduct > 0:
                return deduct
            else:
                print("Invalid move. Try again.")

# STILL NEED TO WRITE TEST SUITE...HOW TO ACCOUNT FOR RANDOM INT
def computer_deduct(bean_pile):
    ''' Name: computer_deduct
        Input: Number of beans remaining, int greater than 0
        Returns: Number of beans computer wishes to deduct (int)
    '''
    if bean_pile > 3:
        deduct = random.randint(1, 3)
    elif bean_pile == 3:
        deduct = 2
    else:
        deduct = 1
    return deduct
