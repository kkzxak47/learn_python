# -*- coding: utf-8 -*-
from shutil import copyfile


with open('e:/mp3temp/mp3list.txt','r',encoding='utf-8') as flist:
# print(flist)
# print(flist.readline())
    for f in flist.readlines():
        print('copying: '+f.split('\\')[-1])
        try:
            copyfile(f.strip(), 'e:/mp3temp/'+f.strip().split('\\')[-1])
            print(f.strip())
        except IOError:
            print('error copying '+ f.strip())

