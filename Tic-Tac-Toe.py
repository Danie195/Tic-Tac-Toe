# Tic-Tac-Toe using Pygame. It's practice for me to be more focused on using object-oriented programming

# TODO:
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


def drawGrid():
    for i in range(0, 3):
        for j in range(0, 3):
            gridRect = pygame.Rect(
                i * (displayWidth / 3), j * (displayHeight / 3), displayWidth / 3, displayHeight / 3)
            pygame.draw.rect(screen, black, gridRect, 1)


class shape:
    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y

    def draw(self):
        objWidth = int(displayWidth / 3)
        objHeight = int(displayHeight / 3)
        shapeSurf = pygame.Surface((objWidth, objHeight))
        if self.type == 0:
            pygame.draw.circle(shapeSurf, red, (objWidth / 2,
                                                objHeight / 2), objWidth / 2 - 5, 5)
        else:
            pygame.draw.line(shapeSurf, blue, (2, 2),
                             (objWidth - 2, objHeight - 2), 5)
            pygame.draw.line(
                shapeSurf, blue, (2, objHeight - 2), (objWidth - 2, 2), 5)
        screen.blit(shapeSurf, (self.x, self.y))


class main:
    pygame.init()
    running = True
    while running:
        screen.fill(white)
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
        drawGrid()
        pygame.display.flip()
        clock.tick(FPS)


main()
