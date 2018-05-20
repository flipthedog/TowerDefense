# Tower Defense Map File
# Hold all the visual objects

import math, pygame
from Cell import Cell
import random
import heapq
from Enemy import Enemy
from Tower import Tower
from Bullet import Bullet
from HUD import HUD

class Map:

    def __init__(self,width,height):
        self.windowWidth = width
        self.windowHeight = height
        self.widthNumber = 0
        self.heightNumber = 0

        self.map = [] # Contains all the cells that make up the map
        self.path = [] # Ordered list of cells that make up the path for the enemies
        self.walls = [] # List containing all the cells that make up the walls
        self.enemies = [] # List of all enemies currently on the field
        self.level = 0 # Incrementing level variable, increases difficulty
        self.towers = [] # List of all towers currently on the map
        self.bullets = [] # List of all bullets

        self.start = 0
        self.end = 0
        self.startCell = None
        self.endCell = None

        self.hud = HUD(width, height)

    def createEnemy(self):
        enemy1 = Enemy(0, 0, self.path)
        self.enemies.append(enemy1)

    def createTower(self, cell, id):
        if(cell.id is 1):
            # The cell is a wall so create the tower
            tower1 = Tower(cell, id)
            self.towers.append(tower1)
        else:
            # The cell is not a tower, so don't create it
            print("Error: Can only build towers on a wall")

    # Generate a map of cells
    # widthNo - the number of cells in width
    # height - the number of cells in height
    # fills self.map and self.path
    def generateMap(self, widthNo, heightNo):
        # Create random start and end points
        self.widthNumber = widthNo
        self.heightNumber = heightNo

        bottomBarHeight = 100
        cellWidth = round(self.windowWidth/widthNo)
        cellHeight = round( (self.windowHeight - bottomBarHeight)/heightNo)

        # Create a map of wall cells
        for i in range(0, heightNo):

            for j in range(0, widthNo):
                color = [0, 0, 0] # HSV Array containing the cell color
                randomInt = random.randint(1, 30)
                color[0] = randomInt
                color[1] = randomInt
                color[2] = randomInt

                newCell = Cell(j * cellWidth, i * cellHeight, cellWidth, cellHeight, 0, color)
                # find all the neighbors of the cell

                self.map.append(newCell)

        self.findNeighbors()

        # Defining the start and end cells
        # Start cell, top left quarter of map
        # End cell, bottom right quarter of map
        self.start = [random.randint(0, round(widthNo/4)), random.randint(0, round(heightNo/4))]
        self.end = [random.randint(round(3*widthNo/4), widthNo), random.randint(round(3*heightNo/4), heightNo)]
        # print("This is start: " + str(self.start))
        # print("This is end: " + str(self.end))

        startPosition = [self.start[0] * self.map[0].width, self.start[1] * self.map[0].height]
        self.startCell = self.findCursorCell(startPosition)

        endPosition = [self.end[0] * self.map[0].width, self.end[1] * self.map[0].height]
        self.endCell = self.findCursorCell(endPosition)

        # Debugging print statement in order to print out the current map
        # self.printArrayCellContents()

    # Create a path from the start to the end, make the path a little interesting
    def generatePath(self, widthNo, heightNo):
        path = [] # contains all the cells that make up the path

        # Create multiple different waypoints and connect them with paths
        # Waypoint for the top right quarter
        waypoint1 = [random.randint(round(widthNo/4), round(3*widthNo/4)), random.randint(0, round(heightNo/2))]
        # Waypoint for the bottom left corner
        waypoint2 = [random.randint(0, round(widthNo/2)), random.randint(round(heightNo/4), round(3*heightNo/4))]

        way1Position = [waypoint1[0] * self.map[0].width, waypoint1[1] * self.map[0].height]
        self.waypoint1Cell = self.findCursorCell(way1Position)

        way2Position = [waypoint2[0] * self.map[0].width, waypoint2[1] * self.map[0].height]
        self.waypoint2Cell = self.findCursorCell(way2Position)

        self.waypoint1Cell.id = 2
        self.waypoint2Cell.id = 2

        self.waypoint1Cell.redoColor()
        self.waypoint2Cell.redoColor()

        path1 = self.greedyBFS(self.startCell,self.waypoint1Cell)
        path2 = self.greedyBFS(self.waypoint1Cell, self.waypoint2Cell)
        path3 = self.greedyBFS(self.waypoint2Cell, self.endCell)

        for cell in path1:
            path.append(cell)
        for cell in path2:
            path.append(cell)
        for cell in path3:
            path.append(cell)


        # Find the corresponding waypoint cells
        for cell in path:
            # Update the cell ids in the path
            cell.id = 2
            cell.redoColor()

        self.path = path
        self.generateWall()
        self.createEnemy()

        self.createTower(self.walls[0], 0)

    def greedyBFS(self, startCell, endCell):
        evaluated = []

        # HEAP
        # stores tuples
        #   FIRST - fCost of the cell
        #   SECOND - cell itself
        notEvaluated = [] # Keep this as a heap with heapify
        notEvaluatedCheck = [] # Array to make sure everything stays on the same page

        # Dictionary containing the path
        previousCells = []

        # Calculate the euclidian distance to the cell
        startFCost = startCell.calcDistance(endCell)

        heapq.heappush(notEvaluated, (startFCost, startCell))
        notEvaluatedCheck.append(startCell)

        while not len(notEvaluatedCheck) <= 0 :
            heapq.heapify(notEvaluated)
            currentCell = heapq.heappop(notEvaluated)[1]
            notEvaluatedCheck.remove(currentCell)

            if currentCell.isSameLocation(endCell):
                # print("Found a path")
                return previousCells

            # print("Iterated")
            evaluated.append(currentCell)
            previousCells.append(currentCell)

            for neighbor in currentCell.neighbors:

                if neighbor in evaluated or neighbor is None:
                    continue


                if not notEvaluatedCheck.__contains__(neighbor):
                    neighborFCost = neighbor.calcDistance(endCell)
                    heapq.heappush(notEvaluated, (neighborFCost, neighbor))
                    notEvaluatedCheck.append(neighbor)
                    # print("Neighbor added" + str(len(notEvaluatedCheck)))

        print("\n\nPATH NOT FOUND\n\n")

    def printArrayCellContents(self):

        for cell in self.map:
            print("X: " + str(cell.x))
            print("Y: " + str(cell.y))
            print("width: " + str(cell.width))
            print("height: " + str(cell.height))
            print("id: " + str(cell.id))
            print("color: " + str(cell.color))

    # find all the neighbors of a cell
    # cell - the cell of which the neighbors need to be found
    # @return - an array of all the neighbors
    def findNeighbors(self):

        map = self.map

        for i in range(0, len(map)):
            neighbors = []

            # Check the upper
            if i-self.widthNumber > 0:
                neighbors.append(map[i-self.widthNumber])
            else:
                neighbors.append(None)

            # Check the lower
            if i + self.widthNumber < (self.widthNumber * self.heightNumber):
                neighbors.append(map[i + self.widthNumber])
            else:
                neighbors.append(None)

            # Check the left
            if ((i) % self.widthNumber) is not 0 and i - 1 > 0:
                neighbors.append(map[i - 1])
            else:
                neighbors.append(None)

            # Check the right
            if i + 1 < (self.widthNumber * self.heightNumber) and ((i + 1) % self.widthNumber) is not 0:
                neighbors.append(map[i + 1])
            else:
                neighbors.append(None)

            map[i].neighbors = neighbors

    # Designate a certain number of empty cells along the path as walls which can house buildings
    def generateWall(self):
        numberPath = []
        self.walls = []

        for cell in self.path:
            numberOfWalls = random.randint(0,2) # Create between 0 and 2 walls
            numberPath.append(numberOfWalls)

        for i in range(0,len(self.path)):
            cell = self.path[i]
            neighbors = cell.neighbors
            limitWalls = numberPath[i]
            currentWalls = 0
            for i in range(0,len(neighbors)):
                neighborCell = neighbors[i]
                if limitWalls <= currentWalls:
                    if neighborCell is not None and not neighborCell.id is 2:
                        neighborCell.id = 1
                        neighborCell.redoColor()
                        self.walls.append(neighborCell)
                        currentWalls = currentWalls + 1

    # Update each enemy position based on where it is in the path
    def update(self,screen, deltaT):

        # Draw the hud on the screen
        self.hud.drawHUD(screen)

        for tower in self.towers:
            tower.drawTower(screen)

            # Update the tower and bullets
            tower.updateTower(screen, self.enemies, self.path, self.windowWidth, self.windowHeight, deltaT)

        for enemy in self.enemies:
            enemy.updatePosition()
            enemy.drawEnemy(screen)

            if enemy.goalReached:
                # The enemy has arrived at the goal
                self.enemies.remove(enemy)
                self.hud.baseHealth -= 1


    # Find the closest cell based on a position entered
    def findCursorCell(self, position):
        maxDistance = 1000000000
        xCur = position[0] - (self.windowWidth/self.widthNumber)/2
        yCur = position[1] - (self.windowHeight/self.heightNumber)/2
        closestCell = self.map[0]

        for i in range(0,len(self.map)):
            cell = self.map[i]
            x = (cell.x)
            y = (cell.y)
            # print("Mouse x: " + str(xCur))
            # print("Mouse x: " + str(yCur))
            # print("Cell x: " + str(x))
            # print("Cell y: " + str(y))
            distance = math.sqrt((x - xCur) ** 2 + (y - yCur) ** 2)
            # print("Distance: " + str(distance))

            if(distance <= maxDistance):
                # print("Mouse x: " + str(xCur))
                # print("Mouse x: " + str(yCur))
                # print("Cell x: " + str(x))
                # print("Cell y: " + str(y))
                # print("distance: " + str(distance))
                maxDistance = distance
                closestCell = cell

        return closestCell