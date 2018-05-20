# Tower Defense Tower File
# Contains the tower file
# Floris van Rossum

import pygame, math
from Bullet import Bullet

class Tower:

    def __init__(self, cell, id):

        # Tower info
        self.cell = cell
        self.x = cell.x
        self.y = cell.y
        self.centerX = 0
        self.centerY = 0

        self.id = id # ID of the tower, distiguishes type
        self.level = 0 # Level of the tower
        self.damage = 0 # Damage of the tower
        self.rate = 1000 # Fire rate of the tower
        self.range = 500 # Firing range of the tower

        # Firing info
        self.canFire = False
        self.rate_timer = 0
        self.targetMode = 0 # Different targeting modes (weak, first, strong)
        self.orientation = 0 # Orientation of tower head
        self.shootEvent = pygame.USEREVENT + 1
        pygame.time.set_timer(self.shootEvent, self.rate)

        self.target = None

        # Bullet info
        self.bullets = []

        # Tower image stuff
        self.towerImage = None
        self.towerRect = None
        self.towerWidth = 10
        self.towerHeight = 10

        # Tower identification to load a specific tower
        if id is 0:
            self.damage = 1
        elif id is 1:
            pass
        else:
            print("Invalid tower id")

        #self.toggleFireTrue()

    # toggle the can fire variable
    def toggleFireFalse(self):
        print("Toggled False")
        self.canFire = False

    def toggleFireTrue(self):
        print("Toggled True")
        self.canFire = True

    # rotate the tower to face the enemy
    def rotate(self):
        pass

    # update tower variables
    def updateTower(self, screen, enemies, path, windowWidth, windowHeight, deltaT):

        self.rate_timer += deltaT
        if self.rate_timer >= self.rate:
            #print("SPAWN")
            self.fire(path,enemies)
            self.rate_timer -= self.rate

        # for e in pygame.event.get():
        #     print("Event detected")
        #     if e is self.shootEvent:
        #         self.fire(path,enemies)

        if len(self.bullets) > 0:

            for bullet in self.bullets:
                # bullet.printEnemy()

                if bullet.x < 0 or bullet.x > windowWidth or bullet.y < 0 or bullet.y > windowHeight:
                    self.bullets.remove(bullet)
                    # print("Bullet removed outside")
                else:

                    if bullet.distanceToTarget() < 10:
                        self.bullets.remove(bullet)
                        # print("Bullet removed - target hit")
                    else:
                        bullet.updateBullet()
                        bullet.drawBullet(screen)

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

        self.centerX = int(round(self.x + self.cell.width / 2 + imageOffset / 2))
        self.centerY = int(round(self.y + self.cell.height / 2 + imageOffset / 2))

        pygame.draw.circle(screen, pygame.Color('white'), [self.centerX, self.centerY], self.range, 2)

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

    def fire(self, path, enemies):
        enemyTarget = self.findTarget(enemies)

        if enemyTarget is not None:
            newBullet = Bullet(self.x + path[0].width / 2, self.y + path[0].height / 2,
                               20, enemyTarget)
            self.bullets.append(newBullet)