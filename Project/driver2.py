from game import *  # SHOULD I SPECIFY WHICH FUNCTIONS LATER?

# FILE CONSTANTS
SCOREFILE = "scorefile.txt"     # NEED TO CREATE FUNCTION

def main():
    game = Game(SCOREFILE)
    game.collect_settings()

main()
