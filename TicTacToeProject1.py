import random

# Declarations
board = [ ["_", "_", "_"] , ["_", "_", "_"] , ["_", "_", "_"] ]

################ Functions ################
# This function check if the game move is valid
def isValidMove(row, column):
    if row in range(3) and column in range(3):
        if (board[row][column] == "_"):
            return True
        else:
            return False
    else:
        return False

# This function check valid input
def checkInput(input):
        if input.isdigit() == True:
            return True
        return False
    

# This function prints all board elements  
def printBaord():
    for row in board:
        for col in row:
            print(col, end = ' ')
        print("\n")



# This function determain who is the winner
def isParticipateWon(X_or_O):
    if (X_or_O == 'X'):
        sign = 'X'
    else:
        sign = 'O'

    if (board[0][0] == sign and board[1][1] and sign and board[2][2] == sign
        or board[0][2] == sign and board[1][1] == sign and board[2][0] == sign
        or board[0][0] == sign and board[0][1] == sign and board[0][2] == sign
        or board[1][0] == sign and board[1][1] == sign and board[1][2] == sign
        or board[2][0] == sign and board[2][1] == sign and board[2][2] == sign
        or board[0][0] == sign and board[1][0] == sign and board[2][0] == sign
        or board[0][1] == sign and board[1][1] == sign and board[2][1] == sign
        or board[0][2] == sign and board[1][2] == sign and board[2][2] == sign):
        return True
    else:
        return False
        
############ Main ###################
print("Tic Tac Tow - manue")
print("Press C if you want to play against the computer")
print("Press CC if you want two computers will play")
print("Press P if you want to play against somevody else")
print("Start to pay")
option = input()

printBaord()
turn = 0 
isX_won = False
isO_won = False




######################## Playing against somebody else ##################3
# if option == 'P':
# Play until there is a winner or there is a tie
while isX_won == False and isO_won == False and turn < 9:
    row_input = input("Enter row:")
    col_input = input("Enter column:")
    if checkInput(row_input) == True and checkInput(col_input) == True:
        row = int(row_input)
        col = int(col_input)
        if isValidMove(row, col) == True:
        # move is valid
            if turn % 2 == 0: # Turn of X
                board[row][col] = 'X'
            elif option == 'P': # Turn of O
                board[row][col] = 'O'
        printBaord()

        if isParticipateWon('X') == True:
            isX_won = True
        if  isParticipateWon('O') == True:
            isO_won = True
        turn+=1       
    else:
        print("Error, please try again")

###################### Check the game state #####################
if isX_won == True:
    print("The winner is X")
elif isO_won == True:
   print("The winner is O")
else:
    print("Tie!")
