#import pygame, globals
from pygame.locals import *

#from GameObject import GameObject

class Scene(object):
    
    def __init__(self, isVisible = False):
        self.gameObjects = []
        self.isVisible = isVisible
     
    def update(self, dt, events):
        if self.isVisible:
            [gO.update(dt, events) for gO in self.gameObjects]
    
    def draw(self, screen):
        if self.isVisible:
            [gO.draw(screen) for gO in self.gameObjects]
        
