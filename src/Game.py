import pygame
from pygame.locals import *
from Plane import *

# import sys
# sys.path.insert(0, 'src\\GameObject\\Plane.py')

import Plane

class Game(object):
    
    def init(self, screen):
        plane_img = pygame.image.load('assets\\PNG\\Planes\\planeRed1.png')
        self.plane = Plane.Plane(pygame.math.Vector2(screen.get_width() / 2, screen.get_height() / 2), plane_img)
        # self.plane = Plane.Plane(pygame.math.Vector2(300, 300), plane_img)
        
    
    def update(self, dt, events):
        self.plane.update(dt, events)
    
    def draw(self, screen):
        self.plane.draw(screen)