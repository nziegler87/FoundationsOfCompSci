'''
    Nathanial Ziegler
    CS 5001
    February, 26 2020
    HW 6
    Description:
        Functions for Wheel of Fortune driver
    Consulted:

'''

PUZZLE_OPTIONS = "wof.txt"
TXT_EXT = ".txt"
MAX_TURNS = 5

from wof_functions import (choose_puzzle, make_blank_puzzle, print_puzzle,
                           print_game_results, collect_guess, update_puzzle,
                           collect_user_info, convert_to_filename,
                           display_menu, return_score, print_score,
                           print_remaining_turns, write_score, check_match)

MENU_LETTERS = ["G", "S"]
MENU_OPTIONS = ["Guess a Letter", "Solve"]


def main():

    # collect username/filename and display current score, if any
    username = collect_user_info()
    filename = convert_to_filename(username, TXT_EXT)
    score = return_score(filename)
    print_score(score)    

    # pick puzzle at random and display to user
    category, puzzle = choose_puzzle(PUZZLE_OPTIONS)
    print("Your puzzle category is:", category, "\n")
    computer_puzzle = list(puzzle)
    print(puzzle)                                           # REMOVE EVENTUALLY
    display_puzzle = make_blank_puzzle(computer_puzzle)
    print_puzzle(display_puzzle)

    # ask user for options
    turns = MAX_TURNS
    while turns > 0:
        choice = display_menu(MENU_LETTERS, MENU_OPTIONS)
        if choice == "G":
            guess = collect_guess()
            update_puzzle(guess, computer_puzzle, display_puzzle)
            print_puzzle(display_puzzle)
            turns -= 1
            print_remaining_turns(turns)
        else:
            break
    final_guess = input("Enter your final guess: ").upper()
    if check_match(final_guess, puzzle):
        score += 1
        print("That was correct! The game is now over and your score is saved.")
        write_score(filename, score)
    else:        
        print_game_results(final_guess, puzzle)

main()

