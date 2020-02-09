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


CHAR_99 = [["Jake", JAKE], ["Rosa", ROSA], ["Holt", HOLT], ["Gina", GINA]]

OWN_QUOTE = "A"
RANDOM_QUOTE = "B"
QUIT = "C"

ABBREVS = ["A", "B", "C"]
OPTIONS = ["Type in my own quote", "Select a quote at random", "Quit"]

# RESEARCH GETTING RID OF APPEND FUNCTION
# RESEARCH INCORPORATING COUNT FUNCTION

def select_menu(show_name):
    ''' Name: select_menu
        Inputs: show_name as string
        Returns: A letter, a validated option
    '''
    print("Welcome to", show_name, "AI. I will use my wealth of knowledge to "
          "guess which character from", show_name, "said a quote that either "
          "you enter or that I select at random. You can select from the "
          "following options:")
    for i in range(len(ABBREVS)):
        print("\t", ABBREVS[i], ": ", OPTIONS[i], sep = "")
    choice = input("\nEnter your selection: ")
    while choice.upper() not in ABBREVS:
        choice = input("Invalid option. Enter your selection: ")
    return choice.upper()

def pick_random_character(match_results):
    ''' Name: pick_random_character
        Input: nested list of match results [["name", 0],["name", 0]]
        Returns: randomly selected character
    '''
    # if results are inconclusive because zero word match, pick any character
    if check_zero_sum(match_results):
        characters = isolate_nested_list(match_results, 0)
        character = characters[random.randint(0, len(characters) - 1)]

    # determine characters with top word matches and randomly select one
    else:
        characters = []
        scores = isolate_nested_list(match_results, 1)
        max_count = max(scores)
        for character in match_results:
            if character[1] == max_count:
                character_name = character[0]
                characters.append(character_name)
        character = random.choice(characters)

    return character

def name_person(match_results):
    ''' Name: name_person
        Input: match_results
        Returns: name "string" of person in match_reults with highest match
    '''
    # sort results from greatest to least
    name = sort_nested_list(match_results)

    # trim results to top match
    name = trim_list(name, 1)

    # isolate name from nested results list
    name = isolate_nested_list(name, 0)
    name = name[0]
    
    return name

def return_match_results(match_list):
    ''' Name: return_match_results
        Input: nested list of match results [["name", 0],["name", 0]]
        Returns: UPDATE
    '''
    string = ""
    for i in range(len(match_list)):
        if i == len(match_list) - 1:
            string += "and " + str(match_list[i][1]) + \
                      " word(s) in common with " + match_list[i][0] + "."
        else:
            string += str(match_list[i][1]) + " word(s) in common with " + \
                      match_list[i][0] + ", "
    return string         


def check_inconclusive(match_results):
    ''' Name: check_tie
        Input: nested list of match results [["name", 0],["name", 0]]
        Returns: True if numbers in nested list are 0 or there is tie
    '''
    if check_tie(match_results) or check_zero_sum(match_results):
        return True

def check_tie(match_results):
    ''' Name: check_tie
        Input: nested list of match results [["name", 0],["name", 0]]
        Returns: True if there is a tie
    '''
    numbers = isolate_nested_list(match_results, 1)
    count = 0

    # check to see if each number is in result list, exclusive of number
    for i in range(len(numbers)):
        compare_list = numbers.copy()
        compare_list.pop(i)
        if numbers[i] == 0:
            continue
        if numbers[i] in compare_list:
            count += 1

    # return True of there any duplicats
    if count > 0:
        return True

def check_zero_sum(match_results):
    ''' Name: check_zero_sum
        Input: nested list of match results [["name", 0],["name", 0]]
        Returns: True if sum of results is 0
    '''
    numbers = isolate_nested_list(match_results, 1)
    if sum(numbers) == 0:
        return True
    
def return_top_count(characters, quote, stop_words, top_5):
    ''' Name: return_top_count
        Input: nested list of strings of character quotes with character name
               saved at index 0 and quotes index 1 through 5
        Returns: 
    '''
    match_results = []
    # iterate through character list
    for character in characters:

        # separate character name from their top words
        char_name = character[0]
        top_words = character[1:]

        # count frequency of each char top words in quote
        frequency = count_common_words(top_words, quote)

        # append count of top words in quote to nested list
        user_match = [char_name, frequency]
        match_results.append(user_match)

    return match_results
    
def count_common_words(word_list, quote):
    ''' Name: count_common_words
        Input: quote (string) and word_list, list of words (strings)
        Returns: number of times words in top five list appear in quote (int)
    '''
    # split quote into list of words and make all words lower-case
    quote_words = quote.split(" ")
    quote_words = convert_lower(quote_words)

    # convert list of words to lower-case
    word_list = convert_lower(word_list)

    # iterate through words in quote and 
    count = 0
    for word in quote_words:
        if word in word_list:
            count += 1

    return count
            
def compare_quotes(quote, character_list):
    ''' Name: compqre_quotes
        Input: quote (string) and nested list of character names and variable
               where list of their quotes (strings) are saved -- [["name", VAR]]
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

def link_top_words(character_list, stop_words, top_5):
    ''' Name: link_top_words
        Input: nested list of character names and variable where list of their
               quotes (strings) are saved -- [["name", VAR]], and list of
               top words (strings)
        Returns: nested list of lists with character name, string (saved at
                 index 0 followed by their top five words at index 1 - 5)
    '''
    char_words = []
    # iterate throughlist of characters
    for i in range(len(character_list)):

        # isolate name from nested list
        char_name = character_list[i][0]

        # isolate character string of quotes from nested list
        char_quotes = character_list[i][1]

        # calculate top words for character
        top_words = calculate_top_words(char_quotes, stop_words, top_5)

        # add character name to position 0 then append list to full list
        char_combined = top_words
        char_combined.insert(0, char_name)
        char_words.append(char_combined)
        
    return char_words
        

def calculate_top_words(quote_list, stop_words, top_n):
    ''' Name: calculate_top_words:
        Inputs: list of sentences (strings), list of stop words (strings),
                top_n..ex top 5..words to isolate (int)
        Returns: top n words in list minus stop_words
    '''
    # split quote list into words
    word_list = split_quotes(quote_list)
    
    # convert all words to lower case
    word_list = convert_lower(word_list)

    # remove stop words from list
    word_list = scrub_list(word_list, stop_words)
    
    # calculate frequency of each word, minus stop_words, saved in nested list
    word_frequency = calculate_word_frequency(word_list)
    
    # sorted_nested_list based count of each item in nested list
    top_count = sort_nested_list(word_frequency)
    
    # trim sorted list to top n (5 in this case)
    top_five = trim_list(top_count, top_n)
    
    # isolate words from nested list, which are saved at index 0
    top_five = isolate_nested_list(top_five, 0)
    
    return top_five

def isolate_nested_list(nested_list, item_location):
    ''' Name: isolate_nested_list
        Inputs: nested list with format - [["string", int],["string",[int]]..,
                index location of items to be isolated (int)
        Returns: list of item at item_location in each nested list
    '''
    culled_list = []

    # iterate through nested list, appending item at index 0 to new list
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

def sort_nested_list(words_counted_list):
    ''' Name: sort_nested_list
        Inputs: nested list with format - [["string", int],["string",[int]]..,
        Returns: nested list reverse sorted by itm at index 1 item in each list
        Does: sorts nested list based on item at index 1
    '''
    top_count = words_counted_list
    top_count.sort(key = lambda item: item[1], reverse = True)

    return top_count

def calculate_word_frequency(word_list):
    ''' Name: calculate_word_frequency
        Input: List of strings
        Returns: nested list formated: [["string", int],["string", int],...
        Does: Counts frequency of word usage in word_list and returns
              nested list - [["word", frequency],["word", frequency]]
    '''
    count_list = []
    
    # iterate through each word in list
    for word in word_list:
        
        # if this is first word to review, add it to count_list
        if len(count_list) == 0:
            count_list = append_to_nested(count_list, word)
            
        # if word in count_list, increase frequency count of word by one
        elif check_nested_list(word, count_list, 0):
            pos = search_nested_list(word, count_list, 0)
            count_list[pos][1] += 1
            
        # if no previous conditions true, add word to list with count 1
        else:
            count_list = append_to_nested(count_list, word)

    return count_list

def scrub_list(word_list, stop_words):
    ''' Name: scrub_list
        Input: list of words (strings), list of stop_words (strings)
        Returns: list of words (strings) with words in stop_list removed
    '''
    scrubbed_list = []
    for i in range(len(word_list)):
        if word_list[i] in stop_words:
            continue
        else:
            scrubbed_list.append(word_list[i])
    return scrubbed_list

def append_to_nested(append_list, word):
    ''' Name: append_to_nested
        Input: list to append and word (string)
        Returns: nested list with item added
        Does: appends current word (string) with an initial frequency count of 1
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

def check_nested_list(item, nested_list, index):
    ''' Name: check_nested_list
        Input: nested_list with structure - [["string", int],["string", int]],
               item whose format = search items (str = str)
        Returns: True if word is in list at n index
    '''
    # iterate through nested list; checks if word is in nested list at index n 
    for i in range(len(nested_list)):
        if item == nested_list[i][index]:
            return True

def search_nested_list(item, nested_list, index):
    ''' Name: search_nested_list
        Input: nested_list with structure - [["string", int],["string", int]]..,
               item whose format = search items (str = str)
        Returns: True if word is in list at n index
        Returns: index (int) of nested list in which item occurs
    '''
    # iterate over nested list, checking for word at n location in nested list
    for i in range(len(nested_list)):
        if item == nested_list[i][index]:
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
