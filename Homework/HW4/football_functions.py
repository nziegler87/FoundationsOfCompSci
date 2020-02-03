'''
    Nathanial Ziegler
    CS 5001
    February 5, 2020
    HW 4
    Description:
        Functions for football_stats

    Consulted:
    https://realpython.com/python-sleep/
'''

import time

# Constants for count_one_wins
ONE_GOAL = 1
WIN = "W"

# Constants for compile_streaks
GAMES_IN_SEASON = 38
WIN_POINTS = 3
DRAW_POINTS = 1
LOSS_POINTS = 0

def count_result(result_list, outcome):
    ''' Name: count_result
        Input: list results, each item as string, comparison string
        Returns: count (int) of results in list
    '''
    count = 0
    for i in range(len(result_list)):
        if result_list[i] == outcome:
            count += 1
    return count

def print_all_results(results, result_options):
    ''' Name: print_all_results
        Input: list of strings
        Return: nothing
        Does: Calls count_result functions, passing each itteration of
              result_options to count_result functions and prints output
    '''
    for i in range(len(result_options)):
        outcome = count_result(results, result_options[i])
        print("\t", result_options[i], ": ", outcome, sep = "")
    print()

def count_one_wins(result_list, goals_list):
    ''' Name: count_one_wins
        Inputs: list of game results (each item a string), list of goal
                results (each item an int)
        Returns: number of games won with only one goal (int)
    '''
    count = 0
    for i in range(len(result_list)):
        if result_list[i] == WIN and goals_list[i] == ONE_GOAL:
            count += 1
    return count

def compile_streaks(result_list):
    ''' Name: compile_streaks
        Input: list of results, each item a string
        Returns: list of results, with streaks combined
    '''
    list_length = len(result_list)
    count = 1
    streak_list = []
    for i in range(len(result_list)):
        streak = (str(count) + result_list[i])
        if i < (list_length - 1):
            if list_length == 1:
                streak_list.append(streak)
            elif result_list[i] == result_list[(i + 1)]:
                count += 1
            else:
                streak_list.append(streak)
                count = 1
        else:
            streak_list.append(streak)
    final_string = convert_to_string(streak_list)
    return final_string

def convert_to_string(original_list):
    ''' Name: convert_to_string
        Input: list of strings
        Returns: list of strings joined as one string
    '''
    output_string = ""
    for i in range(len(original_list)):
        if i < (len(original_list) - 1):
            output_string += (original_list[i] + " ")
        else:
            output_string += (original_list[i])
    return output_string

def sum_points(result_list, season, game_number):
    ''' Name: sum_points
        Input: list of results, each item as a string;
               season and game_number - ints
        Returns: number of points up to season and game_number as int
    '''
    game = (season - 1) * GAMES_IN_SEASON
    game += game_number
    short_list = result_list[:game]
    total = 0
    for i in short_list:
        if i == "W":
            total += WIN_POINTS
        elif i == "D":
            total += DRAW_POINTS
        else:
            total += LOSS_POINTS
    return total

def average_score(result_list, goals_list):
    ''' Name: average_score
        Input: list of results (strs), list of goals (ints),
               outcome (str)
        Returns: average score (float)
        Does: Calculates the average score for games that were won
    '''
    count = 0
    total = 0
    for i in range(len(result_list)):
        if result_list[i] == WIN:
            count += 1
            total += goals_list[i]
    average = total / count
    average = round(average, 2)
    return average

def print_with_delay(string):
    ''' Name: print_with_delay
        Input:
        Returns: Nothing
        Does: Prints and then delays to next line
    '''
    print(string, "\n")
    time.sleep(2)      
