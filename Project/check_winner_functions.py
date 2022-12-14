'''
    CS 5001
    Nathanial Ziegler
    April 2020
    Final Project
    Description:
        Functions used to check four in a row pieces
'''

from stack import Stack

# constant that makes it "Connect 4"
# changing this to n makes it "Connect n"
STREAK = 4

def check_winner(lst):
    ''' Name: check_winner
        Parameters: a list of items
        Returns: if there is a streak of n or greater in the list of items,
                 excluding blank lsts, item is returned
    '''
    streak = create_streak(lst)
    return(check_four(streak))
    
def check_four(tuples_list):
    ''' Name: check_four
        Parameters: list of tuples -- [(count (an int), item)]
        Returns: the first item with a streak of n or greater,
                 excluding blank lsts
    '''
    for i in range(len(tuples_list)):
        # looks for streak of four or greater, ignoring any blanks
        if tuples_list[i][0] >= STREAK and tuples_list[i][1] != "":
                winner = tuples_list[i][1]
                return winner

def create_streak(lst):
    ''' Name: create_streak
        Parameters: a list
        Returns: a list of tuples with list items reported as streaks --
                    [(count (an int), item),(count (an int), item)]
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
