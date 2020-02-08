'''
    Nathanial Ziegler
    CS 5001
    February 11, 2020
    HW 5
    Description:
        UPDATE
'''

from classify_data import *
from classify_functions import *

TOP_N = 5
COUNT_LOCATION = 1
WORD_LOCATION = 0

CHAR_99 = [["Jake", JAKE], ["Rosa", ROSA], ["Holt", HOLT], ["Gina", GINA]]

def main():
    selection = input("Hit enter to select an random quote.\n")
    test_quote = select_test_quote(TESTING)
    if compare_quotes(test_quote, CHAR_99):   
        character = compare_quotes(test_quote, CHAR_99)
        print("This was said by", character) 
    else:
        print("Quote not found")

main()
