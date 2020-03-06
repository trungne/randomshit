theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

#check row, column and diagonal
position = [[0,1,2],
            [3,4,5],
            [6,7,8],

            [0,3,6],
            [1,4,7],
            [2,5,8],

            [0,4,8],
            [2,4,6]]

#default turn, X goes first.
turn = 'X'

for i in range(9): #9 possible moves
    printBoard(theBoard)

    print('Now is '+turn+'.'+' Please make your move.')
    move = input()
    theBoard[move] = turn

#check winning condition
    ListOfMoves = list(theBoard.values())
    count = 0
    for x in position:
        if count == 3:
            break
        else: count = 0
        for y in x:
            if ListOfMoves[y] == turn:
                count += 1

            if count == 3:
                print('The winner is ' + turn)
                printBoard(theBoard)
                break

    if count == 3:
        break

    #switch turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'


