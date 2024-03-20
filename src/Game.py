import pygame, globals
from pygame.locals import *

from GameObject import GameObject
from Plane import Plane
from Parallax import Parallax
from Cliff import Cliff


class Game(object):
    obstacleSpeed = 2.5
    SCREEN_CENTER = 0
    score = 0
    gameOver = False
    paused = False
    def init(self, screen):   
        #variables
        self.SCREEN_CENTER = pygame.math.Vector2(globals.HALF_SCREEN_WIDTH, globals.HALF_SCREEN_HEIGHT)
        #player
        plane_img = pygame.image.load('assets\\PNG\\Planes\\planeRed1.png')
        self.player = Plane(self.SCREEN_CENTER.copy(), plane_img, True)
        #cliffs
        cliffObs = []
        cliffImg = pygame.image.load('assets\\PNG\\rockGrass.png')
        for i in range(6):
            cliffObs.append(Cliff(pygame.math.Vector2(globals.SCREEN_WIDTH, globals.HALF_SCREEN_HEIGHT), cliffImg, self.player, True))
        self.cliffPrlx = Parallax(cliffObs, self.obstacleSpeed, globals.SCREEN_WIDTH, -1, 200)
        
        #background
        bgImg = pygame.image.load('assets\\PNG\\background.png')
        bgObs = []
        for i in range(2):
            bgObs.append(GameObject(self.SCREEN_CENTER.copy(), bgImg))
        self.background = Parallax(bgObs, 1, globals.HALF_SCREEN_WIDTH)
        
        #forground
        fgImg = pygame.image.load('assets\\PNG\\groundGrass.png')
        fgObs = []
        for i in range(3):
            fgObs.append(GameObject(pygame.math.Vector2(globals.HALF_SCREEN_WIDTH, globals.SCREEN_HEIGHT - (fgImg.get_height() * 0.3)), fgImg))
        self.foreground = Parallax(fgObs, self.obstacleSpeed, globals.HALF_SCREEN_WIDTH)   
    
    def update(self, dt, events):
        #update objects
        if(self.paused == False):
            self.player.update(dt, events)
            
        if(self.gameOver == False or self.paused == False):
            self.cliffPrlx.update(dt, events)
            self.background.update(dt, events)
            self.foreground.update(dt, events)
        
        #game logic
        for event in  events:
            if event.type == globals.PLAYER_SCORED:
                self.score += 1
                print("Player score: ", self.score)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    print("game reset")
                    self.background.reset()
                    self.cliffPrlx.reset()
                    self.foreground.reset()
                    self.player.reset()
                    self.reset()
        #todo increase parallax speed as score goes up
        
    
    def draw(self, screen):
        self.background.draw(screen)
        self.cliffPrlx.draw(screen)
        self.foreground.draw(screen)
        self.player.draw(screen)
        
    def reset(self):
        self.score = 0
        gameOver = False
        paused = False
        