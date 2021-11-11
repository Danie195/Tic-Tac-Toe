# Tic-Tac-Toe using Pygame. It's practice for me to be more focused on using object-oriented programming

import pygame
import sys

# Screen and clock
displayWidth = 400
displayHeight = 400
screen = pygame.display.set_mode((displayWidth, displayHeight))
clock = pygame.time.Clock()
FPS = 60

# Colors
white = (255, 255, 255)
black = (0, 0, 0)


class main:
    pygame.init()
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
