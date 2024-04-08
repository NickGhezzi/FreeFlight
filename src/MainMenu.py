import pygame, globals
from pygame.locals import *

from Scene import Scene

from GameObject import GameObject
from Parallax import Parallax
from UIText import UIText
from UIButton import UIButton


class MainMenu(Scene):
    def __init__(self):   
        self.SCREEN_CENTER = pygame.math.Vector2(globals.HALF_SCREEN_WIDTH, globals.HALF_SCREEN_HEIGHT)
        #background
        bgImg = pygame.image.load('assets\\PNG\\background.png')
        bgObs = []
        for i in range(2):
            bgObs.append(GameObject(self.SCREEN_CENTER.copy(), bgImg))
        self.background = Parallax(bgObs, 0.5, globals.HALF_SCREEN_WIDTH)
        
        # title text
        font = pygame.font.Font('assets\\Font\\kenvector_future.ttf', 72)
        self.titleFont = UIText(pygame.math.Vector2(self.SCREEN_CENTER.x + 25, self.SCREEN_CENTER.y - 125), None, font, "Free   Flight", (0,0,0))
        
        #buttons
        font = pygame.font.Font('assets\\Font\\kenvector_future.ttf', 32)
        bImg = pygame.image.load('assets\\PNG\\UI\\buttonLarge.png')
        self.playB = UIButton(pygame.math.Vector2(self.SCREEN_CENTER.x - 180, self.SCREEN_CENTER.y + 50), bImg, UIText(pygame.math.Vector2(0, 0), None, font, "Play", (0,0,0)), self.playGame)
        self.quitB = UIButton(pygame.math.Vector2(self.SCREEN_CENTER.x + 180, self.SCREEN_CENTER.y + 50), bImg, UIText(pygame.math.Vector2(0, 0), None, font, "Quit", (0,0,0)), self.quitGame)
        
    def playGame(self):
        pygame.event.post(pygame.event.Event(globals.SCENE_CHANGE, scene='Game'))

    def quitGame(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))
    
    def update(self, dt, events):
        #update objects
        self.background.update(dt, events)
        self.playB.update(dt, events)
        self.quitB.update(dt, events)      
              

    def draw(self, screen):
        self.background.draw(screen)
        self.titleFont.draw(screen)
        self.playB.draw(screen)
        self.quitB.draw(screen)
        
        