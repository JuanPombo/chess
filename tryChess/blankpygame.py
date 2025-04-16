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
#           WTorre1,WCaballo1,WAlfil1,WRey,WReina,WAlfil2,WCaballo2,WTorre2
#           WPeon1,WPeon2,WPeon3,WPeon4,WPeon5,WPeon6,WPeon7,WPeon8
#           BTorre1,BCaballo1,BAlfil1,BRey,BReina,BAlfil2,BCaballo2,BTorre2
#           BPeon1,BPeon2,BPeon3,BPeon4,BPeon5,BPeon6,BPeon7,BPeon8
mouseBoo = [False,False,False,False,False,False,False,False,
            False,False,False,False,False,False,False,False,
            False,False,False,False,False,False,False,False,
            False,False,False,False,False,False,False,False,]
#pygame.draw.rect(DISPLAYSURF,GREEN,(0,0,640,640))
mouseTem = [False,False,False]
flag = False

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



    DISPLAYSURF.blit(kingB,kingBPos)
    DISPLAYSURF.blit(queenB,queenBPos)
    DISPLAYSURF.blit(rookB0,rookB0Pos)
    DISPLAYSURF.blit(rookB1,rookB1Pos)
    DISPLAYSURF.blit(knightB0,knightB0Pos)
    DISPLAYSURF.blit(knightB1,knightB1Pos)
    DISPLAYSURF.blit(bishopB0,bishopB0Pos)
    DISPLAYSURF.blit(bishopB1,bishopB1Pos)
    DISPLAYSURF.blit(pawnB0,pawnB0Pos)
    DISPLAYSURF.blit(pawnB1,pawnB1Pos)
    DISPLAYSURF.blit(pawnB2,pawnB2Pos)
    DISPLAYSURF.blit(pawnB3,pawnB3Pos)
    DISPLAYSURF.blit(pawnB4,pawnB4Pos)
    DISPLAYSURF.blit(pawnB5,pawnB5Pos)
    DISPLAYSURF.blit(pawnB6,pawnB6Pos)
    DISPLAYSURF.blit(pawnB7,pawnB7Pos)

    
    
    if ((kingBPos.x < mousePos.x < (kingBPos.x + 80)) and (kingBPos.y < mousePos.y < (kingBPos.y + 80))): #Check if the mouse is click-on the king
        mouseBoo[3] = True

    if mouseBoo[3] == True:    
        if (((-80+kingBPos.x)<mousePos.x<(kingBPos.x + 160)) and ((-80+kingBPos.y)<mousePos.y<(kingBPos.y + 160))):
            if ((mousePos.x > kingBPos.x + 80) and (mousePos.y < kingBPos.y)): #diagonal superior derecha
                kingBPos = pygame.Vector2(kingBPos.x + 80,kingBPos.y-80)
                mouseBoo[3] = False
                mousePos = pygame.Vector2(-1,-1)
            elif ((mousePos.x > kingBPos.x+80) and (mousePos.y > kingBPos.y+80)):#diagonal inferior derecha
                kingBPos = pygame.Vector2(kingBPos.x + 80,kingBPos.y+80)
                mouseBoo[3] = False
                mousePos = pygame.Vector2(-1,-1)
            elif ((mousePos.x < kingBPos.x) and (mousePos.y < kingBPos.y)):#diagonal superior izquierda
                kingBPos = pygame.Vector2(kingBPos.x-80,kingBPos.y-80)
                mouseBoo[3] = False
                mousePos = pygame.Vector2(-1,-1)
            elif ((mousePos.x < kingBPos.x) and (mousePos.y > kingBPos.y+80)):#diagonal inferior izquierda
                kingBPos = pygame.Vector2(kingBPos.x-80,kingBPos.y+80)
                mouseBoo[3] = False
                mousePos = pygame.Vector2(-1,-1)
            elif ((mousePos.y < kingBPos.y)):#Recto arriba
                kingBPos = pygame.Vector2(kingBPos.x,kingBPos.y-80)
                mouseBoo[3] = False
                mousePos = pygame.Vector2(-1,-1)
            elif ((mousePos.y > kingBPos.y+80)):#Recto abajo
                kingBPos = pygame.Vector2(kingBPos.x,kingBPos.y+80)
                mouseBoo[3] = False
                mousePos = pygame.Vector2(-1,-1)
            elif ((mousePos.x < kingBPos.x)):#Recto izquierda
                kingBPos = pygame.Vector2(kingBPos.x-80,kingBPos.y)
                mouseBoo[3] = False
                mousePos = pygame.Vector2(-1,-1)
            elif ((mousePos.x > kingBPos.x+80)):#Recto derecha
                kingBPos = pygame.Vector2(kingBPos.x+80,kingBPos.y)
                mouseBoo[3] = False
                mousePos = pygame.Vector2(-1,-1)
        else:
            mouseBoo[3] = False
  
    
    pygame.display.flip()       
    pygame.display.update()