'''
    Nathanial Ziegler
    CS 5001
    February 26, 2020
    HW 6
    Description:
        Simplified Wheel of Fortune functions
    Consulted:
        https://www.geeksforgeeks.org/python-string-rstrip/
        https://realpython.com/intro-to-python-threading/
'''
import random, string, time

#Constants
ZERO_SCORE = 0
EXCLUDE = list(string.digits + string.punctuation + string.whitespace)


def process_guess(puzzle, display_puzzle, turns):
    ''' Name: process_guess
        Parameters: current puzzle (str), display_puzzle (list of strings),
                    and turns (int)
        Returns: number of turns remaining (int)
    '''
    guess = collect_guess()
    update_puzzle(guess, puzzle, display_puzzle)
    print_puzzle(display_puzzle)
    turns -= 1
    print_remaining_turns(turns)
    return turns

def collect_user_info():
    ''' Name: collect_use_info
        Paramters: none
        Returns: first name of user, all lowercase, as string
    '''
    name = input("Enter your name to log in. No password needed!: ").lower()
    return name

def collect_filename(extension):
    ''' Name: convert_to_filename
        Parameters: filename extension as string e.g. ".txt"
        Returns: string with user's name and filename extension concatenated
    '''
    name = input("Enter your name to log in. No password needed!: ").lower()
    return (name + extension)

def print_score(score):
    ''' Name: print_score
        Parameters: current score, an int
        Returns: nothing
    '''
    if score == 1:
        print("So far, you have solved", score, "puzzle.")
    else:
        print("So far, you have solved", score, "puzzles.")

def display_menu(menu_letters, menu_options):
    ''' Name: display_menu
        Parameters: two lists of strings, identical in length -- one with
                    single letters and other with descriptor for each menu item
        Returns: user choice, a string, validated against menu_select
    '''
    while True:

        # print menu using menu_letters and menu_options
        for i in range(len(menu_letters)):
            print("     ", menu_letters[i], " -- ", menu_options[i], sep = "")

        # collect choice and validate against menu letters
        choice = input("Enter your selection: ").upper()
        if choice not in menu_letters:
            print("\nInvalid selection. Try again.")
            continue
        else:
            return choice

def write_score(filename, value):
    ''' Name: write_score
        Parameters: .txt file name, string: "name.txt" and score to write, int
        Returns: nothing
    '''
    with open(filename, "w") as outfile:
        _ = outfile.write(str(value))

def return_score(filename):
    ''' Name: return_score
        Parameters: file name (string) of .txt file, "name.txt", containing number
        Returns: contents of file or 0 if file doesn't exist, both int
    '''
    try:
        # open and return entire contents of file as one string
        with open(filename, "r") as infile:
            contents = int(infile.read())
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

def update_puzzle(character, master_string, user_list):
    ''' Name: update_puzzle
        Paramters: a character (str), a string & list of strings of same length
        Returns: nothing...modifies user_list in place
    '''
    # iterate through each item in master list
    for i in range(len(master_string)):

        # if character is equal to master_list value, change user_list
        if character == master_string[i]:
            user_list[i] = character

def print_puzzle(character_list):
    ''' Name: print_puzzle
        Parameters: list of characters
        Returns: string of characters
    '''
    # convert user list to string for return
    user_string = " ".join(character_list)
    print(user_string)

def check_match(master_string, user_string):
    ''' Name: check_match
        Parameters: two strings
        Returns: True if strings are identical
    '''
    if master_string == user_string:
        return True

def remove_last_char(string):
    ''' Name: remove_last_char
        Parameters: string of characters
        Returns: string with last charatcter removed
    '''
    return string[:-1]

def make_blank_puzzle(input_string):
    ''' Name: make_blank_puzzle
        Parameters: string of characters
        Returns: list where every non-space character is converedted to "_"
    '''
    blank_puzzle = []
    for i in  range(len(input_string)):

        # if value at position i is anything other than a space, insert "_"
        if input_string[i] not in EXCLUDE:
            blank_puzzle.append("_")

        # otherwise, insert a " "
        else:
            blank_puzzle.append(input_string[i])
            
    return blank_puzzle

def print_remaining_turns(count):
    ''' Name: print_remaining_turns
        Parameters: number of turns remaining, an int
        Returns: nothing
    '''
    if count > 1:
        print("You have", count, "turns remaining.")
    elif count > 0:
        print("You have", count, "turn remaining.")
    else:
        print("You are out of turns.")

def print_game_results(user_guess, computer_string, score):
    ''' Name: print_game_results
        Parameters: user_guess and computer_string (strings), running score, int
        Returns: nothing
    '''
    if user_guess == computer_string and score == 1:
        print("Congrats! You you have now solved", score, "puzzle!\n"
              "Your progress has been saved.")
    elif user_guess == computer_string and score == 0 or score > 1:
        print("Congrats! You have now solved", score, "puzzles!\n"
              "Your progress has been saved.")
    else:
        print("I'm sorry, that wasn't correct. Your puzzle was:\n",
              computer_string, sep = "")
        
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
