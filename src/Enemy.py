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
        self.id = id # ID of the enemy
        self.level = level # Level of the enemy
        self.gold = 0 # Gold given upon kill
        self.damage = 1 # Damage dealt to the base upon arrival

        self.enemyImage = None
        self.enemyRect = None

        # the path that the enemy has to follow
        self.path = path
        self.index = 1 # Where along the path the enemy currently is

        # Toggle variable to determine if enemy has arrived at base
        self.goalReached = False

        if id is 0:
            self.hp = 10
            self.gold = 1
            self.damage = 1

    def generateWave(self,level):
        pass

    # Based on enemy id, draw an enemy
    def drawEnemy(self, screen):

        if self.id is 0:
            self.enemyImage = pygame.image.load("Images/index.png")
            self.enemyRect = self.enemyImage.get_rect()
        elif self.id is 1:
            pass
        elif self.id is 2:
            pass

        self.enemyRect.x = self.x
        self.enemyRect.y = self.y
        screen.blit(self.enemyImage, self.enemyRect)

    # Update the position of the enemy
    def updatePosition(self):

        if not self.goalReached:
            goal = self.path[self.index]  # The goal cell that the enemy is

        # If we have not reached the goal
        if not self.index > len(self.path) - 1 and not self.goalReached:

            # Distance to the goal
            enemyDist = math.sqrt((goal.x - self.x) ** 2 + (goal.y - self.y) ** 2)
            # print("this is the distance: " + str(enemyDist))
            enemyDistThresh = 0.1
            if(enemyDist < enemyDistThresh):
                self.index = self.index + 1

            if self.index > len(self.path) - 1:
                self.goalReached = True

            if not self.goalReached:
                goal = self.path[self.index] # The goal cell that the enemy is travelling to

                # print("Target goal: (" + str(goal.x) + "," + str(goal.y) + ")")
                # print("Index: " + str(self.index))

                if (goal.x > self.x):
                    # going down
                    # print("Going right")
                    self.dir[0] = 1
                elif (goal.x < self.x):
                    # going up
                    # print("Going left")
                    self.dir[0] = -1
                else:
                    # Stop
                    # print("Stopped moving X")
                    self.dir[0] = 0

                if(goal.y < self.y):
                    # Going right
                    # print("Going up")
                    self.dir[1] = 1
                elif (goal.y > self.y):
                    # Going left
                    # print("Going down")
                    self.dir[1] = -1
                else:
                    # Stop
                    # print("Stopped moving Y")
                    self.dir[1] = 0

                if abs(goal.x - self.x) > enemyDistThresh:
                    self.x = self.x + self.vx * self.dir[0]

                if abs(goal.y - self.y) > enemyDistThresh:
                    self.y = self.y - self.vy * self.dir[1]

        else:
            # print("Goal reached")
            self.dir = [0,0] # Stop moving
            self.goalReached = True
            self.index = 0
