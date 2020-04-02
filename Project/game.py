'''
    Nathanial Ziegler
    CS 5001
    April 2020
    Consulted:
        https://www.fgbradleys.com/rules/Connect%20Four.pdf
'''

from stack import Stack
from player import Player

# constants for game setup
ROWS = "rows"
COLS = "cols"
MIN_DIMENSION = 4

# constants for player types
PLAYERS = {"C": "Computer", "H": "Another Human"}
COMPUTER = "C"

# game piece colors
RED = "red"
YELLOW = "yellow"

# constants for printing instructions
CENTER_SPACING = 20
INSTRUCTIONS = "OVERVIEW".center(CENTER_SPACING, "-") + \
               "\nThe rules are simple. Try to build a streak of four " + \
               "checkers while keeping your opponent from doing " + \
               "the same.\n\n" + \
               "OBJECTIVE".center(CENTER_SPACING, "-") + \
               "\nBe the first player to get four of your colored checkers " + \
               "in a row -- horizontally, vertically, or diagonally.\n\n" + \
               "SETUP".center(CENTER_SPACING, "-") + \
               "\n1. Select the number of rows and columns, ," + \
               "min " + str(MIN_DIMENSION) + " x " + \
               str(MIN_DIMENSION) + "\n" + \
               "2. Choose if you want to play human:human or " + \
               "human:computer\n" + \
               "3. Decide who goes first\n\n" + \
               "GAMEPLAY".center(CENTER_SPACING, "-") + \
               "\n1. First player drops one of their checkers on ANY " + \
               "of the columns.\n" + \
               "2. Players alternate until one player gets FOUR checkers " + \
               "in a row. The four in a row can be horizontal, vertical, " + \
               "or diagonal\n3. A draw is declared if the entire board " + \
               "is full and neither player earned four in a row.\n"

# functions for collecting and validating user game settings
def ask_player_type():
    ''' Name: ask_play_type
        Parameters: nothing
        Returns: True, if they want to play against the computer
    '''
    print("Do you want to play against the computer or another human?")
    for k, v in PLAYERS.items():
        print("  ", k, "-", v)
    response = input("Enter your selection: ").upper()
    while response not in PLAYERS.keys():
        response = input("Invalid entry. Try again: ").upper()

    if response == COMPUTER:
        return True
    else:
        return False

def get_dimensions(string):
    ''' Name: get_dimensions
        Parameters: a string
        Returns: an int
    '''
    value = input("Number of " + string + " (min " + str(MIN_DIMENSION) + "): ")
    while not value.isdigit() or int(value) < MIN_DIMENSION:
        value = input("That was not a valid input. Try again: ")
    return int(value)

# functions for checking winner
def check_winner(lst):
    ''' Name: check_winner
        Parameter: a list of items
        Returns: if there is a streak of items four or great in the list,
                 a tuple with (True, item)
    '''
    tuples = create_streak(lst)
    check_four(tuples)
    
def check_four(tuples_list):
    ''' Name: check_four
        Parameters: list of tuples -- [("count (an int)", item)]
        Returns: True if an item has streak of four or more and the
                 item with the streak as a tuple -- {TRUE, item)
    '''
    for i in range(len(tuples_list)):
        # looks for streak of four or greater, ignoring any blanks
        if tuples_list[i][0] >= 4 and tuples_list[i][1] != "":
                winner = tuples_list[i][1]
                return (True, winner)

def create_streak(lst):
    ''' Name: create_streak
        Parameters: a list
        Returns: a list of tuples with list items reported as streaks --
                    [("count (an int)", item),( "count (an int)", item)]
    '''
    stack = Stack()
    streak = []
    count = 1

    # iterate through list in reverse
    for i in range(len(lst) - 1, -1, -1):
        stack.push(lst[i])

    # get first item and remove it from stack
    while not stack.is_empty():
        item = stack.top()
        stack.pop()

        # if next item on stack matches first, increase count, else append
        if stack.top() == item:
            count += 1
        else:
            streak.append((count, item))
            count = 1

    return streak

class Game:
    ''' class: Game
        Attributes: play_computer, first_move, rows, columns
        Methods: setup_game
    '''
            
    def __init__(self):     # NEED TO TEST
        '''
        Constructor -- creates a new instance of game
        Parameters:
            self -- the current object
            play_computer -- "", to be replaced with boolean
            first_move -- "", to be replaced with player one color (string)
            rows -- "", to be replaced with an int
            cols -- "", to be replaced with an int
            score -- a blank dictionary to hold score
        '''
        self.play_computer = ""
        self.first_move = ""
        self.rows = "" 
        self.cols = ""
        self.score = {}
    
    def collect_settings(self):           # I DON'T SEE HOW TO TEST THIS
        '''
        Method: collect default game values from user
        Parameters:
            self -- the current object
        Does: 
        '''
        print(INSTRUCTIONS)
        
        print("Specify game board dimensions.")
        self.rows = get_dimensions(ROWS)
        self.cols = get_dimensions(COLS)
        self.play_computer = ask_player_type() 
