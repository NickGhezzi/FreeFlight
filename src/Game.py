import pygame, globals
from pygame.locals import *

from Scene import Scene

from GameObject import GameObject
from Plane import Plane
from Parallax import Parallax
from Cliff import Cliff
from UIText import UIText
from PauseMenu import PauseMenu
from GameOverMenu import GameOverMenu

class Game(Scene):

    def __init__(self):   
        #variables
        self.SCREEN_CENTER = pygame.math.Vector2(globals.HALF_SCREEN_WIDTH, globals.HALF_SCREEN_HEIGHT)
        self.obstacleSpeed = 2.5
        self.score = 0
        self.paused = False #used to activate pause menu
        self.gameStart = True 
        self.stopped = True
        ### GAME OBJECTS ###
        #player
        plane_img = pygame.image.load('assets\\PNG\\Planes\\planeRed1.png')
        self.player = Plane(pygame.math.Vector2(self.SCREEN_CENTER.x - 150, self.SCREEN_CENTER.y), plane_img, True)
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
        ### UI OBJECTS ###
        #score UI
        font = pygame.font.Font('assets\\Font\\kenvector_future.ttf', 24)
        self.scoreFont = UIText(pygame.math.Vector2(globals.HALF_SCREEN_WIDTH, 10), None, font, "0", (0,0,0))
        #high-score UI number
        font = pygame.font.Font('assets\\Font\\kenvector_future.ttf', 24)
        self.hScoreFont = UIText(pygame.math.Vector2(globals.SCREEN_WIDTH - 20, 10), None, font, "0", (0,0,0))
        #high-score UI label
        font = pygame.font.Font('assets\\Font\\kenvector_future.ttf', 24)
        self.hScoreLabelFont = UIText(pygame.math.Vector2(globals.SCREEN_WIDTH - 130, 10), None, font, "High-score: ", (0,0,0))
        #Begin text
        font = pygame.font.Font('assets\\Font\\kenvector_future.ttf', 48)
        self.beginFont = UIText(pygame.math.Vector2(globals.HALF_SCREEN_WIDTH, globals.SCREEN_HEIGHT - 100), None, font, "Click to Begin...", (64,64,64))
        #pause menu
        self.pauseMenu = PauseMenu(self.reset)
        self.pauseMenu.isVisible = False
        #death menu
        self.gameOverMenu = GameOverMenu(self.reset)
        self.gameOverMenu.isVisible = False
        
        
    
    def update(self, dt, events):
        #update objects            
        if(self.stopped == False):
            self.player.update(dt, events)
            self.cliffPrlx.update(dt, events)
            self.background.update(dt, events)
            self.foreground.update(dt, events)
        
        #event handling
        for event in  events:
            #begin
            if(self.gameStart == True and self.paused == False):
                if event.type == pygame.MOUSEBUTTONUP:
                    self.stopped = False
                    self.gameStart = False
                    return
            #Handle player score event
            if event.type == globals.PLAYER_SCORED:
                self.score += 1
                self.background.increaseSpeed(0.2)
                self.cliffPrlx.increaseSpeed(0.2)
                self.foreground.increaseSpeed(0.2)
                self.scoreFont.text = str(self.score)
                self.hScoreFont.text = str(self.score)
                print("Player score: ", self.score)            
            #Handle user input
            if event.type == pygame.KEYDOWN:
                #reset
                if event.key == pygame.K_r:
                    print("game reset")
                    self.reset()
                #pause
                if event.key == pygame.K_ESCAPE:                    
                    self.paused = not self.paused
                    self.pauseMenu.isVisible = self.paused
                    if self.gameStart == False: self.stopped = self.paused
                    
        self.pauseMenu.update(dt, events)
        self.gameOverMenu.update(dt, events)
        

                    
        
    
    def draw(self, screen):
        self.background.draw(screen)
        self.cliffPrlx.draw(screen)
        self.foreground.draw(screen)
        self.player.draw(screen)
        self.scoreFont.draw(screen)
        self.hScoreFont.draw(screen)
        self.hScoreLabelFont.draw(screen)
        if(self.gameStart == True):
            self.beginFont.draw(screen)
        
        if(self.player.isDead == True):
            #show "Dead. press r to restart"
            self.stopped = True
            self.gameOverMenu.isVisible = True
        self.pauseMenu.draw(screen)
        self.gameOverMenu.draw(screen)
        
        
        
    def reset(self):
        self.score = 0
        self.scoreFont.text = "0"
        self.background.reset()
        self.cliffPrlx.reset()
        self.foreground.reset()
        self.player.reset()
        self.paused = False
        self.gameStart = True
        self.stopped = True
        self.pauseMenu.isVisible = False
        self.gameOverMenu.isVisible = False
        
        