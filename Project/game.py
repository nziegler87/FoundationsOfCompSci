'''
    Nathanial Ziegler
    CS 5001
    April 2020
    Consulted:
        https://www.fgbradleys.com/rules/Connect%20Four.pdf
'''

from stack import Stack
from player import Player           # STILL NEED TO DO THIS
from game_board import Game_Board
from graphics import *
import random

# constants for player types
PLAYERS = {"C": "Computer", "H": "Another Human"}
COMPUTER = "C"

OPTIONS = {"yes": True, "no": False}

# game piece colors
RED = "red"
YELLOW = "yellow"

CLICK_BUFFER = 30

COMPUTER_NAME = "Computer"
PLAYER_ONE = "player 1"
PLAYER_TWO = "player 2"

# constants for printing instructions
CENTER_SPACING = 20
INSTRUCTIONS = "OVERVIEW".center(CENTER_SPACING, "-") + \
               "\nThe rules are simple. Try to build a streak of four " + \
               "checkers while keeping your opponent from doing " + \
               "the same.\n\n" + \
               "OBJECTIVE".center(CENTER_SPACING, "-") + \
               "\nBe the first player to get four of your colored checkers " + \
               "in a row -- horizontally, vertically, or diagonally.\n\n" + \
               "GAMEPLAY".center(CENTER_SPACING, "-") + \
               "\n1. First player drops one of their checkers on ANY " + \
               "of the columns.\n" + \
               "2. Players alternate until one player gets FOUR checkers " + \
               "in a row. The four in a row can be horizontal, vertical, " + \
               "or diagonal\n3. A draw is declared if the entire board " + \
               "is full and neither player earned four in a row.\n"

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

    # iterate through list in reverse and push to stack
    for i in range(len(lst) - 1, -1, -1):
        stack.push(lst[i])

    # get first item and remove it from stack
    while not stack.is_empty():
        item = stack.top()
        stack.pop()

        # if next item identical, increase count, else append and reset count
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
            current_move -- "", to be replaced with player one color (string)
            default_board -- "", to be replaced with a boolean
            score -- a blank dictionary to hold score
        '''
        self.play_computer = ""
        self.default_board = ""
        self.game_over = False
        self.score = {}
        self.board = Game_Board()

        self.current_move = ""
        self.current_img = ""
        self.players = []

    def ask_player_type(self):
        ''' Method: ask_player_type
            Parameters:
                self -- the current object
            Returns: nothing
        '''
        print("Do you want to play against the computer or another human?")
        for k, v in PLAYERS.items():
            print("  ", k, "-", v)
        response = input("Enter your selection: ").upper()
        while response not in PLAYERS.keys():
            response = input("Invalid entry. Try again: ").upper()

        if response == COMPUTER:
            self.play_computer = True
        else:
            self.play_computer = False

    def ask_board_size(self):
        ''' Method: ask_board_size
            Parameters:
                self -- the current object
            Returns: nothing
        '''
        print("\nDo you want to use the default board size of ",
              str(self.board.rows), " rows and ",
              str(self.board.cols), " columns? ", sep = "")
        
        for k in OPTIONS.keys():
            print("  ", k.capitalize())

        response = input("Enter your selection: ").lower()

        while response not in OPTIONS.keys():
            response = input("Invalid entry. Try again: ").lower()

        self.default_board = OPTIONS[response]

    def initialize_game(self):           # I DON'T SEE HOW TO TEST THIS
        '''
        Method: collect default game values from user
        Parameters:
            self -- the current object
        Does: 
        '''
        print(INSTRUCTIONS)
        
        self.ask_player_type()
        self.collect_player_info()
        self.pick_starting_player()
        self.set_current_img()
        self.ask_board_size()
        if self.default_board is False:
            self.board.get_dimensions()
        self.board.setup_board()

        self.setup_graphics()

    def collect_player_info(self):
        ''' Method: collect_player_info
            Parameters:
                self -- the current object
            Returns: nothing
            Does: calls player class two create two player objects
                  and saves instances in self.players list
        '''
        # collect player 1 info
        player_1 = Player(PLAYER_ONE)
        print(player_1.name.capitalize(), "information:")
        player_1.collect_name()
        player_1.collect_color()
        self.players.append(player_1)

        # collect player 2 info
        if self.play_computer == True:
            player_2 = Player(COMPUTER_NAME)
        else:
            player_2 = Player(PLAYER_TWO)
            print(player_2.name.capitalize(), "information:")
            player_2.collect_name()
        self.players.append(player_2)

        # set play 2 color, based on player 1 selection
        if self.players[0].color == RED:
            self.players[1].color = YELLOW
        else:
            self.players[1].color = RED         
        print(self.players[1].name, " your color is ",
              self.players[1].color, ".", sep = "")

    def pick_starting_player(self):
        self.current_move = random.randint(0, 1)
        print(self.players[self.current_move].name, "goes first!")

    def set_current_img(self):
        if self.players[self.current_move].color == RED:
            self.current_img = RED_IMG
        else:
            self.current_img = YELLOW_IMG
            
    def switch_player(self):
        if self.current_move == 1:
            self.current_move = 0
        else:
            self.current_move = 1
        
    def setup_graphics(self):
        # initialize turtle objects, each as global
        global screen
        screen = setup_screen()
        
        global piece
        piece = setup_piece()
        
        global arrows
        arrows = setup_arrow()

        # draw gameboard
        draw_board(self.board.board, piece, screen, WHITE_IMG)
        draw_arrows(self.board.arrows, arrows, screen, ARROW_IMG)

    def play_game(self):
        screen.onclick(self.handle_click)

    def handle_click(self, x, y):
        if self.game_over is True:
            print("Game is over")
        else:
            if self.players[self.current_move].name == COMPUTER_NAME:
                self.computer_turn()
            else:
                self.process_turn(x, y)

    def computer_turn(self):
##        while True:
##            column = random.randint(0, len(self.board.board[0]) - 1)
##            if not self.board.board[0][column].filled:
##                break
        valid_cols = []
        for i in range(len(self.board.board[0])):
            if not self.board.board[0][i].filled:
                valid_cols.append(i)
        print(valid_cols)
        column = random.choice(valid_cols)
        print(column)
        for i in range(len(self.board.board) - 1, -1, -1):
            if not self.board.board[i][column].filled:
                self.board.board[i][column].fill_piece(self.players[self.current_move].color)
                x, y = (self.board.board[i][column].x, self.board.board[i][column].y)
                break
        update_piece(arrows, screen, column, x, y, self.current_img)
        self.check_full()
        self.check_horizontal_streak()
        self.switch_player()
        self.set_current_img()
        print(self.board)

                
    def process_turn(self, x, y):
        '''
        returns column number, an int
        '''
        # check to see if click is in arrow region and on an arrow
        # if true, return the corresponding column
        arrow_y = self.board.arrows[0].y
        if y > arrow_y - CLICK_BUFFER and y < arrow_y + CLICK_BUFFER:
            for arrow in self.board.arrows:
                if x > (arrow.x - CLICK_BUFFER) and x < (arrow.x + CLICK_BUFFER):
                    column = arrow.identifier
                    
                    # if column has an empty space, drop it and update screen
                    # if column full, do not update screen and keep current player
                    move_value = self.drop_piece(column,
                                                 self.players[self.current_move].color)
                    if move_value is False:
                        pass
                    else:
                        x, y = move_value
                        update_piece(arrows, screen, column, x, y,
                                     self.current_img)
                        self.check_full()
                        self.check_horizontal_streak()
                        self.switch_player()
                        self.set_current_img()
                        print(self.board)


    def drop_piece(self, column, color):
        if self.board.board[0][column].filled:
            print("That column is full. Try again.")
            return False
        for i in range(len(self.board.board) - 1, -1, -1):
            if not self.board.board[i][column].filled:
                self.board.board[i][column].fill_piece(color)
                return (self.board.board[i][column].x, self.board.board[i][column].y)
            
# THESE I PULLED FROM GAME_BOARD AND PUT HERE BECAUSE THEY RELATE TO GAME PLAY
# NEED TO INTEGRATE

    def check_full(self):
        total_filled = 0
        for i in range(len(self.board.board)):
            for j in range(len(self.board.board[i])):
                if self.board.board[i][j].filled != "":
                    total_filled += 1
        if self.board.total_pieces == total_filled:
            self.game_over = True
            print("The board is full and it is a draw.")

    def check_win(sef):
        all_directions = self.collect_all_directions()
        for i in range(len(all_directions)):
            for j in range(len(all_directions[0])):
                self.game_over, winner = check_winner(all_directions[i][j])
                
            

    def collect_all_directions(self):
        master = []
        master.append(self.collect_horizontals())
        master.append(self.collect_verticals())
        master.append(self.collect_diagonals())
        master.append(self.collect_antidiagonals())
        return master
        

    def collect_horizontals(self):
        master = []
        for i in range(len(self.board.board)):
            row_streak = []
            for j in range(len(self.board.board[i])):
                row_streak.append(self.board.board[i][j].filled)
            master.append(row_streak)
        return master

    def collect_verticals(self):
        master = []
        for j in range(len(self.board.board[0])):
            col_streak = []
            for i in range(len(self.board.board)):
                col_streak.append(self.board.board[i][j].filled)
            master.append(col_streak)
        return master

    def collect_diagonals(self):
        height = len(self.board.board)
        width = len(self.board.board[0])
        master = []
        for p in range(height + width - 1):
            diagonal = []
            for q in range(max(p - height + 1, 0), min(p + 1, width)):
                diagonal.append(self.board.board[height - p + q - 1][q].filled)
            master.append(diagonal)
        return master

    def collect_antidiagonals(self):
        height = len(self.board.board)
        width = len(self.board.board[0])
        master = []
        for p in range(height + width - 1):
            antidiagonal = []
            for q in range(max(p - height + 1,0), min(p + 1, width)):
                antidiagonal.append(self.board.board[p - q][q].filled)
            master.append(antidiagonal)
        return master

    # CAN DELETE THIS AT SOMEPOINT
    def initialize_players2(self):
        print(self.player_1.name.capitalize(), "information:")
        self.player_1.collect_name()
        self.player_1.collect_color()
        
        if self.player_1.color == RED:
            self.player_2.color = YELLOW
        else:
            self.player_2.color = RED
            
        if self.play_computer == True:
            self.player_2.name = COMPUTER_NAME
        else:
            print(self.player_2.name.capitalize(), "information:")
            self.player_2.collect_name()
            print(self.player_2.name, " your color is ",
                  self.player_2.color, ".", sep = "")

        self.player_1.initialize_score()
        self.player_2.initialize_score()
