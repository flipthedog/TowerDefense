# Tower Defense Enemy File
# The enemy class
# Floris van Rossum

import pygame, math

class Enemy:

    def __init__(self,id,level, path):
        # Position and velocity of the enemy
        self.x = path[0].x # Initialize the enemy on the first tile of path
        self.y = path[0].y # Initialize the enemy on the first tile of  path
        self.dir = [0,0] # Direction that the enemy moves in
        self.vx = 1 # velocity variables of the enemy
        self.vy = 1 # velocity variables of the enemy

        # Type of enemy variables
        self.hp = 0
        self.armor = 0
        self.id = id
        self.level = level

        self.enemyImage = None
        self.enemyRect = None

        # the path that the enemy has to follow
        self.path = path
        self.index = 1 # Where along the path the enemy currently is

        # Toggle variable to determine if enemy has arrived at base
        self.goalReached = False

        if id is 0:
            self.hp = 10

    def generateWave(self,level):
        pass

    # Based on enemy id, draw an enemy
    def drawEnemy(self, screen):
        self.enemyImage = pygame.image.load("Images/index.png")
        self.enemyRect = self.enemyImage.get_rect()
        self.enemyRect.x = self.x
        self.enemyRect.y = self.y
        screen.blit(self.enemyImage, self.enemyRect)

    # Update the position of the enemy
    def updatePosition(self):

        goal = self.path[self.index]  # The goal cell that the enemy is

        # If we have not reached the goal
        if not self.index > len(self.path) and not self.goalReached:

            # Distance to the goal
            enemyDist = math.sqrt((goal.x - self.x) ** 2 + (goal.y - self.y) ** 2)
            print("this is the distance: " + str(enemyDist))
            enemyDistThresh = 0.5
            if(enemyDist < enemyDistThresh):
                self.index = self.index + 1

            goal = self.path[self.index] # The goal cell that the enemy is travelling to

            print("Target goal: (" + str(goal.x) + "," + str(goal.y) + ")")
            print("Index: " + str(self.index))

            if (goal.x > self.x):
                # going down
                print("Going right")
                self.dir[0] = 1
            elif (goal.x < self.x):
                # going up
                print("Going left")
                self.dir[0] = -1
            else:
                # Stop
                print("Stopped moving X")
                self.dir[0] = 0

            if(goal.y < self.y):
                # Going right
                print("Going up")
                self.dir[1] = 1
            elif (goal.y > self.y):
                # Going left
                print("Going down")
                self.dir[1] = -1
            else:
                # Stop
                print("Stopped moving Y")
                self.dir[1] = 0

            if abs(goal.x - self.x) > enemyDistThresh:
                self.x = self.x + self.vx * self.dir[0]

            if abs(goal.y - self.y) > enemyDistThresh:
                self.y = self.y - self.vy * self.dir[1]

        else:
            print("Goal reached")
            self.dir = [0,0] # Stop moving
            self.goalReached = True
            self.index = 0
