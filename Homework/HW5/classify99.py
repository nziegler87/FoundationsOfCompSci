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

TOP_5 = 5

CHAR_99 = [["Jake", JAKE], ["Rosa", ROSA], ["Holt", HOLT], ["Gina", GINA]]
SHOW = "Brooklyn_99"

def main():
    # prompt user for selection and display quote
    while True:
        option = select_menu(SHOW)
        if option == QUIT:
            break
        test_quote = process_selection(option)
        print("\nI am trying to figure out who said:\n\n", test_quote, sep = "")
        
        # if exact match, print character name
        if compare_quotes(test_quote, CHAR_99):   
            character = compare_quotes(test_quote, CHAR_99)
            print("\nExact match found!", character, "said this.\n") 

        # if no exact match, analyze quote similarity and print results
        else:
            # generate nested list of each character name and top five words
            char_quotes = link_top_words(CHAR_99, STOPWORDS, TOP_5)

            # compare each character's top five words to quote and return results
            match_results = return_top_count(char_quotes, test_quote, STOPWORDS, TOP_5)
            results = return_match_results(match_results)

            # print top match or if zero match or tie, select at random
            if check_inconclusive(match_results):
                top_match = pick_random_character(match_results)
            else:
                top_match = name_person(match_results)

        print_results(results, top_match)
main()
