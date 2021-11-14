# Tic-Tac-Toe using Pygame. It's practice for me to be more focused on using object-oriented programming
# 1 = circle
# 2 = x

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
        shapeType = (mouseCounter % 2) + 1
        gridX = gridPos[0]
        gridY = gridPos[1]
        i = round(gridX * 3 / displayWidth)
        j = round(gridY * 3 / displayHeight)
        if grid.values[i, j] == 0:
            grid.values[i, j] = shapeType
        return grid.values


def drawShape(mouseCounter, gridPos, i, j):
    gridX = gridPos[0]
    gridY = gridPos[1]
    if mouseCounter % 2 == 0:
        shape(0, gridX, gridY).draw()
    elif mouseCounter % 2 != 0:
        shape(1, gridX, gridY).draw()


def checkWin():
    for i in range(0, 3):
        # Horizontal/vertical win by circle
        if np.all(grid.values[i, :] == 1) or np.all(grid.values[:, i] == 1):
            oWin = True
            xWin = False
            return oWin, xWin
        # Horizontal/vertical win by x
        elif np.all(grid.values[i, :] == 2) or np.all(grid.values[:, i] == 2):
            oWin = False
            xWin = True
            return oWin, xWin
        # Diagonal win by circle
        elif np.all(np.diagonal(grid.values) == 1) or np.all(np.diagonal(np.rot90(grid.values)) == 1):
            oWin = True
            xWin = False
            return oWin, xWin
        # Diagonal win by x
        elif np.all(np.diagonal(grid.values) == 2) or np.all(np.diagonal(np.rot90(grid.values)) == 2):
            oWin = False
            xWin = True
            return oWin, xWin
    return False, False  # Returns false for both if there is no win


def goScreen(checkWin):
    goRunning = True
    oWin = checkWin[0]
    xWin = checkWin[1]
    pygame.font.init()
    goFont1 = pygame.font.SysFont('Arial', 30)
    goFont2 = pygame.font.SysFont('Arial', 20)

    if oWin:
        goText = 'Player 1 Wins'
    elif xWin:
        goText = 'Player 2 Wins'
    elif oWin == False and xWin == False and np.all(grid.values != 0):  # Tie
        goText = 'Tie'
    else:
        return True  # Running variable is true
    screen.fill(white)
    goWinner = goFont1.render(goText, True, black)
    goReset = goFont2.render('Press R to reset', True, black)
    goWinnerRect = goWinner.get_rect(
        center=(displayWidth / 2, displayHeight / 2))
    goResetRect = goReset.get_rect(
        center=(displayWidth / 2, displayHeight / 2 + 30))
    screen.blit(goWinner, goWinnerRect)
    screen.blit(goReset, goResetRect)
    while goRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                goRunning = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    goRunning = False
                    return False  # Running variable is false

        pygame.display.flip()
        clock.tick(FPS)


class main:
    pygame.init()
    while True:
        running = True
        screen.fill(white)
        grid.values = np.zeros((3, 3))
        i = 0
        j = 0
        grid.drawGrid((0, 0), i, j)  # Initialize the grid
        mouseCounter = 0  # Start with x
        while running:
            mousePos = pygame.mouse.get_pos()

            # Checks if the mouse is on the screen within a certain range
            if 0 < mousePos[0] < displayWidth - 5 and 0 < mousePos[1] < displayHeight - 5:
                gridPos = grid.drawGrid(mousePos, i, j)
                i = round(gridPos[0] * 3 / displayWidth)
                j = round(gridPos[1] * 3 / displayHeight)

            if grid.values[i][j] == 0:  # Checks if nothing is in the spot of the grid
                validSpot = True
            else:
                validSpot = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and validSpot:
                    mouseCounter += 1
                    drawShape(mouseCounter, gridPos, i, j)
                    grid.changeValues(gridPos, mouseCounter)
                    print(grid.values)
                    # Checks for a win and starts the go screen if so
                    running = goScreen(checkWin())

            pygame.display.flip()
            clock.tick(FPS)


main()
