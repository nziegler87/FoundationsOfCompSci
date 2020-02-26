'''
    Nathanial Ziegler
    CS 5001
    February, 26 2020
    HW 6
    Description:
        Driver for simplified Wheel of Fortune game.
'''

import time
from wof_functions import *

def main():
    # collect user info, display their stats, and start with no bonus round
    filename, score = get_user_info()
    print_score(score)
    bonus = False
    another_round = True
    
    while another_round is True:
        # based on bonus status, set number of turns and display instructions
        turns = set_turns(bonus)
        print_game_instructions(turns, bonus)

        # pick random puzzle, create blank puzzle for guessing,
        # presolve if in bonus round, and display blank puzzle to user
        category, puzzle = choose_puzzle()
        display_puzzle = make_blank_puzzle(puzzle)
        pre_solve(bonus, display_puzzle, puzzle)
        print_puzzle_info(category, display_puzzle)

        # game play where user selects guess or solve or runs out of turns
        let_player_guess(turns, puzzle, display_puzzle)

        # ask final guess, update score, print results, update next round/bonus 
        final_guess, total_time = collect_final_guess(bonus)
        score = update_score(bonus, score, final_guess, puzzle, total_time)
        print_game_results(bonus, total_time, final_guess, puzzle, score)
        bonus, another_round = update_continue_status(bonus, another_round,
                                                      final_guess, puzzle,
                                                      total_time)
        # write score after each round
        write_score(filename, score)

    print("Game Over. Thank you for playing")

main()
