'''
    Nathanial Ziegler
    CS 5001
    February 26, 2020
    HW 6
    Description:
        Simplified Wheel of Fortune functions
    Consulted:
        https://www.geeksforgeeks.org/python-string-rstrip/
'''
import random, string

#Constants
ZERO_SCORE = "0"
EXCLUDE = list(string.digits + string.punctuation + string.whitespace)

def read_file(filename):
    ''' Name: read_file
        Parameters: file name (string) of .txt file, "name.txt", containing number
        Returns: contents of file
    '''
    try:
        # open and return entire contents of file as one string
        with open(filename, "r") as infile:
            contents = infile.read()
        return contents

        # if file doesn't exist, return ZERO_SCORE value
    except OSError:
        return ZERO_SCORE

def choose_puzzle(text_file):
    ''' Name: choose_puzzle
        Parameters: name of plain txt file as string - "filename.txt"
        Returns: tuple with puzzle category and phrase line, both strings
    '''
    try:
        # open text file and create list of each line
        with open(text_file, "r") as infile:
            lines = infile.readlines()

            # return random line with \n character removed
            rand_line = remove_last_char(random.choice(lines))

            # split line into list, so category and puzzle can be returned
            rand_list = rand_line.split(":")
            category = rand_list[0]
            puzzle = rand_list[1]
        return (category, puzzle)

    except OSError:
        print("File with gameplay options not found. Please save the wof.txt "
              "file in the same folder as this file and restart program.")

def update_puzzle(character, master_list, user_list):
    ''' Name: update_puzzle
        Paramters: a character (str) and two lists of strings, identical length
        Returns: nothing...modifies user_list in place
    '''
    # iterate through each item in master list
    for i in range(len(master_list)):

        # if character is equal to master_list value, change user_list
        if character == master_list[i]:
            user_list[i] = character

def print_puzzle(character_list):
    ''' Name: print_puzzle
        Parameters: list of characters
        Returns: string of characters
    '''
    # convert user list to string for return
    user_string = " ".join(character_list)
    print(user_string)

def check_match(master_list, user_list):
    ''' Name: check_match
        Parameters: two lists of strings, identical in length
        Returns: True if lists are identical
    '''
    if master_list == user_list:
        return True

def remove_last_char(string):
    ''' Name: remove_last_char
        Parameters: string of characters
        Returns: string with last charatcter removed
    '''
    return string[:-1]

def make_blank_puzzle(input_list):
    ''' Name: make_blank_puzzle
        Parameters: list of characters
        Returns: list where every non-space character is converedted to "_"
    '''
    blank_puzzle = []
    for i in  range(len(input_list)):

        # if value at position i is anything other than a space, insert "_"
        if input_list[i] not in EXCLUDE:
            blank_puzzle.append("_")

        # otherwise, insert a " "
        else:
            blank_puzzle.append(input_list[i])
    return blank_puzzle

def print_game_results(user_guess, computer_string):
    ''' Name: print_game_results
        Parameters: two strings
        Returns: nothing
    '''
    if user_guess == computer_string:
        print("Congrats! You solved the puzzle.")
    else:
        print(":( No such luck for you.")
        
def collect_guess():
    ''' Name: collect_guess
        Parameters: none
        Returns: a single character, a string
    '''
    guess = input("Enter your guess: ").upper()
    if len(guess) > 1:
        guess = input("You can only guess one character at a time."
                      "Try again: ").upper()
    else:
        return guess
