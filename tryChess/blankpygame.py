import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((640,640))
pygame.display.set_caption('Chess!')

BLACK = (  0,   0,   0) 
WHITE = (255, 255, 255) 
RED   = (255,   0,   0) 
GREEN = (  0, 255,   0) 
BLUE  = (  0,   0, 255)

king = pygame.image.load("king1.png")
queen = pygame.image.load("queen.png")
king = pygame.transform.scale(king,(40,80))
queen = pygame.transform.scale(queen,(40,80))
 
DISPLAYSURF.fill(WHITE)
pygame.draw.rect(DISPLAYSURF,GREEN,(0,0,640,640))
white = True
for i in range(0,640,80):
    for j in range(0,640,160):
        if (white == True):
            pygame.draw.rect(DISPLAYSURF,WHITE,(j,i,80,80))
            if(j >= 480):
                white = False
        else:
            pygame.draw.rect(DISPLAYSURF,WHITE,(j+80,i,80,80))
            if (j >= 480):
                white = True
running = 1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
    DISPLAYSURF.blit(king,(260,560))
    DISPLAYSURF.blit(queen,(340,560))
    pygame.display.flip()       
    pygame.display.update()