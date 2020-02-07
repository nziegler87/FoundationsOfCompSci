'''
    Nathanial Ziegler
    CS 5001
    February 11, 2020
    HW 5
    Description:
        UPDATE
'''

from classify_data import *

def calculate_top_words(word_list, stop_words):
    ''' Name: calculate_top_words
        Input: List of strings
        Returns: top 5 words in string
    '''
    count_list = []
    for word in word_list:
        if len(count_list) == 0:
            word_count = [word, 1]
            print("word_count:", word_count)
            count_list.append(word_count)
            print(count_list)
        elif not check_nested_list(word, count_list):
            pos = search_nested_list(word, count_list)
            print(pos)
            count_list[pos][0] += 1
        else:
            word_count = [word, 1]
    print(count_list)
            
            

def check_stop_list(word, word_list):
    ''' Name: check_stop_list
        Input: word (string) and list of words (strings)
        Returns: True if word is in word_list
    '''
    if word in word_list:
        return True

def check_nested_list(word, nested_list):
    ''' Name: check_nested_list
        Input: nested_list with structure - [["string", int],["string", int]],
               word (string)
        Returns: True if in list
    '''
    for i in range(len(nested_list)):
        if word in nested_list[i][0]:
            return True

def search_nested_list(word, nested_list):
    ''' Name: search_nested_list
        Input: nested_list with structure - [["string", int],["string", int]],
               word (string)
        Returns: index (int) of nested list in which item occurs
    '''
    for i in range(len(nested_list)):
        if word in nested_list[i][0]:
            pos = i
            return pos

##print("no")
##            print(word)
##            for i in range(len(count_list)):
##                print("i:", i)
##                print("word:", word)
##                if word in count_list[i][0]:
##                    count_list[i][1] += 1
##                else:
##                    count_list.append([word, 1])
##    print(word_list)
##    print(count_list)


##        elif word_list[i] in word_list:
##            local_word = list_of_words[i]
##            count = 1
##            for i in range(len(word_list)):
##                if local_word == word_list[i]:
##                    count += 1
##            word_list.append(list_of_words[i])
##            count_list.append(count)
##        else:
##            count = 1
##            word_list.append(list_of_words[i])
##            count_list.append(count)


def convert_lower(word_list):
    ''' Name: convert_lower
        Input: list of words (strings)
        Returns: list of words with all letters lowercase (strings)
    '''
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
    word_list = []
    for i in range(len(quote_list)):
        single_line = quote_list[i].split(" ")
        word_list += single_line
    return word_list 

