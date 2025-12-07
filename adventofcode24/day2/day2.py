"""
Advent of code 2024 - Day 1 - Part 1 & 2
https://adventofcode.com/2024/day/1
"""

import os

# get path of the file
path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"

with open(FILE, "r", encoding="utf-8") as f:
    data = [l.split(" ") for l in f.read().split("\n")]


p1 = 0



def safe(l):
    l = [int(a) for a in l]
    asc = True
    desc = True
    validate = True
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            asc = False
        if l[i] < l[i + 1]:
            desc = False
        validate = validate and abs(l[i] - l[i + 1]) in [1,2,3]
    if (asc or desc) and validate:
        return True

# Part 1
for l in data:
    if safe(l):
        p1 += 1
    
print(p1)

p2 = 0
# safety systems tolerate a single bad level in what would otherwise be a safe report
for l in data:
    ok = safe(l)
    for i in range(len(l)):
        temp = l.copy()
        temp.pop(i)
        if safe(temp):
            p2 += 1
            break
        
print(p2)

