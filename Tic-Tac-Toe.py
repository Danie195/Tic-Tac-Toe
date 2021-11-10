# Tic-Tac-Toe using Pygame. It's practice for me to be more focused on using object-oriented programming

# NEED TO DO:
# Create cursor and click system
# Create grid
# Create assets
# Create game logic
# Create win/lose screen
# Create AI?

import pygame
import sys


class main:
    pygame.init()

    # Screen and clocl
    displayWidth = 400
    displayHeight = 400
    screen = pygame.display.set_mode((displayWidth, displayHeight))
    clock = pygame.time.Clock()
    FPS = 60

    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        screen.fill(white)
        pygame.display.update()
        clock.tick(FPS)


main()
