# Tower Defense Tower File
# Contains the tower file
# Floris van Rossum

import pygame, math
import Bullet

class Tower:

    def __init__(self, cell, id):
        self.cell = cell
        self.x = cell.x
        self.y = cell.y
        self.id = id # ID of the tower, distiguishes type
        self.level = 0 # Level of the tower
        self.damage = 0 # Damage of the tower
        self.rate = 0 # Fire rate of the tower
        self.range = 1000 # Firing range of the tower

        self.targetMode = 0 # Different targeting modes (weak, first, strong)
        self.orientation = 0 # Orientation of tower head

        self.towerWidth = 10
        self.towerHeight = 10

        # Holds the tower image
        self.towerImage = None
        self.towerRect = None

        self.target = None

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

    # update tower variables
    def updateTower(self):
        pass

    def findTarget(self, enemies):

        for enemy in enemies:
            # Distance from tower to enemy
            distance = math.sqrt((enemy.centerX - self.x) ** 2 + (enemy.centerY - self.y) ** 2)

            if self.targetMode is 0:
                if distance < self.range:
                    # We can fire on the target
                    return enemy

    # Based on an id load a certain image for the tower
    def drawTower(self, screen):

        imageOffset = 10

        if self.id is 0:

            self.towerImage = pygame.image.load("Images/index.png")
            self.towerRect = self.towerImage.get_rect()
            self.towerRect.width = self.cell.width - imageOffset
            self.towerRect.height = self.cell.height - imageOffset

        elif self.id is 1:
            pass

        elif self.id is 2:
            pass

        self.towerRect.x = self.x + imageOffset / 2
        self.towerRect.y = self.y + imageOffset / 2
        screen.blit(self.towerImage, self.towerRect, (0, 0, self.cell.width - imageOffset, self.cell.height - imageOffset))