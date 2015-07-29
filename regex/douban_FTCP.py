# coding: utf-8
import re

string = """[FTCP XXX XXXXXX] 

Pacakage Tid=[00000002] XXXXXXXXXXXXXXXXX 
{ 
XXXXXXXXXX 
###XXXXXXXXXX### 
.... 
XXXXXXXXXX 
} """

ptn = re.compile(r"(\[FTCP[^\]]+\]\s+)(Pacakage[^}]+})")
match = ptn.match(string)

print match.groups()[1] if match else None
