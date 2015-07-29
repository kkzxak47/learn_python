# coding: utf-8
"""
http://www.douban.com/group/topic/78073359/
提取指定Tid的文本段
"""

import re

string = """[FTCP XXX XXXXXX] 

Pacakage Tid=[00000001] XXXXXXXXXXXXXXXXX 
{ 
XXXXXXXXXX 
###XXXXXXXXXX### 
.... 
XXXXXXXXXX 
} 

[FTCP XXX XXXXXX] 

Pacakage Tid=[00000002] XXXXXXXXXXXXXXXXX 
{ 
XXXXXXXXXX 
###XXXXXXXXXX### 
.... 
XXXXXXXXXX 
} """

tid = "{0:08}".format(2)
ptn = re.compile(r"(?<=\[FTCP\s\w{3}\s\w{6}\]\s\s\s)(Pacakage\sTid=\[" + tid + "\][^}]+})")
match = ptn.findall(string)

print match
