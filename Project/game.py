'''
    Nathanial Ziegler
    CS 5001
    April 2020
    Final Project
    Description:
        Game class that uses game_board and player classes as well as
        check_winner_functions and graphics files to setup and play Connect 4
        
    Consulted:
        https://www.fgbradleys.com/rules/Connect%20Four.pdf
        https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
'''

from player import *
from game_board import *
from graphics import *
from check_winner_functions import *
import random, time

# constants for player types
PLAYERS = {"C": "Computer", "H": "Another Human"}
COMPUTER = "C"
COMPUTER_DELAY = 1

# constants for menus
OPTIONS = {"yes": True, "no": False}

# game piece colors
RED = "red"
YELLOW = "yellow"

# constant for onclick handling
CLICK_BUFFER = 30

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

# pop up message constants
GAME_OVER = "Game Over!"
COL_FULL = "Column full. Pick another."
DRAW = "It was a draw. Game over!"
WINNER = "The winner is {}!"
SAVE = ["Saving updated scores", "check shell to confirm", "no save error"]

class Game:
    ''' class: Game
        Attributes: play_computer, default_board, game_over, current_move
                    current_img, players
        Methods: set_player_type, set_board_size, setup_players,
                 pick_starting_player, set_player_img, initialize_game,
                 switch_player, setup_graphics, play_game, handle_click
                 process_human_turn, process_computer_turn, drop_piece
                 post_turn_process, get_column, get_random_column,
                 check_game_end, process_full, check_full, check_win,
                 process_win, collect_all_directions, collect_horizontals,
                 collect_verticals, collect_diagonals, collect_antidiagonals
    '''
            
    def __init__(self):
        '''
        Constructor -- creates a new instance of game
        Parameters:
            self -- the current object
            play_computer -- "", to be replaced with boolean
            default_board -- "", to be replaced with a boolean
            game_over -- a boolean, False by default
            current_move -- "", to be replaced with 0 or 1 (int)
            current_img -- "", to be replaced with img file path (string)
            players -- blank list to be updated with two instances
                           of player objects at position 0 and 1
        '''
        self.play_computer = ""
        self.default_board = ""
        self.game_over = False
        self.board = Game_Board()
        self.current_move = ""
        self.current_img = ""
        self.players = []

    def set_player_type(self):
        ''' Method: set_player_type
            Parameters:
                self -- the current object
            Returns: nothing
            Does:
        '''
        # print question and options
        print("Do you want to play against the computer or another human?")
        for k, v in PLAYERS.items():
            print("  ", k, "-", v)

        # ask for and valdiate response
        response = input("Enter your selection: ").upper()
        while response not in PLAYERS.keys():
            response = input("Invalid entry. Try again: ").upper()

        # set play_computer attribute with boolean based on reponse
        if response == COMPUTER:
            self.play_computer = True
        else:
            self.play_computer = False

    def set_board_size(self):
        ''' Method: set_board_size
            Parameters:
                self -- the current object
            Returns: nothing
        '''
        # print question and options
        print("\nDo you want to use the default board size of ",
              str(self.board.rows), " rows and ",
              str(self.board.cols), " columns? ", sep = "")
        for k in OPTIONS.keys():
            print("  ", k.capitalize())

        # collect and validate response
        response = input("Enter your selection: ").lower()
        while response not in OPTIONS.keys():
            response = input("Invalid entry. Try again: ").lower()

        # update default_board attribute based on response
        self.default_board = OPTIONS[response]

    def setup_players(self):
        ''' Method: setup_players
            Parameters:
                self -- the current object
            Returns: nothing
            Does: calls player class two create two player objects
                  and saves instances in self.players list
        '''
        # create a player instance and collect info
        print("\n", PLAYER_ONE, " information:", sep = "")
        player_1 = Player(PLAYER_ONE)
        player_1.collect_name()
        player_1.collect_color()
        self.players.append(player_1)

        # create second player instance, either set to computer or collect info
        if self.play_computer == True:
            player_2 = Player(COMPUTER_NAME)
        else:
            print("\n", PLAYER_TWO, " information:", sep = "")
            player_2 = Player(PLAYER_TWO)
            player_2.collect_name(self.players[0].name)
        self.players.append(player_2)

        # set player 2 color, based on player 1 selection
        if self.players[0].color == RED:
            self.players[1].color = YELLOW
        else:
            self.players[1].color = RED         
        print("\n", self.players[1].name, ", your color is ",
              self.players[1].color, ".", sep = "")

        # initialize player scores
        for player in self.players:
            player.set_filename()
            player.initialize_score()

    def pick_starting_player(self):
        ''' Method: pick_starting_player
            Parameters:
                self -- the current object
            Returns: nothing
            Does: randomly pick 0 or 1 and set current_move
        '''
        # if playing computer, human user always starts first
        if self.play_computer == True:
            self.current_move = 0

        # otherwise, pick at random
        else:
            self.current_move = random.randint(0, 1)
        player_name = self.players[self.current_move].name
        print("\n", player_name, " goes first!", sep = "")

    def set_player_img(self):
        ''' Method: set_player_img
            Parameters:
                self -- the current object
            Returns: nothing
            Does: sets image piece (red or yellow) based on active player
        '''
        if self.players[self.current_move].color == RED:
            self.current_img = RED_IMG
        else:
            self.current_img = YELLOW_IMG

    def initialize_game(self):
        '''
        Method: collect default game values from user
        Parameters:
            self -- the current object
        Returns: nothing
        Does: calls game and board methods to set up game
        '''
        print(INSTRUCTIONS)

        # ask if user wants to play computer or human and collectinfo
        self.set_player_type()
        self.setup_players()
        self.pick_starting_player()      
        self.set_player_img()

        # ask if user wants default board size or input own dimensions
        self.set_board_size()
        if self.default_board is False:
            self.board.get_dimensions()
        self.board.setup_board()

        # draw blank board and gamesetup on screen
        self.setup_graphics()
            
    def switch_player(self):
        ''' Method: switch_payer
            Parameters:
                self -- the current object
            Returns: nothing
            Does: alternates current_player attribute between 0 and 1 and sets
                  current_player_img accordingly
        '''
        if self.current_move == 1:
            self.current_move = 0
        else:
            self.current_move = 1

        self.set_player_img()
        
    def setup_graphics(self):
        ''' Method: setup_graphics
            Parameters:
                self -- the current object
            Returns: nothing
            Does: creates turtle instances draws gameboard
        '''
        # initialize turtle objects, each as global
        global screen
        screen = setup_screen()
        
        global piece
        piece = setup_turtle()
        
        global arrows
        arrows = setup_turtle()

        global player_notification
        player_notification = setup_turtle()

        global score_message
        score_message = setup_turtle()

        global box_message
        box_message = setup_turtle()

        # draw gameboard
        draw_board(self.board.board, piece, screen, WHITE_IMG)
        draw_arrows(self.board.arrows, arrows, screen, ARROW_IMG)

        # display current user player name and piece image
        update_current_player(player_notification, screen, X_START, Y_START,
                              self.players[self.current_move].name,
                              self.current_img)

        # display current cores
        display_scores(score_message, screen, self.players, X_START, Y_START)

    def play_game(self):
        ''' Method: play_game
            Parameters:
                self -- the current object
            Returns: nothing
            Does: sets up onclick and waits for a click at which point
                  passes x, y coordaintes to handle_click function for gameplay
        '''
        screen.onclick(self.handle_click)

    def handle_click(self, x, y):
        ''' Method: handle_click
            Parameter:
                self -- the current object
                x -- x coordinate (float) of mouse click
                y -- y coordinate (float) of mouse click
        '''
        # if game is over, dislay message
        if self.game_over is True:
            popup_box(box_message, screen, X_START, Y_START, self.board.rows,
                         self.board.cols, PIECE_SIZE, GAME_OVER)

        # if game not over, start with human turn
        else:
            self.process_human_turn(x, y)
            
            # if computer player turned on and game is not over, computer turn
            if (self.players[self.current_move].name == COMPUTER_NAME and
                self.game_over is False):
                self.process_computer_turn(x, y)

    def process_human_turn(self, x, y):
        ''' Method: process_human_turn
            Parameters:
                self -- the current object
                x -- x coordinate (float) of mouse click
                y -- y coordinate (float) of mouse click
            Returns: nothing
        '''
        # translate x, y coordinates to column number
        col = self.get_column(x, y)
        
        # if user clicks but not on an arrow, nothing happens
        if col is not None:
            cord = self.drop_piece(col, self.players[self.current_move].color)
            if cord is None:
                pass
            else:
                self.post_turn_process(cord)
                
    def process_computer_turn(self, x, y):
        ''' Method: process_computer_turn
            Parameters:
                self -- the current object
                x -- x coordinate (float) of mouse click
                y -- y coordinate (float) of mouse click
            Returns: nothing
        '''
        # make the user think the computer takes time to pick a column
        time.sleep(COMPUTER_DELAY)
        
        # randomly pick a column, if filled, pick another
        col = self.get_random_column()

        cord = self.drop_piece(col, self.players[self.current_move].color)
        self.post_turn_process(cord)

    def drop_piece(self, column, color):
        ''' Method: drop_piece
            Parameters:
                self -- the current object
                column -- column number to try and drop piece (an int)
                color -- color of the current player, a string, red or yellow
            Returns: x, y coordinates as a tuple or a Boolean
            Does: if there is an empty game piece in column, fill piece filled
                  attribute with current player color string and return
                  x, y coordinates of the piece
        '''
        if self.board.board[0][column].filled:
            popup_box(box_message, screen, X_START, Y_START, self.board.rows,
                         self.board.cols, PIECE_SIZE, COL_FULL)
        for i in range(len(self.board.board) - 1, -1, -1):
            if not self.board.board[i][column].filled:
                self.board.board[i][column].fill_piece(color)
                return (self.board.board[i][column].x,
                        self.board.board[i][column].y)

    def post_turn_process(self, cord):
        x, y = cord
        update_piece(piece, screen, Y_START, x, y, self.current_img, PIECE_SIZE)
        self.check_game_end()
        if self.game_over is not True:
            self.switch_player()
            update_current_player(player_notification, screen, X_START, Y_START,
                                  self.players[self.current_move].name,
                                  self.current_img)

    def get_column(self, x, y):
        ''' Method: get_column
            Parameters:
                self -- the current object
                x -- x coordinate of click (float)
                y -- y coordinate of click (float)
            Returns: column number {an int)
        '''
        # check to see if click is in arrow region and on an arrow
        # if true, return the corresponding column
        arrow_y = self.board.arrows[0].y
        if y > arrow_y - CLICK_BUFFER and y < arrow_y + CLICK_BUFFER:
            for arrow in self.board.arrows:
                if x > (arrow.x - CLICK_BUFFER) and x < (arrow.x + CLICK_BUFFER):
                    return(arrow.identifier)

    def get_random_column(self):
        ''' Method: get_random_colum
            Parameters:
                self -- the current object
            Returns: a column number (an int)
            Does: randomly returns a number of an unfilled column
        '''
        total_col = self.board.cols
        
        while True:
            col = random.randint(0, total_col - 1)
            if not self.board.board[0][col].filled:
                return col

    def check_game_end(self):
        ''' Method: check_game_end
            Parameters:
                self -- the current object
            Returns: nothing
            Does: uses check_win method first and then process_full to determine
                  if game over, updating the .game_over attribute to True
        '''
        self.check_win()
        if self.game_over == False:
            self.process_full()

    def process_full(self):
        ''' Method: process_full
            Parameters:
                self -- the current object
            Returns: nothing
            Does: checks .filled attribute of each board piece, incrementing
                  a counter each time and comparing total filled pieces to
                  .total_pieces board attribute then updates .game_over and
                  displays message to user if board is filled
        '''
        # check full, and if so, display message
        self.check_full()

        # if board is filled, update .game_over attribute and display message
        if self.game_over == True:
            popup_box(box_message, screen, X_START, Y_START, self.board.rows,
                         self.board.cols, PIECE_SIZE, DRAW)

    def check_full(self):
        ''' Method: check_full_without_message
            Parameters:
                self -- the current object
            Returns: nothing
            Does: checks .filled attribute of each board piece, incrementing
                  a counter each time and comparing total filled pieces to
                  .total_pieces board attribute then updates .game_over
        '''
        total_filled = 0

        # loop through each board piece, increasing counter if piece filled
        for i in range(len(self.board.board)):
            for j in range(len(self.board.board[i])):
                if self.board.board[i][j].filled != "":
                    total_filled += 1

        # if board is filled, update .game_over attribute
        if self.board.total_pieces == total_filled:
            self.game_over = True

    def check_win(self):
        ''' Method: check_win
            Parameters:
                self -- the current object
            Returns: nothing
            Does: checks for a streak of four pieces in all game directions
                  if there is a winner, run process_win method
        '''
        # collect streaks of all horizontal, vertical, diagonal, and
        # antidiagonal options in game and check to see if there is a streak of
        # four in any
        all_directions = self.collect_all_directions()
        for i in range(len(all_directions)):
            for j in range(len(all_directions[i])):
                winner = check_winner(all_directions[i][j])

                # if there is a winner, update .game_over, display message, and
                # save scores
                if winner:
                    self.process_win()
    
    def process_win(self):
        ''' Method: process_win
            Parameters:
                self -- the current object
            Returns: nothing
            Does: updates .game_over to True, displays winner name, increases
                  winner's score, and saves scores
            '''
        self.game_over = True
        
        winner_name = self.players[self.current_move].name
        message = WINNER.format(winner_name)
        popup_box(box_message, screen, X_START, Y_START, self.board.rows,
                     self.board.cols, PIECE_SIZE, message)
        
        self.players[self.current_move].increase_score()
        
        for player in self.players:
            player.save_score()
            
        for message in SAVE:
            popup_box(box_message, screen, X_START, Y_START, self.board.rows,
                         self.board.cols, PIECE_SIZE, message) 
                    
    def collect_all_directions(self):
        ''' Method: collect_all_directions
            Parameters:
                self -- the current object
            Returns: a list of nested lists
            Does: returns a nested list for each possible direction a streak
                  could exists on the board
        '''
        master = []
        master.append(self.collect_horizontals())
        master.append(self.collect_verticals())
        master.append(self.collect_diagonals())
        master.append(self.collect_antidiagonals())

        return master
        
    def collect_horizontals(self):
        ''' Method: collect_horizontals
            Parameters:
                self -- the current object
            Returns: a nested list of each game piece's .filled attribute
                     in each row of the board
        '''
        master = []
        
        for i in range(len(self.board.board)):
            row_streak = []
            for j in range(len(self.board.board[i])):
                row_streak.append(self.board.board[i][j].filled)
            master.append(row_streak)

        return master

    def collect_verticals(self):
        ''' Method: collect_verticals
            Parameters:
                self -- the current object
            Returns: a nested list of each game piece's .filled attribute
                     in each column of the board
        '''
        master = []
        
        for j in range(len(self.board.board[0])):
            col_streak = []
            for i in range(len(self.board.board)):
                col_streak.append(self.board.board[i][j].filled)
            master.append(col_streak)
            
        return master

    def collect_diagonals(self):
        ''' Method: collect_diagonals
            Parameters:
                self -- the current object
            Returns: a nested list of each game piece's .filled attribute
                     in each diagonal of the board
        '''
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
        ''' Method: collect_antidiagonal
            Parameters:
                self -- the current object
            Returns: a nested list of each game piece's .filled attribute
                     in each antidiagonal of the board
        '''
        height = len(self.board.board)
        width = len(self.board.board[0])
        master = []
        
        for p in range(height + width - 1):
            antidiagonal = []
            for q in range(max(p - height + 1,0), min(p + 1, width)):
                antidiagonal.append(self.board.board[p - q][q].filled)
            master.append(antidiagonal)
            
        return master
