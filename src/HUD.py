# Tower Defense HUD file
# Keeps track of in game stats on screen
# Floris van Rossum

import pygame
import pygame.draw as draw
import math, random

class HUD:

    def __init__(self, windowWidth, windowHeight):
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.storeToggled = False

        self.buttonPressed = True

        gridWidth = 200

        hudWidth = 100
        self.hudRectangle = (0, windowHeight - hudWidth, windowWidth, hudWidth)
        self.defaultTextColor = [0, 0, 0]

        storeWidth = 200
        storeHeight = windowHeight
        self.storeRectangle = (windowWidth - storeWidth, 0, storeWidth, storeHeight)

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

        # Check for button clicks
        click = pygame.mouse.get_pressed()
        #print("You clicked here: " + str(click))

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
            self.drawStore(screen)

    def checkIfOnButton(self, mouse, rectangle):
        mouseX = mouse[0]
        mouseY = mouse[1]

        print("Mouse x,y: (" + str(mouseX) + ", " + str(mouseY) + ")")
        print(rectangle)
        if mouseX > rectangle[0] and mouseY > rectangle[1] and mouseX < (rectangle[0] + rectangle[2]) and mouseY < (rectangle[1] + rectangle[3]):
            return True
        else:
            return False

    # Draw the store on the right side of the screen
    def drawStore(self, screen):
        # Store Background
        storeColor = [23, 57, 112]
        pygame.draw.rect(screen,storeColor, self.storeRectangle)

        # Store title text
        textColor = (255,255,255)
        mainText = "Store"
        surface = self.font.render(mainText, False, textColor)
        textSize = self.font.size(mainText)
        screen.blit(surface, (self.storeRectangle[0] + (self.storeRectangle[2] / 2) - (textSize[0] / 2), textSize[1]))

        # Store buttons

        gridX = self.windowWidth - self.storeRectangle[2]
        gridY = 30
        gridWidth = self.storeRectangle[2] / 2
        gridHeight = 100

        # Grid

        # Button background color
        backgroundColor = [86, 42, 142]

        # (1,1)
        backgroundColor[0] = backgroundColor[0] + random.randint(-10, 10)
        backgroundColor[1] = backgroundColor[1] + random.randint(-10, 10)
        backgroundColor[2] = backgroundColor[2] + random.randint(-10, 10)

        self.button1Rectangle = (gridX, gridY, gridWidth, gridHeight)
        pygame.draw.rect(screen, backgroundColor, self.button1Rectangle)

        # (1,2)

        backgroundColor[0] = backgroundColor[0] + random.randint(-10, 10)
        backgroundColor[1] = backgroundColor[1] + random.randint(-10, 10)
        backgroundColor[2] = backgroundColor[2] + random.randint(-10, 10)

        self.button2Rectangle = (gridX + gridWidth, gridY, gridWidth, gridHeight)
        pygame.draw.rect(screen, backgroundColor, self.button2Rectangle)


    # Deal damage to the base
    def dealDamage(self, damage):
        self.baseHealth = self.baseHealth - damage
        self.drawHUD()