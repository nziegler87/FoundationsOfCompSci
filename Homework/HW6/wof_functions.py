'''
    Nathanial Ziegler
    CS 5001
    February 26, 2020
    HW 6
    Description:
        Simplified Wheel of Fortune functions
    Consulted:
        https://www.geeksforgeeks.org/python-string-rstrip/
'''
import random

def read_file(

def choose_puzzle(text_file):
    ''' Name: choose_puzzle
        Parameters: name of plain txt file as string - "filename.txt"
        Returns: tuple with puzzle category and phrase line, both strings
    '''
    try:
        # open text file and create list of each line
        with open(text_file, "r") as infile:
            lines = infile.readlines()

            # return random line with \n character removed
            rand_line = random.choice(lines).rstrip("\n")

            # split line into list, so category and puzzle can be returned
            rand_list = rand_line.split(":")
            category = rand_list[0]
            puzzle = rand_list[1]
        return (category, puzzle)

    except OSError:
        print("File with gameplay options not found. Please save the wof.txt "
              "file in the same folder as this file and restart program.")
