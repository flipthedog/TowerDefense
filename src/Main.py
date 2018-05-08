import sys, pygame
import tkinter
import time
from Map import Map

def drawMap(map):

    for cell in map:
        color = pygame.Color(cell.color[0], cell.color[1], cell.color[2], 255)
        pygame.draw.rect(screen, color, (cell.x, cell.y, cell.width, cell.height), 0)

pygame.init()
root = tkinter.Tk()
width = root.winfo_screenwidth() - 100
height = root.winfo_screenheight() - 100
windowSize = width, height
black = 0, 0, 0

screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Tower Defense")

map = Map(width, height)

map.generateMap(30,20)

map.generatePath()
drawMap(map.map)

mousePos = pygame.mouse.get_pos()
closestCell = map.findCursorCell(mousePos)

print("This is the length of map: " + str(len(map.map)))
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    closestCell.redoColor()

    mousePos = pygame.mouse.get_pos()
    # print("The current mouse: " + str(mousePos))
    closestCell = map.findCursorCell(mousePos)
    # print("Mouse x: " + str(mousePos[0]))
    # print("Mouse x: " + str(mousePos[1]))
    # print("Closesr Cell x:" + str(closestCell.x))
    # print("Closesr Cell y:" + str(closestCell.y))

    closestCell.color = [255,255,0]
    # for neighbor in closestCell.neighbors:
    #     if(neighbor is not None):
    #         neighbor.color = [255,255,0]

    drawMap(map.map)

    pygame.display.flip()
    time.sleep(0.05)
# Draw the map

