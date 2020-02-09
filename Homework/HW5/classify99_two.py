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
    # prompt user for selection
    while True:
        option = select_menu(SHOW)
        if option == QUIT:
            break
        elif option == RANDOM_QUOTE:
            test_quote = select_test_quote(TESTING)
        elif option == OWN_QUOTE:
            test_quote = input("Enter your own quote, without any punctuation: ")
        print("\nI am trying to figure out who said:\n\n", test_quote, sep = "")

        # if there is an exact match print character name
        if compare_quotes(test_quote, CHAR_99):   
            character = compare_quotes(test_quote, CHAR_99)
            print("\nExact match found!", character, "said this.\n") 

        # if not exact match, check frequeny of each user's top words in quote
        else:
            char_quotes = link_top_words(CHAR_99, STOPWORDS, TOP_5)
            match_results = return_top_count(char_quotes, test_quote, STOPWORDS, TOP_5)
            results = return_match_results(match_results)

            # if zero match or tie between characters, pick at random
            if check_inconclusive(match_results):
                semirandom_char = pick_random_character(match_results)
                print("\nThere isn't an exact match. However, there were ",
                      results, " Based on these results, I picked ",
                      semirandom_char, ".\n", sep = "")

            # if one character has clear match based on count
            else:
                top_match = name_person(match_results)
                print("\nThere isn't an exact match. However, there were ",
                      results, " Based on these results, I picked ",
                     top_match, ".\n", sep = "")              
main()
