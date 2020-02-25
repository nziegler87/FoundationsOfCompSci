'''
    Nathanial Ziegler
    CS 5001
    February, 26 2020
    HW 6
    Description:
        Driver for simplified Wheel of Fortune game.
'''

import time
from wof_functions import (choose_puzzle, make_blank_puzzle, print_puzzle,
                           print_game_results, collect_guess, update_puzzle,
                           create_filename, display_menu, return_score,
                           print_score, print_remaining_turns, write_score,
                           check_match, process_guess, pre_solve, set_turns,
                           print_game_instructions, join_list, get_user_info,
                           collect_player_name, print_puzzle_info,
                           let_player_guess, collect_final_guess,
                           print_game_results, update_score, flip_boolean,
                           update_continue_status)

def main():
    # collect filename, display current score, start with no bonus round
    filename, score = get_user_info()
    print_score(score)
    bonus = False
    another_round = True
    
    while another_round is True:
        # set number of turns and display instructions based on bonus status
        turns = set_turns(bonus)
        print_game_instructions(turns, bonus)

        # pick random puzle, create blank puzzle, display to user
        category, puzzle = choose_puzzle()
        display_puzzle = make_blank_puzzle(puzzle)
        pre_solve(bonus, display_puzzle, puzzle)
        print_puzzle_info(category, display_puzzle)

        # game play where user guesses or solves
        let_player_guess(turns, puzzle, display_puzzle)

        # process final guess - update score, game play, and print results
        final_guess, total_time = collect_final_guess(bonus)
        score = update_score(bonus, score, final_guess, puzzle, total_time)
        print_game_results(bonus, total_time, final_guess, puzzle, score)
        bonus, another_round = update_continue_status(bonus, another_round,
                                                      final_guess, puzzle,
                                                      total_time)
        # write score after each round
        write_score(filename, score)

main()
