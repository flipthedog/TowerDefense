import sys, pygame
import time
from Map import Map

def drawMap(map):

    for cell in map:
        color = pygame.Color(cell.color[0], cell.color[1], cell.color[2], 255)
        pygame.draw.rect(screen, color, (cell.x, cell.y, cell.width, cell.height), 0)

pygame.init()

windowSize = width, height = 1720, 1080
black = 0, 0, 0

screen = pygame.display.set_mode(windowSize)

map = Map(width, height)

map.generateMap(30,20)
drawMap(map.map)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #screen.fill(black)
    map.generateMap(30, 20)
    drawMap(map.map)
    pygame.display.flip()
    time.sleep(1)
# Draw the map
