import pygame, sys
from pygame.locals import *
def KingMove(kingPos,mousePos,mouseBoo):
    if ((kingPos.x < mousePos.x < (kingPos.x + 80)) and (kingPos.y < mousePos.y < (kingPos.y + 80))): #Check if the mouse is click-on the king
            mouseBoo[3] = True

    if mouseBoo[3] == True:    
        if (((-80+kingPos.x)<mousePos.x<(kingPos.x + 160)) and ((-80+kingPos.y)<mousePos.y<(kingPos.y + 160))):
            if ((mousePos.x > kingPos.x + 80) and (mousePos.y < kingPos.y)): #diagonal superior derecha
                kingPos = pygame.Vector2(kingPos.x + 80,kingPos.y-80)
                mouseBoo[3] = False
                mousePos = pygame.Vector2(-1,-1)
            elif ((mousePos.x > kingPos.x+80) and (mousePos.y > kingPos.y+80)):#diagonal inferior derecha
                kingPos = pygame.Vector2(kingPos.x + 80,kingPos.y+80)
                mouseBoo[3] = False
                mousePos = pygame.Vector2(-1,-1)
            elif ((mousePos.x < kingPos.x) and (mousePos.y < kingPos.y)):#diagonal superior izquierda
                kingPos = pygame.Vector2(kingPos.x-80,kingPos.y-80)
                mouseBoo[3] = False
                mousePos = pygame.Vector2(-1,-1)
            elif ((mousePos.x < kingPos.x) and (mousePos.y > kingPos.y+80)):#diagonal inferior izquierda
                kingPos = pygame.Vector2(kingPos.x-80,kingPos.y+80)
                mouseBoo[3] = False
                mousePos = pygame.Vector2(-1,-1)
            elif ((mousePos.y < kingPos.y)):#Recto arriba
                kingPos = pygame.Vector2(kingPos.x,kingPos.y-80)
                mouseBoo[3] = False
                mousePos = pygame.Vector2(-1,-1)
            elif ((mousePos.y > kingPos.y+80)):#Recto abajo
                kingPos = pygame.Vector2(kingPos.x,kingPos.y+80)
                mouseBoo[3] = False
                mousePos = pygame.Vector2(-1,-1)
            elif ((mousePos.x < kingPos.x)):#Recto izquierda
                kingPos = pygame.Vector2(kingPos.x-80,kingPos.y)
                mouseBoo[3] = False
                mousePos = pygame.Vector2(-1,-1)
            elif ((mousePos.x > kingPos.x+80)):#Recto derecha
                kingPos = pygame.Vector2(kingPos.x+80,kingPos.y)
                mouseBoo[3] = False
                mousePos = pygame.Vector2(-1,-1)
        else:
            mouseBoo[3] = False