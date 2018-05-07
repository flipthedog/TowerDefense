# Tower Defense Map File
# This will hold all the cells that consist of the map

class Map:

    def __init__(self):
        self.map = [] # Contains all the cells that make up the map
        self.path = [] # Ordered list of cells that make up the path for the enemies
        self.