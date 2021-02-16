#!/usr/bin/python 3
import random

"""
Here's a lottery number generator... Try it. Feeling lucky!?
"""

rnum = 0
vlist = []

while len(vlist) < 5:
    rnum = random.randint(0,70)
    if rnum not in vlist:
        vlist.append(rnum)

print('The potential winning lottery numbers are:\n')
print(vlist[:], ":", random.randint(0,25))