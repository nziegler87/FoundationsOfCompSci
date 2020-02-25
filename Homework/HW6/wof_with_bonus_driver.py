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
                           create_filename, display_menu, return_score,
                           print_score, print_remaining_turns, write_score,
                           check_match, process_guess, pre_solve, set_turns,
                           print_game_instructions, join_list, get_user_info,
                           collect_player_name, print_puzzle_info,
                           let_player_guess)

PUZZLE_OPTIONS = "wof.txt"

REGULAR_TURNS = 5
BONUS_TURNS = 3

BONUS_LETTERS = ["R", "S", "T", "L", "N", "E"]
BONUS_TIME = 20

def main():
    # collect filename, display current score, start with no bonus round
    filename, score = get_user_info()
    print_score(score)
    bonus = False
    another_round = True
    
    while another_round is True:
        # set up game play if in regular or bonus round
        turns = set_turns(bonus, REGULAR_TURNS, BONUS_TURNS)
        print_game_instructions(turns, bonus, BONUS_TIME, BONUS_LETTERS)
        another_round = False

        # pick random puzle, create blank puzzle, display to user
        category, puzzle = choose_puzzle(PUZZLE_OPTIONS)
        display_puzzle = make_blank_puzzle(puzzle)
        pre_solve(bonus, display_puzzle, puzzle, BONUS_LETTERS)
        print_puzzle_info(category, display_puzzle)

        # game play where user guesses or solves
        let_player_guess(turns, puzzle, display_puzzle)

        # if all turns used or solve selected, collect final guess
        if bonus is True:
            print("You have", BONUS_TIME, "seconds to enter "
                  "your guess, starting now.")
        start_time = time.time()
        final_guess = input("Enter your final guess: ").upper()
        end_time = time.time()
        total_time = end_time - start_time

        # check guess against puzzle and time to respond if in bonus round
        if bonus is False:
            if check_match(final_guess, puzzle):
                score += 1
                bonus = True
                another_round = True
            print_game_results(final_guess, puzzle, score)
        else:
            if check_match(final_guess, puzzle) and total_time <= BONUS_TIME:
                score += 1
                print_game_results(final_guess, puzzle, score)
            elif check_match(final_guess, puzzle) and total_time > BONUS_TIME:
                print("I'm sorry. That was correct but you ran out of time. "
                      "It took you you", round(total_time), "seconds to "
                      "respond.\n")
            else:
                print("I'm sorry that was not correct. Your puzzle was:\n",
                      puzzle, "\n", sep = "")
            
    write_score(filename, score)

main()
