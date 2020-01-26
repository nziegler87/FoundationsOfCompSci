'''
    Nathanial Ziegler
    CS 5001
    January 29, 2020
    HW 3
    Description:
       Functions for typing test
'''
# Constant to convert sec to min
SEC_IN_MIN = 60
ZERO_WPM = 0.0

def calculate_wpm(word_count, time):
    ''' Function: calculate_wpm
        Input: number of words (int) and sec (float)
        Returns: words_per_min (float)
    '''
    # Convert time in sec to min
    minutes = time / SEC_IN_MIN

    # Calculate and return wpm
    wpm = word_count / minutes
    return wpm

def calculate_adjusted(word_count, total_mistakes, time):
    ''' Function: calculate_adjusted
        Input: num of total words, mistakes, and time (int, int, float)
        Return: words_per_min adjust for mistakes (float)
    '''
    # Return 0 WPM if user made too many mistakes
    if total_mistakes >= word_count:
        return ZERO_WPM
    else:
        # Conver time in sec to min
        minutes = time / SEC_IN_MIN

        # Calculate and return adjusted wpm
        total_words = word_count - total_mistakes
        adjusted_wpm = total_words / minutes
        return adjusted_wpm
