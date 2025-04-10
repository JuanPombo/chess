import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((640,640))
pygame.display.set_caption('Chess!')
clock = pygame.time.Clock()

BLACK = (  0,   0,   0) 
WHITE = (255, 255, 255) 
RED   = (255,   0,   0) 
GREEN = (  0, 255,   0) 
BLUE  = (  0,   0, 255)

king = pygame.image.load("king1.png")
queen = pygame.image.load("queen.png")
king = pygame.transform.scale(king,(40,80))
queen = pygame.transform.scale(queen,(40,80))

dt = 0
kingPos = pygame.Vector2(260,480)
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
flag = False

while True:
    for event in pygame.event.get():#Exit event
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.Vector2(pygame.mouse.get_pos())
            mouseCont = 0
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



    DISPLAYSURF.blit(king,kingPos)
    DISPLAYSURF.blit(queen,(340,560))
    """
    keys = pygame.key.get_pressed()
    if ((0 < player_pos.x < 600) and (0 < player_pos.y < 561)):
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt
    elif (player_pos.x < 0):
        player_pos = pygame.Vector2(player_pos.x+0.1, player_pos.y)
    elif (player_pos.x > 600):
        player_pos = pygame.Vector2(player_pos.x-0.1, player_pos.y)
    elif (player_pos.y < 0):
        player_pos = pygame.Vector2(player_pos.x,player_pos.y+0.1)
    elif (player_pos.y > 561):
        player_pos = pygame.Vector2(player_pos.x,player_pos.y-0.1)
   
    
    """  
    
    if ((kingPos.x < mousePos.x < (kingPos.x + 80)) and (kingPos.y < mousePos.y < (kingPos.y + 80))): #Check if the mouse click-on the king
        mouseBoo[3] = True

    if mouseBoo[3] == True:     #I need that the King does to the Rect movement and the diagonal inferior derecha
        #print(mouseBoo)

        if (((-80+kingPos.x)<mousePos.x<(kingPos.x + 160)) and ((-80+kingPos.y)<mousePos.y<(kingPos.y + 160))):
            #print(mousePos)
            if ((mousePos.x > kingPos.x + 80) and (mousePos.y < kingPos.y)): #diagonal superior derecha
                kingPos = pygame.Vector2(kingPos.x + 80,kingPos.y-80)
                #print(mousePos,"Flag1")
                mouseBoo[3] = False
            elif ((mousePos.x > kingPos.x+80) and (mousePos.y > kingPos.y+80)):#diagonal inferior derecha
                kingPos = pygame.Vector2(kingPos.x + 80,kingPos.y+80)
                mouseBoo[3] = False
            elif ((mousePos.x < kingPos.x) and (mousePos.y < kingPos.y)):#diagonal superior izquierda
                kingPos = pygame.Vector2(kingPos.x-80,kingPos.y-80)
                #print(mousePos,"Flag2")
                mouseBoo[3] = False
            elif ((mousePos.x < kingPos.x) and (mousePos.y > kingPos.y)):#diagonal inferior izquierda
                kingPos = pygame.Vector2(kingPos.x-80,kingPos.y+80)
                #print(mousePos,"Flag3")
                mouseBoo[3] = False
            elif ((mousePos.y < kingPos.y)):#Recto arriba
                kingPos = pygame.Vector2(kingPos.x,kingPos.y-80)
                mouseBoo[3] = False
            elif ((mousePos.x == kingPos.x) and (mousePos.y > kingPos.y)):#Recto abajo
                kingPos = pygame.Vector2(kingPos.x,kingPos.y+80)
                mouseBoo[3] = False
            elif ((mousePos.x < kingPos.x) and (mousePos.y == kingPos.y)):#Recto izquierda
                kingPos = pygame.Vector2(kingPos.x-80,kingPos.y)
                mouseBoo[3] = False
            elif ((mousePos.x > kingPos.x) and (mousePos.y == kingPos.y)):#Recto derecha
                kingPos = pygame.Vector2(kingPos.x+80,kingPos.y)
                mouseBoo[3] = False
            
                
    dt = clock.tick(60)/1000
  
    
    pygame.display.flip()       
    pygame.display.update()