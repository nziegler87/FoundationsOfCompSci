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

from wof_functions import choose_puzzle, make_blank_puzzle, print_puzzle, print_game_results, collect_guess, update_puzzle


def main():

    category, puzzle = choose_puzzle(PUZZLE_OPTIONS)
    print("Your puzzle category is:", category, "\n")
    computer_puzzle = list(puzzle)
    display_puzzle = make_blank_puzzle(puzzle)
    print_puzzle(display_puzzle)

    print(puzzle)

    guess = collect_guess()

    update_puzzle(guess, computer_puzzle, display_puzzle)
    print_puzzle(display_puzzle)

    final_guess = input("Enter your final guess: ").upper()
    print_game_results(final_guess, puzzle)
    
main()

