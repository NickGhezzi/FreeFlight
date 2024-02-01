import pygame
from pygame.locals import *
from GameObject import *


class Parallax(object):    
    def __init__(self, pieces, speed, startPosX, dir = -1, spacing = 0):
        self.pieces = pieces
        self.dir = dir
        self.speed = speed
        self.sPosX = startPosX
        self.ePosX = 0 
        self.isActive = True 
        self.spacing = spacing #pixels
        
        self.setup()
        
    def setup(self):
        #end position
        self.ePosX = -(self.pieces[0].sprite.get_width() / 2)
        #set up positions and start pos
        x = self.sPosX
        for piece in self.pieces:
             piece.pos.x = x
             x += piece.sprite.get_width() + self.spacing
             
        self.sPosX += self.pieces[0].sprite.get_width() * (len(self.pieces) - 1)
              
    
    def update(self, dt, events):
        # movement
        for piece in self.pieces:
            if(self.isActive == True):
                piece.pos.x += (self.speed * self.dir)
            if(piece.pos.x <= self.ePosX):
                piece.pos.x = self.sPosX
            piece.update(dt, events)
            
    def draw(self, screen):
        for piece in self.pieces:
            piece.draw(screen)