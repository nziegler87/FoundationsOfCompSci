from graphics import Graphics
from game_piece import Game_Piece
from game_test import Game
import time

WHITE = "./images/white_piece_90.gif"
RED = "./images/red_piece_90.gif"
YELLOW = "./images/yellow_piece_90.gif"

graphics = Graphics()
game = Game()

graphics.add_shape(WHITE)
graphics.add_shape(RED)
graphics.add_shape(YELLOW)

count = 0

for i in range(-200, 201, 100):
    for j in range(200, -201, -100):
        piece = Game_Piece(count, i, j, WHITE)
        game.add_piece(count, WHITE, i, j)
        graphics.draw_piece(piece.identifier, piece.x, piece.y, piece.image, piece.size, piece.color)
        count += 1

pieces = game.return_dict()

print(pieces)



for i in range(4):
    graphics.update_piece(pieces[i][0], pieces[i][1], pieces[i][2], RED)
    time.sleep(.1)
    graphics.update_piece(pieces[i][0], pieces[i][1], pieces[i][2], WHITE)
graphics.update_piece(pieces[4][i], pieces[4][1], pieces[4][2], RED)

time.sleep(1)

for i in range(0, 3, 1):
    graphics.update_piece(pieces[i][0], pieces[i][1], pieces[i][2], YELLOW)
    time.sleep(.1)
    graphics.update_piece(pieces[i][0], pieces[i][1], pieces[i][2], WHITE)
graphics.update_piece(pieces[3][i], pieces[3][1], pieces[3][2], YELLOW)

time.sleep(1)

for i in range(5, 9, 1):
    graphics.update_piece(pieces[i][0], pieces[i][1], pieces[i][2], RED)
    time.sleep(.1)
    graphics.update_piece(pieces[i][0], pieces[i][1], pieces[i][2], WHITE)
graphics.update_piece(pieces[9][i], pieces[9][1], pieces[9][2], RED)
