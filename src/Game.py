import pygame
from pygame.locals import *

from GameObject import GameObject
from Plane import Plane
from Parallax import Parallax


class Game(object):
    SCREEN_CENTER = 0
    def init(self, screen):
        #variables
        self.SCREEN_CENTER = pygame.math.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        
        #player
        plane_img = pygame.image.load('assets\\PNG\\Planes\\planeRed1.png')
        self.player = Plane(pygame.math.Vector2(screen.get_width() / 2, screen.get_height() / 2), plane_img)
        
        #background
        bgImg = pygame.image.load('assets\\PNG\\background.png')
        bgObs = []
        for i in range(2):
            bgObs.append(GameObject(pygame.math.Vector2(screen.get_width() / 2, screen.get_height() / 2), bgImg))
        self.background = Parallax(bgObs, 1, screen.get_width() / 2)
        
        #forground
        fgImg = pygame.image.load('assets\\PNG\\groundGrass.png')
        fgObs = []
        for i in range(3):
            fgObs.append(GameObject(pygame.math.Vector2(screen.get_width() / 2, screen.get_height() - (fgImg.get_height() / 2)), fgImg))
        self.foreground = Parallax(fgObs, 4, screen.get_width() / 2)   
    
    def update(self, dt, events):
        self.player.update(dt, events)
        self.background.update(dt, events)
        self.foreground.update(dt, events)
        
    
    def draw(self, screen):
        self.background.draw(screen)
        self.foreground.draw(screen)
        self.player.draw(screen)
        