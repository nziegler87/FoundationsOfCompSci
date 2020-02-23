'''
    Nathanial Ziegler
    CS 5001
    February, 26 2020
    HW 6
    Description:
        Functions for Wheel of Fortune driver
    Consulted:
'''

import time
from wof_functions import (choose_puzzle, make_blank_puzzle, print_puzzle,
                           print_game_results, collect_guess, update_puzzle,
                           collect_filename, display_menu, return_score,
                           print_score, print_remaining_turns, write_score,
                           check_match, process_guess, pre_solve)

PUZZLE_OPTIONS = "wof.txt"
TXT_EXT = ".txt"
REGULAR_TURNS = 5
BONUS_TURNS = 3
MENU_LETTERS = ["G", "S"]
MENU_OPTIONS = ["Guess a Letter", "Solve"]
BONUS_LETTERS = ["R", "S", "T", "L", "N", "E"]
BONUS_TIME = 20

def main():
    # collect filename, display current score, start with no bonus round
    filename = collect_filename(TXT_EXT)
    score = return_score(filename)
    print_score(score)
    bonus = "no"
    another_round = "yes"
    
    while another_round == "yes":
        another_round = "no"
        # pick puzzle at random and display category and blank puzzle
        category, puzzle = choose_puzzle(PUZZLE_OPTIONS)
        display_puzzle = make_blank_puzzle(puzzle)

        # set up game play if in regular or bonus round
        if bonus == "yes":
            pre_solve(display_puzzle, puzzle, BONUS_LETTERS)
            turns = BONUS_TURNS
            print("BONUS ROUND!!!\nIn this round, you only have three guesses, "
                  "afterwich you have only 20 seconds to guess the puzzle.")
        else:
            turns = REGULAR_TURNS

        # diplsay puzzle to user
        print("Your puzzle category is:", category, "\n")
        print(puzzle)                                                           # <<<<<< THIS NEEDS TO BE DELETED
        print_puzzle(display_puzzle)

        # game play where user guesses or solves based on turn # or selection
        while turns > 0:
            choice = display_menu(MENU_LETTERS, MENU_OPTIONS)
            if choice == "G":
                turns = process_guess(puzzle, display_puzzle, turns)
            else:
                break

        # if all turns used or solve selected, collect final guess
        if bonus == "yes":
            print("You have", BONUS_TIME, "seconds to enter "
                  "your guess...starting now.")
        start_time = time.time()
        final_guess = input("Enter your final guess: ").upper()
        end_time = time.time()
        total_time = end_time - start_time

        print(final_guess, puzzle)

        # check guess against puzzle and time to respond if in bonus round
        if bonus == "no":
            if check_match(final_guess, puzzle):
                score += 1
                bonus = "yes"
                another_round = "yes"
            print_game_results(final_guess, puzzle, score)
        else:
            if check_match(final_guess, puzzle) and total_time <= BONUS_TIME:
                score += 1
                print_game_results(final_guess, puzzle, score)
            else:
                print("I'm sorry, you ran out of time. It took you",
                      round(total_time), "seconds to respond.")
            
    write_score(filename, score)

main()
