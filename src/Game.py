import pygame
from pygame.locals import *
# import sys
# sys.path.insert(0, 'src\\GameObject\\Plane.py')

import GameObjects.Plane

class Game(object):
    
    def init(self, screen):
        plane_img = pygame.image.load('assets\\PNG\\Planes\\planeRed1.png')
        self.plane = Plane.Plane(pygame.math.Vector2(screen.get_width/2, screen.get_height/2), plane_img)
    
    def update(self, dt):
        self.plane.update(dt)
    
    def draw(self, screen):
        self.plane.draw(screen)