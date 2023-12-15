"""
Advent of code 2023 - Day 15 - Part 1 & 2
https://adventofcode.com/2023/day/15
"""

import os
path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"


with open(FILE, "r", encoding="utf-8") as f:
    data = f.read().splitlines()
    data = data[0].split(",")


def h(string):
    """Hash function"""
    res = 0
    for c in string:
        res = ((res + ord(c)) * 17) % 256
    return res%256


P1 = sum([h(i) for i in data])
print("Part 1:", P1)

boxes = {}
for s in data:
    if '=' in s:
        t = s.split("=")[0]
        val = s.split("=")[1]
        if h(t) not in boxes:
            boxes[h(t)] = {}
        boxes[h(t)][t] = val
    if '-' in s:
        t = s.split("-")[0]
        if h(t) not in boxes:
            boxes[h(t)] = {}
        if t in boxes[h(t)]:
            del boxes[h(t)][t]

P2 = 0
for k,v in boxes.items():
    for ind,v2 in enumerate(v.values()):
        P2 += (k+1)*(ind+1)*int(v2)

print("Part 2:", P2)
