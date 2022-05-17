import pygame , sys , time
import numpy as np

pygame.init()

#measurements
width = 600
height = 600
lineWidth = 14
boardRows = 3
boardColumns = 3
circleRadius = 60
circleWidth = 15
crossWidth = 25
space = 55

#colors
boardColor = (255,250,205)
lineColor = (245,222,179) #mor de bejul asta
finalColor = (204,149,68)

screen = pygame.display.set_mode( ( width , height ) )
pygame.display.set_caption('EL LEVI GAME')
screen.fill( boardColor )

board = np.zeros( ( boardRows , boardColumns ) )

def target ( row , col , player ) :
    board[row][col] = player
def availableTarget ( row , col ) :
    if ( board[row][col] == 0 ) :
        return True
    else : return False
def freeSpaces() :
    for row in range(boardRows) :
        for col in range(boardColumns) :
            if board[row][col] == 0 :
                return False
    return True

def printTargets( row , column , player ) :
    if player == 1 :
        pygame.draw.line( screen , lineColor , ( column * 200 + space , row * 200 + 200 - space ) , ( column * 200 + 200 - space , row * 200 + space ) ,crossWidth )
        pygame.draw.line( screen , lineColor , ( column * 200 + space , row * 200 + space ) , ( column * 200 + 200 - space , row * 200 + 200 - space ) , crossWidth )
    if player == 2 :
        pygame.draw.circle( screen , lineColor , ( int( column * 200 + 100 ) , int( row * 200 + 100 ) ) , circleRadius , circleWidth )
def printLines() :
  pygame.draw.line ( screen , lineColor , (0,200) , (600,200) , lineWidth ) #1st horizontal
  pygame.draw.line ( screen , lineColor , (0,400) , (600,400) , lineWidth ) #2nd horizontal

  pygame.draw.line ( screen , lineColor , (200,0) , (200,600) , lineWidth ) #1st vertical
  pygame.draw.line ( screen , lineColor , (400,0) , (400,600) , lineWidth ) #2nd vertical
def printWinningLine( mode, row ) :
    if mode == 1 :
        Y = row * 200 + 100
        pygame.draw.line( screen , finalColor , ( 15 , Y ) , ( width - 15 , Y ) , 15 )
    elif mode == 2 :
        X = row * 200 + 100
        pygame.draw.line( screen , finalColor , ( X , 15 ) , ( X , height - 15 ) , 15 )
    elif mode == 3 :
        pygame.draw.line(screen, finalColor, (15, 15), (width - 15, height - 15), 16)
    elif mode == 4 :
        pygame.draw.line(screen, finalColor, (15, height - 15), (width - 15, 15), 16)
    pygame.display.update()

def checkWinner() :
    for row in range(boardRows) :
        if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != 0 :
            printWinningLine(1 , row)
            return 0
        elif board[0][row] == board[1][row] and board[1][row] == board[2][row] and board[0][row] != 0 :
            printWinningLine(2 , row)
            return 0
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != 0 :
        printWinningLine(3 , 0)
        return 0
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] != 0 :
        printWinningLine(4 , 0)
        return 0
    elif freeSpaces() == True :
        return 0
    return 1
printLines()

player = 1

while checkWinner() :
    for event in pygame.event.get() :
        if event.type == pygame.quit:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN :
            mX = event.pos[1]
            mY = event.pos[0]
            clickedRow = int( mX // 200 )
            clickedColumn = int( mY // 200 )
            if availableTarget( clickedRow , clickedColumn ) :
                if player == 1 :
                    target( clickedRow , clickedColumn , player )
                    printTargets(clickedRow, clickedColumn, player)
                    player = 2
                elif player == 2 :
                    target( clickedRow , clickedColumn , player )
                    printTargets( clickedRow , clickedColumn , player )
                    player = 1

    pygame.display.update()
time.sleep(3)
