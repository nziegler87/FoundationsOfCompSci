'''
    Nathanial Ziegler
    CS 5001
    February 26, 2020
    HW 6
    Description:
        Simplified Wheel of Fortune functions
    Consulted:
        https://www.geeksforgeeks.org/python-string-rstrip/
        https://stackoverflow.com/questions/10166686/how-do-i-exit-program-in-try-except    
'''
import random, string, time, sys

TXT_EXT = ".txt"
MENU_LETTERS = ["G", "S"]
MENU_OPTIONS = ["Guess a Letter", "Solve"]
REGULAR_TURNS = 5
BONUS_TURNS = 3
PUZZLE_OPTIONS = "wof.txt"
BONUS_LETTERS = ["R", "S", "T", "L", "N", "E"]
BONUS_TIME = 20
ZERO_SCORE = 0
EXCLUDE = list(string.digits + string.punctuation + string.whitespace)
CENTER_WIDTH = 60

def print_game_instructions(turns, bonus_status):
    ''' Name: print_game_instructions
        Parameters: number of turns and number of seconds in bonus
                    round, both ints
        Returns: nothing
    '''
    bonus_string = join_list(BONUS_LETTERS)
    if bonus_status is True:
        print("BONUS ROUND".center(CENTER_WIDTH, "-"), "\nIn this round, we "
              "have again selected a random puzzle for you to solve. This "
              "time, however, we have pre-filled the letters ", bonus_string,
              ". You have ", turns, " tries to guess letters in the puzzle. "
              "For this round, when it is time to solve the puzzle, "
              "you have only ", BONUS_TIME, " seconds to guess the correct "
              "answer. If you guess the correct phrase but take more than the "
              "allotted amount of time, you lose.\n", sep = "")
 
    else:
        print("Welcome to the Wheel of Fortune! We have selected a random "
              "puzzle for you to solve. You have", turns, "tries "
              "to guess letters that you think may be in the puzzle. "
              "Correct guess will be reflected on the screen. "
              "At any point, you may attempt to solve the puzzle. You "
              "only have one attempt to guess the full puzzle. If you "
              "run out of turns, you will have one try to solve the puzzle.\n")
              
def join_list(input_list):
    ''' Name: join_list
        Parameters: list of items (int or str) to be joined in series
        Returns: string with items joined with ", " and ", and" for last item
    '''
    output_string = ""
    for i in range(len(input_list)):
        if i == len(input_list) - 2:
            output_string += input_list[i] + ", and "
        elif i == len(input_list) - 1:
            output_string += input_list[i]
        else:
            output_string += input_list[i] + ", "
    return output_string

def collect_player_name():
    ''' Name: collect_player_name
        Parameters: nothing
        Returns: name of player as a lower-case string
    '''
    name = input("Enter your name to log in: ").lower()
    return name

def create_filename(extension):
    ''' Name: convert_to_filename
        Parameters: filename extension (ie ".txt") as string
        Returns: string with user's name and filename extension concatenated
    '''
    name = collect_player_name()
    return (name + extension)

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

def get_user_info():
    ''' Name: get_user_info
        Parameters: nothing
        Returns: tiple with filename of user (string) as first value
                 and their current score (int) as second value
    '''
    filename = create_filename(TXT_EXT)
    score = return_score(filename)
    return (filename, score)

def print_score(score):
    ''' Name: print_score
        Parameters: current score, an int
        Returns: nothing
    '''
    if score == 1:
        print("\nSo far, you have solved", score, "puzzle.\n")
    else:
        print("\nSo far, you have solved", score, "puzzles.\n")

def choose_puzzle():
    ''' Name: choose_puzzle
        Parameters: none
        Returns: tuple with puzzle category and phrase line, both strings
    '''
    try:
        # open text file and create list of each line
        with open(PUZZLE_OPTIONS, "r") as infile:
            lines = infile.readlines()

            # return random line with \n character removed
            rand_line = remove_last_char(random.choice(lines))

            # split line into list, so category and puzzle can be returned
            rand_list = rand_line.split(":")
            category = rand_list[0]
            puzzle = rand_list[1]
        return (category, puzzle)

    except OSError:
        sys.exit("Game options file not found. Please save wof.txt "
                 "in the same folder as this file and the restart program.")

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

def set_turns(bonus_status):
    ''' Name: set_turns
        Parameters: bonus, a boolean. True if activated, else false
        Returns: number of turns, an int
    '''
    if bonus_status is True:
        turns = BONUS_TURNS
    else:
        turns = REGULAR_TURNS
    return turns

def pre_solve(bonus_status, user_puzzle, master_string):
    ''' Name: pre_solve
        Parameters: list of characters to presolve puzzle - a string & list
                    of strings of the same length and bonus status, boolean
        Returns: Nothing...modifies list in place
    '''
    if bonus_status is True:
        # iterate through each item in master string
        for i in range(len(master_string)):

            # if character is in letters_list, update user_list
            if master_string[i] in BONUS_LETTERS:
                user_puzzle[i] = master_string[i]

def print_puzzle_info(category, puzzle_list):
    ''' Name: print_puzzle_info
        Parameters: puzzle category (string) list of puzzle characters
        Returns: nothing
    '''
    print("Your puzzle category is:", category)
    print_puzzle(puzzle_list)

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

def let_player_guess(turns, puzzle, display_puzzle):
    ''' Name: let_play_guess
        Parameters: number of turns (int), correct puzzle (string),
                    list of characters for display_puzzle
        Returns: nothing
    '''
    while turns > 0:
        choice = display_menu(MENU_LETTERS, MENU_OPTIONS)
        if choice == "G":
            turns = process_guess(puzzle, display_puzzle, turns)
        else:
            break

def collect_guess():
    ''' Name: collect_guess
        Parameters: none
        Returns: a single character, a string
    '''
    guess = input("Enter your guess: ").upper()
    if len(guess) > 1:
        guess = input("You can only guess one character at a time. "
                      "Try again: ").upper()
    else:
        return guess

def update_puzzle(character, master_string, user_list):
    ''' Name: update_puzzle
        Paramters: a character (str), a string & list of strings of same length
        Returns: nothing...modifies user_list in place
    '''
    # iterate through each item in master string
    for i in range(len(master_string)):

        # if character is equal to master_string value, change user_list
        if character == master_string[i]:
            user_list[i] = character

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

def print_puzzle(character_list):
    ''' Name: print_puzzle
        Parameters: list of characters
        Returns: nothing
    '''
    # convert user list to string for return
    user_string = " ".join(character_list)
    print("\n", user_string, "\n", sep = "")

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

def check_match(master_string, user_string):
    ''' Name: check_match
        Parameters: two strings
        Returns: True if strings are identical
    '''
    if master_string == user_string:
        return True

def calculate_time_elapsed(start_time, end_time):
    ''' Name: calculate_time_elapsed
        Parameters: start time and end time (floats)
        Returns: time elapsed, float
    '''
    return end_time - start_time

def collect_final_guess(bonus):
    ''' Name: collect_final_guess
        Parameters: a boolean indicating if bonus round is active
        Returns: user guess and time it took to respond as tupil
    '''
    if bonus is True:
        print("You have", BONUS_TIME, "seconds to enter "
                  "your guess, starting now.")
    start_time = time.time()
    final_guess = input("Enter your final guess: ").upper()
    end_time = time.time()
    total_time = calculate_time_elapsed(start_time, end_time)
    return (final_guess, total_time)

def print_regular_results(user_guess, computer_string, score):
    ''' Name: print_regular_results
        Parameters: user_guess and computer_string (strs), running score (int)
        Returns: nothing
    '''
    if user_guess == computer_string and score == 1:
            print("\nCongrats! You you have now solved", score, "puzzle!\n")
    elif user_guess == computer_string and score != 1:
        print("\nCongrats! You have now solved", score, "puzzles!\n")
    else:
        print("\nI'm sorry, that wasn't correct. Your puzzle was:\n",
              computer_string, "\n", sep = "")

def print_bonus_results(bonus, total_time, user_guess, computer_string, score):
    ''' Name: print_bonus_results
        Parameters: bonus status, a boolean, response time (float),
                    user_guess and computer_string (strs), running score (int)
        Returns: nothing
    '''
    if check_match(user_guess, computer_string) and total_time <= BONUS_TIME:
        if user_guess == computer_string and score == 1:
            print("\nCongrats! You you have now solved", score, "puzzle!\n")
        elif user_guess == computer_string and score != 1:
            print("\nCongrats! You have now solved", score, "puzzles!\n")
    elif check_match(user_guess, computer_string) and total_time > BONUS_TIME:
        print("I'm sorry. That was correct but you ran out of time. "
              "It took you you", round(total_time, 2), "seconds to "
              "respond.\n")
    else:
        print("I'm sorry that was not correct. Your puzzle was:\n",
                  computer_string, "\n", sep = "")

def print_game_results(bonus, total_time, user_guess, computer_string, score):
    ''' Name: print_game_results
        Parameters: bonus status, a boolean, response time (float),
                    user_guess and computer_string (strs), running score (int)
        Returns: nothing
    '''
    if bonus is False:
        print_regular_results(user_guess, computer_string, score)
    else:
        print_bonus_results(bonus, total_time, user_guess, computer_string,
                            score)

def flip_boolean(boolean_a):
    ''' Name: flip_boolean
        Parameter: a boolean
        Returns: returns boolean with value flipped
    '''
    boolean_a = not boolean_a
    return boolean_a

def update_score(bonus, score, user_string, master_string, total_time):
    ''' Name: update_score
        Inputs: bonus status, a boolean, user_string and master_string,
                and total time it took user to respond (float)
        Returns: updated score (int)
    '''
    if bonus is False:
        if check_match(user_string, master_string):
            score += 1
    else:
        if check_match(user_string, master_string) and total_time <= BONUS_TIME:
            score += 1

    return score

def update_continue_status(bonus, another_round, user_string, master_string,
                           total_time):
    if bonus is False and user_string == master_string:
        bonus = True
        another_round = True
    else:
        bonus = False
        another_round = False

    return bonus, another_round

def write_score(filename, value):
    ''' Name: write_score
        Parameters: .txt file name, string: "name.txt" and score to write, int
        Returns: nothing
    '''
    try:
        with open(filename, "w") as outfile:
            _ = outfile.write(str(value))
        print("Your progress has been saved.\n")
    except:
        print("I'm sorry, your progress cannot be saved at this time. "
              "Please try again later.\n")
