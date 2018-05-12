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
        self.width = 3
        self.height = 3

    # Update the bullet position, speed, target location
    def updateBullet(self):
        targetX = self.target.x
        targetY = self.target.y

        angle = math.tan(targetY / targetX)
        velX = self.velocity * math.cos(angle)
        velY = self.velocity * math.sin(angle)

        self.x = self.x + velX
        self.y = self.y + velY

    # draw the bullet
    def drawBullet(self, screen):

        imageOffset = 10

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
        targetX = self.target.x
        targetY = self.target.y

        return math.sqrt((self.x - targetX) ** 2 + (self.y - targetY) ** 2)
