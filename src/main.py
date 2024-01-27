import pygame, sys, Game

# Init
pygame.init()
#screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
#clock
clock = pygame.time.Clock()
#game
plane_game = Game()
plane_game.init()
    #CIRCLE
# posx = SCREEN_WIDTH/2
# posy =  SCREEN_HEIGHT/2

# #posx = 0
# #posy =  0


# Main game loop
while True:
    # Close game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Delta time
    dt = clock.tick(60) / 1000

    # Background
    screen.fill((0, 0, 0))


    plane_game.update(dt)
    plane_game.draw(screen)



    # gravity = -9.8


    #CIRCLE
    # posy += gravity * dt 
    # # Draw a solid blue circle in the center
    # circle = pygame.draw.circle(screen, (0, 0, 255), (posx, posy), 75)

    # print(circle.center, dt)

    # Flip the display
    pygame.display.flip()
