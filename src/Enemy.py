# Tower Defense Enemy File
# The enemy class
# Floris van Rossum

class Enemy:

    def __init__(self,x,y,id,level):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.hp = 0
        self.armor = 0
        self.id = id
        self.level = level

        if id is 0:
            self.hp = 10

    def generateWave(self,level):

    # Based on enemy id, draw an enemy
    def drawEnemy(self):
        pass

    # Update the position of the enemy
    def updatePosition(self, vx, vy):
        self.x = self.x + vx
        self.y = self.y + vy