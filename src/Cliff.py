import random
import pygame
from pygame.locals import *
from GameObject import *
import globals


class Cliff(GameObject):
    def __init__(self, vec2, sprite, player, canCollide = False):
        super().__init__(vec2, sprite, canCollide)
        self.maxHeight = 1.3
        self.minHeight = 0.7
        self.height = 1
        self.isUp = False
        self.passed = False
        self.playerRef = player
        self.reset()

    def update(self, dt, events):
        #check if player collided with cliff
        if(self.canCollide):
            pRect = self.playerRef.sprite.get_rect(center=(self.playerRef.pos.x, self.playerRef.pos.y))
            if(self.sprite.get_rect(center=(self.pos.x, self.pos.y)).colliderect(pRect)):
                print("Player hit cliff")
                self.canCollide = False
                pygame.event.post(pygame.event.Event(globals.PLAYER_DIED))
                self.playerRef.isDead = True

        #todo look to see if player passed the cliff
        if(self.passed == False):
            if(self.pos.x <= self.playerRef.pos.x):
                self.passed = True
                pygame.event.post(pygame.event.Event(globals.PLAYER_SCORED))
        
                
                 
    def draw(self, screen):
        flipimg = pygame.transform.flip(self.sprite, False, self.isUp)
        scaleimg = pygame.transform.scale_by(flipimg, (1, self.height))
        newimg = pygame.transform.rotate(scaleimg, self.rot)
        new_rect = newimg.get_rect(center = self.sprite.get_rect(center = self.pos.xy).center)
        #debug shape
        if(globals.DEBUG): pygame.draw.rect(screen, pygame.Color(255, 0, 255), new_rect)

        screen.blit(newimg, new_rect)
    
    def reset(self):
        super().reset()
        self.randomizeValues()
        self.passed = False
        self.canCollide = True
    
    def randomizeValues(self):
        #randomize direction
        self.isUp = bool(random.getrandbits(1))
        self.height = random.uniform(self.minHeight, self.maxHeight)
        if(self.isUp):
            self.pos.y = 0 + ((self.sprite.get_height() * self.height) / 2)
        else:
            self.pos.y = (pygame.display.get_surface().get_height() - ((self.sprite.get_height() * self.height) / 2)) 
        