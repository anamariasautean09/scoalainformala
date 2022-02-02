#alegerea incepatorului  choice
#alegerea unei pozitii
#descriere algoritm

"""
import random

jucator = ["human", "robot"]
if random.choice(jucator) == jucator[0]:
    input("Jucatorul alege prima mutare")
if random.choice(jucator) == jucator[1]:
    print("Robotul alege prima mutare")

Board = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}
def printBoard(board):
    print(board['1'] + '  |'+board['2']+'  |'+board['3'])
    print('---|---|---')
    print(board['4'] + '  |'+board['5']+'  |' + board['6'])
    print('---|---|---')
    print(board['7'] + '  |'+board['8']+'  |' + board['9'])
printBoard(Board)

"""
#Create a dictionary
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|'+board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|'+board['mid-M']+'|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|'+board['low-M']+'|' + board['low-R'])
printBoard(theBoard)
import random
def resetBoard(board):
    for k in board.keys():
        board[k]=' '
resetBoard(theBoard)
#Let's take two players
players = ['X','O']
turn = random.choice(players)
for i in range(9):
    print("Turn for "+turn+ ". Which place you want go?")
    print("Your choices are :")
    for k in theBoard.keys():
        if theBoard[k]== ' ':
            print(k,end=" ")
    move = input()
    if move not in theBoard.keys():
        print("Incorrect Move")
    theBoard[move] = turn
    isWon = isWinner(theBoard,turn)
    if isWon:
        print("Congratulations!!")
        printBoard(theBoard)
        #If someone is winner then reset the board for the next game
        resetBoard(theBoard)
        break
    if turn=='X':
        turn = 'O'
    else:
        turn = 'X'
    if i==8:
        print("Match draw!!")


def isWinner(board, turn):
    if not board['top-L'] == ' ' and board['top-L'] == board['top-M'] and not board['top-M'] == ' ' and board[
        'top-M'] == board['top-R']:
        print(board['top-L'] + " Is the Winner")
        return True
    elif not board['mid-L'] == ' ' and board['mid-L'] == board['mid-M'] and not board['mid-M'] == ' ' and board[
        'mid-M'] == board['mid-R']:
        print(board['mid-L'] + " Is the Winner")
        return True

    elif not board['low-L'] == ' ' and board['low-L'] == board['low-M'] and not board['low-M'] == ' ' and board[
        'low-M'] == board['low-R']:
        print(board['low-L'] + " Is the Winner")
        return True
    elif not board['top-L'] == ' ' and board['top-L'] == board['mid-L'] and not board['mid-L'] == ' ' and board[
        'mid-L'] == board['low-L']:
        print(board['top-L'] + " Is the Winner")
        return True
    elif not board['top-M'] == ' ' and board['top-M'] == board['mid-M'] and not board['mid-M'] == ' ' and board[
        'mid-M'] == board['low-M']:
        print(board['top-M'] + " Is the Winner")
        return True

    elif not board['top-R'] == ' ' and board['top-R'] == board['mid-R'] and not board['mid-R'] == ' ' and board[
        'mid-R'] == board['low-R']:
        print(board['top-R'] + " Is the Winner")
        return True

    #     Digonals check
    elif not board['top-L'] == ' ' and board['top-L'] == board['mid-M'] and not board['mid-M'] == ' ' and board[
        'mid-M'] == board['low-R']:
        print(board['top-L'] + " Is the Winner")
        return True

    elif not board['top-R'] == ' ' and board['top-R'] == board['mid-M'] and not board['mid-M'] == ' ' and board[
        'mid-M'] == board['low-L']:
        print(board['top-R'] + " Is the Winner")
        return True