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

        test_quote = select_test_quote(TESTING)
        character = compare_quotes(test_quote, CHAR_99)
        
##    for char in CHAR_99:
##        top_words = calculate_top_words(char[1], STOPWORDS, TOP_N,
##                                        COUNT_LOCATION, WORD_LOCATION)
##        print(char[0], "'s top words were: ", top_words, sep = "")

main()
