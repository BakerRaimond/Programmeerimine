#tic tac toe
# python: Tic Tac Toe Game

import random

# The Game Board
board = [0,1,2,
         3,4,5,
         6,7,8]
def show() :
    print(board[0],'|',board[1],'|',board[2])
    print('--------')
    print(board[3],'|',board[4],'|',board[5])
    print('--------')
    print(board[6],'|',board[7],'|',board[8])

def checkLine(char, spot1, spot2, spot3,):
    if board[spot1] == char and board[spot2] == char and board[spot3] ==  char:
        return True
    
def checkAll(char) :
    if checkLine(char, 1, 2, 3):
        return True
    if checkLine(char, 4, 5, 6):
        return True
    if checkLine(char, 7, 8, 9):
        return True
    if checkLine(char, 1, 4, 7):
        return True
    if checkLine(char, 2, 5, 8):
        return True
    if checkLine(char, 3, 6, 9):
        return True
    if checkLine(char, 1, 5, 9):
        return True
    if checkLine(char, 3, 5, 7):
        return True
    
        
    
while True:

    a = int(input("Select a spot:"))
    

    if board[a] != 'x' and board[a] != 'o':
        board[a] = 'x'

        if checkAll('x') == True:
            print("~~ X WINS ~~")
            break;
     
        
        while True:
            random.seed() # gives a random generator
            opponent = random.randint(0,8)

            if(board[opponent] != 'o' and board[opponent] != 'x'):
                 board[opponent] = 'o'
                 
        if checkAll('o') == True:
            print("~~ O WINS ~~")
            break;

    else:
        print('This spot is taken!')

    show()
