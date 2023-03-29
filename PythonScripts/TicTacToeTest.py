################################################################################
#
#      filename:  TicTacToe.py
#
#   description:  A two player game of TicTacToe
#
#        author:  Minter, Erik
# AMU e-mail id:  erik.minter@my.avemaria.edu
#
#        course:  CSCI 201: Introduction to Computer Programming
#    instructor:  Dr. Perugini
#    assignment:  Homework IX
#
#      assigned:  March 23, 2023
#           due:  April 4, 2023
#
################################################################################
emptyBoard = ['1','2','3','4','5','6','7','8','9']
board1 = ['X','O','X','O','X','O','O','X','O']
board2 = ['X','O','X','O','O','O','O','X','O']
board3 = ['1','X','3','X','5','O','7','8','O']
board4 =['1','2','3','X','5','O','7','O','9']

XWon=False
OWon=False
#*******************************************************************************
#         purpose: To play the game
# 
# input parameter: list
#    return value: a new list
#******************************************************************************/
def playGame():
    print("A Game of Tic Tac Toe\n\n")
    print("Current Status of Board:")
    emptyBoard = ['1','2','3','4','5','6','7','8','9']
    B=['1','2','3','4','5','6','7','8','9']
    printBoard(B)
    used=[]
    X=None
    O=None
#Player X
    while keepPlaying(B)==True:
        X=int(input("Player X, Select a Tile By Position: "))
        if X>=1 and X<=9:
            if B[X-1]!='O' and X not in used:
                index=X-1
                B[index]='X'
                print("\nCurrent Status Of Board:")
                printBoard(B)
                used+=[X]
            while B[X-1]=='O' and X in used:
                print("The tile in position", emptyBoard[X-1],"is occupied")
                print("\nCurrent Status Of Board:")
                printBoard(B)
                X=int(input("Player X, Select a Tile By Position: "))
                if X>=1 and X<=9:
                    if B[X-1]!='O' and X not in used:
                        index=X-1
                        B[index]='X'
                        print("\nCurrent Status Of Board:")
                        printBoard(B)
                        used+=[X]
                while X<1 or X>9:
                    print("That is not a valid position")
                    print("Current Status Of Board:")
                    printBoard(B)
                    X=int(input("Player X, Select a Tile By Position: "))
                    if X>=1 and X<=9:
                        if B[X-1]!='O' and X not in used:
                            index=X-1
                            B[index]='X'
                            print("\nCurrent Status Of Board:")
                            printBoard(B)
                            used+=[X]
        while X<1 or X>9:
            print("That is not a valid position")
            print("Current Status Of Board:")
            printBoard(B)
            X=int(input("Player X, Select a Tile By Position: "))
            if X>=1 and X<=9:
                if B[X-1]!='O' and X not in used:
                    index=X-1
                    B[index]='X'
                    print("\nCurrent Status Of Board:")
                    printBoard(B)
                    used+=[X]
            while B[X-1]=='O' and X in used:
                print("The tile in position", emptyBoard[X-1],"is occupied")
                print("\nCurrent Status Of Board:")
                printBoard(B)
                X=int(input("Player X, Select a Tile By Position: "))
                if X>=1 and X<=9:
                    if B[X-1]!='O' and X not in used:
                        index=X-1
                        B[index]='X'
                        print("\nCurrent Status Of Board:")
                        printBoard(B)
                        used+=[X]
#Player O      
        if keepPlaying(B)==True:
            O=int(input("Player O, Select a Tile By Position: "))
            if O>=1 and O<=9:
                if B[O-1]!='X' and O not in used:
                    index=O-1
                    B[index]='O'
                    print("Current Status Of Board:")
                    printBoard(B)
                    used+=[O]
                while B[O-1]=='X' and O in used:
                    print("The tile in position", emptyBoard[O-1],"is occupied")
                    print("Current Status Of Board:")
                    printBoard(B)
                    O=int(input("Player O, Select a Tile By Position: "))
                    if O>=1 and O<=9:
                        if B[O-1]!='X' and O not in used:
                            index=O-1
                            B[index]='O'
                            print("Current Status Of Board:")
                            printBoard(B)
                            used+=[O]
                    while O<1 or O>9:
                        print("That is not a valid position")
                        print("Current Status Of Board:")
                        printBoard(B)
                        O=int(input("Player O, Select a Tile By Position: "))
                        if O>=1 and O<=9:
                            if B[O-1]!='X' and O not in used:
                                index=O-1
                                B[index]='O'
                                print("Current Status Of Board:")
                                printBoard(B)
                                used+=[O]
            while O<1 or O>9:
                print("That is not a valid position")
                print("Current Status Of Board:")
                printBoard(B)
                O=int(input("Player O, Select a Tile By Position: "))
                if O>=1 and O<=9:
                    if B[O-1]!='X' and O not in used:
                        index=O-1
                        B[index]='O'
                        print("Current Status Of Board:")
                        printBoard(B)
                        used+=[O]
                while B[O-1]=='X' and O in used:
                    print("The tile in position", emptyBoard[O-1],"is occupied")
                    print("Current Status Of Board:")
                    printBoard(B)
                    O=int(input("Player O, Select a Tile By Position: "))
                    if O>=1 and O<=9:
                        if B[O-1]!='X' and O not in used:
                            index=O-1
                            B[index]='O'
                            print("Current Status Of Board:")
                            printBoard(B)
                            used+=[O]              
    else:
        if OWon==False and XWon==False:
            print("Game Ended in a Tie.")
        if OWon==True:
            print("Player O WINS")
        elif XWon==True:
            print("Player X WINS")
        play=(input("Play again? (y/n): "))
        if play=='Y' or play=='y' or play=="Yes" or play=='yes':
            playGame()
        else:
            print("Thanks for Playing!")
            
            
#*******************************************************************************
#         purpose: To print the board
# 
# input parameter: list
#    return value: list
#******************************************************************************/    
def printBoard(B): 
    B=print("+-----------+", "\n|",B[0],"|",B[1],"|", B[2],"|","\n|",B[3],"|",B[4],"|",B[5],"|","\n|",B[6],"|",B[7],"|",B[8],"|",end="\n"),print("+-----------+")
    return B
#*******************************************************************************
#         purpose: To see if all the elements in a list are occupied by O or X
# 
# input parameter: list
#    return value: True or False
#******************************************************************************/ 
def allTilesOccupied(B):
    for element in B:
        if element != 'X' and element != 'O':
            return False
    return True
#*******************************************************************************
#         purpose: To see if the game has ended
# 
# input parameter: Two other functions
#    return value: True or False
#******************************************************************************/
def keepPlaying(B):
    if someoneWon(B)==False and allTilesOccupied(B)==False:
        return True
    else:
        return False
#*******************************************************************************
#         purpose: To see if someone won
# 
# input parameter: list
#    return value: True or False
#******************************************************************************/
def someoneWon(B):
    if B[0:3]==['X','X','X'] or B[3:6]==['X','X','X'] or B[6:9]==['X','X','X'] or (B[0]=='X' and B[4]=='X' and B[8]=='X') or (B[2]=='X' and B[4]=='X' and B[6]=='X') or (B[0]=='X' and B[3]=='X' and B[6]=='X') or (B[1]=='X' and B[4]=='X' and B[7]=='X') or (B[2]=='X' and B[5]=='X' and B[8]=='X'):
        global XWon
        XWon=True
        return XWon
    if B[0:3]==['O','O','O'] or B[3:6]==['O','O','O'] or B[6:9]==['O','O','O'] or (B[0]=='O' and B[4]=='O' and B[8]=='O') or (B[2]=='O' and B[4]=='O' and B[6]=='O') or (B[0]=='O' and B[3]=='O' and B[6]=='O') or (B[1]=='O' and B[4]=='O' and B[7]=='O') or (B[2]=='O' and B[5]=='O' and B[8]=='O'):
        global OWon
        OWon=True
        return OWon
    else:
        return False
    
playGame()