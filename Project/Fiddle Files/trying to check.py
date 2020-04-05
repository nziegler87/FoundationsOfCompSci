from stack import Stack

def check_winner(lst):
    ''' Name: check_winner
        Parameter: a list of items
        Returns: if there is a streak of items four or great in the list,
                 a tuple with (True, item)
    '''
    streak = create_streak(lst)
    return(check_four(streak))
    
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
                return winner

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

lst = [[["a", "a", "a", "a],
      [4, 5, 6, 7],
      [8, 9, 10, 11],
      [12, 13, 14, 15]],
     [[0, 4, 8, 12],
      [1, 5, 9, 13],
      [2, 6, 10, 14],
      [1, 1, 1, 1]],
     [[12],
      [8, 13],
      [4, 9, 14],
      [0, 5, 10, 15],
      [1, 6, 11],
      [2, 7],
      [3]],
     [[0],
      [4, 1],
      [8, 5, 2],
      [12, 9, 6, 3],
      [13, 10, 7],
      [14, 11],
      [15]]]

def check_win(lst):
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            winner = check_winner(lst[i][j])
            if winner:
                return winner
