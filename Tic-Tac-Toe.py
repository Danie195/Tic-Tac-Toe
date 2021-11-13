# Tic-Tac-Toe using Pygame. It's practice for me to be more focused on using object-oriented programming

# TODO:
# 4 Create Game Logic
# 5 Create AI?

import pygame
import sys
import numpy as np

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


class grid:
    values = np.zeros((3, 3))

    def drawGrid(mousePos, i, j):
        for x in range(0, 3):
            for y in range(0, 3):
                gridRect = pygame.Rect(x * (displayWidth / 3), y *
                                       (displayHeight / 3), displayWidth / 3, displayHeight / 3)
                if gridRect.collidepoint(mousePos):
                    gridX = int(x * displayWidth / 3)
                    gridY = int(y * displayHeight / 3)
                if gridRect.collidepoint(mousePos) and grid.values[i][j] == 0:
                    pygame.draw.rect(screen, yellow, gridRect, 1)
                else:
                    pygame.draw.rect(screen, black, gridRect, 1)
        return gridX, gridY

    def changeValues(gridPos, mouseCounter):
        # 1 = circle
        # 2 = x
        shapeType = (mouseCounter % 2) + 1
        gridX = gridPos[0]
        gridY = gridPos[1]
        i = round(gridX * 3 / displayWidth)
        j = round(gridY * 3 / displayHeight)
        if grid.values[i][j] == 0:
            grid.values[i][j] = shapeType
        return grid.values


def drawShape(mouseCounter, gridPos, i, j):
    gridX = gridPos[0]
    gridY = gridPos[1]
    if grid.values[i][j] == 0:  # Checks if nothing is in the spot
        if mouseCounter % 2 == 0:
            shape(1, gridX, gridY).draw()
            print('o')
        elif mouseCounter % 2 != 0:
            shape(0, gridX, gridY).draw()
            print('x')


class main:
    pygame.init()
    running = True
    screen.fill(white)
    i = 0
    j = 0
    grid.drawGrid((0, 0), i, j)  # Initialize the grid
    mouseCounter = 0
    while running:
        mousePos = pygame.mouse.get_pos()

        # Checks if the mouse is on the screen within a certain range
        if 0 < mousePos[0] < displayWidth - 5 and 0 < mousePos[1] < displayHeight - 5:
            gridPos = grid.drawGrid(mousePos, i, j)
            i = round(gridPos[0] * 3 / displayWidth)
            j = round(gridPos[1] * 3 / displayHeight)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseCounter += 1
                drawShape(mouseCounter, gridPos, i, j)
                print(grid.changeValues(gridPos, mouseCounter))

        pygame.display.flip()
        clock.tick(FPS)


main()
