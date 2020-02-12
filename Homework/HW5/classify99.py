'''
    Nathanial Ziegler
    CS 5001
    February 12, 2020
    HW 5
    Description:
        Program that either prompts user to entier a quote or selects a
        random quote by a Brooklyn 99 character. The quote is then compared
        to a list of preentered quotes by Jake, Rosa, Holt, and Gina.
        Analysis is done, comparing top five words from each character to words
        in quote. Character with highest match is announced. If no match or tie
        best match character is selected at random.
'''

from classify_data import *
from classify_functions import *

# characters and associated variables where quotes are saved
CHAR_99 = [["Jake", JAKE], ["Rosa", ROSA], ["Holt", HOLT], ["Gina", GINA]]

# name of show
SHOW = "Brooklyn_99"

def main():
    # prompt user for selection and display quote
    while True:
        option = select_menu(SHOW)
        if option == QUIT:
            break
        test_quote = process_selection(option)
        print("\nI am trying to figure out who said:\n\n", test_quote, sep = "")
        
        # if quote is exact match, print character name
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
