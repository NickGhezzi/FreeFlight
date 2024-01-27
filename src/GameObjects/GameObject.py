import pygame, GameObjects
from pygame.locals import *

class GameObject(object):
    # pos = pygame.math.Vector2(0,0)
    # sprite = 0
    def __init__(self, vec2, sprite):
        self.pos = vec2
        self.sprite = sprite
        
    
    def update(self, dt):
        pass
    
    def draw(self, screen):
        screen.blit(self.sprite, (self.pos.x, self.pos.y))
        
    def isCollision(self, collision):
        self.collision = collision
    
    #TODO:: setter for collision box size