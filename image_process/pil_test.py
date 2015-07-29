#!/usr/bin/env python
# coding: utf-8

import time
from PIL import Image
import tkFileDialog

file2open = tkFileDialog.askopenfilename(
    initialdir=ur'E:\2013-12-21\Python\forfun\image_process')
file2save = tkFileDialog.asksaveasfilename()
start = time.time()
im = Image.open(file2open)
im = im.convert("1")  # convert image to black and white
# im.size == (width, height)
rows = im.size[1] / 8
cols = im.size[0]

aline = bytearray()
with open(file2save, 'w') as output:
    output.write(u"const int bmap[8]= {\n")
    for p in range(rows):
        unit = bytearray()
        for xx in range(cols):
            for yy in range(8):
                pix = im.getpixel((xx, (p * 8) + yy))
                unit.insert(0, "1" if pix == 0 else "0")
            unit.insert(0, "B")
            if (xx % 8 == 7):
                unit += "\n"
            else:
                unit += ", "
            aline += unit
            unit = bytearray()
        # output.write(aline)
        aline = bytearray()
    output.write(u"}")

im.close()
end = time.time()
print "time elapsed:", end - start
