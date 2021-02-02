import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
mc.postToChat("house!")
#mc.setBlock(0,0,0,block.AIR)
#mc.setBlocks(0,0,0,150,150,100,block.AIR)

#位置情報を取得
x,y,z = mc.player.getPos()

#x,y,z軸の表示
mc.postToChat("x coordinate:" + str(x - 68))
mc.postToChat("y coordinate:" + str(y + 64))
mc.postToChat("z coordinate:" + str(z + 248))


#周囲10マスの整地
mc.setBlock((x - 68),(y + 64),(z + 248),block.AIR)
mc.setBlocks((x - 68),(y + 64),(z + 248),(x - 58),(y + 64),(z + 248),block.AIR)
