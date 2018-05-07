# Tower Defense Map File
# This will hold all the cells that consist of the map

import math
from Cell import Cell
import random

class Map:

    def __init__(self,width,height):
        self.windowWidth = width
        self.windowHeight = height
        self.map = [] # Contains all the cells that make up the map
        self.path = [] # Ordered list of cells that make up the path for the enemies

    # Generate a map of cells
    # widthNo - the number of cells in width
    # height - the number of cells in height
    # fills self.map and self.path
    def generateMap(self, widthNo, heightNo):
        cellWidth = self.windowWidth/widthNo
        cellHeight = self.windowHeight/heightNo

        print("Calculated Cell Height Count: " + str(heightNo))
        print("Calculated Cell Width Count: " + str(widthNo))
        print("Calculated Cell Height: " + str(cellHeight))
        print("Calculated Cell Width: " + str(cellWidth))

        # Create a map of wall cells
        for i in range(0, widthNo):

            for j in range(0, heightNo):
                color = [0, 0, 0] # HSV Array containing the cell color
                randomInt = random.randint(1, 30)
                color[0] = randomInt
                color[1] = randomInt
                color[2] = randomInt

                newCell = Cell(i*cellWidth, j*cellHeight, cellWidth, cellHeight, 0, color)
                self.map.append(newCell)




