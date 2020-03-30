
row = 6
col = 7

board = []
count = 0

for r in range(row):
    temp_row = []
    for c in range(col):
        temp_row.append([count, r, c])
        count += 1
    board.append(temp_row)

for col in board:
    print(col)
