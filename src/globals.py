import pygame

#custom events
PLAYER_SCORED = pygame.event.custom_type()
PLAYER_DIED = pygame.event.custom_type()
SCENE_CHANGE = pygame.event.custom_type() #alerts the game of a scene change request. contains the new scene

#screen globals
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480

HALF_SCREEN_WIDTH = SCREEN_WIDTH * 0.5
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT * 0.5

#Makes debug elements visible 
DEBUG = False



