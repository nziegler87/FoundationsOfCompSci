TXT_EXT = ".txt"
PLAYER_COLORS = {"R":"red", "Y":"yellow"}

class Player:

    def __init__(self, name):
        '''
        Constructor -- creates new instance of player
        Parameters:
            self -- the current object
            name -- name of user (a string)
            score -- user's current score (an int)
        '''
        self.name = name
        self.filename = "" + TXT_EXT
        self.score = 0
        self.color = ""

    def collect_name(self):
        self.name = input("Enter your name: ")
        self.filename = self.name + TXT_EXT

    def collect_color(self):
        print("Please select your color.")
        for k, v in PLAYER_COLORS.items():
            print("  ", k, "-", v)
        color = input("Enter your selection: ").upper()
        while color not in PLAYER_COLORS.keys():
            color = input("Invalid selection. Try again: ").upper()

        self.color = PLAYER_COLORS[color]

    def initialize_score(self):
        '''
        Method: initialize_score
        Parameters: self
        Does: opens user file (which only has one number) and sets score to
              to value; if file is unable to be opened, score is set to 0
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
        '''
        Method: increases user score by one
        '''
        self.score += 1

    def save_score(self):
        '''
        Method: save_score
        Parameters: self
        Does: saves current self.score value to self.filename
        '''
        try:
            with open(self.filename, "w") as outfile:
                outfile.write(str(self.score))
        except OSError:
            print("I'm sorry. Your progress cannot be saved at this time.")
