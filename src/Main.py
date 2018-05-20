# Main.py
# Main loop of the tower defense program
# Floris van Rossum

import sys, pygame, os

import time
from Map import Map
from Enemy import Enemy
from HUD import HUD

def drawMap(map):

    for cell in map.map:
        color = pygame.Color(cell.color[0], cell.color[1], cell.color[2], 255)
        pygame.draw.rect(screen, color, (cell.x , cell.y , cell.width, cell.height), 0)

    cell = map.startCell
    color = pygame.Color(0, 255, 0, 255)
    pygame.draw.rect(screen, color, (cell.x, cell.y, cell.width, cell.height), 0)

    cell = map.endCell
    color = pygame.Color(255, 0, 0, 255)
    pygame.draw.rect(screen, color, (cell.x, cell.y, cell.width, cell.height), 0)

pygame.init()

timer = pygame.time.Clock()

print(os.name)
osString = os.name

if osString is "posix":
    import Tkinter
    root = Tkinter.Tk()
else:
    import tkinter
    root = tkinter.Tk()

width = root.winfo_screenwidth() - 100
height = root.winfo_screenheight() - 100
windowSize = width, height
black = 0, 0, 0
win_pos_left = 0
win_pos_top = 25
os.environ['SDL_VIDEO_WINDOW_POS'] = '{0},{1}'.format(win_pos_left, win_pos_top)

screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Tower Defense")

map = Map(width, height)

mapWidthCells = 18
mapHeightCells = 14
map.generateMap(mapWidthCells, mapHeightCells)

map.generatePath(mapWidthCells, mapHeightCells)


drawMap(map)

mousePos = pygame.mouse.get_pos()
closestCell = map.findCursorCell(mousePos)

print("This is the length of map: " + str(len(map.map)))
while 1:

    # Event getter loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            print("You clicked")
            mouse = pygame.mouse.get_pos()
            if map.hud.checkIfOnButton(mouse, map.hud.storeButtonRectangle):
                map.hud.storeToggled = not map.hud.storeToggled


    closestCell.redoColor()

    # Get the latest mouse position
    mousePos = pygame.mouse.get_pos()

    # Find the closest cell
    closestCell = map.findCursorCell(mousePos)

    # Debugging print statements
    # print("The current mouse: " + str(mousePos))
    # print("Mouse x: " + str(mousePos[0]))
    # print("Mouse x: " + str(mousePos[1]))
    # print("Closesr Cell x:" + str(closestCell.x))
    # print("Closesr Cell y:" + str(closestCell.y))

    # Color the closest cell neighbors
    for neighbor in closestCell.neighbors:
         if(neighbor is not None):
             neighbor.color = [255,255,0]



    # Draw the map on the screen
    drawMap(map)

    # Update the timer and the map
    dt = timer.tick(60)
    map.update(screen, dt)

    # Update the screen
    pygame.display.flip()

    # Print the time in between each frame
    #print(timer.get_rawtime())


    for neighbor in closestCell.neighbors:
        if(neighbor is not None):
            neighbor.redoColor()
