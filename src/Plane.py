import pygame
from pygame.locals import *
from GameObject import *


class Plane(GameObject):
    MAX_ACC = 50
    MIN_ACC = 5
    acc_rate = MIN_ACC
    fall_speed = 50
    acc = 0
    
    push_power = 50
    
    MAX_ROT = 45
    ROT_SPEED = 100
    
    def __init__(self, vec2, sprite, rot = 0):
        super().__init__(vec2, sprite, rot)
    
    def update(self, dt, events):
        # input
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
        self.pos.y += self.fall_speed * self.acc * dt
        
        # rotation
        self.rot -= self.ROT_SPEED * dt
        self.rot = pygame.math.clamp(self.rot, -self.MAX_ROT, self.MAX_ROT)
        
    
    # def draw(self):
    #     pass