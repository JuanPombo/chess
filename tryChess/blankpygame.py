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
kingPos = pygame.Vector2(260,560)
mousePos = pygame.Vector2(0,0)
mouseBoo = False
#pygame.draw.rect(DISPLAYSURF,GREEN,(0,0,640,640))


while True:
    for event in pygame.event.get():#Exit event
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.Vector2(pygame.mouse.get_pos())
            mousePos0 = pygame.Vector2(pygame.mouse.get_pos())
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
    
    if ((kingPos.x < mousePos.x < (kingPos.x + 80)) and (kingPos.y < mousePos.y < (kingPos.y + 80))):
        mouseBoo = True
        #mousePos = mouseIPos
        #kingPos = pygame.Vector2(260,480)
        #print(mousePos)
        """
        if ((260 < int(mousePos0.x) < 340 ) and ( 480 < int(mousePos0.y) < 560)):
            kingPos = pygame.Vector2(260,480)
            print("HI")  
        """
    #else:
        #mouseBoo = False

    if mouseBoo == True:
        if ((260 < int(mousePos.x) < 340 ) and ( 480 < int(mousePos0.y) < 560)):
            kingPos = pygame.Vector2(260,480)
            mouseBoo = False
                
    dt = clock.tick(60)/1000
  
    
    pygame.display.flip()       
    pygame.display.update()