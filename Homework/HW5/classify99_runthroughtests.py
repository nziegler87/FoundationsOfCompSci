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

TOP_5 = 4
COUNT_LOCATION = 1
WORD_LOCATION = 0

CHAR_99 = [["Jake", JAKE], ["Rosa", ROSA], ["Holt", HOLT], ["Gina", GINA]]

def main():

    for test_quote in TESTING:
        print("\nI am trying to figure out who said:\n  ", test_quote, sep = "")
        if compare_quotes(test_quote, CHAR_99):   
            character = compare_quotes(test_quote, CHAR_99)
            print("Exact match found! This was said by", character) 
        else:
            print("Exact match not found. Let me investigate further.")
            char_quotes = link_top_words(CHAR_99, STOPWORDS, TOP_5)
            match_results = return_top_count(char_quotes, test_quote, STOPWORDS, TOP_5)
            results = return_match_results(match_results)
            if check_inconclusive(match_results):
                semirandom_char = pick_random_character(match_results)
                print("\nNo exact match. Words in common analysis:\n",
                      results, "Based on these results, I picked ",
                      semirandom_char, ".\n", sep = "")
            else:
                top_match = name_person(match_results)
                print("\nNo exact match. Words in comon analysis:\n",
                      results, "Based on these results, I picked ",
                     top_match, ".\n", sep = "") 

    print("\n----FOR REFERENCE, TOP WORDS----")
    char_quotes = link_top_words(CHAR_99, STOPWORDS, TOP_5)
    for quote in char_quotes:
        print(quote)


            
                
            
main()
