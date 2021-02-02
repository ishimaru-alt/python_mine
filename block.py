
from mine import *

mc = Minecraft()

x,y,z = mc.player.getPos()

mc.setBlock(x,y,z,1)
print('ブロックを置きました')
