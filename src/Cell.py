# Tower Defense Grid Cell Class
# Wi
# Floris van Rossum

import math

class Cell:

    def __init__(self, x, y, width, height, id, color):
        self.x = x # X Location of the center of the cell
        self.y = y # Y Location of the center of the cell
        self.width = width # Total width of the cell
        self.height = height # Total height of the cell

        #CELL IDS:
        # Road - 1
        # Wall - 0
        self.id = id # Contains the id of the cell

        # Color
        # RGB
        # Each cell will have a specific random color
        self.color = color

        self.neighbors = [] # contains all the neighbors of this cell (4 Connected)
        self.tower = None # This will contain a tower later

    def aFunction(self):
        pass

