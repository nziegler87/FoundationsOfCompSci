'''
    Nathanial Ziegler
    CS 5001
    February 11, 2020
    HW 5
    Description:
        UPDATE

    Consulted:
        https://www.programiz.com/python-programming/methods/list/sort
        https://thepythonguru.com/python-lambda-function/
        https://docs.python.org/3/howto/sorting.html
'''
from classify_data import *
import random

# DEBUGGING CONSTANTS
og_family = ["nate", "nick", "jim", "alison"]
extended_family = ["nate", "nick", "jim", "alison", "alison", "buddy",
                   "charlie", "nate", "nick", "lindsey", "lindsey", "wilma",
                   "wilma", "wilma", "wilma"]
count_list = [["nate", 1],["jim", 2]]
stop_words = ["buddy", "snoopy", "lindsey"]

CHAR_99 = [["Jake", JAKE], ["Rosa", ROSA], ["Holt", HOLT], ["Gina", GINA]]

def count_common_words(quote, quote_list):
    # split quotes into list of words and make all words lower-case
    quote_words = quote.split(" ")
    quote_words = convert_lower(quote_words)
    quote_list = split_quotes(quote_list)
    quote_list = convert_lower(quote_list)

    # iterate through words in quote and 
    count = 0
    for word in quote_words:
        if word in quote_list:
            count += 1
    return count

## STOPPED HERE - THIS FUNCTION SHOULD WORK BUT NEED TO COMPARE AGAINST
## TOP FIVE WORDS OF EACH CHARACTER, NOT THE ENTIRE THING
            
def compare_quotes(quote, character_list):
    ''' Name: compqre_quotes
        Input: quote (string) and nested list of characters and variable
               to list of their quotes (strings) formated like [["name", VAR]]
        Returns: name {string) of character who said quote, False if no match
    '''
    compare_quote = quote

    # iterate through number of characters in list
    for  char in range(len(character_list)):

        # iterate through total lines in each character's quote list
        for quote in range(len(character_list[char][1])):
            char_quote = character_list[char][1][quote]

            # if input quote = quote in charcter list, return name
            if compare_quote == char_quote:
                return character_list[char][0]

    # if quote does not appear in any character list, return False
    else:
        return False   

def select_test_quote(test_quotes):
    ''' Name: select_test_quote
        Inputs: list of quotes (strings)
        Returns: random quote from string
    '''
    random_quote = test_quotes[random.randint(0, (len(test_quotes) - 1))]

    return random_quote

def select_char_quote(character_list):
    ''' Name: select_char_quote
        Input: character names (strings) and variables associated with
               a list of quotes saved as global constants
        Returns: random quote (str) from random character quote list
    '''
    random_char = character_list[random.randint(0, (len(character_list) - 1))]
    # get character name from nested list
    
    char_name = random_char[0]

    # get character variable associated with global variable
    char_quotes = random_char[1]

    # pick random quote from character
    random_quote = char_quotes[random.randint(0, (len(char_quotes) - 1))]

    print(random_quote, "-", char_name)
##    return random_quote
    

def calculate_top_words(quote_list, stop_words, top_n,
                        count_location, word_location):
    ''' Name: calculate_top_words:
        Inputs: list of sentences (strings), list of stop words (strings),
                top_n..ex top 5..words to isolate (int), location of
                count number (int), location of word (int)
        Returns: top five words in list minus stop_words
    '''
    # split quote list into words
    word_list = split_quotes(quote_list)
    
    # convert all words to lower case
    word_list = convert_lower(word_list)
    
    # calculate frequency of each sord, minus stop_words, saved in nested list
    word_frequency = calculate_word_frequency(word_list, stop_words, word_location)
    
    # sorted_nested_list based on location of count in nested list
    top_count = sort_nested_list(word_frequency, count_location)
    
    # trim sorted list to top n (5 in this case)
    top_five = trim_list(top_count, top_n)
    
    # isolate words from nested list based on location of count
    top_five = isolate_nested_list(top_five, word_location)
    
    return top_five

def isolate_nested_list(nested_list, item_location):
    ''' Name: isolate_nested_list
        Inputs: nested list with format - [["string", int],["string",[int]]..,
                item_location in list to isolate (str)
        Returns: list of item n in each nested list
    '''
    culled_list = []

    # iterate through nested list, appending item at n location to new list
    for i in range(len(nested_list)):
        culled_list.append(nested_list[i][item_location])
    return culled_list

def trim_list(input_list, stop_n):
    ''' Name: trim_list
        Inputs: list of items, stop_n (int)
        Returns: list trimed to the n item
    '''
    trimmed_list = input_list

    # trim list at the nth item
    trimmed_list = trimmed_list[:stop_n]
    
    return trimmed_list

def sort_nested_list(words_counted_list, sort_location):
    ''' Name: sort_nested_list
        Inputs: nested list with format - [["string", int],["string",[int]]..,
                location of item in nested lists by which to sort
        Returns: nested list reverse sorted by nth item in each list
    '''
    top_count = words_counted_list
    top_count.sort(key = lambda item: item[sort_location], reverse = True)

    return top_count

def calculate_word_frequency(word_list, stop_words, word_location):
    ''' Name: calculate_word_frequency
        Input: List of strings
        Returns: nested list formated: [["string", int],["string",[int]],...
        Does: Counts frequency of word usage in word_list, excluding stop_words
    '''
    count_list = []
    
    # iterate through each word in list
    for word in word_list:
        
        # if word in stop_words list, skip
        if check_list(word, stop_words):
            continue
        
        # if this is first word to review, add it to count_list
        elif len(count_list) == 0:
            count_list = append_to_nested(count_list, word)
            
        # if word in count_list, increase frequency count of word by one
        elif check_nested_list(word, count_list, word_location):
            pos = search_nested_list(word, count_list, word_location)
            count_list[pos][1] += 1
            
        # if no previous conditions true, add word to list with count 1
        else:
            count_list = append_to_nested(count_list, word)

    return count_list

def append_to_nested(append_list, word):
    ''' Name: append_to_nested
        Input: list to append and word (string)
        Returns: nested list with item added
        Does: appens current word (string) with an initial frequency count of 1
    '''
    word_count = [word, 1]
    append_list.append(word_count)
    return append_list

def check_list(word, word_list):
    ''' Name: check_list
        Input: word (string) and list of words (strings)
        Returns: True if word is in word_list
    '''
    if word in word_list:
        return True

def check_nested_list(word, nested_list, word_location):
    ''' Name: check_nested_list
        Input: nested_list with structure - [["string", int],["string", int]],
               word (string)
        Returns: True if word is in list at n location
    '''
    # iterate through nested list and checks if word is in nested list 
    for i in range(len(nested_list)):
        if word in nested_list[i][word_location]:
            return True

def search_nested_list(word, nested_list, word_location):
    ''' Name: search_nested_list
        Input: nested_list with structure - [["string", int],["string", int]]..,
               word (string), location of word in nested list (int)
        Returns: index (int) of nested list in which item occurs
    '''
    # iterate over nested list, checking for word at n location in nested list
    for i in range(len(nested_list)):
        if word in nested_list[i][word_location]:
            pos = i
            return pos

def convert_lower(word_list):
    ''' Name: convert_lower
        Input: list of words (strings)
        Returns: list of words with all letters lowercase (strings)
    '''
    # iterate through list of words, converting each to lowercase
    lowercase_list = []
    for i in range(len(word_list)):
        lower_word = word_list[i].lower()
        lowercase_list.append(lower_word)

    return lowercase_list

def split_quotes(quote_list):
    ''' Name: split_quotes
        Input: list of sentences (strings)
        Returns: list of words (strings)
    '''
    # splits list of sentences into individual words
    word_list = []
    for i in range(len(quote_list)):
        single_line = quote_list[i].split(" ")
        word_list += single_line
    return word_list 

