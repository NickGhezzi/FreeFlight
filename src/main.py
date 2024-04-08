import pygame, sys, globals
from Game import *
from MainMenu import *

# Init
pygame.init()
running = True 
#screen

screen = pygame.display.set_mode([globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT])
#clock
clock = pygame.time.Clock()
#sets up initial scene. starting menu
currentScene = MainMenu()
# currentScene = Game()

# Main game loop
while running:
    #get frame events
    events = pygame.event.get()
    for event in events:
        #Close game
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        #Scene change events
        if event.type == globals.SCENE_CHANGE:
            if(event.scene == 'Game'):
                currentScene = Game()
            elif(event.scene == 'MainMenu'):
                currentScene = MainMenu()  
        

    # Delta time
    dt = clock.tick(60) / 1000

    # Background
    screen.fill((0, 0, 0))


    currentScene.update(dt, events)
    currentScene.draw(screen)


    # Flip the display
    pygame.display.flip()
