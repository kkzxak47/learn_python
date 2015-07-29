# coding: utf-8
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

tid = "00000002"
ptn = re.compile(r"(\[FTCP[^\]]+\]\s+)(Pacakage\s+Tid=\[" + tid + "\][^}]+})")
match = ptn.findall(string)

print [t[1] for t in match]
