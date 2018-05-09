# Tower Defense Grid Cell Class
# Wi
# Floris van Rossum

import random, math

class Cell:

    def __init__(self, x, y, width, height, id, color):
        self.x = x # X Location of the center of the cell
        self.y = y # Y Location of the center of the cell
        # print("New cell x: " + str(x))
        # print("New cell y: " + str(y))

        self.width = width # Total width of the cell
        self.height = height # Total height of the cell

        #CELL IDS:
        # Road - 2
        # Wall - 1
        # Empty - 0
        self.id = id # Contains the id of the cell

        # Color
        # RGB
        # Each cell will have a specific random color
        self.color = color

        self.redoColor()

        self.neighbors = [] # contains all the neighbors of this cell (4 Connected)
        self.tower = None # This will contain a tower later

    # Calculate the distance between given cell and another cell
    def calcDistance(self, otherCell):
        return math.sqrt((otherCell.x - self.x) ** 2 + (otherCell.y - self.y) ** 2)

    # Check if this cell location is same as the given cell location
    def isSameLocation(self, otherCell):
        if self.x is otherCell.x and self.y is otherCell.y:
            # They are the same cell
            return True
        else:
            # They are not the same cell
            return False

    def redoColor(self):
        color = [0, 0, 0]

        if self.id is 0:
            # Empty
            # Gray - Black Shader
            shaderInt = random.randint(72, 126)
            self.color = [shaderInt,shaderInt,shaderInt]
        elif self.id is 1:
            # Wall
            # Gray - Blue
            shaderInt1 = random.randint(10, 23)
            shaderInt2 = random.randint(28, 61)
            self.color = [0, shaderInt1, shaderInt2]
        elif self.id is 2:
            # Road
            # White - Gray shader
            shaderInt = random.randint(173, 221)
            self.color = [shaderInt, shaderInt, shaderInt]
        else:
            self.color = color