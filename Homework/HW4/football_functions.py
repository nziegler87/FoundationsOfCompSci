'''
    Nathanial Ziegler
    CS 5001
    February 5, 2020
    HW 4
    Description:
        Functions for football_stats
'''

GAMES_IN_SEASON = 38
WIN_POINTS = 3
DRAW_POINTS = 1
LOSS_POINTS = 0

def count_result(result_list, result):
    ''' Name: count_result
        Input: list of strings, comparison string
        Returns: count (int) of results in list
    '''
    count = 0
    for i in result_list:
        if i == result:
            count += 1
    return count

def count_one_wins(result_list, goals_list):
    ''' Name: count_one_wins
        Inputs: list of game results (each item a string), list of goal
                results (each item an int)
        Returns: number of games won with only one goal (int)
    '''
    count = 0
    for i in range(len(result_list)):
        if result_list[i] == "W" and goals_list[i] == 1:
            count += 1
    return count


def compile_streaks(result_list):
    ''' Name: compile_streaks
        Input: list of results, each item a string
        Returns: list of results, with streaks combined
    '''
    count = 1
    for i in range(len(result_list)):
        if result_list[i] == result_list[i + 1]:
            count += 1
        else:
            print(count, result_list[i], sep = "", end = " ")
            count = 1
        
            
        

def sum_points(result_list, season, game_number):
    ''' Name: sum_points
        Input: list of results, each item as a string;
               season and game_number - ints
        Returns: number of points up to season and game_number as int
    '''
    game = (((season - 1) * GAMES_IN_SEASON) + game_number)
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



##def count_one_wins(result_list, goals_list, result, goal):
##    ''' Name: count_one_wins
##        Inputs: list of game results (each item a string) and list of goal
##                results (each item an int)
##        Returns: number of games won with only one goal (int)
##    '''
##    count = 0
##    for i in range(len(result_list)):
##        if result_list[i] == result and goals_list[i] == goal:
##            count += 1
##    return count


