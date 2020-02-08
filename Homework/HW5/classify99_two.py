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
COUNT_LOCATION = 1
WORD_LOCATION = 0

CHAR_99 = [["Jake", JAKE], ["Rosa", ROSA], ["Holt", HOLT], ["Gina", GINA]]

def main():
##    while True:
##        selection = input("Hit enter to select an random quote.\n")
    for test_quote in TESTING:
##        test_quote = select_test_quote(TESTING)
        print("\nI am trying to figure out who said:\n  ", test_quote, sep = "")
        if compare_quotes(test_quote, CHAR_99):   
            character = compare_quotes(test_quote, CHAR_99)
            print("Exact match found! This was said by", character) 
        else:
            print("Exact match not found. Let me investigate further.")
            char_quotes = link_top_words(CHAR_99, STOPWORDS, TOP_5)
            print(char_quotes)
            match_results = return_top_count(char_quotes, test_quote, STOPWORDS, TOP_5)
            print(match_results)
            if check_inconclusive(match_results):
                print("Inconclusive result.")
            else:
                name = name_person(match_results)
                print("I think", name, "said this.")

            



            
                
            
main()
