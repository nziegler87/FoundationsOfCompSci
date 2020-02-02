'''
    Nathanial Ziegler
    CS 5001
    February 5, 2020
    HW 4
    Description:
        UPDATE


'''

from football_functions import *
import time

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

    print("How many games did Tottenham win, lose, and draw over the two seasons?")
    for i in POSSIBLE_RESULTS:
        outcome = count_result(RESULTS, i)
        print("\t", i, ": ", outcome, sep = "")
    print()
    time.sleep(2)

    print("How many games did we win despite scoring only one goal?")
    wins = count_one_wins(RESULTS, GOALS)
    print(wins, "\n")

    time.sleep(2)

    print("What did our “streaks” look like over the season?")
    streaks = compile_streaks(RESULTS)
    print(streaks, "\n")

    time.sleep(2)

    print("How many points did Tottenham have after the 20th game of the second ",
          "season in the list?")
    points = sum_points(RESULTS, 2, 20)
    print(points, "\n")

    print("Compare the total goals scored by season 2, game 6 to the same time ",
          "in season 1.")

main()
