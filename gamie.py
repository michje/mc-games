## Game based on stuffabout.com article
## http://www.stuffaboutcode.com/2013/03/raspberry-pi-minecraft-snake.html

from mcpi import minecraft
from mcpi import block
import time
import random

class Gamie:
    def __init__(self, mc, startVec3, playingBottomLeft, playingBottomRight):
        self.mc = mc
        self.length = 5
        self.direction = "up"
        self.playingBottomLeft = playingBottomLeft
        self.playingBottomRight = playingBottomRight
        self.score = 0
        self.tail = []
        self.tail.insert(0, startVec3)
        self.createApple()
                
    def draw(self):
        print "draw"
        for segment in self.tail:
            self.mc.setBlock(segment.x, segment.y, segment.z, block.DIAMOND_BLOCK)

    def addSegment(self, segment):
        self.mc.setBlock(segment.x, segment.y, segment.z, block.DIAMOND_BLOCK)
        self.tail.insert(0, segment)
        if (len(self.tail) > self.length):
            lastSegment = self.tail[len(self.tail) - 1]
            self.mc.setBlock(lastSegment.x, lastSegment.y, lastSegment.z, block.AIR)
            self.tail.pop()

    def move(self):
        print "move"
        newSegment = minecraft.Vec3(self.tail[0].x, self.tail[0].y , self.tail[0].z)
        
        if self.direction == "up":
            newSegment.y = newSegment.y + 1
        elif self.direction == "down":
            newSegment.y = newSegment.y - 1
        elif self.direction == "left":
            newSegment.x = newSegment.x - 1
        elif self.direction == "right":
            newSegment.x = newSegment.x + 1

        if (self.checkCollision(newSegment) == False):
            self.addSegment(newSegment)

            if (matchVec3(newSegment, self.apple) == True):
                self.length = self.length + 1;
                self.score = self.score + 10
                self.createApple()
                
            return True
                
        else:

            time.sleep(5)
            mc.postToChat("Game over - score = " + str(self.score))
            time.sleep(5)
            return False

    def changeDirection(self, newDirection):
        print "change direction to: %s" %newDirection
        if (newDirection == "up"):
                if (self.direction != "down"):
                    self.direction = newDirection
        elif (newDirection == "down"):
                if (self.direction != "up"):
                    self.direction = newDirection
        elif (newDirection == "left"):
                if (self.direction != "right"):
                    self.direction = newDirection
        elif (newDirection == "right"):
                if (self.direction != "left"):
                    self.direction = newDirection


    def checkCollision(self, newSegment):
        if  ((newSegment.x == self.playingBottomLeft.x) or (newSegment.y == self.playingBottomLeft.y) or (newSegment.x == self.playingBottomRight.x) or (newSegment.y == self.playingBottomRight.y)):
            return True
        else:
            hitTail = False
            for segment in self.tail:
                if (matchVec3(segment, newSegment) == True):
                    hitTail = True
                    break
                
            return hitTail
        
    def createApple(self):
        badApple = True

        while (badApple == True):
            
            x = random.randrange(self.playingBottomLeft.x, self.playingBottomRight.x)
            y = random.randrange(self.playingBottomLeft.y, self.playingBottomRight.y)
            z = playingBottomLeft.z
            newApple = minecraft.Vec3(x, y , z)
            badApple = self.checkCollision(newApple)

        self.apple = newApple
        self.mc.setBlock(self.apple.x, self.apple.y, self.apple.z, block.GLOWING_OBSIDIAN)

## Utility methods
def matchVec3(vec1, vec2):
    if ((vec1.x == vec2.x) and (vec1.y == vec2.y) and (vec1.z == vec2.z)):
        return True
    else:
        return False

def drawVerticalOutline(mc, x0, y0, x1, y1, z, blockType, blockData=0):
    mc.setBlocks(x0, y0, z, x0, y1, z, blockType, blockData)
    mc.setBlocks(x0, y1, z, x1, y1, z, blockType, blockData)
    mc.setBlocks(x1, y1, z, x1, y0, z, blockType, blockData)
    mc.setBlocks(x1, y0, z, x0, y0, z, blockType, blockData)
    
    

    
## start main program
if __name__ == "__main__":

    ## Constants
    screenBottomLeft = minecraft.Vec3(-10,4,15)
    screenTopRight = minecraft.Vec3(10,24,15)
    playingBottomLeft = minecraft.Vec3(-10,4,14)
    playingTopRight = minecraft.Vec3(10,24,14)
    gamieStart= minecraft.Vec3(0,5,14)
    upControl= minecraft.Vec3(0, -1, 1)
    downControl= minecraft.Vec3(0, -1, -1)
    leftControl= minecraft.Vec3(-1, -1, 0)
    rightControl= minecraft.Vec3(1, -1, 0)
    middleControl= minecraft.Vec3(0, 0, 0)


    ## Connect to minecraft by creating the mc object
    ## mc needs to be running and in game
    mc = minecraft.Minecraft.create()

    ## mc needs to be running and in game
    mc.postToChat("hi there, starting gamie on %s" %(time.ctime()))

    ##Build game board
    ## clear a suitable large area
    mc.setBlocks(-10, 0, -5, 10, 25, 16, block.AIR)

    ## create playing board
    mc.setBlocks(screenBottomLeft.x, screenBottomLeft.y, screenBottomLeft.z,screenTopRight.x, screenTopRight.y, screenTopRight.z, block.STONE)

    drawVerticalOutline(mc, playingBottomLeft.x, playingBottomLeft.y, playingTopRight.x, playingTopRight.y, playingTopRight.z, block.OBSIDIAN)
    
    ## create control buttons
    mc.setBlock(upControl.x, upControl.y, upControl.z, block.DIAMOND_BLOCK)
    mc.setBlock(downControl.x, downControl.y, downControl.z, block.DIAMOND_BLOCK)
    mc.setBlock(leftControl.x, leftControl.y, leftControl.z, block.DIAMOND_BLOCK)
    mc.setBlock(rightControl.x, rightControl.y, rightControl.z, block.DIAMOND_BLOCK)

    ## blocks around control buttons, to stop player moving of buttons
    mc.setBlock(middleControl.x + 2, middleControl.y + 1, middleControl.z, block.GLASS)
    mc.setBlock(middleControl.x - 2, middleControl.y + 1, middleControl.z, block.GLASS)
    mc.setBlock(middleControl.x, middleControl.y + 1, middleControl.z + 2, block.GLASS)
    mc.setBlock(middleControl.x, middleControl.y + 1, middleControl.z - 2, block.GLASS)
    mc.setBlock(middleControl.x - 1, middleControl.y + 1, middleControl.z - 1, block.GLASS)
    mc.setBlock(middleControl.x - 1, middleControl.y + 1, middleControl.z + 1, block.GLASS)
    mc.setBlock(middleControl.x + 1, middleControl.y + 1, middleControl.z + 1, block.GLASS)
    mc.setBlock(middleControl.x + 1, middleControl.y + 1, middleControl.z - 1, block.GLASS)
    mc.setBlock(middleControl.x, middleControl.y - 1, middleControl.z, block.GLASS)
    

    ## put player in the middel of th control
    mc.player.setPos(middleControl.x + 0.5, middleControl.y, middleControl.z + 0.5)

    ## time for minecraft to catchup
    time.sleep(3)

    mc.postToChat("Walk forward, backward, left, right to control the spacecraft")

    time.sleep(3)

    ## create gamie
    gamie = Gamie(mc, gamieStart, playingBottomLeft, playingTopRight)

    gamie.draw()

    playing = True

    
    try:
        ## loop until game over
        while playing == True:
            
            time.sleep(0.3)

            playerTilePos = mc.player.getTilePos()

            playerTilePos.y = playerTilePos.y - 1
            
            if matchVec3(playerTilePos, upControl) == True:
                gamie.changeDirection("up")
            elif matchVec3(playerTilePos, downControl) == True:
                gamie.changeDirection("down")
            elif matchVec3(playerTilePos, leftControl) == True:
                gamie.changeDirection("left")
            elif matchVec3(playerTilePos, rightControl) == True:
                gamie.changeDirection("right")

            playing = gamie.move()
            
    except KeyboardInterrupt:
        print "stopped because of interrupt"
   



    
    

    
    
    




