import random

def clearBoard():
	'''
	Print 10 lines to clear the previous board
	'''
	print('\n'*10)


def displayBoard(board):
	'''
	Display the current board
	'''
	clearBoard()
	print(board[7]+' | '+board[8]+' | '+board[9])
	print("---------")
	print(board[4]+' | '+board[5]+' | '+board[6])
	print("---------")
	print(board[1]+' | '+board[2]+' | '+board[3])


def placeMarker(board, marker,position):
	'''
	Place the player 1 and player markers on the board internally
	'''
	board[position] = marker

def winCheck(board, mark):
	'''
	All rows share the same marker
	All columns share the same marker
	2 diagonals share the same marker
	'''
	return ((board[1] == board[2] == board[3] == mark) or
	(board[4] == board[5] == board[6] == mark) or
	(board[7] == board[8] == board[9] == mark) or
	(board[1] == board[4] == board[7] == mark) or
	(board[2] == board[5] == board[8] == mark) or
	(board[3] == board[6] == board[9] == mark) or
	(board[1] == board[5] == board[9] == mark) or
	(board[3] == board[5] == board[7] == mark))


def chooseFirst():
	'''
	Randomly decide which player will play first
	'''
	flip = random.randint(0,1)

	if flip == 0:
		return 'Player 1'
	else:
		return 'Player 2'


def checkFreeSpace(board, position):
	'''
	Check for free space on the board to play the next turn
	'''
	return board[position] == ''


def checkBoardIsFull(board):
	'''
	Check if the the board is full to declare a draw
	'''
	for i in range(1,10):
		if checkFreeSpace(board, i):
			return False
	#Board is Full if retruned True
	return True

def playerChoice(board, turn):
	'''
	check if the player choice is a valid move
	'''
	value = 0
	possible = [1,2,3,4,5,6,7,8,9]
	if value not in possible or not checkFreeSpace(board,position):
		position = int(input(turn+' choose a position 1-9: '))

	return position

def replayGame():
	'''
	ASk if the players want to play again
	'''
	choice = input("Play again? Enter yes or no: ")
	return choice=='yes'


def playGame():
	'''
	Ask the player to choose a marker and assign the other marker to player 2
	'''
	marker = ''
	#ASK the player to choose 'x' or 'o'
	while marker!='x' and marker!='o':
		marker = input('Player 1 choose x or o:')

	player1= marker

	if player1 == 'x':
		player2 = 'o'
	else:
		player2 = 'x'

	return player1, player2

#Construct the default board
theBoard = ['']*10
#While loop to run the game
print("Welcome to Tic Tac Toe!!")
while True:
	theBoard = ['']*10
	player1Marker, player2Marker = playGame()
	turn = chooseFirst()
	print(turn + " will go first!")

	playGame= input("Ready to play game? yes or no?")
	if playGame == 'yes':
		game = True
	else:
		game = False

	while game:
		if turn  == 'Player 1':
			displayBoard(theBoard)
			position = playerChoice(theBoard, turn)
			placeMarker(theBoard, player1Marker,position)
			if winCheck(theBoard,player1Marker):
				displayBoard(theBoard)
				print('Player 1 has won!!')
				game = False
			elif checkBoardIsFull(theBoard):
					displayBoard(theBoard)
					print("TIE GAME")
					game = False
			else:
				turn = 'Player 2'

		else:
			displayBoard(theBoard)
			position = playerChoice(theBoard,turn)
			placeMarker(theBoard, player2Marker,position)
			if winCheck(theBoard,player2Marker):
				displayBoard(theBoard)
				print('Player 2 has won!!')
				game = False
			elif checkBoardIsFull(theBoard):
					displayBoard(theBoard)
					print("TIE GAME")
					game = False
		
			else:
				turn = 'Player 1'


#break while loop on replayGame function()
	if not replayGame():
		break
