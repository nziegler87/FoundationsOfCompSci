from graphics import Graphics
from game_piece import Game_Piece
from game_board import Game_Board
from game import * ## SHOULD I SPECIFY WHICH FUNCTIONS LATER?

WHITE = "./images/white_piece_90.gif"
RED = "./images/red_piece_90.gif"
YELLOW = "./images/yellow_piece_90.gif"
ARROW = "./images/down_arrow.gif"

IMAGE_LIST = [WHITE, RED, YELLOW, ARROW]

SIZE = 100
COLOR = "blue"

def main():

    graphics = Graphics()
    g_board = Game_Board()

    for image in IMAGE_LIST:
        graphics.add_shape(image)






    count = 0
    num_row = 6
    num_col = 7
    x_start = -250
    y_start = 250

    x_end = x_start + SIZE * g_board.rows
    y_end = y_start - SIZE * g_board.columns


    # This draw the board
    for col in range(y_start, y_end, -SIZE):
        temp_row = []
        column = 1
        for row in range(x_start, x_end, SIZE):
            piece = Game_Piece(column, row, col, WHITE, SIZE, COLOR)
            g_board.add_piece(count, WHITE, row, col)
            graphics.draw_piece(piece.identifier, piece.x, piece.y, piece.image, piece.size, piece.color)
            temp_row.append(piece)
            column += 1
        g_board.board.append(temp_row)

    temp_x = -250
    temp_y = 350

    # This draw the arrows
    for i in range(num_row):
        graphics.draw_arrow(ARROW, temp_x, temp_y)
        temp_x += 100

    turn = input("Red or Yellow?\n").lower()

    while True:
        place_col = int(input(str(turn.capitalize()) + ", what column?\n")) - 1
        if turn == "red":
            color = RED
        else:
            color = YELLOW
        piece = g_board.drop_piece(place_col, color, turn)
        graphics.update_piece(piece.identifier, piece.x, piece.y, color)
        g_board.check_horizontal_streak()
        g_board.check_vertical_streak()
        g_board.check_full()

        if turn == "red":
            turn = "yellow"
        else:
            turn = "red"
        

main()


##color = "red"
##image = RED
##
##for i in range(len(g_board.board)):
##    for j in range(len(g_board.board[0])):
##        piece = g_board.board[i][j]
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
##for i in range(len(g_board.board)):
##    for j in range(len(g_board.board[0])):
##        print(g_board.board[i][j])

