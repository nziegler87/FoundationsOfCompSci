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

from wof_functions import choose_puzzle

def main():
    category, puzzle = choose_puzzle(PUZZLE_OPTIONS)    

main()

