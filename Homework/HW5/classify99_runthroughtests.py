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
            if check_inconclusive(match_results):
                results = return_match_results(match_results)
                random_char = pick_random_character(match_results)
                print("There were", results, "Of the highest matches, "
                      "I picked", random_char)
            else:
                name = name_person(match_results)
                print("Based on my word analysis, I think", name, "said this.")

    print("\n----FOR REFERENCE, TOP WORDS----")
    char_quotes = link_top_words(CHAR_99, STOPWORDS, TOP_5)
    for quote in char_quotes:
        print(quote)


            
                
            
main()
