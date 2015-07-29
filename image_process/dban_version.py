#!/env/python
# coding: utf-8

import time
from PIL import Image
import tkFileDialog


def main():
    file2open = tkFileDialog.askopenfilename(
        initialdir=ur'E:\Python\forfun\image_proces')
    file2save = tkFileDialog.asksaveasfilename()
    if not file2open or file2save:
        return
    start = time.time()
    im = Image.open(file2open)
    im = im.convert("1")  # convert image to black and white
    # im.size == (width, height)
    rows = im.size[1] / 8
    cols = im.size[0]

    val = ""
    with open(file2save, 'w') as output:
        output.write(u"const int bmap[8]= {\n")
        for p in range(rows):
            for xx in range(cols):
                for yy in range(8):
                    pix = im.getpixel((xx, (p * 8) + yy))
                    val = ('0' if pix else '1') + val
                if (xx % 8 == 7):
                    output.write("B{}\n".format(val))
                else:
                    output.write("B{}, ".format(val))
                val = ""
        output.write(u"}\n")

    im.close()
    end = time.time()
    print "time elapsed:", end - start

if __name__ == '__main__':
    main()
