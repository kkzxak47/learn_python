# -*- coding: utf-8 -*-

import os

with open('e:/mp3temp/mp3list.txt','r',encoding='utf-8') as flist:
# print(flist)
# print(flist.readline())
    for f in flist.readlines():
        try:
            print('deleting: '+f.strip())
            os.remove('e:/mp3temp/'+f.strip().split('\\')[-1])
        except IOError:
            print('error deleting '+ f.strip())