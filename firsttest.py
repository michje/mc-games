 
from mcpi import minecraft
from mcpi import block
import time


mc = minecraft.Minecraft.create()

mc.postToChat("Start First test script at %s" %(time.ctime()))




##time.sleep(2)

##x,y,z = mc.player.getPos()
##mc.player.setPos(x, y + 100, z)

playerPos = mc.player.getPos()
print(playerPos)

playerPos = minecraft.Vec3(int(playerPos.x),int(playerPos.y),int(playerPos.z))
print(playerPos)

time.sleep(5)

x,y,z = playerPos

print ("x:%s, y:%s, z:%s" %(x,y,z))

blocktype = mc.getBlock(playerPos.x,playerPos.y-1,playerPos.z)

mc.postToChat("Block below feed is - " + str(blocktype))

for i in xrange(10):
    mc.setBlock(playerPos.x + 1 + i,playerPos.y,playerPos.z, block.STONE_BRICK)
    
    for y in xrange(10):
        mc.setBlock(playerPos.x + 1 + i,playerPos.y + y,playerPos.z ,block.STONE_BRICK)
    
            
##mc.setBlock(x+1,y,block.DIRT)
##mc.setBlock(x+1,y+1,block.DIRT)


