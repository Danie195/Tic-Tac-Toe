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
yellow = (255, 255, 0)


class shape:
    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y

    def draw(self):
        objWidth = int(displayWidth / 3)
        objHeight = int(displayHeight / 3)
        shapeSurf = pygame.Surface((objWidth, objHeight))
        shapeSurf.fill(white)
        if self.type == 0:
            pygame.draw.circle(shapeSurf, red, (objWidth / 2,
                                                objHeight / 2), objWidth / 2 - 5, 5)
        else:
            pygame.draw.line(shapeSurf, blue, (2, 2),
                             (objWidth - 2, objHeight - 2), 5)
            pygame.draw.line(
                shapeSurf, blue, (2, objHeight - 2), (objWidth - 2, 2), 5)
        screen.blit(shapeSurf, (self.x, self.y))


def drawGrid(mousePos):
    for i in range(0, 3):
        for j in range(0, 3):
            gridRect = pygame.Rect(i * (displayWidth / 3), j *
                                   (displayHeight / 3), displayWidth / 3, displayHeight / 3)
            if gridRect.collidepoint(mousePos):
                pygame.draw.rect(screen, yellow, gridRect, 1)
                gridX = int(i * displayWidth / 3)
                gridY = int(j * displayWidth / 3)
            else:
                pygame.draw.rect(screen, black, gridRect, 1)
    return gridX, gridY


def drawShape(mouseCounter, gridPos):
    # Need to draw a set number of shapes based on the mouse counter
    gridX = gridPos[0]
    gridY = gridPos[1]
    if mouseCounter % 2 == 0:
        shapeCircle = shape(1, gridX, gridY).draw
    elif mouseCounter % 2 != 0:
        shapeX = shape(0, gridX, gridY).draw


class main:
    pygame.init()
    running = True

    mouseCounter = 0
    while running:
        screen.fill(white)
        mousePos = pygame.mouse.get_pos()
        gridPos = drawGrid(mousePos)
        drawShape(mouseCounter, gridPos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseCounter += 1
                print(mouseCounter)

        pygame.display.flip()
        clock.tick(FPS)


main()
