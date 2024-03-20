import pygame, globals
from pygame.locals import *
from GameObject import *


class Plane(GameObject):
    MAX_ACC = 25
    MIN_ACC = 5
    acc_rate = MIN_ACC
    fall_speed = 25
    acc = 0
    
    push_power = 35
    
    MAX_ROT = 35
    ROT_SPEED = 100
    
    isDead = False
    
    def __init__(self, vec2, sprite, canCollide = False):
        super().__init__(vec2, sprite, canCollide)
    
    def update(self, dt, events):
        # input
        if(self.isDead == False):
            for event in  events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.rot = 250
                        self.acc = 0
                        self.acc_rate = self.MIN_ACC
                        self.pos.y -= self.push_power
                
        # gravity
        self.acc_rate += self.MAX_ACC * dt
        self.acc += self.acc_rate * dt
        self.acc = pygame.math.clamp(self.acc, 0, self.MAX_ACC)
        self.pos.y = pygame.math.clamp(self.pos.y + self.fall_speed * self.acc * dt, 0, globals.SCREEN_HEIGHT)
        
        # rotation
        self.rot -= self.ROT_SPEED * dt
        self.rot = pygame.math.clamp(self.rot, -self.MAX_ROT, self.MAX_ROT)
        
    
    def reset(self):
        super().reset()
        self.isDead = False
        self.canCollide = True
        self.acc_rate = self.MIN_ACC
        self.acc = 0