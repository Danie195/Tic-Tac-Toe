# Tic-Tac-Toe using Pygame. It's practice for me to be more focused on using object-oriented programming

# TODO:
# 2 Create Grid
# 3 Create Assets
# 4 Create Game Logic
# 5 Create AI?

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
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)


class main:
    pygame.init()
    running = True
    while running:
        screen.fill(white)
        mousePos = pygame.mouse.get_pos()

        testRect = pygame.Rect(100, 200, 50, 100)  # For testing delete later
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        print(mousePos)
        pygame.draw.rect(screen, black, testRect)

        # Checks if the mouse is in the box
        if testRect.collidepoint((mousePos)):
            pygame.draw.rect(screen, red, testRect)

        pygame.display.update()
        clock.tick(FPS)


main()
