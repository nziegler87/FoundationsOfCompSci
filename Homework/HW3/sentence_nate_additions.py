'''
    CS5001
    Spring 2020
    Starter code for HW3
'''

import time
import random

PHRASES = ['How a Data Science Professor May Help Your Doctor Cure What Ails You',
           'During her co-op, Align student merges biology and CS.'
           'NU News: Fitness Trackers need to go beyond counting steps. Here is why.'
           'Four Khoury faculty awarded Global Resilience Institute grants.',
           'You might not want to put so much thought into that thoughtful gift.'
           'This website uses cookies and similar technologies to understand your use of our website.',
           'Oh dear, Brussels! Boris has ALREADY outsmarted EU negotiators.',
           'The PM says Brexit is one step closer after MPs back withdrawal bill by a majority of 124.',
           'The most upsetting text to get is just your first name followed by no punctuation or context.'
           '12:30... lunch. 2:30-7:30... a constant, immeasurable flow of snacks. 8:00... dinner.',
           'cat 911: what is your emergency? cat: a cup on the counter and I want to knock it over.',
           'Jenny don\'t change your number 867-5309 867-5309.',
           '525,600 minutes... how do you measure, measure a year?',
           'Don\'t be sad, don\'t be sad. 2 out of 3 ain\'t bad.',
           'It takes 2 baby, me and you, it takes 2.',
           'Please take your dog, Cali, out for a walk; she needs exercise!',
           'What a beautiful day it is on the beach, here in sunny Hawaii.',
           'Dr. Quinfrey, a renowned scientist, made an invisibility machine.',
           'why are all those chemicals are so hazardous to the environment?',
           'The two kids collected twigs outside in the freezing cold!',
           'How many times have I told you? NEVER look at your race photos.',
           'Didn\'t see a moose, though. Come on, Maine.',
           'Yo minneapolis is cold',
            'Amazingly few discotheques provide jukeboxes!',
           'Jovial Debra Frantz swims quickly with grace and expertise.',
           'Six crazy kings vowed to abolish my quite pitiful jousts.',
           'Rex enjoys playing with farm ducks by the quiet lazy river?',
           'The five boxing wizards jumped quickly!',
           'The 116 saved 49 size 64 items for 26 friends going May 3',
           'Send 99 people to do 8 sets of 150 shows.',
           'The new school holds 3092 students; the older one, 568 more.',
           'He has seat 459 in car 985 of train 78, which is now at gate 31.',
           'The 36 men won 663 prizes in 52 games and 57 in 129 others.',
           'The Quick Brown Fox Jumps Over The Lazy Dog.',
           'I bEt ThIs AlTeRnAtInG cApS iS rEaLlY sLoWiNg YoU dOwN.',
           'Thank you for your booking, Nathanial Ziegler. '
           'Stay well at Westin Hotels & Resorts.']

def select_sentence():
    ''' Function select_sentence
        Input: nothing
        Returns: a randomly-chosen sentence from the list above (string)
    '''
    return random.choice(PHRASES)

def count_words(sentence):
    ''' Function count_words
        Input: a string
        Returns: an int, the number of words in the given string.
                 Uses one white space as a delimiter, nothing else.
    '''
    words = sentence.split(' ')
    return len(words)

def count_mismatches(phrase_one, phrase_two):
    ''' Function count_mismatches
        Input: two strings for comparison
        Returns: an int, the number of differences between the two strings.
                 We count differences in each word (not each character).
                 If the words at position i in each sentence differ at ALL,
                 case included, that's a mismatch.
                 If one sentence is longer than the other, each extra word
                 it has is also a mismatch.
    '''
    list_one = phrase_one.split(' ')
    list_two = phrase_two.split(' ')
    min_length = min(len(list_one), len(list_two))

    # Count the position-by-position mismatches
    errors = 0
    for i in range(min_length):
        if list_one[i] != list_two[i]:
            errors += 1

    # Add on any mismatches if one phrase was longer
    errors += abs(len(list_one) - len(list_two))

    return errors
