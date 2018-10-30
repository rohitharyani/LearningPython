#Gloabal variables
board = [' ']*10
game_state = True
announce = ''

def clear():
	print('\n'*10)

def reset_board():
	global board, game_state
	board = [' ']*10
	game_state = True

def display_board():
	clear()
	print(board[7]+' | '+board[8]+' | '+board[9])
	print("---------")
	print(board[4]+' | '+board[5]+' | '+board[6])
	print("---------")
	print(board[1]+' | '+board[2]+' | '+board[3])

def win_check(board, mark):
	return ((board[1] == board[2] == board[3] == mark) or
	(board[4] == board[5] == board[6] == mark) or
	(board[7] == board[8] == board[9] == mark) or
	(board[1] == board[4] == board[7] == mark) or
	(board[2] == board[5] == board[8] == mark) or
	(board[3] == board[6] == board[9] == mark) or
	(board[1] == board[5] == board[9] == mark) or
	(board[3] == board[5] == board[7] == mark))


	