'''
    Nathanial Ziegler
    CS 5001
    February 5, 2020
    HW 4
    Description:
        Prints statistics for English football
'''

from football_functions import *
import time

# Constants for functions
POSSIBLE_RESULTS = ["W", "L", "D"]

RESULTS = ['W', 'L', 'D', 'W', 'D', 'W', 'W', 'W', 'W', 'L',
           'W', 'L', 'D', 'L', 'D', 'W', 'W', 'L', 'W', 'W',
           'W', 'D', 'W', 'D', 'W', 'D', 'W', 'W', 'W', 'W',
           'W', 'W', 'L', 'D', 'W', 'L', 'W', 'W', 'W', 'W',
           'W', 'L', 'L', 'W', 'W', 'W', 'W', 'L', 'W', 'W',
           'W', 'L', 'W', 'W', 'W', 'W', 'W', 'L', 'W', 'L',
           'W', 'W', 'W', 'W', 'L', 'L', 'D', 'L', 'L', 'W',
           'W', 'L', 'W', 'L', 'L', 'D']

GOALS = [2, 1, 1, 3, 0, 3, 4, 1, 4, 0, 1, 0, 1, 1, 1,
         5, 2, 1, 3, 5, 2, 1, 4, 1, 2, 2, 1, 1, 2, 4,
         3, 2, 3, 1, 2, 0, 1, 5, 1, 3, 3, 1, 1, 2, 2,
         1, 1, 0, 3, 1, 3, 2, 3, 2, 1, 6, 5, 1, 3, 0,
         2, 2, 1, 3, 1, 0, 1, 1, 1, 2, 4, 0, 1, 0, 0, 2]

def main():
    # Print number of games, won, lost, and drawn over the seasons
    print_results_question()
    print_all_results(RESULTS, POSSIBLE_RESULTS)
    time.sleep(2)

    # Print number of games won despite scoring only one goal
    print("How many games did we win, despite scoring only one goal?")
    wins = count_one_wins(RESULTS, GOALS)
    print_with_delay(wins)

    # Print streaks across the season
    print("What did our “streaks” look like over the season?")
    streaks = compile_streaks(RESULTS)
    print_with_delay(streaks)

    # Print total points after Season 2, Game 20
    print_sum_question()
    points = sum_points(RESULTS, 2, 20)
    print_with_delay(points)

    # Print average score for all games won
    print("What is the average score for all games won across the season?")
    average = average_score(RESULTS, GOALS)
    print_with_delay(average)

    print("Thank you!")

main()
