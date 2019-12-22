from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
x, y, z = mc.player.getPos()
for i in range(8):
    mc.setBlock(1, y, 1, 41)
    sleep(0.1)
    y = y + 1
