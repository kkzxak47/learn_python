# coding: utf-8
import re

string = """[FTCP XXX XXXXXX] 

Pacakage Tid=[00000002] XXXXXXXXXXXXXXXXX 
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

ptn = re.compile(r"(\[FTCP[^\]]+\]\s+)(Pacakage[^}]+})")
match = ptn.findall(string)

print [t[1] for t in match] if match else None
