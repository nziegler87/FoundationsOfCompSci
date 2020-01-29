'''
    Nathanial Ziegler
    CS 5001
    January 29, 2020
    HW 3
    Description:
        Basic typing tests. User is prompted to hit enter to begin test.
        They type the random generated sentence, hitting enter at each line
        to generate a new sentences. When finsihed, user types DONE.
        WPM, Number of Mistakes, and Adjusted WPM are then displayed.

    My results from test:
        You typed 29 words in 27.20 seconds.
        Your average wpm is 64
        You made 0 mistakes, so your adjusted wpm is 64
'''

from sentence_nate_additions import *
from typing_functions import *
import time

def main():
    # Welcome user and explain program
    print("Welcome to the WPM test...a simplified version of "
          "Mavis Beacon.\nType each sentence exactly as it appears below.\n"
          "Hit return at the end of the line to generate a new sentence.\n"
          "When you want to end the typing test, type DONE\n")

    # Start test and record time
    start_trigger = input("Hit enter when you are ready and we will start "
                          "the clock!")
    start_time = round(time.time(), 2)

    # Set starting word and error counts
    total_word_count = 0
    total_errors = 0

    while True:
        # Randomly select and display sentence
        sentence = select_sentence()
        print("\n", sentence, sep = "")

        # Capture user typing
        user_input = input()

        # If user types DONE, capture end time and break loop
        if user_input == "DONE":
            end_time = round(time.time(), 2)
            break

        # Else, calculate words typed and errors and add to running totals
        else:
            words_typed = count_words(user_input)
            errors = count_mismatches(sentence, user_input)
            total_word_count += words_typed
            total_errors += errors

    # Calculate total time and report result with word count
    total_time = end_time - start_time
    print("You typed", total_word_count, "words in {:.2f} "
          "seconds.".format(total_time))

    # Calculate and print wpm
    wpm = calculate_wpm(total_word_count, total_time)
    print("Your average wpm is", round(wpm))

    # Calculate and print adjusted wpm
    adjusted_wpm = calculate_adjusted(total_word_count, total_errors,
                                      total_time)
    print("You made", total_errors, "mistakes, so your adjusted wpm "
          "is", round(adjusted_wpm))

main()
