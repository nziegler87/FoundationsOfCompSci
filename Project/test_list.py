from graphics import Graphics
from game_piece import Game_Piece
from game import Game
import time

WHITE = "./images/white_piece_90.gif"
RED = "./images/red_piece_90.gif"
YELLOW = "./images/yellow_piece_90.gif"

SIZE = 100
COLOR = "blue"

graphics = Graphics()
game = Game()
game2 = Game()

graphics.add_shape(WHITE)
graphics.add_shape(RED)
graphics.add_shape(YELLOW)


count = 0
num_row = 2
num_col = 2
x_start = -250
y_start = 250

x_end = x_start + SIZE * num_row
y_end = y_start - SIZE * num_col



for col in range(y_start, y_end, -SIZE):
    temp_row = []
    column = 1
    for row in range(x_start, x_end, SIZE):
        piece = Game_Piece(column, row, col, WHITE, SIZE, COLOR)
        game.add_piece(count, WHITE, row, col)
        graphics.draw_piece(piece.identifier, piece.x, piece.y, piece.image, piece.size, piece.color)
        temp_row.append(piece)
        column += 1
    game.board.append(temp_row)

turn = input("Red or Yellow?\n").lower()

while True:
    place_col = int(input("What column?\n")) - 1
    if turn == "red":
        color = RED
    else:
        color = YELLOW
    piece = game.drop_piece(place_col, color, turn)
    graphics.update_piece(piece.identifier, piece.x, piece.y, color)
    print("Row Streaks")
    game.check_horizontal_streak()
    print("Column Streaks")
    game.check_vertical_streak()
    print("Full Board Check")
    game.check_full()

    if turn == "red":
        turn = "yellow"
    else:
        turn = "red"
    




##color = "red"
##image = RED
##
##for i in range(len(game.board)):
##    for j in range(len(game.board[0])):
##        piece = game.board[i][j]
##        piece.fill_piece(color)
##        graphics.update_piece(piece.identifier, piece.x, piece.y, image)
##        time.sleep(1)
##        if color == "red":
##            color = "yelow"
##            image = YELLOW
##        else:
##            color = "red"
##            image = RED
##
##
##
##for i in range(len(game.board)):
##    for j in range(len(game.board[0])):
##        print(game.board[i][j])

