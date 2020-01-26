'''
    Nathanial Ziegler
    CS 5001
    January 29, 2020
    HW3
    Description:
        Game of NIM with one pile of beans, ranging from 5 and 30.
'''

import random

from nim_functions import *

def main():

    # Introduce game and collect user name
    print("Welcome! Let's play a game of NIM.\nA coin toss will determine "
          "who goes first.\n")
    player_name = input("But first who am I playing against? "
                        "Enter your name: ")

    # Coin toss to select first player
    user_choice = user_coin_selection(player_name)
    toss_result = coin_flip(random.randint(1,2))
    turn = coin_toss_result(user_choice, toss_result, player_name)
    if turn == "computer":
        print("\nYou lost the coin toss. I get to go first!\n")
    else:
        print("\n", player_name, ", you won the coint toss, so you go "
              "first.\n", sep = "")
    
    # Set size of bean pile
    bean_pile = random.randint(5, 30)
    print("We are starting with a pile of", bean_pile, "beans.")

    # Start of game
    while not is_over(bean_pile):

        # Computer action
        if turn == "computer":
            # Switch player for next term
            turn = player_name

            # Collect number of beans to remove from pile
            deduct = computer_deduct(bean_pile)

            # Deduct beans from pile
            bean_pile -= deduct
            print("\nI took", deduct, "bean(s).")

        # Player action
        else:
            # Switch player for next term
            turn = "computer"

            # Collect number of beans to remove from pile
            deduct = user_deduct(bean_pile)

            # Deduct beans from pile
            bean_pile -= deduct

    # Display winner
    if turn == "computer":
        print("\nI won. Sorry for your loss.")
    else:
        print("\n", player_name, ", somehow you won. Congrats!", sep = "")

main()

