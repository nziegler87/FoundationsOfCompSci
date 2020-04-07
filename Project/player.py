# constant for creating filenames
TXT_EXT = ".txt"

# player constants
PLAYER_COLORS = {"R":"red", "Y":"yellow"}
COMPUTER_NAME = "Computer"
PLAYER_ONE = "Player 1"
PLAYER_TWO = "Player 2"

class Player:
    ''' class: Player
        Attributes: name, filename, score, color
        Methods: collect_name, set_filename, collect_color,
                 initialize_score, increase_score, save_score
    '''
    def __init__(self, name):
        '''
        Constructor -- creates new instance of player
        Parameters:
            self -- the current object
            name -- name of user (a string)
            filename -- inputed name with TXT_EXT concatenated, starts blank
            score -- user's current score (an int), starts as 0
            color -- color of player, red or yellow, starts blank
        '''
        self.name = name
        self.filename = ""
        self.score = 0
        self.color = ""

    def collect_name(self, second_player = ""):
        ''' Method: collect_name
            Parameters:
                self -- the current object
                second_player -- optional, name of 2nd player(string) if exists
            Returns: nothing
            Does: asks for player name, making sure it doesn't match
                  computer name and that player 2 name != player 1 name
                  and updates player.name attribute with input
        '''
        self.name = input("Enter your name: ")
        
        while self.name == COMPUTER_NAME:
            self.name = input("Your name cannot match the computer name. " +
                              "Try again: ")
            
        if len(second_player) != 0:
            while self.name == second_player or self.name == COMPUTER_NAME:
                self.name = input("Your name must be different than " + \
                                  "player 1 and/or cannot match computer " + \
                                  "name. Try again: ")

    def set_filename(self):
        ''' Method: set_filename
            Parameters:
                self -- the current object
            Returns: nothing
            Does: updates player.filename attribute
        '''
        self.filename = self.name + TXT_EXT

    def collect_color(self):
        ''' Method: collect_color
            Parameters:
                self -- the current object
            Returns: nothing
            Does: asks player for color selection, validating
                  against given options and updates player.color attribute
        '''
        print("Please select your color.")
        for k, v in PLAYER_COLORS.items():
            print("  ", k, "-", v)
            
        color = input("Enter your selection: ").upper()
        while color not in PLAYER_COLORS.keys():
            color = input("Invalid selection. Try again: ").upper()

        self.color = PLAYER_COLORS[color]

    def initialize_score(self):
        ''' Method: initialize_score
            Parameters: self
            Does: opens user file (which only has one number) and sets score to
                  value; if file is unable to be opened, score is set to 0
        '''
        try:
            with open(self.filename, "r") as infile:
                score = infile.read().strip()
                try:
                    self.score = int(score)
                except ValueError:
                    self.score = 0
        except OSError:
            self.score = 0
        
    def increase_score(self):
        ''' Method: increase_score
            Parameters:
                self -- the current object
            Returns: nothing
            Does: increases user score by one
        '''
        self.score += 1

    def save_score(self):
        ''' Method: save_score
            Parameters:
                self -- the current object
            Returns: nothing
            Does: saves current self.score value to self.filename
        '''
        try:
            with open(self.filename, "w") as outfile:
                outfile.write(str(self.score))
        except OSError:
            print("I'm sorry. Your progress cannot be saved at this time.")
