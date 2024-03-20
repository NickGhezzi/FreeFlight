import pygame, globals
from pygame.locals import *
class GameObject(object):
    def __init__(self, vec2, sprite, canCollide = False):
        self.pos = vec2
        self.sprite = sprite
        self.rot = 0
        self.canCollide = canCollide
        self.resetPosition = vec2.copy()
        print(type(self.resetPosition), type(vec2))

    def update(self, dt, events):
        pass
    
    def draw(self, screen):
        newimg = pygame.transform.rotate(self.sprite, self.rot)
        new_rect = newimg.get_rect(center = self.sprite.get_rect(center = self.pos.xy).center)
        #debug shape
        if(globals.DEBUG): pygame.draw.rect(screen, pygame.Color(255, 0, 255), new_rect)
        #draw to screen
        screen.blit(newimg, new_rect)
        
    def isCollision(self, collision):
        self.collision = collision
        
    #override to implement reset behaviour 
    def reset(self):
        print("GOBJ reset")
        self.pos = self.resetPosition.copy()
        self.rot = 0