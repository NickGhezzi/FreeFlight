import pygame, sys
from Game import *

# Init
pygame.init()
running = True 
#screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
#clock
clock = pygame.time.Clock()
#game
plane_game = Game()
plane_game.init(screen)

# Main game loop
while running:
    #get frame events
    events = pygame.event.get()
    # Close game
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    # Delta time
    dt = clock.tick(60) / 1000

    # Background
    screen.fill((0, 0, 0))


    plane_game.update(dt, events)
    plane_game.draw(screen)


    # Flip the display
    pygame.display.flip()
