# Tower Defense HUD file
# Keeps track of in game stats on screen
# Floris van Rossum

import pygame
import pygame.draw as draw

class HUD:

    def __init__(self, windowWidth, windowHeight):
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.storeToggled = False

        gridWidth = 200

        hudWidth = 100
        self.hudRectangle = (0, windowHeight - hudWidth, windowWidth, hudWidth)
        self.defaultTextColor = [0, 0, 0]

        storeWidth = 200
        storeHeight = windowHeight
        self.storeRectangle = (10, windowHeight - (hudWidth/ 2) + 5, storeWidth, storeHeight)

        storeButtonHeight = 30
        storeButtonWidth = 150
        self.storeButtonRectangle = (10 + gridWidth, windowHeight - (hudWidth/ 2) + 5, storeButtonWidth, storeButtonHeight)

        goldRectangleWidth = 150
        goldRectangleHeight = 30
        self.goldRectangle = (10, windowHeight - (hudWidth/ 2) + 5, goldRectangleWidth, goldRectangleHeight)

        healthRectangleWidth = 150
        healthRectangleHeight = 30
        self.healthRectangle = (10, windowHeight - (hudWidth / 2) - 25, healthRectangleWidth, healthRectangleHeight)

        self.baseHealth = 100  # Starting health of the base
        self.gold = 100  # Starting gold of the player

        # Initialize the font object
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 20)

    def drawButton(self, screen, rectangle, rectangleColor, text, textColor):

        draw.rect(screen, rectangleColor, rectangle)

        if text is not None:
            surface = self.font.render(text, False, textColor)
            textSize = self.font.size(text)
            screen.blit(surface, (rectangle[0] + rectangle[2] / 2 - textSize[0] / 2, rectangle[1] + rectangle[3] / 2 - textSize[1] / 2))

    # Draw the HUD on the top right
    # Includes gold and base health, called repeatedly to update
    def drawHUD(self, screen):

        # Background rectangle
        backgroundColor = pygame.Color(60, 35, 71, 255)
        draw.rect(screen, backgroundColor, self.hudRectangle)

        # Draw the current gold
        goldColor = [206, 173, 53]
        textColor = self.defaultTextColor
        self.drawButton(screen, self.goldRectangle, goldColor, 'Gold: ' + str(self.gold), textColor)

        # Draw the current health
        healthColor = [114, 18, 18]
        textColor = self.defaultTextColor
        self.drawButton(screen, self.healthRectangle, healthColor, 'Health: ' + str(self.baseHealth), textColor)

        # Draw the store button
        storeButtonColor = [27, 99, 33]
        textColor = self.defaultTextColor
        self.drawButton(screen, self.storeButtonRectangle, storeButtonColor, 'Open Store', textColor)

        # Draw the store
        if self.storeToggled:
            self.drawStore()

    # Draw the store on the right side of the screen
    def drawStore(self):
        pass

    # Deal damage to the base
    def dealDamage(self, damage):
        self.baseHealth = self.baseHealth - damage
        self.drawHUD()