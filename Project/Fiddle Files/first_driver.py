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

##count = 0
##for row in range(-300, 300, 100):
##    for col in range(300, -400, -100):
##        piece = Game_Piece(count, row, col, WHITE, SIZE, COLOR)
##        game.add_piece(count, WHITE, row, col)
##        graphics.draw_piece(piece.identifier, piece.x, piece.y, piece.image, piece.size, piece.color)
##        count += 1
##pieces = game.return_dict()
##print(pieces)

count = 0
num_row = 9
num_col = 3
x_start = -300
y_start = 300

x_end = x_start + SIZE * num_row
y_end = y_start - SIZE * num_col

for col in range(y_start, y_end, -SIZE):
    for row in range(x_start, x_end, SIZE):
        piece = Game_Piece(count, row, col, WHITE, SIZE, COLOR)
        game2.add_piece(count, WHITE, row, col)
        graphics.draw_piece(piece.identifier, piece.x, piece.y, piece.image, piece.size, piece.color)
        count += 1
    


##for i in range(4):
##    graphics.update_piece(i, pieces[i][1], pieces[i][2], RED)
##    time.sleep(.1)
##    graphics.update_piece(i, pieces[i][1], pieces[i][2], WHITE)
##graphics.update_piece(i, pieces[4][1], pieces[4][2], RED)
##
##time.sleep(1)
##
##for i in range(0, 3, 1):
##    graphics.update_piece(i, pieces[i][1], pieces[i][2], YELLOW)
##    time.sleep(.1)
##    graphics.update_piece(i, pieces[i][1], pieces[i][2], WHITE)
##graphics.update_piece(i, pieces[3][1], pieces[3][2], YELLOW)
##
##time.sleep(1)
##
##for i in range(5, 9, 1):
##    graphics.update_piece(i, pieces[i][1], pieces[i][2], RED)
##    time.sleep(.1)
##    graphics.update_piece(i, pieces[i][1], pieces[i][2], WHITE)
##graphics.update_piece(i, pieces[9][1], pieces[9][2], RED)
