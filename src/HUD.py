# Tower Defense HUD file
# Keeps track of in game stats on screen
# Floris van Rossum

class HUD:

    def __init__(self, screen):
        self.baseHealth = 100
        self.gold = 100
        self.screen = screen

    # Draw the HUD on the top right
    # Includes gold and base health
    def drawHUD(self):
        pass

    # Deal damage to the base
    def dealDamage(self, damage):
        self.baseHealth = self.baseHealth - damage
        self.drawHUD()