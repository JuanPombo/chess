import pygame, sys
from pygame.locals import *
#import kingMove

pygame.init()
DISPLAYSURF = pygame.display.set_mode((640,640))
pygame.display.set_caption('Chess!')
clock = pygame.time.Clock()

BLACK = (  0,   0,   0) 
WHITE = (255, 255, 255) 
RED   = (255,   0,   0) 
GREEN = (  0, 255,   0) 
BLUE  = (  0,   0, 255)

sizePiece = (80,80)
#BLACK PIECES
kingB = pygame.transform.scale(pygame.image.load("piezas/KingB.png"),sizePiece)
queenB = pygame.transform.scale(pygame.image.load("piezas/QueenB.png"),sizePiece)
rookB0 = pygame.transform.scale(pygame.image.load("piezas/RookB.png"),sizePiece)
rookB1 = pygame.transform.scale(pygame.image.load("piezas/RookB.png"),sizePiece)
knightB0 = pygame.transform.scale(pygame.image.load("piezas/KnightB.png"),sizePiece)
knightB1 = pygame.transform.scale(pygame.image.load("piezas/KnightB.png"),sizePiece)
bishopB0 = pygame.transform.scale(pygame.image.load("piezas/BishopB.png"),sizePiece)
bishopB1 = pygame.transform.scale(pygame.image.load("piezas/BishopB.png"),sizePiece)
pawnB0 = pygame.transform.scale(pygame.image.load("piezas/PawnB.png"),sizePiece)
pawnB1 = pygame.transform.scale(pygame.image.load("piezas/PawnB.png"),sizePiece)
pawnB2 = pygame.transform.scale(pygame.image.load("piezas/PawnB.png"),sizePiece)
pawnB3 = pygame.transform.scale(pygame.image.load("piezas/PawnB.png"),sizePiece)
pawnB4 = pygame.transform.scale(pygame.image.load("piezas/PawnB.png"),sizePiece)
pawnB5 = pygame.transform.scale(pygame.image.load("piezas/PawnB.png"),sizePiece)
pawnB6 = pygame.transform.scale(pygame.image.load("piezas/PawnB.png"),sizePiece)
pawnB7 = pygame.transform.scale(pygame.image.load("piezas/PawnB.png"),sizePiece)


kingBPos = pygame.Vector2(320,0)
queenBPos = pygame.Vector2(240,0)
rookB0Pos = pygame.Vector2(0,0)
rookB1Pos = pygame.Vector2(560,0)
knightB0Pos = pygame.Vector2(80,0)
knightB1Pos = pygame.Vector2(480,0)
bishopB0Pos = pygame.Vector2(160,0)
bishopB1Pos = pygame.Vector2(400,0)
pawnB0Pos = pygame.Vector2(0,80)
pawnB1Pos = pygame.Vector2(80,80)
pawnB2Pos = pygame.Vector2(160,80)
pawnB3Pos = pygame.Vector2(240,80)
pawnB4Pos = pygame.Vector2(320,80)
pawnB5Pos = pygame.Vector2(400,80)
pawnB6Pos = pygame.Vector2(480,80)
pawnB7Pos = pygame.Vector2(560,80)
mousePos = pygame.Vector2(0,0)

matrix = [[[rookB0Pos,False,True],[knightB0Pos,False],[bishopB0Pos,False],[queenBPos,False],[kingBPos,False,True],[bishopB1Pos,False],[knightB1Pos,False],[rookB1Pos,False,True],
           [pawnB0Pos,False,True],[pawnB1Pos,False,True],[pawnB2Pos,False,True],[pawnB3Pos,False,True],[pawnB4Pos,False,True],[pawnB5Pos,False,True],[pawnB6Pos,False,True],[pawnB7Pos,False,True]]]
move = pygame.Vector2(0,0)

while True:
    for event in pygame.event.get():#Exit event
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.Vector2(pygame.mouse.get_pos())
            # mouseCont = 0
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
    DISPLAYSURF.fill(GREEN)
    white = True
    for i in range(0,640,80): #Make the board
        for j in range(0,640,160):
            if (white == True):
                pygame.draw.rect(DISPLAYSURF,WHITE,(j,i,80,80))
                if(j >= 480):
                    white = False
            else:
                pygame.draw.rect(DISPLAYSURF,WHITE,(j+80,i,80,80))
                if (j >= 480):
                    white = True



    DISPLAYSURF.blit(kingB,matrix[0][4][0])
    DISPLAYSURF.blit(queenB,matrix[0][3][0])
    DISPLAYSURF.blit(rookB0,matrix[0][0][0])
    DISPLAYSURF.blit(rookB1,matrix[0][7][0])
    DISPLAYSURF.blit(knightB0,matrix[0][1][0])
    DISPLAYSURF.blit(knightB1,matrix[0][6][0])
    DISPLAYSURF.blit(bishopB0,matrix[0][2][0])
    DISPLAYSURF.blit(bishopB1,matrix[0][5][0])
    DISPLAYSURF.blit(pawnB0,matrix[0][8][0])
    DISPLAYSURF.blit(pawnB1,matrix[0][9][0])
    DISPLAYSURF.blit(pawnB2,matrix[0][10][0])
    DISPLAYSURF.blit(pawnB3,matrix[0][11][0])
    DISPLAYSURF.blit(pawnB4,matrix[0][12][0])
    DISPLAYSURF.blit(pawnB5,matrix[0][13][0])
    DISPLAYSURF.blit(pawnB6,matrix[0][14][0])
    DISPLAYSURF.blit(pawnB7,matrix[0][15][0])

    
    for i in range(1):
        for j in range(16):
            if ((matrix[i][j][0].x < mousePos.x < (matrix[i][j][0].x + 80)) and (matrix[i][j][0].y < mousePos.y < (matrix[i][j][0].y + 80))): #Check if the mouse is click-on any piece
                matrix[i][j][1] = True

    if matrix[0][4][1] == True:#KING BLACK
        if ((matrix[0][4][2] == True) and ((matrix[0][0][2] == True)or(matrix[0][7][2] == True))): #Moment when the king has the posibility of castling
            if (matrix[0][0][2]==True):
                if (160<mousePos.x<240):
                   matrix[0][4][0] = pygame.Vector2(matrix[0][4][0].x - 160,matrix[0][4][0].y)
                   matrix[0][0][0] = pygame.Vector2(matrix[0][0][0].x + 240,matrix[0][0][0].y)
                   matrix[0][4][2] = False
                   matrix[0][0][2] = False
                   mousePos = pygame.Vector2(-1,-1)
            if (matrix[0][7][2]==True):
                if (480<mousePos.x<560):
                   matrix[0][4][0] = pygame.Vector2(matrix[0][4][0].x + 160,matrix[0][4][0].y)
                   matrix[0][7][0] = pygame.Vector2(matrix[0][7][0].x - 160,matrix[0][7][0].y)
                   matrix[0][4][2] = False
                   matrix[0][7][2] = False
                   mousePos = pygame.Vector2(-1,-1)
        if (((-80 + matrix[0][4][0].x)<mousePos.x<(matrix[0][4][0].x + 160)) and ((-80 + matrix[0][4][0].y)<mousePos.y<(matrix[0][4][0].y + 160))):#Range of the King
            if ((mousePos.x > matrix[0][4][0].x + 80) and (mousePos.y < matrix[0][4][0].y)): #Upper right diagonally 
                matrix[0][4][0] = pygame.Vector2(matrix[0][4][0].x + 80,matrix[0][4][0].y-80)
                matrix[0][4][1] = False
                matrix[0][4][2] = False #The castling has been losted
                mousePos = pygame.Vector2(-1,-1)
            elif ((mousePos.x > matrix[0][4][0].x+80) and (mousePos.y > matrix[0][4][0].y+80)):#Lower right diagonally
                matrix[0][4][0] = pygame.Vector2(matrix[0][4][0].x + 80,matrix[0][4][0].y+80)
                matrix[0][4][1] = False
                matrix[0][4][2] = False #The castling has been losted
                mousePos = pygame.Vector2(-1,-1)
            elif ((mousePos.x < matrix[0][4][0].x) and (mousePos.y < matrix[0][4][0].y)):#Upper left diagonally
                matrix[0][4][0] = pygame.Vector2(matrix[0][4][0].x-80,matrix[0][4][0].y-80)
                matrix[0][4][1] = False
                matrix[0][4][2] = False #The castling has been losted
                mousePos = pygame.Vector2(-1,-1)
            elif ((mousePos.x < matrix[0][4][0].x) and (mousePos.y > matrix[0][4][0].y+80)):#Lowerleft diagonally
                matrix[0][4][0] = pygame.Vector2(matrix[0][4][0].x-80,matrix[0][4][0].y+80)
                matrix[0][4][1] = False
                matrix[0][4][2] = False #The castling has been losted
                mousePos = pygame.Vector2(-1,-1)
            elif ((mousePos.y < matrix[0][4][0].y)):#Upper
                matrix[0][4][0] = pygame.Vector2(matrix[0][4][0].x,matrix[0][4][0].y-80)
                matrix[0][4][1] = False
                matrix[0][4][2] = False #The castling has been losted
                mousePos = pygame.Vector2(-1,-1)
            elif ((mousePos.y > matrix[0][4][0].y+80)):#Lower
                matrix[0][4][0] = pygame.Vector2(matrix[0][4][0].x,matrix[0][4][0].y+80)
                matrix[0][4][1] = False
                matrix[0][4][2] = False #The castling has been losted
                mousePos = pygame.Vector2(-1,-1)
            elif ((mousePos.x < matrix[0][4][0].x)):#left
                matrix[0][4][0] = pygame.Vector2(matrix[0][4][0].x-80,matrix[0][4][0].y)
                matrix[0][4][1] = False
                matrix[0][4][2] = False #The castling has been losted
                mousePos = pygame.Vector2(-1,-1)
            elif ((mousePos.x > matrix[0][4][0].x+80)):#Right
                matrix[0][4][0] = pygame.Vector2(matrix[0][4][0].x+80,matrix[0][4][0].y)
                matrix[0][4][1] = False
                matrix[0][4][2] = False #The castling has been losted
                mousePos = pygame.Vector2(-1,-1)
        else:
            matrix[0][4][1] = False
    if matrix[0][0][1] == True:#ROOK BLACK 0
        if ((matrix[0][0][0].y<mousePos.y<matrix[0][0][0].y + 80) or (matrix[0][0][0].x<mousePos.x<matrix[0][0][0].x + 80)):#Range of Rook    
            if (mousePos.x>matrix[0][0][0].x+80): #Right movement
                for i in range(2,9):    
                    if matrix[0][0][0].x + 80*(i-1) < mousePos.x < matrix[0][0][0].x + 80*i:
                        move = pygame.Vector2(80,0)*(i-1)
                matrix[0][0][0] = pygame.Vector2(matrix[0][0][0].x ,matrix[0][0][0].y) + move 
                matrix[0][0][1] = False
                matrix[0][0][2] = False #The castling has been losted
                mousePos = pygame.Vector2(-1,-1)
            if (0<mousePos.x<matrix[0][0][0].x):#Left movement
                for i in range(2,9):
                    if matrix[0][0][0].x - 80*(i-1) < mousePos.x < matrix[0][0][0].x - 80*(i-2):    
                        move = pygame.Vector2(80,0) * (i-1)
                matrix[0][0][0] = pygame.Vector2(matrix[0][0][0].x ,matrix[0][0][0].y) - move
                matrix[0][0][1] = False
                matrix[0][0][2] = False #The castling has been losted
                mousePos = pygame.Vector2(-1,-1)
            if (mousePos.y>matrix[0][0][0].y+80):#Lower movement
                for i in range(2,9):    
                    if matrix[0][0][0].y + 80*(i-1) < mousePos.y < matrix[0][0][0].y + 80*i:
                        move = pygame.Vector2(0,80)*(i-1)
                matrix[0][0][0] = pygame.Vector2(matrix[0][0][0].x ,matrix[0][0][0].y) + move
                matrix[0][0][1] = False
                matrix[0][0][2] = False #The castling has been losted
                mousePos = pygame.Vector2(-1,-1)
            if (0<mousePos.y<matrix[0][0][0].y):#Upper movement
                for i in range(2,9):
                    if matrix[0][0][0].y - 80*(i-1) < mousePos.y < matrix[0][0][0].y - 80*(i-2):    
                        move = pygame.Vector2(0,80) * (i-1)
                matrix[0][0][0] = pygame.Vector2(matrix[0][0][0].x ,matrix[0][0][0].y) - move
                matrix[0][0][1] = False
                matrix[0][0][2] = False #The castling has been losted
                mousePos = pygame.Vector2(-1,-1)
        else:
            matrix[0][0][1] = False
    if matrix[0][7][1] == True:#ROOK BLACK 1
        if ((matrix[0][7][0].y<mousePos.y<matrix[0][7][0].y + 80) or (matrix[0][7][0].x<mousePos.x<matrix[0][7][0].x + 80)):#Range of Rook
            if (mousePos.x>matrix[0][7][0].x+80): #Right movement
                for i in range(2,9):    
                    if matrix[0][7][0].x + 80*(i-1) < mousePos.x < matrix[0][7][0].x + 80*i:
                        move = pygame.Vector2(80,0)*(i-1)
                matrix[0][7][0] = pygame.Vector2(matrix[0][7][0].x ,matrix[0][7][0].y) + move 
                matrix[0][7][1] = False
                matrix[0][7][2] = False #The castling has been losted
                mousePos = pygame.Vector2(-1,-1)
            if (0<mousePos.x<matrix[0][7][0].x):#Left movement
                for i in range(2,9):
                    if matrix[0][7][0].x - 80*(i-1) < mousePos.x < matrix[0][7][0].x - 80*(i-2):    
                        move = pygame.Vector2(80,0) * (i-1)
                matrix[0][7][0] = pygame.Vector2(matrix[0][7][0].x ,matrix[0][7][0].y) - move
                matrix[0][7][1] = False
                matrix[0][7][2] = False #The castling has been losted
                mousePos = pygame.Vector2(-1,-1)
            if (mousePos.y>matrix[0][7][0].y+80):#Lower movement
                for i in range(2,9):    
                    if matrix[0][7][0].y + 80*(i-1) < mousePos.y < matrix[0][7][0].y + 80*i:
                        move = pygame.Vector2(0,80)*(i-1)
                matrix[0][7][0] = pygame.Vector2(matrix[0][7][0].x ,matrix[0][7][0].y) + move
                matrix[0][7][1] = False
                matrix[0][7][2] = False #The castling has been losted
                mousePos = pygame.Vector2(-1,-1)
            if (0<mousePos.y<matrix[0][7][0].y):#Upper movement
                for i in range(2,9):
                    if matrix[0][7][0].y - 80*(i-1) < mousePos.y < matrix[0][7][0].y - 80*(i-2):    
                        move = pygame.Vector2(0,80) * (i-1)
                matrix[0][7][0] = pygame.Vector2(matrix[0][7][0].x ,matrix[0][7][0].y) - move
                matrix[0][7][1] = False
                matrix[0][7][2] = False #The castling has been losted
                mousePos = pygame.Vector2(-1,-1)
        else:
            matrix[0][7][1] = False
    if matrix[0][1][1] == True:#KNIGHT BLACK 0
        if (matrix[0][1][0].x + 80 < mousePos.x < matrix[0][1][0].x + 160 and matrix[0][1][0].y - 160 < mousePos.y < matrix[0][1][0].y - 80):#Upper right corner
            matrix[0][1][0] = pygame.Vector2(matrix[0][1][0].x+80,matrix[0][1][0].y-160)
            matrix[0][1][1] = False
            mousePos = pygame.Vector2(-1,-1)
        elif (matrix[0][1][0].x + 160 < mousePos.x < matrix[0][1][0].x + 240 and matrix[0][1][0].y - 80 < mousePos.y < matrix[0][1][0].y):#Upper right down corner
            matrix[0][1][0] = pygame.Vector2(matrix[0][1][0].x+160,matrix[0][1][0].y-80)
            matrix[0][1][1] = False
            mousePos = pygame.Vector2(-1,-1)
        elif (matrix[0][1][0].x + 160 < mousePos.x < matrix[0][1][0].x + 240 and matrix[0][1][0].y + 80 < mousePos.y < matrix[0][1][0].y + 160):#Lower right up corner
            matrix[0][1][0] = pygame.Vector2(matrix[0][1][0].x+160,matrix[0][1][0].y+80)
            matrix[0][1][1] = False
            mousePos = pygame.Vector2(-1,-1)
        elif (matrix[0][1][0].x + 80 < mousePos.x < matrix[0][1][0].x + 160 and matrix[0][1][0].y + 160 < mousePos.y < matrix[0][1][0].y + 240):#Lower right corner
            matrix[0][1][0] = pygame.Vector2(matrix[0][1][0].x+80,matrix[0][1][0].y+160)
            matrix[0][1][1] = False
            mousePos = pygame.Vector2(-1,-1)
        elif (matrix[0][1][0].x - 80 < mousePos.x < matrix[0][1][0].x and matrix[0][1][0].y + 160 < mousePos.y < matrix[0][1][0].y + 240):#Lower left corner
            matrix[0][1][0] = pygame.Vector2(matrix[0][1][0].x-80,matrix[0][1][0].y+160)
            matrix[0][1][1] = False
            mousePos = pygame.Vector2(-1,-1)
        elif (matrix[0][1][0].x - 160 < mousePos.x < matrix[0][1][0].x - 80 and matrix[0][1][0].y + 80 < mousePos.y < matrix[0][1][0].y + 160):#Lower left up corner
            matrix[0][1][0] = pygame.Vector2(matrix[0][1][0].x-160,matrix[0][1][0].y+80)
            matrix[0][1][1] = False
            mousePos = pygame.Vector2(-1,-1)
        elif (matrix[0][1][0].x - 160 < mousePos.x < matrix[0][1][0].x - 80 and matrix[0][1][0].y - 80 < mousePos.y < matrix[0][1][0].y ):#Upper left down corner
            matrix[0][1][0] = pygame.Vector2(matrix[0][1][0].x-160,matrix[0][1][0].y-80)
            matrix[0][1][1] = False
            mousePos = pygame.Vector2(-1,-1)
        elif (matrix[0][1][0].x - 80 < mousePos.x < matrix[0][1][0].x and matrix[0][1][0].y - 160 < mousePos.y < matrix[0][1][0].y - 80 ):#Upper left corner
            matrix[0][1][0] = pygame.Vector2(matrix[0][1][0].x-80,matrix[0][1][0].y-160)
            matrix[0][1][1] = False
            mousePos = pygame.Vector2(-1,-1)
    if matrix[0][6][1] == True:#KNIGHT BLACK 1
        if (matrix[0][6][0].x + 80 < mousePos.x < matrix[0][6][0].x + 160 and matrix[0][6][0].y - 160 < mousePos.y < matrix[0][6][0].y - 80):#Upper right corner
            matrix[0][6][0] = pygame.Vector2(matrix[0][6][0].x+80,matrix[0][6][0].y-160)
            matrix[0][6][1] = False
            mousePos = pygame.Vector2(-1,-1)
        elif (matrix[0][6][0].x + 160 < mousePos.x < matrix[0][6][0].x + 240 and matrix[0][6][0].y - 80 < mousePos.y < matrix[0][6][0].y):#Upper right down corner
            matrix[0][6][0] = pygame.Vector2(matrix[0][6][0].x+160,matrix[0][6][0].y-80)
            matrix[0][6][1] = False
            mousePos = pygame.Vector2(-1,-1)
        elif (matrix[0][6][0].x + 160 < mousePos.x < matrix[0][6][0].x + 240 and matrix[0][6][0].y + 80 < mousePos.y < matrix[0][6][0].y + 160):#Lower right up corner
            matrix[0][6][0] = pygame.Vector2(matrix[0][6][0].x+160,matrix[0][6][0].y+80)
            matrix[0][6][1] = False
            mousePos = pygame.Vector2(-1,-1)
        elif (matrix[0][6][0].x + 80 < mousePos.x < matrix[0][6][0].x + 160 and matrix[0][6][0].y + 160 < mousePos.y < matrix[0][6][0].y + 240):#Lower right corner
            matrix[0][6][0] = pygame.Vector2(matrix[0][6][0].x+80,matrix[0][6][0].y+160)
            matrix[0][6][1] = False
            mousePos = pygame.Vector2(-1,-1)
        elif (matrix[0][6][0].x - 80 < mousePos.x < matrix[0][6][0].x and matrix[0][6][0].y + 160 < mousePos.y < matrix[0][6][0].y + 240):#Lower left corner
            matrix[0][6][0] = pygame.Vector2(matrix[0][6][0].x-80,matrix[0][6][0].y+160)
            matrix[0][6][1] = False
            mousePos = pygame.Vector2(-1,-1)
        elif (matrix[0][6][0].x - 160 < mousePos.x < matrix[0][6][0].x - 80 and matrix[0][6][0].y + 80 < mousePos.y < matrix[0][6][0].y + 160):#Lower left up corner
            matrix[0][6][0] = pygame.Vector2(matrix[0][6][0].x-160,matrix[0][6][0].y+80)
            matrix[0][6][1] = False
            mousePos = pygame.Vector2(-1,-1)
        elif (matrix[0][6][0].x - 160 < mousePos.x < matrix[0][6][0].x - 80 and matrix[0][6][0].y - 80 < mousePos.y < matrix[0][6][0].y ):#Upper left down corner
            matrix[0][6][0] = pygame.Vector2(matrix[0][6][0].x-160,matrix[0][6][0].y-80)
            matrix[0][6][1] = False
            mousePos = pygame.Vector2(-1,-1)
        elif (matrix[0][6][0].x - 80 < mousePos.x < matrix[0][6][0].x and matrix[0][6][0].y - 160 < mousePos.y < matrix[0][6][0].y - 80 ):#Upper left corner
            matrix[0][6][0] = pygame.Vector2(matrix[0][6][0].x-80,matrix[0][6][0].y-160)
            matrix[0][6][1] = False
            mousePos = pygame.Vector2(-1,-1)
    if matrix[0][2][1] == True:#BISHOP BLACK 0
        for i in range(1,9):
            if not (mousePos.x < 0 and mousePos.y < 0):
                if((matrix[0][2][0].x - i*80< mousePos.x < matrix[0][2][0].x-(i-1)*80) and (matrix[0][2][0].y - i*80 < mousePos.y < matrix[0][2][0].y-(i-1)*80)):#Upper left diagonally
                    matrix[0][2][0] = pygame.Vector2(matrix[0][2][0].x - (i*80),matrix[0][2][0].y - (i*80))
                    matrix[0][2][1] = False
                    mousePos = pygame.Vector2(-1,-1)
                elif((matrix[0][2][0].x + i*80< mousePos.x < matrix[0][2][0].x+(i+1)*80) and (matrix[0][2][0].y - i*80 < mousePos.y < matrix[0][2][0].y-(i-1)*80)):#Upper right diagonally
                    matrix[0][2][0] = pygame.Vector2(matrix[0][2][0].x + (i*80),matrix[0][2][0].y - (i*80))
                    matrix[0][2][1] = False
                    mousePos = pygame.Vector2(-1,-1)
                elif((matrix[0][2][0].x + i*80< mousePos.x < matrix[0][2][0].x+(i+1)*80) and (matrix[0][2][0].y +i*80 < mousePos.y < matrix[0][2][0].y+(i+1)*80)):#Lower  right diagonally
                    matrix[0][2][0] = pygame.Vector2(matrix[0][2][0].x + (i*80),matrix[0][2][0].y + (i*80))
                    matrix[0][2][1] = False
                    mousePos = pygame.Vector2(-1,-1)
                elif((matrix[0][2][0].x - i*80< mousePos.x < matrix[0][2][0].x-(i-1)*80) and (matrix[0][2][0].y +i*80 < mousePos.y < matrix[0][2][0].y+(i+1)*80)):#Lower left diagonaly
                    matrix[0][2][0] = pygame.Vector2(matrix[0][2][0].x - (i*80),matrix[0][2][0].y + (i*80))
                    matrix[0][2][1] = False
                    mousePos = pygame.Vector2(-1,-1)
                if not (matrix[0][2][0].x<mousePos.x<matrix[0][2][0].x+80 and matrix[0][2][0].y<mousePos.y<matrix[0][2][0].y+80):#Check if the clik was in outside of his zone
                    matrix[0][2][1] = False
    if matrix[0][5][1] == True:#BISHOP BLACK 1
        for i in range(1,9):
            if not (mousePos.x < 0 and mousePos.y < 0):
                if((matrix[0][5][0].x - i*80< mousePos.x < matrix[0][5][0].x-(i-1)*80) and (matrix[0][5][0].y - i*80 < mousePos.y < matrix[0][5][0].y-(i-1)*80)):#Upper left diagonally
                    matrix[0][5][0] = pygame.Vector2(matrix[0][5][0].x - (i*80),matrix[0][5][0].y - (i*80))
                    matrix[0][5][1] = False
                    mousePos = pygame.Vector2(-1,-1)
                elif((matrix[0][5][0].x + i*80< mousePos.x < matrix[0][5][0].x+(i+1)*80) and (matrix[0][5][0].y - i*80 < mousePos.y < matrix[0][5][0].y-(i-1)*80)):#Upper right diagonally
                    matrix[0][5][0] = pygame.Vector2(matrix[0][5][0].x + (i*80),matrix[0][5][0].y - (i*80))
                    matrix[0][5][1] = False
                    mousePos = pygame.Vector2(-1,-1)
                elif((matrix[0][5][0].x + i*80< mousePos.x < matrix[0][5][0].x+(i+1)*80) and (matrix[0][5][0].y +i*80 < mousePos.y < matrix[0][5][0].y+(i+1)*80)):#Lower  right diagonally
                    matrix[0][5][0] = pygame.Vector2(matrix[0][5][0].x + (i*80),matrix[0][5][0].y + (i*80))
                    matrix[0][5][1] = False
                    mousePos = pygame.Vector2(-1,-1)
                elif((matrix[0][5][0].x - i*80< mousePos.x < matrix[0][5][0].x-(i-1)*80) and (matrix[0][5][0].y +i*80 < mousePos.y < matrix[0][5][0].y+(i+1)*80)):#Lower left diagonaly
                    matrix[0][5][0] = pygame.Vector2(matrix[0][5][0].x - (i*80),matrix[0][5][0].y + (i*80))
                    matrix[0][5][1] = False
                    mousePos = pygame.Vector2(-1,-1)
                if not (matrix[0][5][0].x<mousePos.x<matrix[0][5][0].x+80 and matrix[0][5][0].y<mousePos.y<matrix[0][5][0].y+80):#Check if the clik was in outside of his zone
                    matrix[0][5][1] = False                
    if matrix[0][3][1] == True:#QUEEN BLACK
        if ((matrix[0][3][0].y<mousePos.y<matrix[0][3][0].y + 80) or (matrix[0][3][0].x<mousePos.x<matrix[0][3][0].x + 80)):#Range of Rook    
            if (mousePos.x>matrix[0][3][0].x+80): #Right movement
                for i in range(2,9):    
                    if matrix[0][3][0].x + 80*(i-1) < mousePos.x < matrix[0][3][0].x + 80*i:
                        move = pygame.Vector2(80,0)*(i-1)
                matrix[0][3][0] = pygame.Vector2(matrix[0][3][0].x ,matrix[0][3][0].y) + move 
                matrix[0][3][1] = False
                mousePos = pygame.Vector2(-1,-1)
            if (0<mousePos.x<matrix[0][3][0].x):#Left movement
                for i in range(2,9):
                    if matrix[0][3][0].x - 80*(i-1) < mousePos.x < matrix[0][3][0].x - 80*(i-2):    
                        move = pygame.Vector2(80,0) * (i-1)
                matrix[0][3][0] = pygame.Vector2(matrix[0][3][0].x ,matrix[0][3][0].y) - move
                matrix[0][3][1] = False
                mousePos = pygame.Vector2(-1,-1)
            if (mousePos.y>matrix[0][3][0].y+80):#Lower movement
                for i in range(2,9):    
                    if matrix[0][3][0].y + 80*(i-1) < mousePos.y < matrix[0][3][0].y + 80*i:
                        move = pygame.Vector2(0,80)*(i-1)
                matrix[0][3][0] = pygame.Vector2(matrix[0][3][0].x ,matrix[0][3][0].y) + move
                matrix[0][3][1] = False
                mousePos = pygame.Vector2(-1,-1)
            if (0<mousePos.y<matrix[0][3][0].y):#Upper movement
                for i in range(2,9):
                    if matrix[0][3][0].y - 80*(i-1) < mousePos.y < matrix[0][3][0].y - 80*(i-2):    
                        move = pygame.Vector2(0,80) * (i-1)
                matrix[0][3][0] = pygame.Vector2(matrix[0][3][0].x ,matrix[0][3][0].y) - move
                matrix[0][3][1] = False
                mousePos = pygame.Vector2(-1,-1)
        else:
            matrix[0][3][1] = False
        for i in range(1,9):
            if not (mousePos.x < 0 and mousePos.y < 0):
                if((matrix[0][3][0].x - i*80< mousePos.x < matrix[0][3][0].x-(i-1)*80) and (matrix[0][3][0].y - i*80 < mousePos.y < matrix[0][3][0].y-(i-1)*80)):#Upper left diagonally
                    matrix[0][3][0] = pygame.Vector2(matrix[0][3][0].x - (i*80),matrix[0][3][0].y - (i*80))
                    matrix[0][3][1] = False
                    mousePos = pygame.Vector2(-1,-1)
                elif((matrix[0][3][0].x + i*80< mousePos.x < matrix[0][3][0].x+(i+1)*80) and (matrix[0][3][0].y - i*80 < mousePos.y < matrix[0][3][0].y-(i-1)*80)):#Upper right diagonally
                    matrix[0][3][0] = pygame.Vector2(matrix[0][3][0].x + (i*80),matrix[0][3][0].y - (i*80))
                    matrix[0][3][1] = False
                    mousePos = pygame.Vector2(-1,-1)
                elif((matrix[0][3][0].x + i*80< mousePos.x < matrix[0][3][0].x+(i+1)*80) and (matrix[0][3][0].y +i*80 < mousePos.y < matrix[0][3][0].y+(i+1)*80)):#Lower  right diagonally
                    matrix[0][3][0] = pygame.Vector2(matrix[0][3][0].x + (i*80),matrix[0][3][0].y + (i*80))
                    matrix[0][3][1] = False
                    mousePos = pygame.Vector2(-1,-1)
                elif((matrix[0][3][0].x - i*80< mousePos.x < matrix[0][3][0].x-(i-1)*80) and (matrix[0][3][0].y +i*80 < mousePos.y < matrix[0][3][0].y+(i+1)*80)):#Lower left diagonaly
                    matrix[0][3][0] = pygame.Vector2(matrix[0][3][0].x - (i*80),matrix[0][3][0].y + (i*80))
                    matrix[0][3][1] = False
                    mousePos = pygame.Vector2(-1,-1)
                if not (matrix[0][3][0].x<mousePos.x<matrix[0][3][0].x+80 and matrix[0][3][0].y<mousePos.y<matrix[0][3][0].y+80):#Check if the clik was in outside of his zone
                    matrix[0][3][1] = False
    for i in range(8,16):
        if (matrix[0][i][1] == True):
            if matrix[0][i][2] == True:
                if (matrix[0][i][0].x<mousePos.x<matrix[0][i][0].x+80 and matrix[0][i][0].y+80<mousePos.y<matrix[0][i][0].y+240):
                    if (mousePos.y - matrix[0][i][0].y < 160):
                        matrix[0][i][0] = pygame.Vector2(matrix[0][i][0].x,matrix[0][i][0].y+80)
                        matrix[0][i][1] = False
                        matrix[0][i][2] = False
                        mousePos = pygame.Vector2(-1,-1)
                    else:
                        matrix[0][i][0] = pygame.Vector2(matrix[0][i][0].x,matrix[0][i][0].y+160)
                        matrix[0][i][1] = False
                        matrix[0][i][2] = False
                        mousePos = pygame.Vector2(-1,-1)
            elif (matrix[0][i][0].x<mousePos.x<matrix[0][i][0].x+80 and matrix[0][i][0].y+80<mousePos.y<matrix[0][i][0].y+160):
                matrix[0][i][0] = pygame.Vector2(matrix[0][i][0].x,matrix[0][i][0].y+80)
                matrix[0][i][1] = False
                mousePos = pygame.Vector2(-1,-1)
            if not (matrix[0][i][0].x<mousePos.x<matrix[0][i][0].x+80 and matrix[0][i][0].y<mousePos.y<matrix[0][i][0].y+160):
                matrix[0][i][1] = False
    pygame.display.flip()       
    pygame.display.update()