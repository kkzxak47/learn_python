[code]#!/env/python
import sys
import numpy
from PIL import Image

im = Image.open(sys.argv[1])
im = im.convert("1")   # 把图片转换为黑白二值型
rows=im.size[1]/8  # 图片高/8，下面在处理的时候8行一组输出
cols=im.size[0]  # 图片宽
val=""
print "const int bmap[8]= {"
for p in range(rows):  # 每8行
for xx in range(cols):  # 每列
for yy in range(8):
pix=im.getpixel((xx,(p*8)+yy))  # 获取每个像素点的值
if (pix == 0 ):  # 0黑，输出1
val="1"+val
else:
val="0"+val  # 非黑，即白，输出0
val = "B"+val
print val +",",  # 每8个像素点一组，图片像素是从上到下，输出的时候是从右到左
val=""
if (xx%8 == 7):  # 每8组一行
print ""
print "}"[/code]
不是特别熟悉PIL这个库，但是用过。
处理顺序是从上到下（8行一组），从左到右。
形如的图片（8x8，已放大，每个方块是一个像素），会产生
[code]B00100100, B01001001, B10010010, B01100100, B00001001, B10110010, B01000100, B00011001,[/code]
的结果。每组数字对应一竖列，顺序从左到右；每组内部的顺序是从下到上，比如第二组B01001001就对应第二列，从下往上：白黑白白黑白白黑。