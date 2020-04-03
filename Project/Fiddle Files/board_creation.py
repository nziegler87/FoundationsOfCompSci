
X_START = -250
Y_START = 300
SIZE = 100

def create_board(rows, cols):
    board = []
    y = Y_START
    for i in range(rows):
        x = X_START
        temp_row = []
        for j in range(cols):
            temp_row.append((x, y))
            x += SIZE
        board.append(temp_row)
        y -= SIZE
    print(board)

def create_board2(rows, cols):
    board = []
    for i in range(rows):
        temp_row = []
        for j in range(cols):
            temp_row.append([i,j,"empty"])
        board.append(temp_row)
    print(board)
    
def add_cords(lst):
    y = Y_START
    for i in range(len(lst)):
        x = X_START
        for j in range(len(lst[0])):
            lst[i][j][2] = str(x) + "-" + str(y)
            x += SIZE
        y -= SIZE

    print(lst)
                   
board = [[(-250, 300), (-150, 300), (-50, 300), (50, 300)],
         [(-250, 200), (-150, 200), (-50, 200), (50, 200)],
         [(-250, 100), (-150, 100), (-50, 100), (50, 100)],
         [(-250, 0), (-150, 0), (-50, 0), (50, 0)]]
