# coding: UTF-8

import mcpi.minecraft as minecraft
import sys

mc = minecraft.Minecraft.create()

#位置情報を取得
x,y,z = mc.player.getPos()

#東西の座標
mc.postToChat("x-position:" + str(x))
#高さの座標
mc.postToChat("y-position:" + str(y))
#南北の座標
mc.postToChat("z-position:" + str(z))

#/setblock <x><y><z> <ブロック名>
#自分の場所に石ブロックを1個設置する
#これで置けるのか？
mc.setBlock(x,y,z,1)

#土ブロックを設置する
#周囲５マス分に設置する
#mc.setBlocks(x,y,z,(x+5),(y+5),(z+5),3)

#python test.py a
args = sys.argv
# test.py
mc.postToChat(args[0])
# a
mc.postToChat("args1:" + args[1])


#引数があるかどうかの判断
if args[1] == None :
  print("変数の中身がない")
else:
  print("変数の中身がある")
  mc.postToChat("The value entered is" + args[1])

#引数の数どうかの判断
if len(sys.argv) > 0:
  mc.postToChat("The value entered is" + str(len(sys.argv)))
  mc.postToChat("The value entered is" + str(args[1]))
else:
  print("引数がないよ")

#周囲何マスの整地を行うか
#プラス方向
width = x + int(args[1]) - 1
height = y + int(args[1]) - 1
depth = z + int(args[1]) - 1

#マイナス方向
min_width = x - (int(args[1]) - 1)
min_depth = z - (int(args[1]) - 1)

#周囲？マス分を整地する
mc.setBlocks(min_width,y,min_depth,width,height,depth,0)

mc.postToChat("Complete")

