'''
    Nathanial Ziegler
    CS 5001
    January 29, 2020
    HW 3
    Description:
        Functions for nim -- coin_flip and is_over
'''

import random

##user_choice = input("Enter H for Heads or T for tales: ")
##toss_result = random.randint(1, 2)

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
        return False
    else:
        return True
    
    
