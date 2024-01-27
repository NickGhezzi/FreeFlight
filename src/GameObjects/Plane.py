import pygame, GameObjects.GameObject
from pygame.locals import *

class Plane(GameObjects.GameObject):
    def __init__(self, vec2, sprite):
        super.__init__(vec2, sprite)
        pass
    
    def update(self, dt):
        self.pos.y -= 9.8 * dt
    
    # def draw(self):
    #     pass