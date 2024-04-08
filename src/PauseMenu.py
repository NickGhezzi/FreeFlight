import pygame, globals
from pygame.locals import *

from Scene import Scene

from UIText import UIText
from UIButton import UIButton


class PauseMenu(Scene):
    def __init__(self, resetCallBack):   
        self.SCREEN_CENTER = pygame.math.Vector2(globals.HALF_SCREEN_WIDTH, globals.HALF_SCREEN_HEIGHT)       
        # title text
        font = pygame.font.Font('assets\\Font\\kenvector_future.ttf', 48)
        self.titleFont = UIText(pygame.math.Vector2(self.SCREEN_CENTER.x + 25, self.SCREEN_CENTER.y - 125), None, font, "Paused", (64,64,64))
        
        #buttons
        font = pygame.font.Font('assets\\Font\\kenvector_future.ttf', 16)
        bImg = pygame.image.load('assets\\PNG\\UI\\buttonSmall.png')
        self.mainMenuB = UIButton(pygame.math.Vector2(self.SCREEN_CENTER.x - 180, self.SCREEN_CENTER.y + 50), bImg, UIText(pygame.math.Vector2(0, 0), None, font, "MainMenu", (0,0,0)), self.mainMenu)
        self.resetButton = UIButton(pygame.math.Vector2(self.SCREEN_CENTER.x, self.SCREEN_CENTER.y + 50), bImg, UIText(pygame.math.Vector2(0, 0), None, font, "Reset", (0,0,0)), resetCallBack)
        self.quitB = UIButton(pygame.math.Vector2(self.SCREEN_CENTER.x + 180, self.SCREEN_CENTER.y + 50), bImg, UIText(pygame.math.Vector2(0, 0), None, font, "Quit", (0,0,0)), self.quitGame)
        
    def mainMenu(self):
        pygame.event.post(pygame.event.Event(globals.SCENE_CHANGE, scene='MainMenu'))

    def quitGame(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))
    
    def update(self, dt, events):
        #update objects
        if(self.isVisible == False):
            return
        self.mainMenuB.update(dt, events)
        self.resetButton.update(dt, events)
        self.quitB.update(dt, events)      
              

    def draw(self, screen):
        if(self.isVisible == False):
            return
        #pygame.draw.rect(screen, pygame.Color(0, 0, 0, 128), screen.get_rect())
        self.titleFont.draw(screen)
        self.mainMenuB.draw(screen)
        self.resetButton.draw(screen)
        self.quitB.draw(screen)
        
        