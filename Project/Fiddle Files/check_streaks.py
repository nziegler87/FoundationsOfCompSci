from stack import Stack

def check_winner(lst):
    tuples = create_streak(lst)
    print(tuples)
    check_four(tuples)

def check_four(lst_of_tuples):
    for i in range(len(lst_of_tuples)):
        if lst_of_tuples[i][0] >= 4 and lst_of_tuples[i][1] != "":
            winner = lst_of_tuples[i][1]
            print("The winner is", winner)

def create_streak(lst):
    stack = Stack()
    streak = []
    count = 1

    for i in range(len(lst) - 1, -1, -1):
        stack.push(lst[i])

    # get first item and remove it from stack
    while not stack.is_empty():
        item = stack.top()
        stack.pop()

        if stack.top() == item:
            count += 1
        else:
            streak.append((count,item))
            count = 1

    return streak
