import pygame
from pygame.locals import *

class GameObject(object):
    # pos = pygame.math.Vector2(0,0)
    # sprite = 0
    def __init__(self, vec2, sprite, rot = 0):
        self.pos = vec2
        self.sprite = sprite
        self.rot = rot
        
    
    def update(self, dt):
        pass
    
    def draw(self, screen):
        newimg = pygame.transform.rotate(self.sprite, self.rot)
        new_rect = newimg.get_rect(center = self.sprite.get_rect(center = self.pos.xy).center)

        screen.blit(newimg, new_rect)
        
    def isCollision(self, collision):
        self.collision = collision
    
    #TODO:: setter for collision box size