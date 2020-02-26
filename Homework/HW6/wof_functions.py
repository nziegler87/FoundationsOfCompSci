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

# CONSTANT FOR TXT FILE EXTENSION AND PUZZLE TEXT FILE
TXT_EXT = ".txt"
PUZZLE_OPTIONS = "wof.txt"

# CONSTANTS FOR MENU SELECTION
MENU_LETTERS = ["G", "S"]
GUESS = "G"
MENU_OPTIONS = ["Guess a Letter", "Solve"]

# CONSTANTS 
REGULAR_TURNS = 5
BONUS_TURNS = 3
BONUS_TIME = 20

BONUS_LETTERS = ["R", "S", "T", "L", "N", "E"]

ZERO_SCORE = 0
EXCLUDE = list(string.digits + string.punctuation + string.whitespace)
CENTER_WIDTH = 60

def print_game_instructions(turns, bonus_status):
    ''' Name: print_game_instructions
        Parameters: number of turns and number of seconds in bonus
                    round, both ints
        Returns: nothing
    '''
    # join bonus letters list for prnting in bonus round instructions
    bonus_string = join_list(BONUS_LETTERS)

    # print instructions for either regular or bonus play
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
        Returns: a string of list items joined together
    '''

    # make blank output string
    output_string = ""

    # iterate through each item in input_list
    for i in range(len(input_list)):

        # if second to last item in list, join with ", and "
        if i == len(input_list) - 2:
            output_string += input_list[i] + ", and "

        # if last item in list, do not add joining text
        elif i == len(input_list) - 1:
            output_string += input_list[i]
        else:

        # if any other item in list, join with ", "
            output_string += input_list[i] + ", "

    return output_string

def collect_player_name():
    ''' Name: collect_player_name
        Parameters: nothing
        Returns: name of player as a lower-case string
    '''

    # collect player name in lowercase letters
    name = input("Enter your name to log in: ").lower()

    return name

def create_filename(extension):
    ''' Name: create_filename
        Parameters: filename extension (ie ".txt") as string
        Returns: string with user's name and filename extension concatenated
    '''
    name = collect_player_name()
    
    return (name + extension)

def return_score(filename):
    ''' Name: return_score
        Parameters: filename (string) of .txt file, "name.txt"
                    containing only a number
        Returns: contents of file or 0 if file doesn't exist, both int
    '''
    # open and return entire contents of file as one string
    try:
        with open(filename, "r") as infile:
            contents = infile.read()
            
        # return number in file, converted from string to int
        return int(contents)

    # if file doesn't exist, return ZERO_SCORE value
    except OSError:
        return ZERO_SCORE

def get_user_info():
    ''' Name: get_user_info
        Parameters: nothing
        Returns: tuple with filename of user (string) as first value
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
    # if score is 1, puzzle should be singular; else plural
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

    # if file cannot be open, use sys.exit to end program
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

    # iterate through each value in input string of characters
    for i in range(len(input_string)):

        # if i is a character other than punctuation or a space, append "_"
        if input_string[i] not in EXCLUDE:
            blank_puzzle.append("_")

        # otherwise, insert value of i
        else:
            blank_puzzle.append(input_string[i])
            
    return blank_puzzle

def set_turns(bonus):
    ''' Name: set_turns
        Parameters: bonus (boolean) where True if activated, else False
        Returns: number of turns user has, an int
    '''
    if bonus is True:
        turns = BONUS_TURNS
    else:
        turns = REGULAR_TURNS

    return turns

def pre_solve(bonus, user_puzzle, master_string):
    ''' Name: pre_solve
        Parameters: bonus state (a boolean), puzzle that user is trying to
                    solve (string of characters), and master_string or
                    the computer-generated puzzle user is trying to guess
        Returns: Nothing; modifies list in place
    '''
    if bonus is True:
        # iterate through each item in master string
        for i in range(len(master_string)):

            # if character is in BONUS_LETTERS, update user_list
            if master_string[i] in BONUS_LETTERS:
                user_puzzle[i] = master_string[i]

def print_puzzle_info(category, puzzle_list):
    ''' Name: print_puzzle_info
        Parameters: puzzle category, string, and list of puzzle characters
        Returns: nothing
    '''
    print("Your puzzle category is:", category)
    print_puzzle(puzzle_list)

def display_menu(menu_letters, menu_options):
    ''' Name: display_menu
        Parameters: two lists of strings, identical in length -- one with
                    single letters and other with descriptor for each menu item
        Returns: user choice, a string, validated against menu_letters
    '''
    while True:
        
        # print menu using menu_letters and menu_options
        for i in range(len(menu_letters)):
            print("     ", menu_letters[i], " -- ", menu_options[i], sep = "")

        # collect choice and validate against menu_letters
        choice = input("Enter your selection: ").upper()
        if choice not in menu_letters:
            print("\nInvalid selection. Try again.")
            continue

        else:
            return choice

def let_player_guess(turns, puzzle, display_puzzle):
    ''' Name: let_player_guess
        Parameters: number of turns (int), correct puzzle (string),
                    list of characters for display_puzzle
        Returns: nothing
    '''
    # allow user to guess while they still have turns available
    while turns > 0:

        # collect choice from user using display_menu function
        choice = display_menu(MENU_LETTERS, MENU_OPTIONS)

        # if user selects guess, update puzzle they are solving and reduce turns
        if choice == GUESS:
            turns = process_guess(puzzle, display_puzzle, turns)

        # if they run out of turns or select solve, break loop
        else:
            break

def collect_guess():
    ''' Name: collect_guess
        Parameters: none
        Returns: a single character, a string
    '''
    guess = input("Enter your guess: ").upper()

    # validate so they only enter one character
    while True:
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
    # iterate through each item in master string, or computer-generated puzzle
    for i in range(len(master_string)):

        # if character is equal to master_string value, change user_list
        if character == master_string[i]:
            user_list[i] = character

def print_remaining_turns(count):
    ''' Name: print_remaining_turns
        Parameters: number of turns remaining, an int
        Returns: nothing
    '''
    # check if turns should be printed as singular or plural
    if count > 1:
        print("You have", count, "turns remaining.")
    elif count > 0:
        print("You have", count, "turn remaining.")

    # let user know they are out of turns
    else:
        print("You are out of turns.")

def print_puzzle(character_list):
    ''' Name: print_puzzle
        Parameters: list of characters
        Returns: nothing
    '''
    # convert user list to string and then print
    user_string = " ".join(character_list)
    print("\n", user_string, "\n", sep = "")

def process_guess(master_string, display_puzzle, turns):
    ''' Name: process_guess
        Parameters: master_string or computer selected puzzle (str),
                    display_puzzle (list of strings), and turns (int)
        Returns: number of turns remaining (int)
    '''
    # use collect_guess function to collect guess
    guess = collect_guess()

    # update list of strings user is trying to fill in with guess and print
    update_puzzle(guess, master_string, display_puzzle)
    print_puzzle(display_puzzle)

    # decrease turns and print number of turns left
    turns -= 1
    print_remaining_turns(turns)

    # return value of turns
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
        Returns: user guess (str) and time (int) for user to respond as tuple
    '''
    # if bonus is active, let user know how many seconds they have to solve
    if bonus is True:
        print("You have", BONUS_TIME, "seconds to enter "
                  "your guess, starting now.")

    # capture start time
    start_time = time.time()

    # collect user guess in uppercase
    final_guess = input("Enter your final guess: ").upper()

    # capture end time
    end_time = time.time()

    # calculate total time it took user to respond
    total_time = calculate_time_elapsed(start_time, end_time)
    
    return (final_guess, total_time)

def print_regular_results(user_guess, master_string, score):
    ''' Name: print_regular_results
        Parameters: user_guess and master_string (strs), running score (int)
        Returns: nothing
    '''
    # print congrats message with correct plural/nonplural of puzzles
    if check_match(user_guess, master_string) and score == 1:
            print("\nCongrats! You you have now solved", score, "puzzle!\n")
    elif check_match(user_guess, master_string) and score != 1:
        print("\nCongrats! You have now solved", score, "puzzles!\n")

    # if guess does not match, display user the string
    else:
        print("\nI'm sorry, that wasn't correct. Your puzzle was:\n",
              master_string, "\n", sep = "")

def print_bonus_results(bonus, total_time, user_guess, master_string, score):
    ''' Name: print_bonus_results
        Parameters: bonus status, a boolean, response time (float),
                    user_guess and master_string (strs), running score (int)
        Returns: nothing
    '''
    # if guess is correct and less than time alloted display congrats
    if check_match(user_guess, master_string) and total_time <= BONUS_TIME:
        print_regular_results(user_guess, master_string, score)

    # if match was correct but they used too much time, display message
    elif check_match(user_guess, master_string) and total_time > BONUS_TIME:
        print("I'm sorry. That was correct but you ran out of time. "
              "It took you you", round(total_time, 2), "seconds to "
              "respond.\n")

    # if guess was incorrect, display correct string
    else:
        print("I'm sorry that was not correct. Your puzzle was:\n",
                  master_string, "\n", sep = "")

def print_game_results(bonus, total_time, user_guess, master_string, score):
    ''' Name: print_game_results
        Parameters: bonus status, a boolean, response time (float),
                    user_guess and master_string (strs), running score (int)
        Returns: nothing
    '''
    # if bonus is not activated, call print_regular_results
    if bonus is False:
        print_regular_results(user_guess, master_string, score)

    # if bonus is activated, call print_bonus_results
    else:
        print_bonus_results(bonus, total_time, user_guess, master_string,
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
    # if bonus is not activated, simply compare scores and update score
    if bonus is False:
        if check_match(user_string, master_string):
            score += 1

    # if in bonus round, factor in time it took for user to respond
    else:
        if check_match(user_string, master_string) and total_time <= BONUS_TIME:
            score += 1

    return score

def update_continue_status(bonus, another_round, user_string, master_string,
                           total_time):
    ''' Name: update_continue_status
        Parameters: bonus and another_round statuses (booleans), user_string
                    (a string of their guess), master_string (string of
                    random puzzle) and total time to respond (float)
        Returns: status of bonus and another_round booleans as a tuple
    '''
    # if not a bonus round and guess is correct, allow next turn as bonus round
    if bonus is False and user_string == master_string:
        bonus = True
        another_round = True

    # If guess is wrong or already completed bonus round, do not allow continue
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
