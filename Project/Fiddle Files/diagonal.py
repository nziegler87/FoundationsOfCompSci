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

grid_a = [["A", "B", "C", "D", "D"],
        ["F", "G", "H", "I", "J"],
        ["K", "L", "M", "N", "O"],
        ["P", "Q", "R", "S", "T"],
        ["U", "V", "W", "X", "Y"]]

grid_n = [["00", "01", "02", "yellow", "04", "05", "06"],
          ["10", "11", "12", "13", "yellow", "15", "16"],
          ["20", "21", "22", "red", "24", "yellow", "26"],
          ["30", "31", "red", "33", "34", "35", "yellow"],
          ["40", "red", "42", "43", "44", "45", "46"],
          ["red", "51", "52", "53", "54", "55", "56"]]

def diagonal(matrix):
    for i in range(1, (len(matrix) + len(matrix[0]))):
        start_col = max(0, i - len(matrix))
        count = min(i, (len(matrix[0]) - start_col), len(matrix))
        for j in range(0, count):
            print(matrix[min(len(matrix), i) - j - 1][start_col + j], end = " ")
        print()

def diagonal_LT(matrix):
    master = []
    for i in range(1, (len(matrix) + len(matrix[0]))):
        start_col = max(0, i - len(matrix))
        count = min(i, (len(matrix[0]) - start_col), len(matrix))
        mini = []
        for j in range(0, count):
            mini.append(matrix[min(len(matrix), i) - j - 1][start_col + j])
        master.append(mini)
    return master

def diagonal_TR(matrix):
    pass
                   
diagonal = diagonal_LT(grid_n)

for lst in diagonal:
    check_winner(lst)

