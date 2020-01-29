'''
    Nathanial Ziegler
    CS 5001
    January 29, 2020
    HW3
    Description:
        Game of NIM with one pile of beans, ranging from 5 and 30. Game is between
        computer and one player. Begins with coin toss and alternates turns
        until no beans are left. Player to take last bean loses the game.
'''

import random
from nim_functions import *

COIN_SIDE_A = "H"
COIN_SIDE_B = "T"
COMPUTER_NAME = "Alvin"

def main():

    # Introduce game and collect user name
    print("Welcome! Let's play a game of NIM.\nA coin toss will determine "
          "who goes first.\n")
    player_name = input("My name is " + COMPUTER_NAME + ". Who am I playing "
                        "against? Enter your name: ")

    # Ask if player wants to be heads or tails
    while True:
        user_choice = user_coin_selection(player_name)
        if not validate_input(user_choice, COIN_SIDE_A, COIN_SIDE_B):
            print("\nI'm sorry, that is not a valid input. You must enter "
                  "either ", COIN_SIDE_A, " or ", COIN_SIDE_B,".", sep = "")
        else:
            break

    # Actual coin toss. Compare against user selection. Determine first turn.
    toss_result = coin_flip(random.randint(1,2))
    turn = coin_toss_result(user_choice, toss_result, player_name,
                            COMPUTER_NAME)

    # Announce coin toss winner
    if turn == COMPUTER_NAME:
        print("\nYou lost the coin toss. I get to go first!\n")
    else:
        print("\nYou won the coint toss, so you go first.\n")
    
    # Set size of bean pile
    bean_pile = random.randint(5, 30)
    print("We are starting with a pile of", bean_pile, "beans.")

    # Start of back and forth game
    while not is_over(bean_pile):

        # Computer action
        if turn == COMPUTER_NAME:
            # Switch player for next term
            turn = player_name

            # Calculate number of beans to remove from pile
            deduct = computer_deduct(bean_pile)

            # Deduct beans from pile
            bean_pile -= deduct
            print("\nI took", deduct, "bean(s).")

        # Player action
        else:
            # Switch player for next term
            turn = COMPUTER_NAME

            # Collect number of beans to remove from pile
            while True:
                deduct = int(input("\nThere are " + str(bean_pile) + " beans "
                           "remaining.\nYou must take at least one bean "
                           "but no more than three.\nHow many do you want "
                           "to take? "))
                if not validate_deduct(bean_pile, deduct):
                    print("\nInvalid move. Try again.")
                else:
                    break

            # Deduct beans from pile
            bean_pile -= deduct

    # Display winner
    if turn == COMPUTER_NAME:
        print("\nI won. Sorry for your loss.")
    else:
        print("\n", player_name, ", somehow you won. Congrats!", sep = "")

main()

