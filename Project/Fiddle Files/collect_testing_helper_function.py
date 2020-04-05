>>> game = Game()
>>> game.board.get_dimensions()
>>> game.board.setup_board()
>>> count = 0
>>> for i in range(len(game.board.board)):
	for j in range(len(game.board.board[i])):
		game.board.board[i][j].filled = count
		count += 1
