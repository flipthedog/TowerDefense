# Tower Defense Map File
# This will hold all the cells that consist of the map

import math
from Cell import Cell
import random

class Map:

    def __init__(self,width,height):
        self.windowWidth = width
        self.windowHeight = height
        self.widthNumber = 0
        self.heightNumber = 0
        self.start = 0
        self.end = 0
        self.map = [] # Contains all the cells that make up the map
        self.path = [] # Ordered list of cells that make up the path for the enemies

    # Generate a map of cells
    # widthNo - the number of cells in width
    # height - the number of cells in height
    # fills self.map and self.path
    def generateMap(self, widthNo, heightNo):
        # Create random start and end points
        self.widthNumber = widthNo
        self.heightNumber = heightNo
        self.start = [random.randint(0, widthNo), random.randint(0,heightNo)]
        self.end = [random.randint(0, widthNo), random.randint(0,heightNo)]

        cellWidth = self.windowWidth/widthNo
        cellHeight = self.windowHeight/heightNo

        # print("Calculated Cell Height Count: " + str(heightNo))
        # print("Calculated Cell Width Count: " + str(widthNo))
        # print("Calculated Cell Height: " + str(cellHeight))
        # print("Calculated Cell Width: " + str(cellWidth))

        # Create a map of wall cells
        for i in range(0, heightNo):

            for j in range(0, widthNo):
                color = [0, 0, 0] # HSV Array containing the cell color
                randomInt = random.randint(1, 30)
                color[0] = randomInt
                color[1] = randomInt
                color[2] = randomInt

                newCell = Cell(i*cellWidth, j*cellHeight, cellWidth, cellHeight, 0, color)
                # find all the neighbors of the cell

                self.map.append(newCell)


    # Create a path from the start to the end, make the path a little interesting
    def generatePath(self):
        path = [] # contains all the cells that make up the path


        for cell in path:
            # Update the cell ids in the path
            cell.id = 1
            cell.color = [0, 0, 0]

        self.path = path

    # find all the neighbors of a cell
    # cell - the cell of which the neighbors need to be found
    # @return - an array of all the neighbors
    def findNeighbors(self):
        neighbors = []

        map = self.map

        cellZero = map[0]
        cellZero_1 = map[1]
        cellZero_2 = map[self.widthNumber]
        cellZero.neighbors = [cellZero_1, cellZero_2, None, None]

        self.findNeighborsCell(cellZero_1)
        self.findNeighborsCell(cellZero_2)
        
        return neighbors

    def findNeighborsCell(self,cell):
        neighbors = []

        return neighbors