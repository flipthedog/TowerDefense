# Tower Defense Tower File
# Contains the tower file
# Floris van Rossum

class Tower:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = id
        self.level = 0
        self.damage = 0
        self.rate = 0
        self.orientation = 0

        # Based on the id load a specific tower
        if id is 0:
            self.damage = 1
        elif id is 1:
            pass
        else:
            print("Invalid tower id")

    # rotate the tower to face the enemy
    def rotate(self):
        pass

    # Based on an id load a certain image for the tower
    def loadImage(self):
        pass