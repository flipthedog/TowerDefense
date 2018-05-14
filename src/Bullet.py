# Tower Defense Bullet File
# Bullet class for shooting
# Floris van Rossum

import math, pygame

class Bullet:

    def __init__(self, x, y, velocity, target):
        self.x = x # The x position
        self.y = y # The y position
        self.velocity = velocity # The total velocity of the bullet
        self.target = target # Enemy target object
        self.impact = False # Impacted the enemy?
        self.width = 10
        self.height = 10

    # Update the bullet position, speed, target location
    def updateBullet(self):
        targetX = self.target.centerX
        targetY = self.target.centerY

        if (-targetX + self.x) is not 0.0:
            angle = math.tan(  (-targetY + self.y) / (-targetX + self.x))

        #print(angle)
        velX = self.velocity * math.cos(angle)
        velY = self.velocity * math.sin(angle)

        self.x = self.x + velX
        self.y = self.y + velY

    def printEnemy(self):
        print("X: " + str(self.target.x) + "Y: " + str(self.target.y))

    # draw the bullet
    def drawBullet(self, screen):

        imageOffset = 1

        if not self.impact:
            self.bulletImage = pygame.image.load("Images/index.png")
            self.bulletRect = self.bulletImage.get_rect()
            self.bulletRect.x = self.x + imageOffset / 2
            self.bulletRect.y = self.y + imageOffset / 2
            self.centerX = self.x + self.width + imageOffset / 2
            self.centerY = self.y + self.height + imageOffset / 2

            screen.blit(self.bulletImage, (self.bulletRect.x, self.bulletRect.y, self.x + 10, self.y + 10), (0, 0,
                                                                                                          self.width - imageOffset,
                                                                                                          self.height - imageOffset))

    # Calculate the distance from bullet to target
    def distanceToTarget(self):
        targetX = self.target.centerX
        targetY = self.target.centerY

        return math.sqrt((self.x - targetX) ** 2 + (self.y - targetY) ** 2)
