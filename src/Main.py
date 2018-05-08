import sys, pygame
import Tkinter
import time
from Map import Map

def drawMap(map):

    for cell in map:
        color = pygame.Color(cell.color[0], cell.color[1], cell.color[2], 255)
        pygame.draw.rect(screen, color, (cell.x, cell.y, cell.width, cell.height), 0)

pygame.init()
root = Tkinter.Tk()
width = root.winfo_screenwidth() - 100
height = root.winfo_screenheight() - 100
windowSize = width, height
black = 0, 0, 0

screen = pygame.display.set_mode(windowSize)

map = Map(width, height)

map.generateMap(30,20)
map.generatePath()
drawMap(map.map)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #screen.fill(black)

    map.generateMap(30, 20) # Generate a nxn map
    map.generatePath() # Generate a path in the map
    drawMap(map.map) # Draw the map
    drawMap(map.path) # Draw the path

    pygame.display.flip()
    time.sleep(1)
# Draw the map
