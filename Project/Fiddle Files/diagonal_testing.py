grid_a = [["A", "B", "C", "D", "D"],
          ["F", "G", "H", "I", "J"],
          ["K", "L", "M", "N", "O"],
          ["P", "Q", "R", "S", "T"],
          ["U", "V", "W", "X", "Y"]]


ROW = 3
COL = 4

matrix = [[1, 2, 3, "a"],
          [4, 5, 6, "b"],
          [7, 8, 9, "c"]]

def diagonal_LT(matrix):
    for line in range(1, ROW + COL):
        start_col = max(0, line - ROW)
        count = min(line, (COL - start_col), ROW)
        for j in range(count):
            print(matrix[min(ROW, line) - j - 1][start_col + j], end = " ")
        print()

def diagonal_LT_reverse(matrix):
    for i in range(ROW + COL - 1, 0, -1):
        start_col = max(0, i - ROW)
        count = min(i, (COL - start_col), ROW)
        for j in range(count - 1, -1, -1):
            print(matrix[min(ROW, i) - j - 1][start_col + j], end = " ")
        print()

def diagonal_RT(matrix):
    for line in range(1, ROW + COL):
        if line <= COL:
            start_col = COL - 1
        else:
            start_col -= 1
        if ROW == COL:
            if line <= COL:
                count = line
            else:
                count -= 1
        elif COL > ROW:
            if line <= COL:
                count = line
            elif line == COL + 1:
                count = ROW
            else:
                count -= 1


        for j in range(count - 1, -1, -1):
            print(matrix[min(ROW, line) - j - 1][start_col - j], end = " ")
        print()




# breakdown of first matrix

##for i in range (1, 6):      # i = 1
##    start_col = max(0, 1 - 3) # answer = 0
##    count = min(1, (3 - 0), 3) # answer = 1
##    for j in range(0, 1)
##        print(matrix[min(3, 1) - 0 - 1][0 + 0])
##
##for i in range (1, 6):     # i = 2
##    start_col = max(0, 2 - 3) # answer = 0
##    count = min(2, (3 - 0), 3) # answer = 2
##    for j in range(0, 2):
##        print(matrix[min(3, 2) - 0 - 1][0 + 0])
##        print(matrix[min(3, 2) - 1 - 1][0 + 1])
##
##for i in range (1, 6): # i = 3
##    start_col = max(0, 3 - 3)   # 0
##    count = min(3, (3 - 0), 3)  # 3
##    for j in range(0, 3):
##        print(matrix[min(3, 3) - 0 - 1][0 + 0])
##        print(matrix[min(3, 3) - 1 - 1][0 + 1])
##
##for i in range (1, 6): # i = 4
##    start_col = max(0, 4 - 3)  # answer = 1
##    count = min(4, (3 - 1), 3) # answer = 2
##    for j in range(0, 2):
##        print(matrix[min(3, 4) - 0 - 1][1 + 0])
##        print(matrix[min(3, 4) - 1 - 1][1 + 1])
##
##for in range (1, 6): # i = 5
##    start_col = max(0, 5 - 3) # answer = 2
##    count = min(5, (3 - 2), 3) # answer = 1
##    for j in range(0, 1):
##        print(matrix[min(3, 5) - 0 - 1][2 + 0]
                    
