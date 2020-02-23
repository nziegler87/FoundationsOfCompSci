'''
    Nathanial Ziegler
    CS 5001
    February, 26 2020
    HW 6
    Description:
        Functions for Wheel of Fortune driver
    Consulted:
'''

from wof_functions import (choose_puzzle, make_blank_puzzle, print_puzzle,
                           print_game_results, collect_guess, update_puzzle,
                           collect_filename, display_menu, return_score,
                           print_score, print_remaining_turns, write_score,
                           check_match, process_guess)

PUZZLE_OPTIONS = "wof.txt"
TXT_EXT = ".txt"
MAX_TURNS = 5
MENU_LETTERS = ["G", "S"]
MENU_OPTIONS = ["Guess a Letter", "Solve"]


def main():
    # collect username/filename and display current score, if any
    filename = collect_filename(TXT_EXT)
    score = return_score(filename)
    print_score(score)    

    # pick puzzle at random and display category and blank puzzle
    category, puzzle = choose_puzzle(PUZZLE_OPTIONS)
    print("Your puzzle category is:", category, "\n")
    display_puzzle = make_blank_puzzle(puzzle)
    print(puzzle)
    print_puzzle(display_puzzle)

    # Gameplay where user has option to solve or guess with five turns
    turns = MAX_TURNS
    while turns > 0:
        choice = display_menu(MENU_LETTERS, MENU_OPTIONS)
        if choice == "G":
            turns = process_guess(puzzle, display_puzzle, turns)
        else:
            break

    # if all turns used or solve selected, compare final guess and save reults
    final_guess = input("Enter your final guess: ").upper()
    if check_match(final_guess, puzzle):
        score += 1
        write_score(filename, score)
    print_game_results(final_guess, puzzle, score)

main()
