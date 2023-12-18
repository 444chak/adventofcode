# pylint: disable=W0123
"""
Advent of code 2023 - Day 18 - Part 1 & 2
https://adventofcode.com/2023/day/18
"""

import os
import time
path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"

t = time.time()

with open(FILE, "r", encoding="utf-8") as f:
    data = f.read().splitlines()

mov = []
mov2 = []


for ind,l in enumerate(data):
    mov.append([l.split()[0], int(l.split()[1])])
    mov2.append([int(l.split()[2][2:-2],16), int(l.split()[2][-2])])


pos = [0,0]
R,D,L,U = (0,1), (1,0), (0,-1), (-1,0)
conv = {0 : 'R', 1 : 'D', 2 : 'L', 3 : 'U'}


all_pos = [pos]
STEPS1 = 0
for i in mov:
    pos = [pos[0] + i[1]*eval(i[0])[0], pos[1] + i[1]*eval(i[0])[1]]
    STEPS1 += i[1]
    all_pos.append(pos)

all_pos2 = [pos]

P1 = 0
for i,j in zip(all_pos, all_pos[1:]):
    P1 += (i[0]+j[0]) * (i[1]-j[1]) / 2

P1 = int(abs(P1+STEPS1/2+1))

print(f"Part 1 : {P1} in {time.time() - t:.4f} seconds")

STEPS2 = 0
for i in mov2:
    i[1] = conv[i[1]]
    i = i[::-1]
    pos = [pos[0] + i[1]*eval(i[0])[0], pos[1] + i[1]*eval(i[0])[1]]
    STEPS2 += i[1]
    all_pos2.append(pos)

P2 = 0
for i,j in zip(all_pos2, all_pos2[1:]):
    P2 += (i[0]+j[0]) * (i[1]-j[1]) / 2

P2 = int(abs(P2+STEPS2/2+1))

print(f"Part 2 : {P2} in {time.time() - t:.4f} seconds")
